"""
Script per popolare l'anagrafica con i calciatori delle serie italiane 2024/25
Esegui con: python populate_players_full.py
Opzioni:
  --reset   : elimina tutti i calciatori esistenti prima di inserire
  --skip    : salta i duplicati (default)

  python populate_players.py --reset
"""
import sys
import os

sys.path.insert(0, os.path.dirname(__file__))

from database import SessionLocal, engine, Base
from models import RegistryPlayer

Base.metadata.create_all(bind=engine)

RESET = '--reset' in sys.argv

# ============================================================
# (nome, ruolo, numero, anno_nascita, nazionalità, squadra)
# ============================================================
PLAYERS = [

    # ═══════════════════════════════════════════════════════
    # SERIE A 2024/25
    # ═══════════════════════════════════════════════════════

    # ── Inter ──
    ("Sommer", "POR", 1, 1988, "Svizzera", "Inter"),
    ("Audero", "POR", 24, 1997, "Italia", "Inter"),
    ("Di Gennaro", "POR", 40, 1988, "Italia", "Inter"),
    ("Pavard", "TD", 28, 1996, "Francia", "Inter"),
    ("Dumfries", "TD", 2, 1996, "Olanda", "Inter"),
    ("Darmian", "TD", 36, 1989, "Italia", "Inter"),
    ("Acerbi", "DC", 15, 1988, "Italia", "Inter"),
    ("De Vrij", "DC", 6, 1992, "Olanda", "Inter"),
    ("Bisseck", "DC", 31, 2000, "Germania", "Inter"),
    ("Bastoni", "TS", 23, 1999, "Italia", "Inter"),
    ("Carlos Augusto", "TS", 30, 1999, "Brasile", "Inter"),
    ("Barella", "CC", 23, 1997, "Italia", "Inter"),
    ("Calhanoglu", "CDC", 20, 1994, "Turchia", "Inter"),
    ("Mkhitaryan", "CC", 22, 1989, "Armenia", "Inter"),
    ("Frattesi", "CC", 16, 1999, "Italia", "Inter"),
    ("Zielinski", "CC", 7, 1994, "Polonia", "Inter"),
    ("Asllani", "CDC", 14, 2002, "Albania", "Inter"),
    ("Dimarco", "ALS", 32, 1997, "Italia", "Inter"),
    ("Lautaro Martinez", "ATT", 10, 1997, "Argentina", "Inter"),
    ("Thuram", "ATT", 9, 1997, "Francia", "Inter"),
    ("Taremi", "ATT", 99, 1992, "Iran", "Inter"),
    ("Correa", "ATT", 11, 1994, "Argentina", "Inter"),
    ("Arnautovic", "ATT", 8, 1989, "Austria", "Inter"),

    # ── Milan ──
    ("Maignan", "POR", 16, 1995, "Francia", "Milan"),
    ("Sportiello", "POR", 57, 1992, "Italia", "Milan"),
    ("Emerson Royal", "TD", 12, 1999, "Brasile", "Milan"),
    ("Calabria", "TD", 2, 1996, "Italia", "Milan"),
    ("Tomori", "DC", 23, 1997, "Inghilterra", "Milan"),
    ("Thiaw", "DC", 28, 2001, "Germania", "Milan"),
    ("Pavlovic", "DC", 31, 2001, "Serbia", "Milan"),
    ("Theo Hernandez", "TS", 19, 1997, "Francia", "Milan"),
    ("Terracciano", "TS", 17, 1999, "Italia", "Milan"),
    ("Fofana", "CDC", 29, 2000, "Francia", "Milan"),
    ("Musah", "CC", 80, 2002, "USA", "Milan"),
    ("Reijnders", "CC", 14, 1998, "Olanda", "Milan"),
    ("Loftus-Cheek", "CC", 8, 1996, "Inghilterra", "Milan"),
    ("Bennacer", "CDC", 4, 1997, "Algeria", "Milan"),
    ("Pulisic", "ALD", 11, 1998, "USA", "Milan"),
    ("Leao", "ALS", 10, 1999, "Portogallo", "Milan"),
    ("Okafor", "ALS", 77, 2000, "Svizzera", "Milan"),
    ("Chukwueze", "ALD", 21, 1999, "Nigeria", "Milan"),
    ("Morata", "ATT", 9, 1992, "Spagna", "Milan"),
    ("Abraham", "ATT", 90, 1997, "Inghilterra", "Milan"),
    ("Jovic", "ATT", 34, 1997, "Serbia", "Milan"),

    # ── Juventus ──
    ("Di Gregorio", "POR", 1, 1997, "Italia", "Juventus"),
    ("Perin", "POR", 36, 1992, "Italia", "Juventus"),
    ("Pinsoglio", "POR", 23, 1990, "Italia", "Juventus"),
    ("Cambiaso", "TD", 27, 2000, "Italia", "Juventus"),
    ("Danilo", "TD", 13, 1991, "Brasile", "Juventus"),
    ("Savona", "TD", 37, 2003, "Italia", "Juventus"),
    ("Gatti", "DC", 4, 1998, "Italia", "Juventus"),
    ("Bremer", "DC", 3, 1997, "Brasile", "Juventus"),
    ("Kalulu", "DC", 5, 2000, "Francia", "Juventus"),
    ("Cabal", "TS", 15, 2001, "Colombia", "Juventus"),
    ("Locatelli", "CDC", 5, 1998, "Italia", "Juventus"),
    ("Thuram M.", "CC", 19, 1997, "Francia", "Juventus"),
    ("McKennie", "CC", 16, 1998, "USA", "Juventus"),
    ("Fagioli", "CC", 21, 2001, "Italia", "Juventus"),
    ("Douglas Luiz", "CDC", 26, 1998, "Brasile", "Juventus"),
    ("Koopmeiners", "CC", 8, 1998, "Olanda", "Juventus"),
    ("Conceicao", "ALD", 7, 2002, "Portogallo", "Juventus"),
    ("Yildiz", "TRQ", 10, 2005, "Turchia", "Juventus"),
    ("Nico Gonzalez", "ALS", 11, 1998, "Argentina", "Juventus"),
    ("Vlahovic", "ATT", 9, 2000, "Serbia", "Juventus"),
    ("Milik", "ATT", 14, 1994, "Polonia", "Juventus"),

    # ── Napoli ──
    ("Meret", "POR", 1, 1997, "Italia", "Napoli"),
    ("Contini", "POR", 26, 1995, "Italia", "Napoli"),
    ("Di Lorenzo", "TD", 22, 1993, "Italia", "Napoli"),
    ("Mazzocchi", "TD", 5, 1995, "Italia", "Napoli"),
    ("Rrahmani", "DC", 13, 1994, "Kosovo", "Napoli"),
    ("Buongiorno", "DC", 4, 1999, "Italia", "Napoli"),
    ("Juan Jesus", "DC", 5, 1991, "Brasile", "Napoli"),
    ("Olivera", "TS", 17, 1997, "Uruguay", "Napoli"),
    ("Spinazzola", "TS", 19, 1993, "Italia", "Napoli"),
    ("Anguissa", "CC", 99, 1995, "Camerun", "Napoli"),
    ("Lobotka", "CDC", 68, 1994, "Slovacchia", "Napoli"),
    ("Gilmour", "CC", 14, 2001, "Scozia", "Napoli"),
    ("McTominay", "CC", 8, 1996, "Scozia", "Napoli"),
    ("Politano", "ALD", 21, 1993, "Italia", "Napoli"),
    ("Neres", "ALD", 77, 1997, "Brasile", "Napoli"),
    ("Kvaratskhelia", "ALS", 77, 2001, "Georgia", "Napoli"),
    ("Ngonge", "ALS", 11, 2000, "Belgio", "Napoli"),
    ("Lukaku", "ATT", 11, 1993, "Belgio", "Napoli"),
    ("Raspadori", "ATT", 81, 2000, "Italia", "Napoli"),
    ("Simeone", "ATT", 18, 1995, "Argentina", "Napoli"),

    # ── Roma ──
    ("Svilar", "POR", 99, 2000, "Belgio", "Roma"),
    ("Ryan", "POR", 1, 1992, "Australia", "Roma"),
    ("Celik", "TD", 37, 1997, "Turchia", "Roma"),
    ("Saelemaekers", "TD", 56, 1999, "Belgio", "Roma"),
    ("Mancini", "DC", 23, 1996, "Italia", "Roma"),
    ("Ndicka", "DC", 5, 1999, "Francia", "Roma"),
    ("Hummels", "DC", 15, 1988, "Germania", "Roma"),
    ("Angelino", "TS", 39, 1997, "Spagna", "Roma"),
    ("Zalewski", "TS", 59, 2002, "Polonia", "Roma"),
    ("Paredes", "CDC", 5, 1994, "Argentina", "Roma"),
    ("Koné", "CC", 52, 2001, "Francia", "Roma"),
    ("Cristante", "CC", 4, 1995, "Italia", "Roma"),
    ("Pisilli", "CC", 55, 2004, "Italia", "Roma"),
    ("Pellegrini", "TRQ", 7, 1996, "Italia", "Roma"),
    ("Dybala", "TRQ", 21, 1993, "Argentina", "Roma"),
    ("El Shaarawy", "ALS", 92, 1992, "Italia", "Roma"),
    ("Baldanzi", "TRQ", 11, 2003, "Italia", "Roma"),
    ("Dovbyk", "ATT", 9, 1997, "Ucraina", "Roma"),
    ("Shomurodov", "ATT", 14, 1995, "Uzbekistan", "Roma"),

    # ── Lazio ──
    ("Provedel", "POR", 1, 1994, "Italia", "Lazio"),
    ("Mandas", "POR", 22, 2001, "Grecia", "Lazio"),
    ("Lazzari", "TD", 29, 1993, "Italia", "Lazio"),
    ("Marusic", "TD", 77, 1994, "Montenegro", "Lazio"),
    ("Patric", "DC", 4, 1993, "Spagna", "Lazio"),
    ("Romagnoli", "DC", 13, 1995, "Italia", "Lazio"),
    ("Gila", "DC", 23, 2002, "Spagna", "Lazio"),
    ("Pellegrini L.", "TS", 3, 1991, "Italia", "Lazio"),
    ("Nuno Tavares", "TS", 18, 2000, "Portogallo", "Lazio"),
    ("Guendouzi", "CC", 8, 1999, "Francia", "Lazio"),
    ("Rovella", "CDC", 6, 2001, "Italia", "Lazio"),
    ("Dele-Bashiru", "CC", 4, 2001, "Inghilterra", "Lazio"),
    ("Vecino", "CC", 8, 1991, "Uruguay", "Lazio"),
    ("Isaksen", "ALD", 19, 2001, "Danimarca", "Lazio"),
    ("Zaccagni", "ALS", 20, 1995, "Italia", "Lazio"),
    ("Pedro", "TRQ", 9, 1987, "Spagna", "Lazio"),
    ("Dia", "ATT", 10, 1996, "Senegal", "Lazio"),
    ("Castellanos", "ATT", 11, 1998, "Argentina", "Lazio"),
    ("Noslin", "ATT", 31, 1999, "Olanda", "Lazio"),

    # ── Atalanta ──
    ("Carnesecchi", "POR", 29, 2000, "Italia", "Atalanta"),
    ("Rossi F.", "POR", 95, 1997, "Italia", "Atalanta"),
    ("Bellanova", "TD", 2, 2000, "Italia", "Atalanta"),
    ("Zappacosta", "TD", 77, 1992, "Italia", "Atalanta"),
    ("Scalvini", "DC", 42, 2003, "Italia", "Atalanta"),
    ("Hien", "DC", 5, 1999, "Svezia", "Atalanta"),
    ("Kolasinac", "TS", 23, 1993, "Bosnia", "Atalanta"),
    ("Bonfanti", "DC", 15, 2002, "Italia", "Atalanta"),
    ("De Roon", "CDC", 15, 1991, "Olanda", "Atalanta"),
    ("Ederson", "CC", 13, 2000, "Brasile", "Atalanta"),
    ("Pasalic", "CC", 88, 1995, "Croazia", "Atalanta"),
    ("Koopmeiners", "CC", 7, 1998, "Olanda", "Atalanta"),
    ("Samardzic", "TRQ", 24, 2002, "Serbia", "Atalanta"),
    ("De Ketelaere", "TRQ", 17, 2001, "Belgio", "Atalanta"),
    ("Lookman", "ALD", 11, 1998, "Nigeria", "Atalanta"),
    ("Cuadrado", "ALD", 16, 1988, "Colombia", "Atalanta"),
    ("Retegui", "ATT", 32, 1999, "Italia", "Atalanta"),
    ("Scamacca", "ATT", 9, 1999, "Italia", "Atalanta"),
    ("Touré", "ATT", 99, 2004, "Norvegia", "Atalanta"),

    # ── Fiorentina ──
    ("De Gea", "POR", 1, 1990, "Spagna", "Fiorentina"),
    ("Terracciano P.", "POR", 16, 1990, "Italia", "Fiorentina"),
    ("Dodò", "TD", 2, 1998, "Brasile", "Fiorentina"),
    ("Kayode", "TD", 29, 2003, "Nigeria", "Fiorentina"),
    ("Milenkovic", "DC", 4, 1997, "Serbia", "Fiorentina"),
    ("Martinez Quarta", "DC", 28, 1996, "Argentina", "Fiorentina"),
    ("Comuzzo", "DC", 99, 2005, "Italia", "Fiorentina"),
    ("Biraghi", "TS", 3, 1992, "Italia", "Fiorentina"),
    ("Parisi", "TS", 5, 2000, "Italia", "Fiorentina"),
    ("Cataldi", "CDC", 6, 1994, "Italia", "Fiorentina"),
    ("Richardson", "CC", 8, 2000, "USA", "Fiorentina"),
    ("Bove", "CC", 4, 2002, "Italia", "Fiorentina"),
    ("Adli", "TRQ", 10, 2000, "Francia", "Fiorentina"),
    ("Gonzalez", "ALD", 10, 1998, "Argentina", "Fiorentina"),
    ("Sottil", "ALS", 11, 2000, "Italia", "Fiorentina"),
    ("Colpani", "TRQ", 7, 2000, "Italia", "Fiorentina"),
    ("Kean", "ATT", 9, 2000, "Italia", "Fiorentina"),
    ("Gudmundsson", "TRQ", 21, 1997, "Islanda", "Fiorentina"),

    # ── Bologna ──
    ("Skorupski", "POR", 28, 1991, "Polonia", "Bologna"),
    ("Ravaglia", "POR", 22, 1999, "Italia", "Bologna"),
    ("Posch", "TD", 13, 1997, "Austria", "Bologna"),
    ("Holm", "TD", 7, 2000, "Svezia", "Bologna"),
    ("Beukema", "DC", 34, 1998, "Olanda", "Bologna"),
    ("Lucumi", "DC", 5, 1998, "Colombia", "Bologna"),
    ("Erlic", "DC", 6, 1997, "Croazia", "Bologna"),
    ("Kristiansen", "TS", 19, 2001, "Danimarca", "Bologna"),
    ("Miranda", "TS", 17, 2004, "Spagna", "Bologna"),
    ("Ferguson", "CC", 17, 2004, "Irlanda", "Bologna"),
    ("Freuler", "CDC", 11, 1992, "Svizzera", "Bologna"),
    ("Pobega", "CC", 4, 1999, "Italia", "Bologna"),
    ("Moro", "CC", 23, 2002, "Italia", "Bologna"),
    ("Orsolini", "ALD", 7, 1997, "Italia", "Bologna"),
    ("Ndoye", "ALS", 22, 2002, "Svizzera", "Bologna"),
    ("Fabbian", "TRQ", 8, 2003, "Italia", "Bologna"),
    ("Odgaard", "ATT", 9, 1999, "Danimarca", "Bologna"),
    ("Dallinga", "ATT", 11, 2000, "Olanda", "Bologna"),
    ("Castro", "ATT", 19, 2004, "Argentina", "Bologna"),

    # ── Torino ──
    ("Milinkovic-Savic V.", "POR", 32, 1997, "Serbia", "Torino"),
    ("Paleari", "POR", 22, 1995, "Italia", "Torino"),
    ("Vojvoda", "TD", 22, 1995, "Kosovo", "Torino"),
    ("Pedersen", "TD", 17, 1999, "Norvegia", "Torino"),
    ("Coco", "DC", 3, 2001, "Spagna", "Torino"),
    ("Maripan", "DC", 13, 1994, "Cile", "Torino"),
    ("Masina", "TS", 5, 1994, "Marocco", "Torino"),
    ("Sosa", "TS", 6, 1998, "Austria", "Torino"),
    ("Ricci", "CDC", 28, 2001, "Italia", "Torino"),
    ("Ilic", "CC", 8, 2001, "Serbia", "Torino"),
    ("Linetty", "CC", 14, 1995, "Polonia", "Torino"),
    ("Gineitis", "CC", 32, 2004, "Lituania", "Torino"),
    ("Lazaro", "ALD", 17, 1996, "Austria", "Torino"),
    ("Karamoh", "ALS", 19, 1998, "Costa d'Avorio", "Torino"),
    ("Adams", "ATT", 9, 2001, "USA", "Torino"),
    ("Zapata", "ATT", 91, 1991, "Colombia", "Torino"),
    ("Sanabria", "ATT", 7, 1996, "Paraguay", "Torino"),

    # ── Udinese ──
    ("Okoye", "POR", 24, 2000, "Nigeria", "Udinese"),
    ("Padelli", "POR", 1, 1985, "Italia", "Udinese"),
    ("Kristensen", "TD", 5, 1997, "Danimarca", "Udinese"),
    ("Ehizibue", "TD", 29, 1995, "Olanda", "Udinese"),
    ("Bijol", "DC", 3, 1999, "Slovenia", "Udinese"),
    ("Giannetti", "DC", 17, 1991, "Italia", "Udinese"),
    ("Touré K.", "DC", 44, 1998, "Guinea", "Udinese"),
    ("Zemura", "TS", 27, 2000, "Zimbabwe", "Udinese"),
    ("Modesto", "TS", 22, 2003, "Italia", "Udinese"),
    ("Lovric", "CDC", 8, 1998, "Slovenia", "Udinese"),
    ("Payero", "CC", 20, 1998, "Argentina", "Udinese"),
    ("Karlstrom", "CC", 7, 1995, "Svezia", "Udinese"),
    ("Ekkelenkamp", "TRQ", 10, 1999, "Olanda", "Udinese"),
    ("Brenner", "ATT", 9, 2000, "Brasile", "Udinese"),
    ("Lucca", "ATT", 11, 2000, "Italia", "Udinese"),
    ("Thauvin", "ALD", 17, 1993, "Francia", "Udinese"),

    # ── Genoa ──
    ("Leali", "POR", 1, 1993, "Italia", "Genoa"),
    ("Gollini", "POR", 95, 1995, "Italia", "Genoa"),
    ("De Winter", "TD", 5, 2002, "Belgio", "Genoa"),
    ("Sabelli", "TD", 29, 1993, "Italia", "Genoa"),
    ("Vasquez", "DC", 3, 2000, "Argentina", "Genoa"),
    ("Bani", "DC", 15, 1993, "Italia", "Genoa"),
    ("Matturro", "DC", 5, 2004, "Uruguay", "Genoa"),
    ("Martin", "TS", 27, 2001, "Spagna", "Genoa"),
    ("Pittino", "TS", 66, 2004, "Italia", "Genoa"),
    ("Badelj", "CDC", 8, 1989, "Croazia", "Genoa"),
    ("Frendrup", "CC", 7, 2001, "Danimarca", "Genoa"),
    ("Thorsby", "CC", 9, 1996, "Norvegia", "Genoa"),
    ("Malinovskyi", "TRQ", 10, 1993, "Ucraina", "Genoa"),
    ("Gudmundsson A.", "ALD", 11, 1997, "Islanda", "Genoa"),
    ("Zanoli", "ALD", 24, 2000, "Italia", "Genoa"),
    ("Pinamonti", "ATT", 9, 1999, "Italia", "Genoa"),
    ("Vitinha", "ATT", 19, 2000, "Portogallo", "Genoa"),
    ("Ekhator", "ALS", 21, 2005, "Norvegia", "Genoa"),

    # ── Parma ──
    ("Suzuki", "POR", 12, 1998, "Giappone", "Parma"),
    ("Corvi", "POR", 1, 1994, "Italia", "Parma"),
    ("Coulibaly", "TD", 27, 2000, "Senegal", "Parma"),
    ("Delprato", "DC", 2, 1999, "Italia", "Parma"),
    ("Circati", "DC", 5, 2002, "Italia", "Parma"),
    ("Balogh", "DC", 6, 1999, "Ungheria", "Parma"),
    ("Valeri", "TS", 31, 1998, "Italia", "Parma"),
    ("Hainaut", "TS", 3, 1994, "Francia", "Parma"),
    ("Estevez", "CDC", 29, 1996, "Argentina", "Parma"),
    ("Bernabe", "CC", 10, 2001, "Spagna", "Parma"),
    ("Cyprien", "CC", 8, 1995, "Francia", "Parma"),
    ("Hernani", "CC", 16, 1994, "Brasile", "Parma"),
    ("Man", "ALD", 22, 1997, "Romania", "Parma"),
    ("Almqvist", "ALS", 7, 1999, "Svezia", "Parma"),
    ("Mihaila", "ALD", 28, 2000, "Romania", "Parma"),
    ("Bonny", "ATT", 9, 2003, "Francia", "Parma"),
    ("Charpentier", "ATT", 11, 1999, "Francia", "Parma"),

    # ── Como ──
    ("Audero C.", "POR", 24, 1997, "Italia", "Como"),
    ("Reina", "POR", 25, 1982, "Spagna", "Como"),
    ("Van der Brempt", "TD", 2, 2002, "Belgio", "Como"),
    ("Goldaniga", "DC", 25, 1993, "Italia", "Como"),
    ("Odenthal", "DC", 17, 1998, "Germania", "Como"),
    ("Fabregas", "CDC", 4, 1987, "Spagna", "Como"),
    ("Nico Paz", "TRQ", 10, 2004, "Argentina", "Como"),
    ("Da Cunha", "CC", 28, 2000, "Francia", "Como"),
    ("Strefezza", "ALD", 7, 1997, "Brasile", "Como"),
    ("Cutrone", "ATT", 11, 1998, "Italia", "Como"),
    ("Belhadj", "ATT", 9, 1999, "Algeria", "Como"),

    # ── Hellas Verona ──
    ("Montipo", "POR", 1, 1996, "Italia", "Hellas Verona"),
    ("Berardi", "POR", 99, 2004, "Italia", "Hellas Verona"),
    ("Tchatchoua", "TD", 22, 1999, "Camerun", "Hellas Verona"),
    ("Ghilardi", "DC", 3, 2003, "Italia", "Hellas Verona"),
    ("Coppola", "DC", 4, 2003, "Italia", "Hellas Verona"),
    ("Bradaric", "TS", 17, 1992, "Croazia", "Hellas Verona"),
    ("Duda", "CC", 7, 1994, "Slovacchia", "Hellas Verona"),
    ("Serdar", "CC", 8, 1997, "Germania", "Hellas Verona"),
    ("Belahyane", "CDC", 6, 2004, "Marocco", "Hellas Verona"),
    ("Suslov", "TRQ", 10, 2002, "Slovacchia", "Hellas Verona"),
    ("Lazovic", "ALS", 21, 1990, "Serbia", "Hellas Verona"),
    ("Mosquera", "ATT", 9, 2001, "Colombia", "Hellas Verona"),
    ("Tengstedt", "ATT", 19, 2001, "Danimarca", "Hellas Verona"),

    # ── Cagliari ──
    ("Sherri", "POR", 22, 1999, "Albania", "Cagliari"),
    ("Scuffet", "POR", 1, 1996, "Italia", "Cagliari"),
    ("Zappa", "TD", 28, 1999, "Italia", "Cagliari"),
    ("Azzi", "TD", 19, 2002, "Francia", "Cagliari"),
    ("Mina", "DC", 13, 1994, "Colombia", "Cagliari"),
    ("Luperto", "DC", 6, 1996, "Italia", "Cagliari"),
    ("Augello", "TS", 3, 1994, "Italia", "Cagliari"),
    ("Obert", "TS", 25, 2002, "Slovacchia", "Cagliari"),
    ("Prati", "CC", 8, 2001, "Italia", "Cagliari"),
    ("Makoumbou", "CDC", 29, 1998, "Congo", "Cagliari"),
    ("Deiola", "CC", 5, 1994, "Italia", "Cagliari"),
    ("Gaetano", "TRQ", 7, 2000, "Italia", "Cagliari"),
    ("Viola", "TRQ", 10, 1996, "Italia", "Cagliari"),
    ("Luvumbo", "ALS", 23, 2002, "Angola", "Cagliari"),
    ("Zortea", "ALD", 17, 1999, "Italia", "Cagliari"),
    ("Piccoli", "ATT", 91, 2001, "Italia", "Cagliari"),
    ("Lapadula", "ATT", 9, 1990, "Italia", "Cagliari"),

    # ── Empoli ──
    ("Vasquez E.", "POR", 1, 1999, "Colombia", "Empoli"),
    ("Caprile", "POR", 12, 2001, "Italia", "Empoli"),
    ("Gyasi", "TD", 10, 1995, "Ghana", "Empoli"),
    ("Sambia", "TD", 2, 1997, "Francia", "Empoli"),
    ("Ismajli", "DC", 3, 1997, "Albania", "Empoli"),
    ("Goglichidze", "DC", 5, 2004, "Georgia", "Empoli"),
    ("Viti", "DC", 22, 2002, "Italia", "Empoli"),
    ("Pezzella", "TS", 29, 1992, "Italia", "Empoli"),
    ("Cacace", "TS", 50, 2000, "Nuova Zelanda", "Empoli"),
    ("Grassi", "CDC", 8, 1995, "Italia", "Empoli"),
    ("Henderson", "CC", 6, 1994, "Inghilterra", "Empoli"),
    ("Fazzini", "TRQ", 7, 2003, "Italia", "Empoli"),
    ("Esposito S.", "ATT", 10, 2002, "Italia", "Empoli"),
    ("Colombo", "ATT", 9, 2002, "Italia", "Empoli"),
    ("Solbakken", "ALS", 11, 2001, "Norvegia", "Empoli"),

    # ── Venezia ──
    ("Joronen", "POR", 1, 1993, "Finlandia", "Venezia"),
    ("Candela", "TD", 2, 2000, "Italia", "Venezia"),
    ("Idzes", "DC", 5, 2001, "USA", "Venezia"),
    ("Svoboda", "DC", 3, 1998, "Rep. Ceca", "Venezia"),
    ("Hrustic", "CC", 8, 1996, "Australia", "Venezia"),
    ("Busio", "CDC", 10, 2002, "USA", "Venezia"),
    ("Ellertsson", "CC", 7, 1998, "Islanda", "Venezia"),
    ("Pohjanpalo", "ATT", 9, 1994, "Finlandia", "Venezia"),
    ("Oristanio", "TRQ", 27, 2002, "Italia", "Venezia"),
    ("Gytkjaer", "ATT", 11, 1990, "Danimarca", "Venezia"),

    # ── Lecce ──
    ("Falcone", "POR", 1, 1995, "Italia", "Lecce"),
    ("Borbei", "DC", 5, 2003, "Romania", "Lecce"),
    ("Baschirotto", "DC", 15, 1996, "Italia", "Lecce"),
    ("Gallo", "TS", 3, 1997, "Italia", "Lecce"),
    ("Ramadani", "CDC", 8, 1999, "Kosovo", "Lecce"),
    ("Berisha", "CC", 29, 1994, "Albania", "Lecce"),
    ("Pierret", "CC", 4, 2002, "Francia", "Lecce"),
    ("Morente", "ALD", 77, 1997, "Spagna", "Lecce"),
    ("Coulibaly L.", "ALS", 7, 1999, "Mali", "Lecce"),
    ("Krstovic", "ATT", 9, 2001, "Montenegro", "Lecce"),
    ("Rebic", "ALS", 21, 1993, "Croazia", "Lecce"),

    # ═══════════════════════════════════════════════════════
    # SERIE B 2024/25
    # ═══════════════════════════════════════════════════════

    # ── Sassuolo ──
    ("Satalino", "POR", 1, 1991, "Italia", "Sassuolo"),
    ("Toljan", "TD", 2, 1994, "Croazia", "Sassuolo"),
    ("Erlic S.", "DC", 6, 1997, "Croazia", "Sassuolo"),
    ("Odenthal R.", "DC", 17, 1998, "Germania", "Sassuolo"),
    ("Doig", "TS", 30, 2002, "Scozia", "Sassuolo"),
    ("Thorstvedt", "CC", 8, 2000, "Norvegia", "Sassuolo"),
    ("Boloca", "CDC", 5, 2000, "Romania", "Sassuolo"),
    ("Iannoni", "CC", 23, 2001, "Italia", "Sassuolo"),
    ("Volpato", "TRQ", 10, 2003, "Australia", "Sassuolo"),
    ("Laurienté", "ALS", 7, 1998, "Francia", "Sassuolo"),
    ("Mulattieri", "ATT", 9, 2000, "Italia", "Sassuolo"),

    # ── Pisa ──
    ("Nicolas", "POR", 1, 1993, "Uruguay", "Pisa"),
    ("Calabresi", "TD", 2, 1996, "Italia", "Pisa"),
    ("Caracciolo", "DC", 5, 1986, "Italia", "Pisa"),
    ("Canestrelli", "DC", 6, 1998, "Italia", "Pisa"),
    ("Angori", "TS", 3, 2001, "Italia", "Pisa"),
    ("Marin", "CDC", 8, 1994, "Romania", "Pisa"),
    ("Arena", "CC", 16, 2001, "Italia", "Pisa"),
    ("Piccinini", "CC", 4, 2004, "Italia", "Pisa"),
    ("Tramoni", "ALD", 7, 1999, "Francia", "Pisa"),
    ("Moreo", "ATT", 10, 1992, "Italia", "Pisa"),
    ("Lind", "ATT", 9, 2003, "Danimarca", "Pisa"),

    # ── Spezia ──
    ("Gori", "POR", 1, 1994, "Italia", "Spezia"),
    ("Elia", "TD", 2, 2000, "Italia", "Spezia"),
    ("Mateju", "DC", 5, 1996, "Rep. Ceca", "Spezia"),
    ("Bertola", "DC", 6, 2002, "Italia", "Spezia"),
    ("Reca", "TS", 3, 1995, "Polonia", "Spezia"),
    ("Bandinelli", "CC", 8, 1995, "Italia", "Spezia"),
    ("Nagy", "CDC", 29, 1993, "Ungheria", "Spezia"),
    ("Delle Monache", "ALD", 7, 2004, "Italia", "Spezia"),
    ("Soleri", "ATT", 9, 1997, "Italia", "Spezia"),
    ("Esposito F.", "ATT", 10, 2000, "Italia", "Spezia"),

    # ── Bari ──
    ("Radunovic", "POR", 1, 1996, "Serbia", "Bari"),
    ("Pucino", "TD", 2, 1993, "Italia", "Bari"),
    ("Mantovani", "DC", 5, 1989, "Italia", "Bari"),
    ("Vicari", "DC", 6, 1992, "Italia", "Bari"),
    ("Dorval", "TS", 3, 2004, "Francia", "Bari"),
    ("Benali", "CC", 8, 1996, "Tunisia", "Bari"),
    ("Maiello", "CDC", 4, 1991, "Italia", "Bari"),
    ("Sibilli", "ALD", 7, 1997, "Italia", "Bari"),
    ("Novakovich", "ATT", 9, 1994, "USA", "Bari"),
    ("Falletti", "TRQ", 10, 1994, "Uruguay", "Bari"),

    # ── Palermo ──
    ("Desplanches", "POR", 12, 2002, "Francia", "Palermo"),
    ("Diakité", "TD", 22, 2000, "Francia", "Palermo"),
    ("Nedelcearu", "DC", 5, 1997, "Romania", "Palermo"),
    ("Ceccaroni", "DC", 27, 1995, "Italia", "Palermo"),
    ("Lund", "TS", 30, 1999, "USA", "Palermo"),
    ("Gomes F.", "CDC", 10, 1998, "Portogallo", "Palermo"),
    ("Segre", "CC", 8, 1997, "Italia", "Palermo"),
    ("Ranocchia", "CC", 4, 2001, "Italia", "Palermo"),
    ("Di Mariano", "ALD", 11, 1993, "Italia", "Palermo"),
    ("Brunori", "ATT", 9, 1994, "Italia", "Palermo"),
    ("Insigne R.", "ALS", 7, 1996, "Italia", "Palermo"),

    # ── Cremonese ──
    ("Jungdal", "POR", 1, 2001, "Danimarca", "Cremonese"),
    ("Sernicola", "TD", 2, 1997, "Italia", "Cremonese"),
    ("Bianchetti", "DC", 5, 1993, "Italia", "Cremonese"),
    ("Antov", "DC", 6, 1998, "Bulgaria", "Cremonese"),
    ("Quagliata", "TS", 3, 1999, "Italia", "Cremonese"),
    ("Castagnetti", "CDC", 8, 1991, "Italia", "Cremonese"),
    ("Pickel", "CC", 4, 1996, "Germania", "Cremonese"),
    ("Johnsen", "CC", 7, 1995, "Norvegia", "Cremonese"),
    ("Bonazzoli", "ATT", 9, 1997, "Italia", "Cremonese"),
    ("Vasquez N.", "ATT", 10, 1998, "Argentina", "Cremonese"),

    # ── Catanzaro ──
    ("Fulignati", "POR", 1, 1992, "Italia", "Catanzaro"),
    ("Brighenti", "DC", 5, 1997, "Italia", "Catanzaro"),
    ("Antonini", "TS", 33, 1992, "Italia", "Catanzaro"),
    ("Pompetti", "CC", 8, 2000, "Italia", "Catanzaro"),
    ("Ghion", "CDC", 4, 1998, "Italia", "Catanzaro"),
    ("Iemmello", "ATT", 9, 1992, "Italia", "Catanzaro"),
    ("Biasci", "ATT", 10, 1993, "Italia", "Catanzaro"),

    # ── Brescia ──
    ("Lezzerini", "POR", 1, 1996, "Italia", "Brescia"),
    ("Dickmann", "TD", 2, 1991, "Italia", "Brescia"),
    ("Papetti", "DC", 5, 2003, "Italia", "Brescia"),
    ("Cistana", "DC", 6, 1997, "Italia", "Brescia"),
    ("Moncini", "ATT", 9, 1995, "Italia", "Brescia"),
    ("Borrelli", "ATT", 10, 2001, "Italia", "Brescia"),

    # ═══════════════════════════════════════════════════════
    # SERIE C 2024/25 (selezione principali)
    # ═══════════════════════════════════════════════════════

    # ── Avellino ──
    ("Iannarilli", "POR", 1, 1992, "Italia", "Avellino"),
    ("Benedetti", "DC", 5, 1992, "Italia", "Avellino"),
    ("Enrici", "TD", 2, 2002, "Italia", "Avellino"),
    ("Rocca", "CC", 8, 1998, "Italia", "Avellino"),
    ("Patierno", "ATT", 9, 1995, "Italia", "Avellino"),
    ("Russo", "ATT", 10, 1991, "Italia", "Avellino"),

    # ── Benevento ──
    ("Manfredini", "POR", 1, 1993, "Italia", "Benevento"),
    ("Capellini", "DC", 5, 1997, "Italia", "Benevento"),
    ("Obi", "CDC", 8, 1991, "Nigeria", "Benevento"),
    ("Simonetti", "CC", 4, 1996, "Italia", "Benevento"),
    ("Manconi", "ATT", 9, 1999, "Italia", "Benevento"),

    # ── Reggiana ──
    ("Motta G.", "POR", 1, 1993, "Italia", "Reggiana"),
    ("Meroni L.", "DC", 5, 2004, "Italia", "Reggiana"),
    ("Kabashi", "CC", 8, 1997, "Kosovo", "Reggiana"),
    ("Gondo", "ATT", 9, 1996, "Costa d'Avorio", "Reggiana"),
    ("Girma", "ALS", 11, 2003, "Italia", "Reggiana"),

    # ── Cesena ──
    ("Pisseri", "POR", 1, 1993, "Italia", "Cesena"),
    ("Ciofi", "TD", 2, 1996, "Italia", "Cesena"),
    ("Prestia", "DC", 5, 1989, "Italia", "Cesena"),
    ("Tavcar", "CC", 8, 2000, "Slovenia", "Cesena"),
    ("Shpendi E.", "ATT", 9, 2003, "Italia", "Cesena"),

    # ── Entella ──
    ("Borra", "POR", 1, 1997, "Italia", "Entella"),
    ("Bariti", "DC", 5, 1994, "Italia", "Entella"),
    ("Corbari", "CC", 8, 2000, "Italia", "Entella"),
    ("Parodi", "ATT", 9, 1999, "Italia", "Entella"),

    # ═══════════════════════════════════════════════════════
    # ── PREMIER LEAGUE ───────────────────────────────────────
    # ═══════════════════════════════════════════════════════

    # Manchester City
    ("Ederson", "POR", 31, 1993, "Brasile", "Man City"),
    ("Walker", "TD", 2, 1990, "Inghilterra", "Man City"),
    ("Dias", "DC", 3, 1997, "Portogallo", "Man City"),
    ("Akanji", "DC", 25, 1995, "Svizzera", "Man City"),
    ("Gvardiol", "TS", 24, 2002, "Croazia", "Man City"),
    ("Rodri", "CDC", 16, 1996, "Spagna", "Man City"),
    ("De Bruyne", "TRQ", 17, 1991, "Belgio", "Man City"),
    ("Bernardo Silva", "CC", 20, 1994, "Portogallo", "Man City"),
    ("Foden", "ALS", 47, 2000, "Inghilterra", "Man City"),
    ("Doku", "ALD", 11, 2002, "Belgio", "Man City"),
    ("Haaland", "ATT", 9, 2000, "Norvegia", "Man City"),

    # Arsenal
    ("Raya", "POR", 22, 1995, "Spagna", "Arsenal"),
    ("White", "TD", 4, 1997, "Inghilterra", "Arsenal"),
    ("Saliba", "DC", 12, 2001, "Francia", "Arsenal"),
    ("Gabriel", "DC", 6, 1997, "Brasile", "Arsenal"),
    ("Zinchenko", "TS", 35, 1996, "Ucraina", "Arsenal"),
    ("Partey", "CDC", 5, 1993, "Ghana", "Arsenal"),
    ("Odegaard", "TRQ", 8, 1998, "Norvegia", "Arsenal"),
    ("Rice", "CC", 41, 1999, "Inghilterra", "Arsenal"),
    ("Saka", "ALD", 7, 2001, "Inghilterra", "Arsenal"),
    ("Martinelli", "ALS", 11, 2001, "Brasile", "Arsenal"),
    ("Jesus", "ATT", 9, 1997, "Brasile", "Arsenal"),
    ("Havertz", "ATT", 29, 1999, "Germania", "Arsenal"),

    # Liverpool
    ("Alisson", "POR", 1, 1992, "Brasile", "Liverpool"),
    ("Alexander-Arnold", "TD", 66, 1998, "Inghilterra", "Liverpool"),
    ("Van Dijk", "DC", 4, 1991, "Olanda", "Liverpool"),
    ("Konate", "DC", 5, 2001, "Francia", "Liverpool"),
    ("Robertson", "TS", 26, 1994, "Scozia", "Liverpool"),
    ("Mac Allister", "CDC", 10, 1998, "Argentina", "Liverpool"),
    ("Szoboszlai", "TRQ", 8, 2000, "Ungheria", "Liverpool"),
    ("Gravenberch", "CC", 38, 2002, "Olanda", "Liverpool"),
    ("Salah", "ALD", 11, 1992, "Egitto", "Liverpool"),
    ("Diaz", "ALS", 23, 1997, "Colombia", "Liverpool"),
    ("Nunez", "ATT", 9, 2000, "Uruguay", "Liverpool"),
    ("Jota", "ATT", 20, 1996, "Portogallo", "Liverpool"),

    # Chelsea
    ("Sanchez", "POR", 13, 1997, "Cile", "Chelsea"),
    ("Reece James", "TD", 24, 2000, "Inghilterra", "Chelsea"),
    ("Silva", "DC", 6, 1984, "Brasile", "Chelsea"),
    ("Colwill", "DC", 26, 2003, "Inghilterra", "Chelsea"),
    ("Chilwell", "TS", 21, 1996, "Inghilterra", "Chelsea"),
    ("Caicedo", "CDC", 25, 2001, "Ecuador", "Chelsea"),
    ("Fernandez", "CC", 8, 2001, "Argentina", "Chelsea"),
    ("Gallagher", "CC", 23, 2000, "Inghilterra", "Chelsea"),
    ("Palmer", "TRQ", 20, 2002, "Inghilterra", "Chelsea"),
    ("Sterling", "ALD", 17, 1994, "Inghilterra", "Chelsea"),
    ("Jackson", "ATT", 15, 2001, "Senegal", "Chelsea"),
    ("Nkunku", "ATT", 18, 1997, "Francia", "Chelsea"),

    # Manchester United
    ("Onana", "POR", 24, 1996, "Camerun", "Man United"),
    ("Wan-Bissaka", "TD", 29, 1997, "Inghilterra", "Man United"),
    ("Varane", "DC", 19, 1993, "Francia", "Man United"),
    ("Maguire", "DC", 5, 1993, "Inghilterra", "Man United"),
    ("Shaw", "TS", 23, 1995, "Inghilterra", "Man United"),
    ("Casemiro", "CDC", 18, 1992, "Brasile", "Man United"),
    ("Bruno Fernandes", "TRQ", 8, 1994, "Portogallo", "Man United"),
    ("Mainoo", "CC", 37, 2005, "Inghilterra", "Man United"),
    ("Rashford", "ALS", 10, 1997, "Inghilterra", "Man United"),
    ("Garnacho", "ALD", 49, 2004, "Argentina", "Man United"),
    ("Hojlund", "ATT", 11, 2003, "Danimarca", "Man United"),

    # Tottenham
    ("Vicario", "POR", 13, 1996, "Italia", "Tottenham"),
    ("Porro", "TD", 23, 2000, "Spagna", "Tottenham"),
    ("Romero", "DC", 17, 1998, "Argentina", "Tottenham"),
    ("Van de Ven", "DC", 37, 2001, "Olanda", "Tottenham"),
    ("Udogie", "TS", 38, 2002, "Italia", "Tottenham"),
    ("Bissouma", "CDC", 8, 1996, "Mali", "Tottenham"),
    ("Maddison", "TRQ", 10, 1996, "Inghilterra", "Tottenham"),
    ("Bentancur", "CC", 30, 1997, "Uruguay", "Tottenham"),
    ("Kulusevski", "ALD", 21, 2000, "Svezia", "Tottenham"),
    ("Son", "ALS", 7, 1992, "Corea del Sud", "Tottenham"),
    ("Richarlison", "ATT", 9, 1997, "Brasile", "Tottenham"),

]


def populate():
    db = SessionLocal()
    try:
        existing = db.query(RegistryPlayer).count()
        if existing > 0 and not RESET:
            print(f"⚠️  Già presenti {existing} calciatori.")
            risposta = input("Aggiungere comunque? (s/n): ").strip().lower()
            if risposta != 's':
                print("Operazione annullata.")
                return

        if RESET:
            deleted = db.query(RegistryPlayer).delete()
            db.commit()
            print(f"🗑️  Eliminati {deleted} calciatori esistenti")

        # Evita duplicati per nome+squadra
        existing_keys = set(
            (p.name, p.team_name)
            for p in db.query(RegistryPlayer.name, RegistryPlayer.team_name).all()
        )

        count = 0
        skipped = 0
        for nome, ruolo, numero, anno, nazione, squadra in PLAYERS:
            if (nome, squadra) in existing_keys:
                skipped += 1
                continue
            db.add(RegistryPlayer(
                name=nome,
                role=ruolo,
                number=numero,
                birth_year=anno,
                nationality=nazione,
                team_name=squadra,
            ))
            count += 1

        db.commit()
        total = db.query(RegistryPlayer).count()
        print(f"✅ Aggiunti {count} calciatori ({skipped} già presenti ignorati)")
        print(f"   Totale anagrafica: {total} calciatori")
        print(f"   Serie A:  20 squadre")
        print(f"   Serie B:  ~10 squadre")
        print(f"   Serie C:  ~6 squadre")

    except Exception as e:
        db.rollback()
        print(f"❌ Errore: {e}")
        import traceback;
        traceback.print_exc()
    finally:
        db.close()


if __name__ == "__main__":
    populate()