"# TeamConfigurator" 

Crea File Unico
py C:\dev\ProjetcManagement_Backend\app\util\concat_project.py . --ext .md --ignore venv -o TeamConfigurator_19_03_26.txt
		

1 — Nuova Release su GitHub
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