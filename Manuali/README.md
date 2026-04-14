"# TeamConfigurator" 

Crea File Unico
cd TeamConfigurator
py C:\dev\ProjetcManagement_Backend\app\util\concat_project.py . --ext .md --ignore venv -o TeamConfigurator_19_03_26.txt
		

1 — Nuova Release su GitHub
https://github.com/pasflocc1-blip/TeamConfigurator.git
cd C:\Dev\TeamConfigurator

git add .
git commit -m "feat: release v1.3.0 - rose 2025/26, export Word, pannello DB, nuovi moduli"
git push origin main

git tag v1.3.0
git push origin v1.3.0 
```

GitHub Actions partirà automaticamente, compilerà il `.app` e creerà la Release. Vai su **Actions** per seguire il progresso (~10 minuti).

---

## 2 — Inizializzare il DB sul Mac

Dopo aver installato la nuova versione del `.app`, il DB è vuoto. Per popolarlo con i calciatori hai due strade:

### Strada A — Copia il DB da Windows (più veloce)

Il DB di Windows si trova in:
```
C:\Dev\TeamConfigurator\backend\myapp.db
```

Copialo sul Mac in:
```
/Users/sergiofloccari/.myapp/myapp.db

Strada B — Esegui lo script sul Mac
# Apri il Terminale sul Mac

# Vai nella cartella del bundle
cd /Applications/TeamConfigurator.app/Contents/MacOS

# Esegui lo script di popolamento
./TeamConfigurator populate_2526.py --reset

Oppure se hai Python installato separatamente:
cd /tmp
# Copia populate_2526.py sul Mac (via AirDrop/USB)
python3 populate_2526.py --reset


Fai: git add ., git commit -m "test action", git push origin main.

# Crea un tag chiamato v1.0.0 (puoi cambiare il numero)
C:\Dev\TeamConfigurator>git tag -a v2.0.0 -m "Versione stabile con export Word e fix anagrafica"

# Invia il tag specifico al server
C:\Dev\TeamConfigurator>git push origin v2.0.0

# Come verificare il successo
# Dopo il push, vai su GitHub:
# Sulla destra della pagina principale vedrai la voce "Releases". Lì troverai la tua versione v1.0.0.
# Nella tab "Actions", vedrai la build partire con il nome del tag anziché il nome del branch.


# Creare un progetto da zero
Creare un nuovo Progetto da Git
cd dove scaricare il progetto
git clone https://github.com/pasflocc1-blip/TeamConfigurator


BackEnd
Assicurati di essere dentro la cartella BackEnd serve la versione di Python11 o 12
python -m venv venv
.\venv\Scripts\activate
python -m pip install -r requirements.txt
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe -m uvicorn main:app --reload

FrontEnd
Assicurati di essere dentro la cartella frontend
npm install
npm run dev