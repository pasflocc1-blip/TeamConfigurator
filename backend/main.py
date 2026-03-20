import uvicorn
import webbrowser
import threading
import time
import os
import sys

# ── PyInstaller: imposta il path ─────────────────────────
if getattr(sys, "frozen", False):
    bundle_dir = sys._MEIPASS
    if bundle_dir not in sys.path:
        sys.path.insert(0, bundle_dir)
    os.chdir(bundle_dir)
    print(f"[BUNDLE] sys._MEIPASS: {bundle_dir}")
    print(f"[BUNDLE] sys.path: {sys.path[:3]}")

from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse, JSONResponse
from fastapi.middleware.cors import CORSMiddleware

from database import engine, Base
print("[OK] database importato")

# Import routers con gestione errori esplicita
try:
    from routers import teams
    print("[OK] routers.teams importato")
except Exception as e:
    print(f"[ERRORE] routers.teams: {e}")
    teams = None

try:
    from routers import registry
    print("[OK] routers.registry importato")
except Exception as e:
    print(f"[ERRORE] routers.registry: {e}")
    registry = None

try:
    from routers import debug
    print("[OK] routers.debug importato")
except Exception as e:
    print(f"[ERRORE] routers.debug: {e}")
    debug = None

Base.metadata.create_all(bind=engine)
print("[OK] tabelle DB create")

app = FastAPI(title="Football Team Builder", version="1.0.0", docs_url="/api/docs")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://localhost:8000",
                   "http://127.0.0.1:5173", "http://127.0.0.1:8000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ── API Routes ────────────────────────────────────────────
if teams:
    app.include_router(teams.router, prefix="/api")
    print("[OK] teams router registrato")
if registry:
    app.include_router(registry.router, prefix="/api")
    print("[OK] registry router registrato")
if debug:
    app.include_router(debug.router, prefix="/api")
    print("[OK] debug router registrato")

# Stampa tutte le route registrate
print("[ROUTES] Route registrate:")
for route in app.routes:
    if hasattr(route, 'path'):
        print(f"  {route.path}")


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

    @app.get("/favicon.svg", response_class=FileResponse)
    async def serve_favicon():
        return FileResponse(os.path.join(frontend_path, "favicon.svg"))

    @app.get("/{full_path:path}", response_class=FileResponse)
    async def serve_spa(request: Request, full_path: str):
        if full_path.startswith("api/"):
            return JSONResponse({"detail": "Not found"}, status_code=404)
        file_path = os.path.join(frontend_path, full_path)
        if os.path.exists(file_path) and os.path.isfile(file_path):
            return FileResponse(file_path)
        return FileResponse(os.path.join(frontend_path, "index.html"))


def find_free_port(default=8000):
    import socket
    for port in range(default, default + 10):
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.bind(('127.0.0.1', port))
                return port
        except OSError:
            continue
    return default


if __name__ == "__main__":
    port = find_free_port(8000)
    threading.Thread(
        target=lambda: (time.sleep(2.0), webbrowser.open(f"http://localhost:{port}")),
        daemon=True
    ).start()
    print(f"🚀 Football Team Builder avviato su http://localhost:{port}")
    uvicorn.run(app, host="127.0.0.1", port=port, reload=False)