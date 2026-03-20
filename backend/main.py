import uvicorn
import webbrowser
import threading
import time
import os
import sys
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware

# Quando eseguito come .app PyInstaller, aggiungi il bundle al path
if getattr(sys, "frozen", False):
    sys.path.insert(0, sys._MEIPASS)
    os.chdir(sys._MEIPASS)

from database import engine, Base
from routers import teams

# Crea le tabelle al primo avvio
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Football Team Builder", version="1.0.0", docs_url="/api/docs")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://localhost:8000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ── API Routes ──────────────────────────────────────────
app.include_router(teams.router, prefix="/api")


# ── Serve Vue3 build (produzione / PyInstaller) ─────────
def get_frontend_path():
    if getattr(sys, "frozen", False):
        base = sys._MEIPASS
    else:
        base = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(base, "frontend_dist")


frontend_path = get_frontend_path()

if os.path.exists(frontend_path):
    assets_path = os.path.join(frontend_path, "assets")
    if os.path.exists(assets_path):
        app.mount("/assets", StaticFiles(directory=assets_path), name="assets")

    @app.get("/", response_class=FileResponse)
    async def serve_index():
        return FileResponse(os.path.join(frontend_path, "index.html"))

    @app.get("/{full_path:path}", response_class=FileResponse)
    async def serve_spa(full_path: str):
        file_path = os.path.join(frontend_path, full_path)
        if os.path.exists(file_path) and os.path.isfile(file_path):
            return FileResponse(file_path)
        return FileResponse(os.path.join(frontend_path, "index.html"))


def open_browser():
    time.sleep(2.0)
    webbrowser.open("http://localhost:8000")


if __name__ == "__main__":
    threading.Thread(target=open_browser, daemon=True).start()
    print("🚀 Football Team Builder avviato su http://localhost:8000")
    # Passa l'oggetto app direttamente — non la stringa "main:app"
    # così PyInstaller non deve risolvere il modulo per nome
    uvicorn.run(app, host="127.0.0.1", port=8000, reload=False)
