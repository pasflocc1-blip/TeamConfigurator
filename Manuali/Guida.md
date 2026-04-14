# MyApp — FastAPI + Vue3 + SQLite per Mac
### Sviluppo su Windows → Distribuzione su Mac • 100% Offline • 100% Gratuito

---
"""
## Struttura del progetto

```
myapp/
├── .github/
│   └── workflows/
│       └── build-mac.yml      ← GitHub Action: compila il .app su Mac
│
├── backend/
│   ├── main.py                ← FastAPI + serve Vue3 build
│   ├── database.py            ← SQLAlchemy + SQLite
│   ├── models.py              ← Modelli DB
│   ├── schemas.py             ← Pydantic schemas
│   ├── requirements.txt       ← Dipendenze Python
│   ├── myapp.spec             ← Config PyInstaller
│   ├── routers/
│   │   └── items.py           ← Esempio router API
│   └── frontend_dist/         ← Generata automaticamente da `npm run build`
│
└── frontend/
    ├── vite.config.js         ← Build → backend/frontend_dist
    ├── package.json
    └── src/
        ├── services/
        │   └── api.js         ← Axios con baseURL: /api
        ├── App.vue
        └── main.js
```
"""
---

## Come funziona tutto insieme

```
┌─────────────────────────────────────────────────┐
│                   Mac dell'utente                │
│                                                  │
│   Doppio click su MyApp.app                      │
│          ↓                                       │
│   FastAPI si avvia su localhost:8000             │
│          ↓                                       │
│   Browser si apre automaticamente               │
│          ↓                                       │
│   Vue3 (file statici) serviti da FastAPI         │
│          ↓                                       │
│   Chiamate /api → FastAPI → SQLite (locale)     │
│                                                  │
│   100% offline, niente server remoti            │
└─────────────────────────────────────────────────┘
```

---

## Setup iniziale (una volta sola)

### Backend Python

```bash
cd backend
python -m venv venv
venv\Scripts\activate        # Windows
pip install -r requirements.txt
```

### Frontend Vue3

```bash
cd frontend
npm install
```

---

## Sviluppo quotidiano

Avvia i due processi in due terminali separati:

**Terminale 1 — Backend:**
```bash
cd backend
venv\Scripts\activate
uvicorn main:app --reload --port 8000
```

**Terminale 2 — Frontend:**
```bash
cd frontend
npm run dev
```

Apri il browser su `http://localhost:5173`

Il proxy Vite manda automaticamente le chiamate `/api` al backend su porta 8000.

---

## Aggiungere una nuova feature (esempio)

### 1. Crea il modello in `backend/models.py`

```python
class Project(Base):
    __tablename__ = "projects"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
```

### 2. Crea il router in `backend/routers/projects.py`

```python
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db

router = APIRouter(prefix="/projects", tags=["projects"])

@router.get("/")
def get_projects(db: Session = Depends(get_db)):
    return db.query(Project).all()
```

### 3. Registra il router in `main.py`

```python
from routers import projects
app.include_router(projects.router, prefix="/api")
```

### 4. Chiama l'API da Vue3

```javascript
import api from '@/services/api'

const projects = await api.get('/projects')
```

---

## Build per Mac — 3 modi

### Modo A — Automatico con GitHub Actions (consigliato)

Ogni volta che vuoi un nuovo build:

```bash
git add .
git commit -m "feat: nuova funzione"
git tag v1.0.0
git push origin main --tags
```

GitHub Actions avvierà automaticamente un runner Mac, compilerà il `.app` e lo renderà disponibile nella tab **Actions** o come **Release**. Scarichi lo ZIP, lo mandi al Mac, estrai e usi.

### Modo B — Manuale tramite GitHub Actions UI

1. Vai su GitHub → tab **Actions**
2. Seleziona **Build Mac App**
3. Clicca **Run workflow** → **Run workflow**
4. Dopo ~5 minuti scarica l'artifact `MyApp-mac.zip`

### Modo C — Su un Mac fisico (se ne hai accesso temporaneo)

```bash
# Sul Mac:
pip install pyinstaller
cd backend
npm run build   # dalla cartella frontend prima
pyinstaller myapp.spec
# Il file è in backend/dist/MyApp.app
```

---

## Prima di fare il build: preparare il frontend

Prima di ogni build, esegui:

```bash
cd frontend
npm run build
```

Questo genera `backend/frontend_dist/` che PyInstaller include nel `.app`.

Se usi GitHub Actions, il workflow lo fa automaticamente.

---

## Il database SQLite

Il file del database viene creato automaticamente al primo avvio:

- **Su Mac (app bundle):** `~/.myapp/myapp.db`
- **In sviluppo Windows:** `backend/myapp.db`

Il percorso `~/.myapp/` nella home utente garantisce che il DB **sopravviva agli aggiornamenti** dell'app — aggiornare l'app non cancella i dati.

---

## Distribuzione al Mac

1. GitHub Actions genera `MyApp-mac.zip`
2. Scarichi lo ZIP
3. Lo trasferisci al Mac (AirDrop, USB, email, Google Drive...)
4. Sul Mac: estrai lo ZIP → trascina `MyApp.app` in Applicazioni
5. Primo avvio: tasto destro → Apri (necessario per app non firmate da Apple)
6. Il browser si apre automaticamente su `http://localhost:8000`

> **Nota:** Se vuoi evitare il warning "app non verificata" di macOS, puoi firmare l'app con un Apple Developer account ($99/anno) ma per uso personale non è necessario.

---

## Checklist build

- [ ] `npm run build` eseguito (genera `frontend_dist/`)
- [ ] `requirements.txt` aggiornato con tutte le dipendenze
- [ ] Tag Git creato (`git tag v1.x.x`)
- [ ] GitHub Action completata senza errori
- [ ] ZIP scaricato e testato sul Mac
- [ ] DB creato correttamente in `~/.myapp/`
