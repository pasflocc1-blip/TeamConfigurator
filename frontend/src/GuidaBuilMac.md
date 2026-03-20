# Guida Build Mac da Windows
## FastAPI + Vue3 → `.app` macOS con GitHub Actions

---

## Perché non puoi usare PyInstaller su Windows per Mac

PyInstaller non fa cross-compile: genera eseguibili solo per il sistema operativo su cui gira. Per creare un `.app` macOS devi eseguirlo su un Mac reale.

La soluzione gratuita è **GitHub Actions**: GitHub mette a disposizione runner macOS gratuiti (`macos-latest`). Fai push del codice, GitHub compila il `.app` per te e lo mette a disposizione per il download.

---

## Struttura del repository

```
my-app/
├── .github/
│   └── workflows/
│       └── build-mac.yml      ← workflow GitHub Actions
├── backend/
│   ├── main.py
│   ├── requirements.txt
│   └── myapp.spec             ← configurazione PyInstaller
└── frontend/
    ├── package.json
    ├── vite.config.js
    └── src/
```

---

## Step 1 — Crea il repository su GitHub

1. Vai su [github.com](https://github.com) e crea un account se non ce l'hai
2. Clicca **New repository**
3. Dai un nome (es. `TeamConfigurator`)
4. Lascia **Public** (i runner Mac gratuiti funzionano anche sui privati, ma con limitazioni sui minuti)
5. Clicca **Create repository**

---

## Step 2 — Carica il codice

Dal tuo terminale Windows (cmd o PowerShell):

```cmd
cd C:\Dev\TeamConfigurator_Backend

git init
git add .
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/TUO-USERNAME/TeamConfigurator.git
git push -u origin main
```

Poi carica anche il frontend nello stesso repo (cartella `frontend/`).

---

## Step 3 — Crea il file `myapp.spec`

Nella cartella `backend/`, crea `myapp.spec`:

```python
# -*- mode: python ; coding: utf-8 -*-

a = Analysis(
    ['main.py'],
    pathex=['.'],
    binaries=[],
    datas=[
        ('frontend_dist', 'frontend_dist'),  # build Vue3
    ],
    hiddenimports=[
        'uvicorn.logging',
        'uvicorn.loops', 'uvicorn.loops.auto',
        'uvicorn.protocols', 'uvicorn.protocols.http',
        'uvicorn.protocols.http.auto',
        'uvicorn.lifespan', 'uvicorn.lifespan.on',
        'anyio', 'anyio._backends._asyncio',
        'sqlalchemy.dialects.sqlite',
    ],
    hookspath=[],
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
)

pyz = PYZ(a.pure)

exe = EXE(
    pyz, a.scripts, [],
    exclude_binaries=True,
    name='TeamConfigurator',
    debug=False,
    strip=False,
    upx=True,
    console=False,      # niente finestra terminale
    argv_emulation=True,
)

coll = COLLECT(
    exe, a.binaries, a.zipfiles, a.datas,
    strip=False, upx=True,
    name='TeamConfigurator',
)

app = BUNDLE(
    coll,
    name='TeamConfigurator.app',
    icon=None,  # puoi mettere 'icon.icns' se hai un'icona
    bundle_identifier='com.tuonome.teamconfigurator',
    info_plist={
        'NSHighResolutionCapable': True,
        'LSBackgroundOnly': False,
    },
)
```

---

## Step 4 — Crea il workflow GitHub Actions

Crea la cartella `.github/workflows/` e il file `build-mac.yml`:

```yaml
name: Build Mac App

on:
  push:
    tags:
      - 'v*'           # si attiva con: git tag v1.0.0 && git push --tags
  workflow_dispatch:   # oppure avvialo manualmente dalla UI GitHub

jobs:
  build-mac:
    runs-on: macos-latest

    steps:
      - name: Checkout codice
        uses: actions/checkout@v4

      - name: Setup Python 3.11
        uses: actions/setup-python@v5
        with:
          python-version: '3.11'

      - name: Setup Node.js 22
        uses: actions/setup-node@v4
        with:
          node-version: '22'

      - name: Build frontend Vue3
        working-directory: frontend
        run: |
          npm ci
          npm run build
        # Output → backend/frontend_dist (configurato in vite.config.js)

      - name: Installa dipendenze Python
        working-directory: backend
        run: |
          pip install -r requirements.txt
          pip install pyinstaller

      - name: Build .app con PyInstaller
        working-directory: backend
        run: |
          pyinstaller myapp.spec

      - name: Crea archivio ZIP
        run: |
          cd backend/dist
          zip -r TeamConfigurator-mac.zip TeamConfigurator.app

      - name: Carica artifact (scaricabile per 30 giorni)
        uses: actions/upload-artifact@v4
        with:
          name: TeamConfigurator-mac
          path: backend/dist/TeamConfigurator-mac.zip
          retention-days: 30

      - name: Crea Release GitHub (solo su tag)
        if: startsWith(github.ref, 'refs/tags/')
        uses: softprops/action-gh-release@v2
        with:
          files: backend/dist/TeamConfigurator-mac.zip
          generate_release_notes: true
```

---

## Step 5 — Avvia il build

### Opzione A — tramite tag (consigliato per rilasci)

```cmd
git add .
git commit -m "release: v1.0.0"
git tag v1.0.0
git push origin main --tags
```

GitHub Actions parte automaticamente.

### Opzione B — manuale dalla UI

1. Vai su GitHub → il tuo repository
2. Clicca la tab **Actions**
3. Seleziona **Build Mac App** nel menu a sinistra
4. Clicca **Run workflow** → **Run workflow**

---

## Step 6 — Scarica il `.app`

Dopo 5-10 minuti (il build Node + Python richiede tempo):

1. GitHub → **Actions** → clicca il workflow completato (✅)
2. Scorri fino a **Artifacts**
3. Clicca **TeamConfigurator-mac** per scaricare lo ZIP

Oppure se hai creato un tag, vai su **Releases** e scarica direttamente.

---

## Step 7 — Installa sul Mac

1. Trasferisci `TeamConfigurator-mac.zip` sul Mac (AirDrop, USB, Google Drive...)
2. Estrai lo ZIP → ottieni `TeamConfigurator.app`
3. Trascina l'app nella cartella **Applicazioni**
4. **Primo avvio:** tasto destro sull'app → **Apri**
   (necessario perché l'app non è firmata con Apple Developer ID)
5. Clicca **Apri** nel popup di avviso
6. Il browser si apre automaticamente su `http://localhost:8000`

> Il database SQLite viene creato in `~/.teamconfigurator/data.db` la prima volta.
> I dati sopravvivono agli aggiornamenti dell'app.

---

## Workflow aggiornamento

Ogni volta che vuoi aggiornare l'app sul Mac:

```cmd
REM Su Windows — fai le modifiche al codice, poi:
git add .
git commit -m "fix: descrizione modifica"
git tag v1.0.1
git push origin main --tags
```

GitHub Actions compila la nuova versione. Scarichi il nuovo ZIP, sostituisci l'app sul Mac.

---

## Troubleshooting

| Problema | Causa | Soluzione |
|---|---|---|
| Workflow non parte | Nessun tag push | Usa `git push --tags` oppure avvia manualmente |
| Build fallisce su `npm ci` | `package-lock.json` mancante | Esegui `npm install` e committa `package-lock.json` |
| `frontend_dist` non trovato | Build Vue non eseguito | Verifica che `vite.config.js` abbia `outDir: '../backend/frontend_dist'` |
| App non si apre su Mac | Gatekeeper blocca | Tasto destro → Apri (non doppio click) |
| Porta 8000 già in uso | Altra app usa la porta | Chiudi l'altra app o cambia porta in `main.py` |
| DB non trovato | Percorso errato | Verifica `get_db_path()` in `database.py` |

---

## Minuti gratuiti GitHub Actions

GitHub offre **2.000 minuti/mese** gratuiti per repository pubblici (illimitati) e privati.
Un build Mac richiede circa **6-8 minuti**. Con 2.000 minuti hai circa 250 build al mese — più che sufficienti per uso personale.