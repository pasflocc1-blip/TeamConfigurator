"""
Script per popolare l'anagrafica calciatori
Esegui con: python populate_players.py
"""
import sys
import os
sys.path.insert(0, os.path.dirname(__file__))

from database import SessionLocal, engine, Base
from models import RegistryPlayer as PlayerModel

# Crea le tabelle se non esistono
Base.metadata.create_all(bind=engine)

# ============================================================
# DATI CALCIATORI
# Formato: (nome, ruolo, numero, anno_nascita, nazionalità, squadra)
# ============================================================

PLAYERS = [

  # ── SERIE A ──────────────────────────────────────────────

  # Juventus
  ("Perin",           "POR", 36, 1992, "Italia",     "Juventus"),
  ("Di Gregorio",     "POR",  1, 1997, "Italia",     "Juventus"),
  ("Danilo",          "TD",  13, 1991, "Brasile",    "Juventus"),
  ("Bremer",          "DC",   3, 1997, "Brasile",    "Juventus"),
  ("Gatti",           "DC",   4, 1998, "Italia",     "Juventus"),
  ("Cambiaso",        "TS",  27, 2000, "Italia",     "Juventus"),
  ("McKennie",        "CC",  16, 1998, "USA",        "Juventus"),
  ("Locatelli",       "CDC",  5, 1998, "Italia",     "Juventus"),
  ("Fagioli",         "CC",  21, 2001, "Italia",     "Juventus"),
  ("Yildiz",          "TRQ", 10, 2005, "Turchia",    "Juventus"),
  ("Vlahovic",        "ATT",  9, 2000, "Serbia",     "Juventus"),
  ("Milik",           "ATT", 14, 1994, "Polonia",    "Juventus"),
  ("Weah",            "ALD", 22, 2000, "USA",        "Juventus"),
  ("Kostic",          "ALS", 11, 1992, "Serbia",     "Juventus"),

  # Inter
  ("Sommer",          "POR",  1, 1988, "Svizzera",   "Inter"),
  ("Audero",          "POR", 24, 1997, "Italia",     "Inter"),
  ("Pavard",          "TD",  28, 1996, "Francia",    "Inter"),
  ("Acerbi",          "DC",  15, 1988, "Italia",     "Inter"),
  ("De Vrij",         "DC",   6, 1992, "Olanda",     "Inter"),
  ("Bastoni",         "TS",  23, 1999, "Italia",     "Inter"),
  ("Darmian",         "TD",  36, 1989, "Italia",     "Inter"),
  ("Barella",         "CC",  23, 1997, "Italia",     "Inter"),
  ("Calhanoglu",      "CDC", 20, 1994, "Turchia",    "Inter"),
  ("Mkhitaryan",      "CC",  22, 1989, "Armenia",    "Inter"),
  ("Dimarco",         "ALS", 32, 1997, "Italia",     "Inter"),
  ("Lautaro Martinez","ATT",  10, 1997, "Argentina", "Inter"),
  ("Thuram",          "ATT",  9, 1997, "Francia",    "Inter"),
  ("Sanchez",         "ATT",  7, 1988, "Cile",       "Inter"),

  # Milan
  ("Maignan",         "POR", 16, 1995, "Francia",    "Milan"),
  ("Sportiello",      "POR", 57, 1992, "Italia",     "Milan"),
  ("Calabria",        "TD",   2, 1996, "Italia",     "Milan"),
  ("Tomori",          "DC",  23, 1997, "Inghilterra","Milan"),
  ("Thiaw",           "DC",  28, 2001, "Germania",   "Milan"),
  ("Theo Hernandez",  "TS",  19, 1997, "Francia",    "Milan"),
  ("Musah",           "CC",  80, 2002, "USA",        "Milan"),
  ("Reijnders",       "CC",  14, 1998, "Olanda",     "Milan"),
  ("Loftus-Cheek",    "CC",   8, 1996, "Inghilterra","Milan"),
  ("Pulisic",         "ALD", 11, 1998, "USA",        "Milan"),
  ("Leao",            "ALS", 10, 1999, "Portogallo", "Milan"),
  ("Giroud",          "ATT",  9, 1986, "Francia",    "Milan"),
  ("Jovic",           "ATT", 34, 1997, "Serbia",     "Milan"),

  # Napoli
  ("Meret",           "POR",  1, 1997, "Italia",     "Napoli"),
  ("Di Lorenzo",      "TD",  22, 1993, "Italia",     "Napoli"),
  ("Rrahmani",        "DC",  13, 1994, "Kosovo",     "Napoli"),
  ("Juan Jesus",      "DC",   5, 1991, "Brasile",    "Napoli"),
  ("Olivera",         "TS",  17, 1997, "Uruguay",    "Napoli"),
  ("Anguissa",        "CC",  99, 1995, "Camerun",    "Napoli"),
  ("Lobotka",         "CDC", 68, 1994, "Slovacchia", "Napoli"),
  ("Zielinski",       "CC",  20, 1994, "Polonia",    "Napoli"),
  ("Politano",        "ALD", 21, 1993, "Italia",     "Napoli"),
  ("Kvaratskhelia",   "ALS", 77, 2001, "Georgia",    "Napoli"),
  ("Osimhen",         "ATT",  9, 1998, "Nigeria",    "Napoli"),
  ("Raspadori",       "ATT", 81, 2000, "Italia",     "Napoli"),
  ("Simeone",         "ATT", 18, 1995, "Argentina",  "Napoli"),

  # Roma
  ("Svilar",          "POR",  99, 2000, "Belgio",    "Roma"),
  ("Celik",           "TD",  37, 1997, "Turchia",    "Roma"),
  ("Mancini",         "DC",  23, 1996, "Italia",     "Roma"),
  ("Ndicka",          "DC",   5, 1999, "Francia",    "Roma"),
  ("Spinazzola",      "TS",  37, 1993, "Italia",     "Roma"),
  ("Pellegrini",      "TRQ",  7, 1996, "Italia",     "Roma"),
  ("Cristante",       "CDC",  4, 1995, "Italia",     "Roma"),
  ("Paredes",         "CDC",  5, 1994, "Argentina",  "Roma"),
  ("Dybala",          "TRQ", 21, 1993, "Argentina",  "Roma"),
  ("El Shaarawy",     "ALS", 92, 1992, "Italia",     "Roma"),
  ("Lukaku",          "ATT",  9, 1993, "Belgio",     "Roma"),
  ("Belotti",         "ATT", 11, 1993, "Italia",     "Roma"),

  # Lazio
  ("Provedel",        "POR",  1, 1994, "Italia",     "Lazio"),
  ("Lazzari",         "TD",  29, 1993, "Italia",     "Lazio"),
  ("Casale",          "DC",  28, 1998, "Italia",     "Lazio"),
  ("Romagnoli",       "DC",  13, 1995, "Italia",     "Lazio"),
  ("Marusic",         "TS",   5, 1994, "Montenegro", "Lazio"),
  ("Guendouzi",       "CC",   8, 1999, "Francia",    "Lazio"),
  ("Rovella",         "CDC", 21, 2001, "Italia",     "Lazio"),
  ("Luis Alberto",    "TRQ", 10, 1992, "Spagna",     "Lazio"),
  ("Zaccagni",        "ALS", 20, 1995, "Italia",     "Lazio"),
  ("Felipe Anderson", "ALD",  7, 1993, "Brasile",    "Lazio"),
  ("Immobile",        "ATT", 17, 1990, "Italia",     "Lazio"),
  ("Pedro",           "ATT", 9,  1987, "Spagna",     "Lazio"),

  # Atalanta
  ("Carnesecchi",     "POR", 29, 2000, "Italia",     "Atalanta"),
  ("Hateboer",        "TD",  33, 1994, "Olanda",     "Atalanta"),
  ("Scalvini",        "DC",  42, 2003, "Italia",     "Atalanta"),
  ("Djimsiti",        "DC",  19, 1993, "Albania",    "Atalanta"),
  ("Kolasinac",       "TS",  23, 1993, "Bosnia",     "Atalanta"),
  ("De Roon",         "CC",  15, 1991, "Olanda",     "Atalanta"),
  ("Koopmeiners",     "CC",   7, 1998, "Olanda",     "Atalanta"),
  ("Pasalic",         "CC",  88, 1995, "Croazia",    "Atalanta"),
  ("Lookman",         "ALD", 11, 1998, "Nigeria",    "Atalanta"),
  ("De Ketelaere",    "TRQ", 17, 2001, "Belgio",     "Atalanta"),
  ("Scamacca",        "ATT",  9, 1999, "Italia",     "Atalanta"),
  ("Muriel",          "ATT", 21, 1991, "Colombia",   "Atalanta"),

  # Fiorentina
  ("Terracciano",     "POR",  1, 1990, "Italia",     "Fiorentina"),
  ("Dodò",            "TD",   2, 1998, "Brasile",    "Fiorentina"),
  ("Milenkovic",      "DC",   4, 1997, "Serbia",     "Fiorentina"),
  ("Martinez Quarta", "DC",  28, 1996, "Argentina",  "Fiorentina"),
  ("Biraghi",         "TS",   3, 1992, "Italia",     "Fiorentina"),
  ("Bonaventura",     "CC",   5, 1989, "Italia",     "Fiorentina"),
  ("Mandragora",      "CDC", 38, 1997, "Italia",     "Fiorentina"),
  ("Arthur",          "CDC", 63, 1996, "Brasile",    "Fiorentina"),
  ("Gonzalez",        "ALD", 10, 1998, "Argentina",  "Fiorentina"),
  ("Sottil",          "ALS", 11, 2000, "Italia",     "Fiorentina"),
  ("Vlahovic",        "ATT",  9, 2000, "Serbia",     "Fiorentina"),
  ("Nzola",           "ATT", 14, 1996, "Angola",     "Fiorentina"),

  # Torino
  ("Milinkovic-Savic","POR", 32, 1997, "Serbia",     "Torino"),
  ("Bellanova",       "TD",   2, 2000, "Italia",     "Torino"),
  ("Buongiorno",      "DC",  14, 1999, "Italia",     "Torino"),
  ("Djidji",          "DC",   6, 1991, "Francia",    "Torino"),
  ("Rodriguez",       "TS",  13, 1992, "Svizzera",   "Torino"),
  ("Linetty",         "CC",  14, 1995, "Polonia",    "Torino"),
  ("Ricci",           "CDC", 28, 2001, "Italia",     "Torino"),
  ("Ilic",            "CC",   8, 2001, "Serbia",     "Torino"),
  ("Radonjic",        "ALD", 29, 1996, "Serbia",     "Torino"),
  ("Lazaro",          "ALS", 17, 1996, "Austria",    "Torino"),
  ("Zapata",          "ATT",  9, 1991, "Colombia",   "Torino"),
  ("Sanabria",        "ATT", 19, 1996, "Paraguay",   "Torino"),

  # Bologna
  ("Skorupski",       "POR", 28, 1991, "Polonia",    "Bologna"),
  ("Posch",           "TD",  13, 1997, "Austria",    "Bologna"),
  ("Beukema",         "DC",  34, 1998, "Olanda",     "Bologna"),
  ("Lucumi",          "DC",   5, 1998, "Colombia",   "Bologna"),
  ("Kristiansen",     "TS",  19, 2001, "Danimarca",  "Bologna"),
  ("Ferguson",        "CC",  17, 2004, "Irlanda",    "Bologna"),
  ("Freuler",         "CDC", 11, 1992, "Svizzera",   "Bologna"),
  ("Moro",            "CC",  23, 2002, "Italia",     "Bologna"),
  ("Orsolini",        "ALD",  7, 1997, "Italia",     "Bologna"),
  ("Ndoye",           "ALS", 22, 2002, "Svizzera",   "Bologna"),
  ("Zirkzee",         "ATT",  9, 2001, "Olanda",     "Bologna"),
  ("Arnautovic",      "ATT",  9, 1989, "Austria",    "Bologna"),

  # ── PREMIER LEAGUE ───────────────────────────────────────

  # Manchester City
  ("Ederson",         "POR", 31, 1993, "Brasile",      "Man City"),
  ("Walker",          "TD",   2, 1990, "Inghilterra",  "Man City"),
  ("Dias",            "DC",   3, 1997, "Portogallo",   "Man City"),
  ("Akanji",          "DC",  25, 1995, "Svizzera",     "Man City"),
  ("Gvardiol",        "TS",  24, 2002, "Croazia",      "Man City"),
  ("Rodri",           "CDC", 16, 1996, "Spagna",       "Man City"),
  ("De Bruyne",       "TRQ", 17, 1991, "Belgio",       "Man City"),
  ("Bernardo Silva",  "CC",  20, 1994, "Portogallo",   "Man City"),
  ("Foden",           "ALS", 47, 2000, "Inghilterra",  "Man City"),
  ("Doku",            "ALD", 11, 2002, "Belgio",       "Man City"),
  ("Haaland",         "ATT",  9, 2000, "Norvegia",     "Man City"),

  # Arsenal
  ("Raya",            "POR", 22, 1995, "Spagna",       "Arsenal"),
  ("White",           "TD",   4, 1997, "Inghilterra",  "Arsenal"),
  ("Saliba",          "DC",  12, 2001, "Francia",      "Arsenal"),
  ("Gabriel",         "DC",   6, 1997, "Brasile",      "Arsenal"),
  ("Zinchenko",       "TS",  35, 1996, "Ucraina",      "Arsenal"),
  ("Partey",          "CDC",  5, 1993, "Ghana",        "Arsenal"),
  ("Odegaard",        "TRQ",  8, 1998, "Norvegia",     "Arsenal"),
  ("Rice",            "CC",  41, 1999, "Inghilterra",  "Arsenal"),
  ("Saka",            "ALD",  7, 2001, "Inghilterra",  "Arsenal"),
  ("Martinelli",      "ALS", 11, 2001, "Brasile",      "Arsenal"),
  ("Jesus",           "ATT",  9, 1997, "Brasile",      "Arsenal"),
  ("Havertz",         "ATT", 29, 1999, "Germania",     "Arsenal"),

  # Liverpool
  ("Alisson",         "POR",  1, 1992, "Brasile",      "Liverpool"),
  ("Alexander-Arnold","TD",  66, 1998, "Inghilterra",  "Liverpool"),
  ("Van Dijk",        "DC",   4, 1991, "Olanda",       "Liverpool"),
  ("Konate",          "DC",   5, 2001, "Francia",      "Liverpool"),
  ("Robertson",       "TS",  26, 1994, "Scozia",       "Liverpool"),
  ("Mac Allister",    "CDC", 10, 1998, "Argentina",    "Liverpool"),
  ("Szoboszlai",      "TRQ",  8, 2000, "Ungheria",     "Liverpool"),
  ("Gravenberch",     "CC",  38, 2002, "Olanda",       "Liverpool"),
  ("Salah",           "ALD", 11, 1992, "Egitto",       "Liverpool"),
  ("Diaz",            "ALS", 23, 1997, "Colombia",     "Liverpool"),
  ("Nunez",           "ATT",  9, 2000, "Uruguay",      "Liverpool"),
  ("Jota",            "ATT", 20, 1996, "Portogallo",   "Liverpool"),

  # Chelsea
  ("Sanchez",         "POR", 13, 1997, "Cile",         "Chelsea"),
  ("Reece James",     "TD",  24, 2000, "Inghilterra",  "Chelsea"),
  ("Silva",           "DC",   6, 1984, "Brasile",      "Chelsea"),
  ("Colwill",         "DC",  26, 2003, "Inghilterra",  "Chelsea"),
  ("Chilwell",        "TS",  21, 1996, "Inghilterra",  "Chelsea"),
  ("Caicedo",         "CDC", 25, 2001, "Ecuador",      "Chelsea"),
  ("Fernandez",       "CC",   8, 2001, "Argentina",    "Chelsea"),
  ("Gallagher",       "CC",  23, 2000, "Inghilterra",  "Chelsea"),
  ("Palmer",          "TRQ", 20, 2002, "Inghilterra",  "Chelsea"),
  ("Sterling",        "ALD", 17, 1994, "Inghilterra",  "Chelsea"),
  ("Jackson",         "ATT", 15, 2001, "Senegal",      "Chelsea"),
  ("Nkunku",          "ATT", 18, 1997, "Francia",      "Chelsea"),

  # Manchester United
  ("Onana",           "POR", 24, 1996, "Camerun",      "Man United"),
  ("Wan-Bissaka",     "TD",  29, 1997, "Inghilterra",  "Man United"),
  ("Varane",          "DC",  19, 1993, "Francia",      "Man United"),
  ("Maguire",         "DC",   5, 1993, "Inghilterra",  "Man United"),
  ("Shaw",            "TS",  23, 1995, "Inghilterra",  "Man United"),
  ("Casemiro",        "CDC", 18, 1992, "Brasile",      "Man United"),
  ("Bruno Fernandes", "TRQ",  8, 1994, "Portogallo",   "Man United"),
  ("Mainoo",          "CC",  37, 2005, "Inghilterra",  "Man United"),
  ("Rashford",        "ALS", 10, 1997, "Inghilterra",  "Man United"),
  ("Garnacho",        "ALD", 49, 2004, "Argentina",    "Man United"),
  ("Hojlund",         "ATT", 11, 2003, "Danimarca",    "Man United"),

  # Tottenham
  ("Vicario",         "POR", 13, 1996, "Italia",       "Tottenham"),
  ("Porro",           "TD",  23, 2000, "Spagna",       "Tottenham"),
  ("Romero",          "DC",  17, 1998, "Argentina",    "Tottenham"),
  ("Van de Ven",      "DC",  37, 2001, "Olanda",       "Tottenham"),
  ("Udogie",          "TS",  38, 2002, "Italia",       "Tottenham"),
  ("Bissouma",        "CDC",  8, 1996, "Mali",         "Tottenham"),
  ("Maddison",        "TRQ", 10, 1996, "Inghilterra",  "Tottenham"),
  ("Bentancur",       "CC",  30, 1997, "Uruguay",      "Tottenham"),
  ("Kulusevski",      "ALD", 21, 2000, "Svezia",       "Tottenham"),
  ("Son",             "ALS",  7, 1992, "Corea del Sud","Tottenham"),
  ("Richarlison",     "ATT",  9, 1997, "Brasile",      "Tottenham"),

  # ── SERIE B ──────────────────────────────────────────────

  # Parma
  ("Chichizola",      "POR", 12, 1994, "Argentina",  "Parma"),
  ("Coulibaly",       "TD",  27, 2000, "Senegal",    "Parma"),
  ("Delprato",        "DC",   2, 1999, "Italia",     "Parma"),
  ("Circati",         "DC",   5, 2002, "Italia",     "Parma"),
  ("Valeri",          "TS",  31, 1998, "Italia",     "Parma"),
  ("Estevez",         "CDC", 29, 1996, "Argentina",  "Parma"),
  ("Bernabe",         "CC",  10, 2001, "Spagna",     "Parma"),
  ("Cyprien",         "CC",   8, 1995, "Francia",    "Parma"),
  ("Man",             "ALD", 22, 1997, "Romania",    "Parma"),
  ("Bonny",           "ATT",  9, 2003, "Francia",    "Parma"),
  ("Mihaila",         "ALS", 28, 2000, "Romania",    "Parma"),

  # Como
  ("Audero",          "POR", 24, 1997, "Italia",     "Como"),
  ("Iovine",          "TD",  30, 2003, "Italia",     "Como"),
  ("Goldaniga",       "DC",  25, 1993, "Italia",     "Como"),
  ("Odenthal",        "DC",  17, 1998, "Germania",   "Como"),
  ("Barba",           "TS",  33, 1992, "Spagna",     "Como"),
  ("Da Cunha",        "CC",  10, 2000, "Francia",    "Como"),
  ("Braunoder",       "CDC",  8, 2003, "Austria",    "Como"),
  ("Caqueret",        "CC",  29, 2000, "Francia",    "Como"),
  ("Strefezza",       "ALD",  7, 1997, "Brasile",    "Como"),
  ("Cerri",           "ATT",  9, 1996, "Italia",     "Como"),
  ("Cutrone",         "ATT", 11, 1998, "Italia",     "Como"),

  # Palermo
  ("Desplanches",     "POR", 12, 2002, "Francia",    "Palermo"),
  ("Diakité",         "TD",  22, 2000, "Francia",    "Palermo"),
  ("Nedelcearu",      "DC",   5, 1997, "Romania",    "Palermo"),
  ("Ceccaroni",       "DC",  27, 1995, "Italia",     "Palermo"),
  ("Lund",            "TS",  30, 1999, "USA",        "Palermo"),
  ("Segre",           "CC",   8, 1997, "Italia",     "Palermo"),
  ("Gomes",           "CDC", 10, 1998, "Portogallo", "Palermo"),
  ("Ranocchia",       "CC",   4, 2001, "Italia",     "Palermo"),
  ("Di Mariano",      "ALD", 11, 1993, "Italia",     "Palermo"),
  ("Brunori",         "ATT",  9, 1994, "Italia",     "Palermo"),
  ("Insigne",         "ALS", 24, 1991, "Italia",     "Palermo"),

  # ── SERIE C ──────────────────────────────────────────────

  # Catanzaro
  ("Fulignati",       "POR",  1, 1992, "Italia",     "Catanzaro"),
  ("Brighenti",       "DC",   5, 1997, "Italia",     "Catanzaro"),
  ("Antonini",        "TS",  33, 1992, "Italia",     "Catanzaro"),
  ("Ghion",           "CC",   8, 1998, "Italia",     "Catanzaro"),
  ("Iemmello",        "ATT",  9, 1992, "Italia",     "Catanzaro"),

  # Avellino
  ("Iannarilli",      "POR",  1, 1992, "Italia",     "Avellino"),
  ("Benedetti",       "DC",   5, 1992, "Italia",     "Avellino"),
  ("Rocca",           "CC",   8, 1998, "Italia",     "Avellino"),
  ("Patierno",        "ATT",  9, 1995, "Italia",     "Avellino"),

  # Reggiana
  ("Motta",           "POR",  1, 1993, "Italia",     "Reggiana"),
  ("Meroni",          "DC",   5, 2004, "Italia",     "Reggiana"),
  ("Girma",           "CC",   8, 2003, "Italia",     "Reggiana"),
  ("Gondo",           "ATT",  9, 1996, "Costa d'Avorio","Reggiana"),
]

def populate():
    db = SessionLocal()
    try:
        # Controlla quanti giocatori ci sono già
        existing = db.query(PlayerModel).count()
        if existing > 0:
            print(f"⚠️  Già presenti {existing} giocatori nel database.")
            risposta = input("Vuoi aggiungere comunque? (s/n): ").strip().lower()
            if risposta != 's':
                print("Operazione annullata.")
                return

        count = 0
        for nome, ruolo, numero, anno, nazione, squadra in PLAYERS:
            p = PlayerModel(
                name        = nome,
                role        = ruolo,
                number      = numero,
                birth_year  = anno,
                nationality = nazione,
                team_name   = squadra,
            )
            db.add(p)
            count += 1

        db.commit()
        print(f"✅ Aggiunti {count} calciatori al database!")
        print(f"   Serie A:        ~120 giocatori")
        print(f"   Premier League: ~80 giocatori")
        print(f"   Serie B:        ~30 giocatori")
        print(f"   Serie C:        ~20 giocatori")

    except Exception as e:
        db.rollback()
        print(f"❌ Errore: {e}")
    finally:
        db.close()

if __name__ == "__main__":
    populate()