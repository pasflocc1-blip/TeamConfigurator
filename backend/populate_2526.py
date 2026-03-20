"""
Rose Serie A / Serie B / Serie C 2025/2026
Fonte: dati aggiornati al marzo 2026
Esegui: python populate_2526.py [--reset]
"""

"""
Script per popolare l'anagrafica con i calciatori delle serie italiane 2024/25
Esegui con: python populate_players_full.py
Opzioni:
  --reset   : elimina tutti i calciatori esistenti prima di inserire
  --skip    : salta i duplicati (default)

  python populate_2526.py --reset
"""

import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from database import SessionLocal, engine, Base
from models import RegistryPlayer
Base.metadata.create_all(bind=engine)
RESET = '--reset' in sys.argv

# (nome, ruolo, numero, anno_nascita, nazionalità, squadra)
PLAYERS = [

  # ═══════════════════════════════════════════════════════════════════
  # SERIE A 2025/2026
  # Squadre: Atalanta, Bologna, Cagliari, Como, Cremonese,
  # Fiorentina, Genoa, Inter, Juventus, Lazio, Lecce, Milan,
  # Napoli, Parma, Pisa, Roma, Sassuolo, Torino, Udinese, Verona
  # ═══════════════════════════════════════════════════════════════════

  # ── Inter ──
  ("Di Gennaro",       "POR", 40, 1988, "Italia",      "Inter"),
  ("Martinez J.",      "POR", 31, 1998, "Spagna",      "Inter"),
  ("Sommer",           "POR",  1, 1988, "Svizzera",    "Inter"),
  ("Acerbi",           "DC",  15, 1988, "Italia",      "Inter"),
  ("Akanji",           "DC",  25, 1995, "Svizzera",    "Inter"),
  ("Carlos Augusto",   "TS",  30, 1999, "Brasile",     "Inter"),
  ("Bastoni",          "TS",  23, 1999, "Italia",      "Inter"),
  ("Bisseck",          "TD",  31, 2000, "Germania",    "Inter"),
  ("Darmian",          "TD",  36, 1989, "Italia",      "Inter"),
  ("De Vrij",          "DC",   6, 1992, "Olanda",      "Inter"),
  ("Dimarco",          "TS",  32, 1997, "Italia",      "Inter"),
  ("Dumfries",         "TD",   2, 1996, "Olanda",      "Inter"),
  ("Barella",          "CC",  23, 1997, "Italia",      "Inter"),
  ("Calhanoglu",       "CDC", 20, 1994, "Turchia",     "Inter"),
  ("Diouf",            "CC",  18, 2002, "Senegal",     "Inter"),
  ("Frattesi",         "CC",  16, 1999, "Italia",      "Inter"),
  ("Luis Henrique",    "ALD", 14, 2001, "Brasile",     "Inter"),
  ("Mkhitaryan",       "CC",  22, 1989, "Armenia",     "Inter"),
  ("Sucic",            "CC",  19, 2003, "Croazia",     "Inter"),
  ("Zielinski",        "CC",   7, 1994, "Polonia",     "Inter"),
  ("Bonny",            "ATT", 34, 2003, "Francia",     "Inter"),
  ("Esposito F.P.",    "ATT", 32, 2002, "Italia",      "Inter"),
  ("Lautaro Martinez", "ATT", 10, 1997, "Argentina",   "Inter"),
  ("Thuram",           "ATT",  9, 1997, "Francia",     "Inter"),

  # ── Juventus ──
  ("Di Gregorio",      "POR",  1, 1997, "Italia",      "Juventus"),
  ("Perin",            "POR", 36, 1992, "Italia",      "Juventus"),
  ("Pinsoglio",        "POR", 23, 1990, "Italia",      "Juventus"),
  ("Cambiaso",         "TD",  27, 2000, "Italia",      "Juventus"),
  ("Danilo",           "TD",  13, 1991, "Brasile",     "Juventus"),
  ("Savona",           "TD",  37, 2003, "Italia",      "Juventus"),
  ("Gatti",            "DC",   4, 1998, "Italia",      "Juventus"),
  ("Bremer",           "DC",   3, 1997, "Brasile",     "Juventus"),
  ("Kalulu",           "DC",   5, 2000, "Francia",     "Juventus"),
  ("Kelly",            "DC",  26, 2000, "Inghilterra", "Juventus"),
  ("Cabal",            "TS",  15, 2001, "Colombia",    "Juventus"),
  ("Locatelli",        "CDC",  5, 1998, "Italia",      "Juventus"),
  ("Thuram M.",        "CC",  19, 1997, "Francia",     "Juventus"),
  ("McKennie",         "CC",  16, 1998, "USA",         "Juventus"),
  ("Fagioli",          "CC",  21, 2001, "Italia",      "Juventus"),
  ("Douglas Luiz",     "CDC", 26, 1998, "Brasile",     "Juventus"),
  ("Koopmeiners",      "CC",   8, 1998, "Olanda",      "Juventus"),
  ("Conceicao",        "ALD",  7, 2002, "Portogallo",  "Juventus"),
  ("Yildiz",           "TRQ", 10, 2005, "Turchia",     "Juventus"),
  ("Nico Gonzalez",    "ALS", 11, 1998, "Argentina",   "Juventus"),
  ("Vlahovic",         "ATT",  9, 2000, "Serbia",      "Juventus"),
  ("David",            "ATT", 24, 1999, "Canada",      "Juventus"),
  ("Milik",            "ATT", 14, 1994, "Polonia",     "Juventus"),

  # ── Milan ──
  ("Maignan",          "POR", 16, 1995, "Francia",     "Milan"),
  ("Sportiello",       "POR", 57, 1992, "Italia",      "Milan"),
  ("Emerson Royal",    "TD",  12, 1999, "Brasile",     "Milan"),
  ("Calabria",         "TD",   2, 1996, "Italia",      "Milan"),
  ("Tomori",           "DC",  23, 1997, "Inghilterra", "Milan"),
  ("Thiaw",            "DC",  28, 2001, "Germania",    "Milan"),
  ("Pavlovic",         "DC",  31, 2001, "Serbia",      "Milan"),
  ("Gabbia",           "DC",  46, 1999, "Italia",      "Milan"),
  ("Theo Hernandez",   "TS",  19, 1997, "Francia",     "Milan"),
  ("Bartesaghi",       "TS",  64, 2005, "Italia",      "Milan"),
  ("Ricci S.",         "CDC",  8, 2001, "Italia",      "Milan"),
  ("Modric",           "CDC", 14, 1985, "Croazia",     "Milan"),
  ("Rabiot",           "CC",  25, 1995, "Francia",     "Milan"),
  ("Reijnders",        "CC",  14, 1998, "Olanda",      "Milan"),
  ("Loftus-Cheek",     "CC",   8, 1996, "Inghilterra", "Milan"),
  ("Bennacer",         "CDC",  4, 1997, "Algeria",     "Milan"),
  ("Pulisic",          "ALD", 11, 1998, "USA",         "Milan"),
  ("Leao",             "ALS", 10, 1999, "Portogallo",  "Milan"),
  ("Okafor",           "ALS", 77, 2000, "Svizzera",    "Milan"),
  ("Chukwueze",        "ALD", 21, 1999, "Nigeria",     "Milan"),
  ("Abraham",          "ATT", 90, 1997, "Inghilterra", "Milan"),
  ("Jovic",            "ATT", 34, 1997, "Serbia",      "Milan"),

  # ── Napoli ──
  ("Caprile",          "POR", 12, 2001, "Italia",      "Napoli"),
  ("Meret",            "POR",  1, 1997, "Italia",      "Napoli"),
  ("Milinkovic-Savic V.","POR",32,1997, "Serbia",      "Napoli"),
  ("Di Lorenzo",       "TD",  22, 1993, "Italia",      "Napoli"),
  ("Mazzocchi",        "TD",   5, 1995, "Italia",      "Napoli"),
  ("Rrahmani",         "DC",  13, 1994, "Kosovo",      "Napoli"),
  ("Buongiorno",       "DC",   4, 1999, "Italia",      "Napoli"),
  ("Juan Jesus",       "DC",   5, 1991, "Brasile",     "Napoli"),
  ("Olivera",          "TS",  17, 1997, "Uruguay",     "Napoli"),
  ("Spinazzola",       "TS",  19, 1993, "Italia",      "Napoli"),
  ("Anguissa",         "CC",  99, 1995, "Camerun",     "Napoli"),
  ("Lobotka",          "CDC", 68, 1994, "Slovacchia",  "Napoli"),
  ("Gilmour",          "CC",  14, 2001, "Scozia",      "Napoli"),
  ("McTominay",        "CC",   8, 1996, "Scozia",      "Napoli"),
  ("Elmas",            "CC",   7, 2000, "Macedonia",   "Napoli"),
  ("De Bruyne",        "TRQ", 17, 1991, "Belgio",      "Napoli"),
  ("Politano",         "ALD", 21, 1993, "Italia",      "Napoli"),
  ("Neres",            "ALD", 77, 1997, "Brasile",     "Napoli"),
  ("Kvaratskhelia",    "ALS", 77, 2001, "Georgia",     "Napoli"),
  ("Lukaku",           "ATT", 11, 1993, "Belgio",      "Napoli"),
  ("Raspadori",        "ATT", 81, 2000, "Italia",      "Napoli"),
  ("Simeone",          "ATT", 18, 1995, "Argentina",   "Napoli"),

  # ── Roma ──
  ("Svilar",           "POR", 99, 2000, "Belgio",      "Roma"),
  ("Gollini",          "POR",  1, 1995, "Italia",      "Roma"),
  ("Celik",            "TD",  37, 1997, "Turchia",     "Roma"),
  ("Saelemaekers",     "TD",  56, 1999, "Belgio",      "Roma"),
  ("Mancini",          "DC",  23, 1996, "Italia",      "Roma"),
  ("Ndicka",           "DC",   5, 1999, "Francia",     "Roma"),
  ("Hummels",          "DC",  15, 1988, "Germania",    "Roma"),
  ("Hermoso",          "DC",  22, 1995, "Spagna",      "Roma"),
  ("Angelino",         "TS",  39, 1997, "Spagna",      "Roma"),
  ("Zalewski",         "TS",  59, 2002, "Polonia",     "Roma"),
  ("Paredes",          "CDC",  5, 1994, "Argentina",   "Roma"),
  ("Koné",             "CC",  52, 2001, "Francia",     "Roma"),
  ("Cristante",        "CC",   4, 1995, "Italia",      "Roma"),
  ("Pisilli",          "CC",  55, 2004, "Italia",      "Roma"),
  ("Pellegrini",       "TRQ",  7, 1996, "Italia",      "Roma"),
  ("Dybala",           "TRQ", 21, 1993, "Argentina",   "Roma"),
  ("El Shaarawy",      "ALS", 92, 1992, "Italia",      "Roma"),
  ("Baldanzi",         "TRQ", 11, 2003, "Italia",      "Roma"),
  ("Dovbyk",           "ATT",  9, 1997, "Ucraina",     "Roma"),
  ("Shomurodov",       "ATT", 14, 1995, "Uzbekistan",  "Roma"),

  # ── Lazio ──
  ("Provedel",         "POR",  1, 1994, "Italia",      "Lazio"),
  ("Mandas",           "POR", 22, 2001, "Grecia",      "Lazio"),
  ("Lazzari",          "TD",  29, 1993, "Italia",      "Lazio"),
  ("Marusic",          "TD",  77, 1994, "Montenegro",  "Lazio"),
  ("Patric",           "DC",   4, 1993, "Spagna",      "Lazio"),
  ("Romagnoli",        "DC",  13, 1995, "Italia",      "Lazio"),
  ("Gila",             "DC",  23, 2002, "Spagna",      "Lazio"),
  ("Pellegrini L.",    "TS",   3, 1991, "Italia",      "Lazio"),
  ("Nuno Tavares",     "TS",  18, 2000, "Portogallo",  "Lazio"),
  ("Guendouzi",        "CC",   8, 1999, "Francia",     "Lazio"),
  ("Rovella",          "CDC",  6, 2001, "Italia",      "Lazio"),
  ("Dele-Bashiru",     "CC",   4, 2001, "Inghilterra", "Lazio"),
  ("Vecino",           "CC",   8, 1991, "Uruguay",     "Lazio"),
  ("Isaksen",          "ALD", 19, 2001, "Danimarca",   "Lazio"),
  ("Zaccagni",         "ALS", 20, 1995, "Italia",      "Lazio"),
  ("Pedro",            "TRQ",  9, 1987, "Spagna",      "Lazio"),
  ("Dia",              "ATT", 10, 1996, "Senegal",     "Lazio"),
  ("Castellanos",      "ATT", 11, 1998, "Argentina",   "Lazio"),
  ("Noslin",           "ATT", 31, 1999, "Olanda",      "Lazio"),

  # ── Atalanta ──
  ("Carnesecchi",      "POR", 29, 2000, "Italia",      "Atalanta"),
  ("Rui Patricio",     "POR",  1, 1988, "Portogallo",  "Atalanta"),
  ("Bellanova",        "TD",   2, 2000, "Italia",      "Atalanta"),
  ("Zappacosta",       "TD",  77, 1992, "Italia",      "Atalanta"),
  ("Scalvini",         "DC",  42, 2003, "Italia",      "Atalanta"),
  ("Hien",             "DC",   5, 1999, "Svezia",      "Atalanta"),
  ("Djimsiti",         "DC",  19, 1993, "Albania",     "Atalanta"),
  ("Kolasinac",        "TS",  23, 1993, "Bosnia",      "Atalanta"),
  ("Bonfanti",         "DC",  15, 2002, "Italia",      "Atalanta"),
  ("De Roon",          "CDC", 15, 1991, "Olanda",      "Atalanta"),
  ("Ederson",          "CC",  13, 2000, "Brasile",     "Atalanta"),
  ("Pasalic",          "CC",  88, 1995, "Croazia",     "Atalanta"),
  ("Samardzic",        "TRQ", 24, 2002, "Serbia",      "Atalanta"),
  ("De Ketelaere",     "TRQ", 17, 2001, "Belgio",      "Atalanta"),
  ("Lookman",          "ALD", 11, 1998, "Nigeria",     "Atalanta"),
  ("Cuadrado",         "ALD", 16, 1988, "Colombia",    "Atalanta"),
  ("Retegui",          "ATT", 32, 1999, "Italia",      "Atalanta"),
  ("Scamacca",         "ATT",  9, 1999, "Italia",      "Atalanta"),
  ("Touré M.",         "ATT", 99, 2004, "Norvegia",    "Atalanta"),

  # ── Fiorentina ──
  ("De Gea",           "POR",  1, 1990, "Spagna",      "Fiorentina"),
  ("Terracciano P.",   "POR", 16, 1990, "Italia",      "Fiorentina"),
  ("Dodò",             "TD",   2, 1998, "Brasile",     "Fiorentina"),
  ("Kayode",           "TD",  29, 2003, "Nigeria",     "Fiorentina"),
  ("Milenkovic",       "DC",   4, 1997, "Serbia",      "Fiorentina"),
  ("Martinez Quarta",  "DC",  28, 1996, "Argentina",   "Fiorentina"),
  ("Comuzzo",          "DC",  99, 2005, "Italia",      "Fiorentina"),
  ("Biraghi",          "TS",   3, 1992, "Italia",      "Fiorentina"),
  ("Parisi",           "TS",   5, 2000, "Italia",      "Fiorentina"),
  ("Cataldi",          "CDC",  6, 1994, "Italia",      "Fiorentina"),
  ("Sohm",             "CC",   8, 1998, "Svizzera",    "Fiorentina"),
  ("Bove",             "CC",   4, 2002, "Italia",      "Fiorentina"),
  ("Adli",             "TRQ", 10, 2000, "Francia",     "Fiorentina"),
  ("Gonzalez",         "ALD", 10, 1998, "Argentina",   "Fiorentina"),
  ("Sottil",           "ALS", 11, 2000, "Italia",      "Fiorentina"),
  ("Colpani",          "TRQ",  7, 2000, "Italia",      "Fiorentina"),
  ("Kean",             "ATT",  9, 2000, "Italia",      "Fiorentina"),
  ("Gudmundsson",      "TRQ", 21, 1997, "Islanda",     "Fiorentina"),

  # ── Bologna ──
  ("Skorupski",        "POR", 28, 1991, "Polonia",     "Bologna"),
  ("Ravaglia",         "POR", 22, 1999, "Italia",      "Bologna"),
  ("Posch",            "TD",  13, 1997, "Austria",     "Bologna"),
  ("Holm",             "TD",   7, 2000, "Svezia",      "Bologna"),
  ("Beukema",          "DC",  34, 1998, "Olanda",      "Bologna"),
  ("Lucumi",           "DC",   5, 1998, "Colombia",    "Bologna"),
  ("Erlic",            "DC",   6, 1997, "Croazia",     "Bologna"),
  ("Kristiansen",      "TS",  19, 2001, "Danimarca",   "Bologna"),
  ("Miranda",          "TS",  17, 2004, "Spagna",      "Bologna"),
  ("Ferguson",         "CC",  17, 2004, "Irlanda",     "Bologna"),
  ("Freuler",          "CDC", 11, 1992, "Svizzera",    "Bologna"),
  ("Pobega",           "CC",   4, 1999, "Italia",      "Bologna"),
  ("Moro",             "CC",  23, 2002, "Italia",      "Bologna"),
  ("Orsolini",         "ALD",  7, 1997, "Italia",      "Bologna"),
  ("Ndoye",            "ALS", 22, 2002, "Svizzera",    "Bologna"),
  ("Fabbian",          "TRQ",  8, 2003, "Italia",      "Bologna"),
  ("Dallinga",         "ATT", 11, 2000, "Olanda",      "Bologna"),
  ("Castro",           "ATT", 19, 2004, "Argentina",   "Bologna"),
  ("Odgaard",          "ATT",  9, 1999, "Danimarca",   "Bologna"),

  # ── Torino ──
  ("Israel",           "POR",  1, 1998, "Portogallo",  "Torino"),
  ("Paleari",          "POR", 22, 1995, "Italia",      "Torino"),
  ("Vojvoda",          "TD",  22, 1995, "Kosovo",      "Torino"),
  ("Pedersen",         "TD",  17, 1999, "Norvegia",    "Torino"),
  ("Coco",             "DC",   3, 2001, "Spagna",      "Torino"),
  ("Maripan",          "DC",  13, 1994, "Cile",        "Torino"),
  ("Nkounkou",         "TS",   5, 2000, "Francia",     "Torino"),
  ("Sosa",             "TS",   6, 1998, "Austria",     "Torino"),
  ("Ricci",            "CDC", 28, 2001, "Italia",      "Torino"),
  ("Ilic",             "CC",   8, 2001, "Serbia",      "Torino"),
  ("Linetty",          "CC",  14, 1995, "Polonia",     "Torino"),
  ("Gineitis",         "CC",  32, 2004, "Lituania",    "Torino"),
  ("Lazaro",           "ALD", 17, 1996, "Austria",     "Torino"),
  ("Karamoh",          "ALS", 19, 1998, "Costa d'Avorio","Torino"),
  ("Adams",            "ATT",  9, 2001, "USA",         "Torino"),
  ("Simeone G.",       "ATT", 18, 1995, "Argentina",   "Torino"),
  ("Sanabria",         "ATT",  7, 1996, "Paraguay",    "Torino"),

  # ── Udinese ──
  ("Sava",             "POR",  1, 2002, "Belgio",      "Udinese"),
  ("Okoye",            "POR", 24, 2000, "Nigeria",     "Udinese"),
  ("Kristensen",       "TD",   5, 1997, "Danimarca",   "Udinese"),
  ("Ehizibue",         "TD",  29, 1995, "Olanda",      "Udinese"),
  ("Bijol",            "DC",   3, 1999, "Slovenia",    "Udinese"),
  ("Bertola",          "DC",  17, 2002, "Italia",      "Udinese"),
  ("Touré K.",         "DC",  44, 1998, "Guinea",      "Udinese"),
  ("Zemura",           "TS",  27, 2000, "Zimbabwe",    "Udinese"),
  ("Lovric",           "CDC",  8, 1998, "Slovenia",    "Udinese"),
  ("Payero",           "CC",  20, 1998, "Argentina",   "Udinese"),
  ("Karlstrom",        "CC",   7, 1995, "Svezia",      "Udinese"),
  ("Zaniolo",          "TRQ", 10, 1999, "Italia",      "Udinese"),
  ("Thauvin",          "ALD", 17, 1993, "Francia",     "Udinese"),
  ("Brenner",          "ATT",  9, 2000, "Brasile",     "Udinese"),
  ("Lucca",            "ATT", 11, 2000, "Italia",      "Udinese"),
  ("Buksa",            "ATT", 18, 1997, "Polonia",     "Udinese"),

  # ── Genoa ──
  ("Leali",            "POR",  1, 1993, "Italia",      "Genoa"),
  ("Gollini G.",       "POR", 95, 1995, "Italia",      "Genoa"),
  ("De Winter",        "TD",   5, 2002, "Belgio",      "Genoa"),
  ("Sabelli",          "TD",  29, 1993, "Italia",      "Genoa"),
  ("Vasquez",          "DC",   3, 2000, "Argentina",   "Genoa"),
  ("Bani",             "DC",  15, 1993, "Italia",      "Genoa"),
  ("Matturro",         "DC",   5, 2004, "Uruguay",     "Genoa"),
  ("Martin",           "TS",  27, 2001, "Spagna",      "Genoa"),
  ("Badelj",           "CDC",  8, 1989, "Croazia",     "Genoa"),
  ("Frendrup",         "CC",   7, 2001, "Danimarca",   "Genoa"),
  ("Thorsby",          "CC",   9, 1996, "Norvegia",    "Genoa"),
  ("Malinovskyi",      "TRQ", 10, 1993, "Ucraina",     "Genoa"),
  ("Zanoli",           "ALD", 24, 2000, "Italia",      "Genoa"),
  ("Ekhator",          "ALS", 21, 2005, "Norvegia",    "Genoa"),
  ("Pinamonti",        "ATT",  9, 1999, "Italia",      "Genoa"),
  ("Vitinha",          "ATT", 19, 2000, "Portogallo",  "Genoa"),

  # ── Cagliari ──
  ("Sherri",           "POR", 22, 1999, "Albania",     "Cagliari"),
  ("Scuffet",          "POR",  1, 1996, "Italia",      "Cagliari"),
  ("Zappa",            "TD",  28, 1999, "Italia",      "Cagliari"),
  ("Azzi",             "TD",  19, 2002, "Francia",     "Cagliari"),
  ("Mina",             "DC",  13, 1994, "Colombia",    "Cagliari"),
  ("Luperto",          "DC",   6, 1996, "Italia",      "Cagliari"),
  ("Augello",          "TS",   3, 1994, "Italia",      "Cagliari"),
  ("Obert",            "TS",  25, 2002, "Slovacchia",  "Cagliari"),
  ("Prati",            "CC",   8, 2001, "Italia",      "Cagliari"),
  ("Makoumbou",        "CDC", 29, 1998, "Congo",       "Cagliari"),
  ("Deiola",           "CC",   5, 1994, "Italia",      "Cagliari"),
  ("Gaetano",          "TRQ",  7, 2000, "Italia",      "Cagliari"),
  ("Viola",            "TRQ", 10, 1996, "Italia",      "Cagliari"),
  ("Luvumbo",          "ALS", 23, 2002, "Angola",      "Cagliari"),
  ("Zortea",           "ALD", 17, 1999, "Italia",      "Cagliari"),
  ("Belotti",          "ATT",  9, 1993, "Italia",      "Cagliari"),
  ("Esposito S.",      "ATT", 10, 2002, "Italia",      "Cagliari"),
  ("Lapadula",         "ATT",  9, 1990, "Italia",      "Cagliari"),

  # ── Como ──
  ("Reina",            "POR", 25, 1982, "Spagna",      "Como"),
  ("Audero C.",        "POR", 24, 1997, "Italia",      "Como"),
  ("Van der Brempt",   "TD",   2, 2002, "Belgio",      "Como"),
  ("Goldaniga",        "DC",  25, 1993, "Italia",      "Como"),
  ("Odenthal",         "DC",  17, 1998, "Germania",    "Como"),
  ("Fabregas",         "CDC",  4, 1987, "Spagna",      "Como"),
  ("Nico Paz",         "TRQ", 10, 2004, "Argentina",   "Como"),
  ("Da Cunha",         "CC",  28, 2000, "Francia",     "Como"),
  ("Baturina",         "CC",  18, 2002, "Croazia",     "Como"),
  ("Rodriguez",        "TS",   3, 1997, "Spagna",      "Como"),
  ("Strefezza",        "ALD",  7, 1997, "Brasile",     "Como"),
  ("Morata",           "ATT",  9, 1992, "Spagna",      "Como"),
  ("Belhadj",          "ATT", 11, 1999, "Algeria",     "Como"),

  # ── Parma ──
  ("Suzuki",           "POR", 12, 1998, "Giappone",    "Parma"),
  ("Corvi",            "POR",  1, 1994, "Italia",      "Parma"),
  ("Coulibaly",        "TD",  27, 2000, "Senegal",     "Parma"),
  ("Delprato",         "DC",   2, 1999, "Italia",      "Parma"),
  ("Circati",          "DC",   5, 2002, "Italia",      "Parma"),
  ("Balogh",           "DC",   6, 1999, "Ungheria",    "Parma"),
  ("Valeri",           "TS",  31, 1998, "Italia",      "Parma"),
  ("Hainaut",          "TS",   3, 1994, "Francia",     "Parma"),
  ("Estevez",          "CDC", 29, 1996, "Argentina",   "Parma"),
  ("Bernabe",          "CC",  10, 2001, "Spagna",      "Parma"),
  ("Hernani",          "CC",  16, 1994, "Brasile",     "Parma"),
  ("Oristanio",        "TRQ", 27, 2002, "Italia",      "Parma"),
  ("Man",              "ALD", 22, 1997, "Romania",     "Parma"),
  ("Almqvist",         "ALS",  7, 1999, "Svezia",      "Parma"),
  ("Mihaila",          "ALD", 28, 2000, "Romania",     "Parma"),
  ("Cutrone",          "ATT", 11, 1998, "Italia",      "Parma"),
  ("Charpentier",      "ATT", 19, 1999, "Francia",     "Parma"),

  # ── Pisa ──
  ("Nicolas",          "POR",  1, 1993, "Uruguay",     "Pisa"),
  ("Loria",            "POR", 22, 1999, "Italia",      "Pisa"),
  ("Calabresi",        "TD",   2, 1996, "Italia",      "Pisa"),
  ("Caracciolo",       "DC",   5, 1986, "Italia",      "Pisa"),
  ("Canestrelli",      "DC",   6, 1998, "Italia",      "Pisa"),
  ("Rus",              "DC",  15, 2000, "Romania",     "Pisa"),
  ("Angori",           "TS",   3, 2001, "Italia",      "Pisa"),
  ("Marin",            "CDC",  8, 1994, "Romania",     "Pisa"),
  ("Arena",            "CC",  16, 2001, "Italia",      "Pisa"),
  ("Piccinini",        "CC",   4, 2004, "Italia",      "Pisa"),
  ("Tramoni",          "ALD",  7, 1999, "Francia",     "Pisa"),
  ("Moreo",            "ATT", 10, 1992, "Italia",      "Pisa"),
  ("Lind",             "ATT",  9, 2003, "Danimarca",   "Pisa"),
  ("Touré I.",         "ATT", 11, 1999, "Guinea",      "Pisa"),

  # ── Sassuolo ──
  ("Satalino",         "POR",  1, 1991, "Italia",      "Sassuolo"),
  ("Pegolo",           "POR", 23, 1984, "Italia",      "Sassuolo"),
  ("Toljan",           "TD",   2, 1994, "Croazia",     "Sassuolo"),
  ("Romagna",          "DC",   5, 1997, "Italia",      "Sassuolo"),
  ("Tressoldi",        "DC",   6, 2000, "Italia",      "Sassuolo"),
  ("Doig",             "TS",  30, 2002, "Scozia",      "Sassuolo"),
  ("Thorstvedt",       "CC",   8, 2000, "Norvegia",    "Sassuolo"),
  ("Boloca",           "CDC",  5, 2000, "Romania",     "Sassuolo"),
  ("Iannoni",          "CC",  23, 2001, "Italia",      "Sassuolo"),
  ("Volpato",          "TRQ", 10, 2003, "Australia",   "Sassuolo"),
  ("Laurienté",        "ALS",  7, 1998, "Francia",     "Sassuolo"),
  ("Mulattieri",       "ATT",  9, 2000, "Italia",      "Sassuolo"),
  ("Thoreau",          "ATT", 11, 2001, "Francia",     "Sassuolo"),

  # ── Cremonese ──
  ("Fulignati",        "POR",  1, 1992, "Italia",      "Cremonese"),
  ("Jungdal",          "POR", 22, 2001, "Danimarca",   "Cremonese"),
  ("Sernicola",        "TD",   2, 1997, "Italia",      "Cremonese"),
  ("Bianchetti",       "DC",   5, 1993, "Italia",      "Cremonese"),
  ("Antov",            "DC",   6, 1998, "Bulgaria",    "Cremonese"),
  ("Quagliata",        "TS",   3, 1999, "Italia",      "Cremonese"),
  ("Castagnetti",      "CDC",  8, 1991, "Italia",      "Cremonese"),
  ("Pickel",           "CC",   4, 1996, "Germania",    "Cremonese"),
  ("Johnsen",          "CC",   7, 1995, "Norvegia",    "Cremonese"),
  ("Zanimacchia",      "ALD", 11, 1998, "Italia",      "Cremonese"),
  ("Bonazzoli",        "ATT",  9, 1997, "Italia",      "Cremonese"),
  ("Vazquez N.",       "ATT", 10, 1998, "Argentina",   "Cremonese"),
  ("De Luca",          "ATT", 18, 1995, "Italia",      "Cremonese"),

  # ── Lecce ──
  ("Falcone",          "POR",  1, 1995, "Italia",      "Lecce"),
  ("Borbei",           "DC",   5, 2003, "Romania",     "Lecce"),
  ("Baschirotto",      "DC",  15, 1996, "Italia",      "Lecce"),
  ("Guilbert",         "TD",   2, 1994, "Francia",     "Lecce"),
  ("Gallo",            "TS",   3, 1997, "Italia",      "Lecce"),
  ("Ramadani",         "CDC",  8, 1999, "Kosovo",      "Lecce"),
  ("Berisha",          "CC",  29, 1994, "Albania",     "Lecce"),
  ("Pierret",          "CC",   4, 2002, "Francia",     "Lecce"),
  ("Morente",          "ALD", 77, 1997, "Spagna",      "Lecce"),
  ("Coulibaly L.",     "ALS",  7, 1999, "Mali",        "Lecce"),
  ("Krstovic",         "ATT",  9, 2001, "Montenegro",  "Lecce"),
  ("Camarda",          "ATT", 90, 2006, "Italia",      "Lecce"),
  ("Rebic",            "ALS", 21, 1993, "Croazia",     "Lecce"),

  # ── Hellas Verona ──
  ("Montipo",          "POR",  1, 1996, "Italia",      "Verona"),
  ("Berardi",          "POR", 99, 2004, "Italia",      "Verona"),
  ("Tchatchoua",       "TD",  22, 1999, "Camerun",     "Verona"),
  ("Ghilardi",         "DC",   3, 2003, "Italia",      "Verona"),
  ("Coppola",          "DC",   4, 2003, "Italia",      "Verona"),
  ("Bradaric",         "TS",  17, 1992, "Croazia",     "Verona"),
  ("Duda",             "CC",   7, 1994, "Slovacchia",  "Verona"),
  ("Serdar",           "CC",   8, 1997, "Germania",    "Verona"),
  ("Belahyane",        "CDC",  6, 2004, "Marocco",     "Verona"),
  ("Suslov",           "TRQ", 10, 2002, "Slovacchia",  "Verona"),
  ("Lazovic",          "ALS", 21, 1990, "Serbia",      "Verona"),
  ("Mosquera",         "ATT",  9, 2001, "Colombia",    "Verona"),
  ("Tengstedt",        "ATT", 19, 2001, "Danimarca",   "Verona"),
  ("Sarr",             "ATT", 11, 2002, "Senegal",     "Verona"),

  # ═══════════════════════════════════════════════════════════════════
  # SERIE B 2025/2026
  # Squadre: Avellino, Bari, Carrarese, Catanzaro, Cesena,
  # Empoli, Frosinone, Juve Stabia, Mantova, Modena,
  # Monza, Padova, Palermo, Pescara, Reggiana,
  # Sampdoria, Spezia, Sudtirol, Venezia, Virtus Entella
  # ═══════════════════════════════════════════════════════════════════

  # ── Avellino ──
  ("Iannarilli",       "POR",  1, 1992, "Italia",      "Avellino"),
  ("Pane",             "POR", 22, 1999, "Italia",      "Avellino"),
  ("Enrici",           "TD",   2, 2002, "Italia",      "Avellino"),
  ("Benedetti",        "DC",   5, 1992, "Italia",      "Avellino"),
  ("Frascatore",       "TS",   3, 1993, "Italia",      "Avellino"),
  ("Rocca",            "CDC",  8, 1998, "Italia",      "Avellino"),
  ("Armellino",        "CC",   4, 1994, "Italia",      "Avellino"),
  ("Tribuzzi",         "TRQ", 10, 1996, "Italia",      "Avellino"),
  ("Cancellieri",      "ALS",  7, 2002, "Italia",      "Avellino"),
  ("Russo",            "ATT",  9, 1991, "Italia",      "Avellino"),
  ("Patierno",         "ATT", 11, 1995, "Italia",      "Avellino"),

  # ── Bari ──
  ("Radunovic",        "POR",  1, 1996, "Serbia",      "Bari"),
  ("Pucino",           "TD",   2, 1993, "Italia",      "Bari"),
  ("Mantovani",        "DC",   5, 1989, "Italia",      "Bari"),
  ("Vicari",           "DC",   6, 1992, "Italia",      "Bari"),
  ("Dorval",           "TS",   3, 2004, "Francia",     "Bari"),
  ("Benali",           "CC",   8, 1996, "Tunisia",     "Bari"),
  ("Maiello",          "CDC",  4, 1991, "Italia",      "Bari"),
  ("Sibilli",          "ALD",  7, 1997, "Italia",      "Bari"),
  ("Novakovich",       "ATT",  9, 1994, "USA",         "Bari"),
  ("Falletti",         "TRQ", 10, 1994, "Uruguay",     "Bari"),
  ("Lasagna",          "ATT", 11, 1992, "Italia",      "Bari"),

  # ── Carrarese ──
  ("Bleve",            "POR",  1, 1997, "Italia",      "Carrarese"),
  ("Bouah",            "TD",   2, 1999, "Francia",     "Carrarese"),
  ("Illanes",          "DC",   5, 1994, "Argentina",   "Carrarese"),
  ("Imperiale",        "DC",   6, 1999, "Italia",      "Carrarese"),
  ("Zanon",            "TS",   3, 1997, "Italia",      "Carrarese"),
  ("Schiavi",          "CDC",  8, 1994, "Italia",      "Carrarese"),
  ("Cerri",            "CC",   4, 1996, "Italia",      "Carrarese"),
  ("Torregrossa",      "ATT",  9, 1992, "Italia",      "Carrarese"),
  ("Finotto",          "ATT", 11, 1993, "Italia",      "Carrarese"),

  # ── Catanzaro ──
  ("Fulignati C.",     "POR",  1, 1992, "Italia",      "Catanzaro"),
  ("Brighenti",        "DC",   5, 1997, "Italia",      "Catanzaro"),
  ("Antonini",         "TS",  33, 1992, "Italia",      "Catanzaro"),
  ("Pompetti",         "CC",   8, 2000, "Italia",      "Catanzaro"),
  ("Ghion",            "CDC",  4, 1998, "Italia",      "Catanzaro"),
  ("Koutsoupias",      "CC",  28, 1999, "Grecia",      "Catanzaro"),
  ("Iemmello",         "ATT",  9, 1992, "Italia",      "Catanzaro"),
  ("Biasci",           "ATT", 10, 1993, "Italia",      "Catanzaro"),
  ("Pittarello",       "ATT", 11, 2000, "Italia",      "Catanzaro"),

  # ── Cesena ──
  ("Pisseri",          "POR",  1, 1993, "Italia",      "Cesena"),
  ("Ciofi",            "TD",   2, 1996, "Italia",      "Cesena"),
  ("Prestia",          "DC",   5, 1989, "Italia",      "Cesena"),
  ("Mangraviti",       "DC",  15, 1997, "Italia",      "Cesena"),
  ("Tavcar",           "CC",   8, 2000, "Slovenia",    "Cesena"),
  ("Calò",             "CDC",  6, 1998, "Italia",      "Cesena"),
  ("Berti",            "CC",  14, 2004, "Italia",      "Cesena"),
  ("Donnarumma A.",    "ATT",  9, 1990, "Italia",      "Cesena"),
  ("Shpendi E.",       "ATT", 10, 2003, "Italia",      "Cesena"),
  ("Van Hooijdonk",    "ATT", 19, 2000, "Olanda",      "Cesena"),

  # ── Empoli ──
  ("Seghetti",         "POR",  1, 2003, "Italia",      "Empoli"),
  ("Caprile E.",       "POR", 12, 2001, "Italia",      "Empoli"),
  ("Gyasi",            "TD",  10, 1995, "Ghana",       "Empoli"),
  ("Ismajli",          "DC",   3, 1997, "Albania",     "Empoli"),
  ("Viti",             "DC",  22, 2002, "Italia",      "Empoli"),
  ("Pezzella",         "TS",  29, 1992, "Italia",      "Empoli"),
  ("Cacace",           "TS",  50, 2000, "Nuova Zelanda","Empoli"),
  ("Grassi",           "CDC",  8, 1995, "Italia",      "Empoli"),
  ("Henderson",        "CC",   6, 1994, "Inghilterra", "Empoli"),
  ("Fazzini",          "TRQ",  7, 2003, "Italia",      "Empoli"),
  ("Esposito S.L.",    "ATT", 10, 2002, "Italia",      "Empoli"),
  ("Colombo",          "ATT",  9, 2002, "Italia",      "Empoli"),

  # ── Frosinone ──
  ("Cerofolini",       "POR",  1, 1998, "Italia",      "Frosinone"),
  ("Monterisi",        "TD",   2, 1999, "Italia",      "Frosinone"),
  ("Lucioni",          "DC",   5, 1989, "Italia",      "Frosinone"),
  ("Marchizza",        "TS",   3, 1995, "Italia",      "Frosinone"),
  ("Gelli",            "CC",   8, 2000, "Italia",      "Frosinone"),
  ("Mazzitelli",       "CDC",  4, 1995, "Italia",      "Frosinone"),
  ("Garritano",        "TRQ", 10, 1994, "Italia",      "Frosinone"),
  ("Ghedjemis",        "ALD",  7, 2001, "Algeria",     "Frosinone"),
  ("Kvernadze",        "ATT",  9, 2004, "Georgia",     "Frosinone"),
  ("Soulé",            "TRQ", 27, 2003, "Argentina",   "Frosinone"),

  # ── Juve Stabia ──
  ("Thiam",            "POR",  1, 1997, "Senegal",     "Juve Stabia"),
  ("Floriani Mussolini","TD",  2, 2002, "Italia",      "Juve Stabia"),
  ("Bellich",          "DC",   5, 2002, "Croazia",     "Juve Stabia"),
  ("Folino",           "DC",   6, 1994, "Italia",      "Juve Stabia"),
  ("Mignanelli",       "TS",   3, 1994, "Italia",      "Juve Stabia"),
  ("Buglio",           "CC",   8, 1996, "Italia",      "Juve Stabia"),
  ("Leone",            "CDC",  4, 1997, "Italia",      "Juve Stabia"),
  ("Candellone",       "ATT",  9, 1997, "Italia",      "Juve Stabia"),
  ("Artistico",        "ATT", 11, 2000, "Italia",      "Juve Stabia"),
  ("Adorante",         "ATT", 19, 1999, "Italia",      "Juve Stabia"),

  # ── Mantova ──
  ("Festa",            "POR",  1, 1997, "Italia",      "Mantova"),
  ("Redolfi",          "DC",   5, 1989, "Italia",      "Mantova"),
  ("Brignani",         "DC",   6, 1992, "Italia",      "Mantova"),
  ("Bani M.",          "TS",   3, 1993, "Italia",      "Mantova"),
  ("Arini",            "CDC",  8, 1997, "Italia",      "Mantova"),
  ("Trimboli",         "CC",   4, 2000, "Italia",      "Mantova"),
  ("Fiori",            "TRQ", 10, 1997, "Italia",      "Mantova"),
  ("Galuppini",        "ALD",  7, 1997, "Italia",      "Mantova"),
  ("Bragantini",       "ATT",  9, 1995, "Italia",      "Mantova"),
  ("Mensah",           "ATT", 11, 1998, "Ghana",       "Mantova"),

  # ── Modena ──
  ("Gagno",            "POR",  1, 1992, "Italia",      "Modena"),
  ("Dellavalle",       "TD",   2, 2004, "Italia",      "Modena"),
  ("Zaro",             "DC",   5, 1997, "Italia",      "Modena"),
  ("Botteghin",        "DC",   6, 1991, "Olanda",      "Modena"),
  ("Idrissi",          "TS",   3, 1996, "Marocco",     "Modena"),
  ("Gerli",            "CDC",  8, 1996, "Italia",      "Modena"),
  ("Magnino",          "CC",  14, 1999, "Italia",      "Modena"),
  ("Palumbo",          "TRQ", 10, 1999, "Italia",      "Modena"),
  ("Battistella",      "ALD",  7, 2001, "Italia",      "Modena"),
  ("Gliozzi",          "ATT",  9, 1994, "Italia",      "Modena"),
  ("Mendes",           "ATT", 11, 1999, "Portogallo",  "Modena"),

  # ── Monza ──
  ("Turati",           "POR",  1, 1997, "Italia",      "Monza"),
  ("D'Alessandro",     "POR", 22, 1996, "Italia",      "Monza"),
  ("Izzo",             "TD",   2, 1992, "Italia",      "Monza"),
  ("Marlon",           "DC",   5, 1995, "Brasile",     "Monza"),
  ("Caldirola",        "DC",   6, 1991, "Germania",    "Monza"),
  ("Kyriakopoulos",    "TS",   3, 1996, "Grecia",      "Monza"),
  ("Pessina",          "CDC",  8, 1997, "Italia",      "Monza"),
  ("Bondo",            "CC",  38, 2002, "Francia",     "Monza"),
  ("Ciurria",          "ALD",  7, 1996, "Italia",      "Monza"),
  ("Vignato",          "TRQ", 20, 2002, "Italia",      "Monza"),
  ("Mota",             "ATT",  9, 2001, "Portogallo",  "Monza"),
  ("Djuric",           "ATT", 10, 1990, "Bosnia",      "Monza"),
  ("Keita Balde",      "ATT", 11, 1995, "Senegal",     "Monza"),

  # ── Padova ──
  ("Donnarumma F.",    "POR",  1, 1990, "Italia",      "Padova"),
  ("Curado",           "DC",   5, 1999, "Spagna",      "Padova"),
  ("Circati F.",       "DC",   6, 2001, "Italia",      "Padova"),
  ("Perrotta",         "TD",   2, 1999, "Italia",      "Padova"),
  ("Delli Carri",      "TS",   3, 1999, "Italia",      "Padova"),
  ("Franchini",        "CDC",  8, 1993, "Italia",      "Padova"),
  ("Lella",            "CC",  14, 1996, "Italia",      "Padova"),
  ("Bortolussi",       "ATT",  9, 1997, "Italia",      "Padova"),
  ("Spagnoli",         "ATT", 11, 1995, "Italia",      "Padova"),

  # ── Palermo ──
  ("Desplanches",      "POR", 12, 2002, "Francia",     "Palermo"),
  ("Nedelcearu",       "DC",   5, 1997, "Romania",     "Palermo"),
  ("Ceccaroni",        "DC",  27, 1995, "Italia",      "Palermo"),
  ("Diakité",          "TD",  22, 2000, "Francia",     "Palermo"),
  ("Lund",             "TS",  30, 1999, "USA",         "Palermo"),
  ("Gomes F.",         "CDC", 10, 1998, "Portogallo",  "Palermo"),
  ("Segre",            "CC",   8, 1997, "Italia",      "Palermo"),
  ("Ranocchia",        "CC",   4, 2001, "Italia",      "Palermo"),
  ("Di Mariano",       "ALD", 11, 1993, "Italia",      "Palermo"),
  ("Brunori",          "ATT",  9, 1994, "Italia",      "Palermo"),
  ("Insigne R.",       "ALS",  7, 1996, "Italia",      "Palermo"),
  ("Henry",            "ATT", 19, 1999, "Francia",     "Palermo"),

  # ── Pescara ──
  ("Plizzari",         "POR",  1, 2000, "Italia",      "Pescara"),
  ("Floriani M.",      "TD",   2, 2002, "Italia",      "Pescara"),
  ("Pellacani",        "DC",   5, 2002, "Italia",      "Pescara"),
  ("Brosco",           "DC",   6, 1993, "Italia",      "Pescara"),
  ("Moruzzi",          "TS",   3, 1999, "Italia",      "Pescara"),
  ("Valzania",         "CDC",  8, 1995, "Italia",      "Pescara"),
  ("Squizzato",        "CC",  14, 2001, "Italia",      "Pescara"),
  ("Ferraris",         "TRQ", 10, 1994, "Italia",      "Pescara"),
  ("Merola",           "ALD",  7, 1998, "Italia",      "Pescara"),
  ("Vergani",          "ATT",  9, 1999, "Italia",      "Pescara"),
  ("Cangiano",         "ATT", 11, 2001, "Italia",      "Pescara"),

  # ── Reggiana ──
  ("Motta G.",         "POR",  1, 1993, "Italia",      "Reggiana"),
  ("Meroni L.",        "DC",   5, 2004, "Italia",      "Reggiana"),
  ("Rozzio",           "DC",   6, 1994, "Italia",      "Reggiana"),
  ("Aurelio",          "TD",   2, 1999, "Italia",      "Reggiana"),
  ("Lucchesi",         "TS",   3, 2002, "Italia",      "Reggiana"),
  ("Kabashi",          "CC",   8, 1997, "Kosovo",      "Reggiana"),
  ("Sersanti",         "CDC",  4, 2001, "Italia",      "Reggiana"),
  ("Girma",            "ALS", 11, 2003, "Italia",      "Reggiana"),
  ("Gondo",            "ATT",  9, 1996, "Costa d'Avorio","Reggiana"),
  ("Lanini",           "ATT", 10, 1996, "Italia",      "Reggiana"),

  # ── Sampdoria ──
  ("Ghidotti",         "POR",  1, 2000, "Italia",      "Sampdoria"),
  ("Romagnoli S.",     "POR", 22, 1994, "Italia",      "Sampdoria"),
  ("Bereszynski",      "TD",   2, 1992, "Polonia",     "Sampdoria"),
  ("Ferrari A.",       "DC",   5, 1991, "Italia",      "Sampdoria"),
  ("Vulikic",          "DC",   6, 2002, "Serbia",      "Sampdoria"),
  ("Ioannou",          "TS",   3, 2001, "Cipro",       "Sampdoria"),
  ("Yepes",            "CDC",  8, 1999, "Colombia",    "Sampdoria"),
  ("Kasami",           "CC",  14, 1992, "Svizzera",    "Sampdoria"),
  ("Tutino",           "ATT",  9, 1996, "Italia",      "Sampdoria"),
  ("Borini",           "ATT", 11, 1991, "Italia",      "Sampdoria"),
  ("La Gumina",        "ATT", 19, 1996, "Italia",      "Sampdoria"),

  # ── Spezia ──
  ("Gori",             "POR",  1, 1994, "Italia",      "Spezia"),
  ("Elia",             "TD",   2, 2000, "Italia",      "Spezia"),
  ("Mateju",           "DC",   5, 1996, "Rep. Ceca",   "Spezia"),
  ("Bertola S.",       "DC",   6, 2002, "Italia",      "Spezia"),
  ("Reca",             "TS",   3, 1995, "Polonia",     "Spezia"),
  ("Bandinelli",       "CC",   8, 1995, "Italia",      "Spezia"),
  ("Nagy",             "CDC", 29, 1993, "Ungheria",    "Spezia"),
  ("Delle Monache",    "ALD",  7, 2004, "Italia",      "Spezia"),
  ("Soleri",           "ATT",  9, 1997, "Italia",      "Spezia"),
  ("Esposito F.",      "ATT", 10, 2000, "Italia",      "Spezia"),
  ("Kouda",            "ALS", 11, 2003, "Svezia",      "Spezia"),

  # ── Südtirol ──
  ("Poluzzi",          "POR",  1, 1996, "Italia",      "Südtirol"),
  ("Zaro M.",          "DC",   5, 1997, "Italia",      "Südtirol"),
  ("Giorgini",         "DC",   6, 1996, "Italia",      "Südtirol"),
  ("Siega",            "TD",   2, 2000, "Italia",      "Südtirol"),
  ("Rover",            "TRQ", 10, 1995, "Italia",      "Südtirol"),
  ("Tait",             "CC",   8, 1993, "Australia",   "Südtirol"),
  ("Casiraghi",        "CDC",  4, 2001, "Italia",      "Südtirol"),
  ("Molina",           "ATT",  9, 1998, "Argentina",   "Südtirol"),
  ("Odogwu",           "ATT", 11, 1998, "Nigeria",     "Südtirol"),

  # ── Venezia ──
  ("Joronen",          "POR",  1, 1993, "Finlandia",   "Venezia"),
  ("Idzes",            "DC",   5, 2001, "USA",         "Venezia"),
  ("Sverko",           "DC",   6, 2002, "Croazia",     "Venezia"),
  ("Candela",          "TD",   2, 2000, "Italia",      "Venezia"),
  ("Hrustic",          "CC",   8, 1996, "Australia",   "Venezia"),
  ("Busio",            "CDC", 10, 2002, "USA",         "Venezia"),
  ("Ellertsson",       "CC",   7, 1998, "Islanda",     "Venezia"),
  ("Pohjanpalo",       "ATT",  9, 1994, "Finlandia",   "Venezia"),
  ("Gytkjaer",         "ATT", 11, 1990, "Danimarca",   "Venezia"),
  ("Pierini",          "TRQ", 27, 1999, "Italia",      "Venezia"),

  # ── Virtus Entella ──
  ("Borra",            "POR",  1, 1997, "Italia",      "Entella"),
  ("Parodi",           "DC",   5, 1999, "Italia",      "Entella"),
  ("Bariti",           "DC",   6, 1994, "Italia",      "Entella"),
  ("Corbari",          "CC",   8, 2000, "Italia",      "Entella"),
  ("Franzoni",         "TD",   2, 2001, "Italia",      "Entella"),
  ("Di Mario",         "TRQ", 10, 2001, "Italia",      "Entella"),
  ("Zamparo",          "ATT",  9, 1994, "Italia",      "Entella"),
  ("Castelli",         "ATT", 11, 1994, "Italia",      "Entella"),

  # ═══════════════════════════════════════════════════════════════════
  # SERIE C 2025/2026 — Girone A (Nord)
  # ═══════════════════════════════════════════════════════════════════

  # ── Atalanta U23 ──
  ("Vismara",          "POR",  1, 2003, "Italia",      "Atalanta U23"),
  ("Bernasconi",       "DC",   5, 2003, "Italia",      "Atalanta U23"),
  ("Muhameti",         "CC",   8, 2003, "Albania",     "Atalanta U23"),
  ("Gyabuaa",          "ATT",  9, 2004, "Ghana",       "Atalanta U23"),

  # ── Pro Vercelli ──
  ("Rizzo M.",         "POR",  1, 1997, "Italia",      "Pro Vercelli"),
  ("Carosso",          "DC",   5, 1995, "Italia",      "Pro Vercelli"),
  ("Artioli",          "CC",   8, 1999, "Italia",      "Pro Vercelli"),
  ("Comi",             "ATT",  9, 1994, "Italia",      "Pro Vercelli"),

  # ── Lecco ──
  ("Furlan",           "POR",  1, 1995, "Italia",      "Lecco"),
  ("Battistini",       "DC",   5, 1993, "Italia",      "Lecco"),
  ("Frigerio",         "CC",   8, 1997, "Italia",      "Lecco"),
  ("Pinzauti",         "ATT",  9, 1999, "Italia",      "Lecco"),

  # ── Novara ──
  ("Gasparini",        "POR",  1, 1991, "Italia",      "Novara"),
  ("Khailoti",         "DC",   5, 1997, "Italia",      "Novara"),
  ("Ranieri",          "CC",   8, 2000, "Italia",      "Novara"),
  ("Gori A.",          "ATT",  9, 1997, "Italia",      "Novara"),

  # ── Ternana ──
  ("Iannarilli T.",    "POR",  1, 1993, "Italia",      "Ternana"),
  ("Mantovani T.",     "DC",   5, 1992, "Italia",      "Ternana"),
  ("Cicerelli",        "ALD",  7, 1995, "Italia",      "Ternana"),
  ("Donnarumma V.",    "ATT",  9, 1992, "Italia",      "Ternana"),

  # ── Feralpisalò ──
  ("De Lucia",         "POR",  1, 1995, "Italia",      "Feralpisalò"),
  ("Pilati",           "DC",   5, 1992, "Italia",      "Feralpisalò"),
  ("Balestrero",       "CC",   8, 1993, "Italia",      "Feralpisalò"),
  ("Miracoli",         "ATT",  9, 1989, "Italia",      "Feralpisalò"),

  # ── Trento ──
  ("Tommasi M.",       "POR",  1, 2002, "Italia",      "Trento"),
  ("Cappelletti",      "DC",   5, 1997, "Italia",      "Trento"),
  ("Sangalli",         "CC",   8, 1997, "Italia",      "Trento"),
  ("Petrovic",         "ATT",  9, 2001, "Serbia",      "Trento"),

  # ── AlbinoLeffe ──
  ("Facchetti",        "POR",  1, 1997, "Italia",      "AlbinoLeffe"),
  ("Borghini",         "DC",   5, 1994, "Italia",      "AlbinoLeffe"),
  ("Cori",             "CC",   8, 2000, "Italia",      "AlbinoLeffe"),
  ("Manconi A.",       "ATT",  9, 2000, "Italia",      "AlbinoLeffe"),

  # ── Triestina ──
  ("Roos",             "POR",  1, 1998, "Olanda",      "Triestina"),
  ("Struna",           "DC",   5, 1989, "Slovenia",    "Triestina"),
  ("Voca",             "CC",   8, 1998, "Kosovo",      "Triestina"),
  ("Vertainen",        "ATT",  9, 1998, "Finlandia",   "Triestina"),

  # ── Renate ──
  ("Nobile",           "POR",  1, 1995, "Italia",      "Renate"),
  ("Auriletto",        "DC",   5, 1999, "Italia",      "Renate"),
  ("Ghezzi",           "CC",   8, 1995, "Italia",      "Renate"),
  ("Artistico L.",     "ATT",  9, 2001, "Italia",      "Renate"),

  # ── Pro Patria ──
  ("Priori",           "POR",  1, 1992, "Italia",      "Pro Patria"),
  ("Sportelli",        "DC",   5, 1993, "Italia",      "Pro Patria"),
  ("Nicco",            "CC",   8, 1995, "Italia",      "Pro Patria"),
  ("Chakir",           "ATT",  9, 2001, "Italia",      "Pro Patria"),

  # ── Vicenza ──
  ("Confente",         "POR",  1, 1997, "Italia",      "Vicenza"),
  ("Pasini",           "DC",   5, 1993, "Italia",      "Vicenza"),
  ("Zonta",            "CC",   8, 1999, "Italia",      "Vicenza"),
  ("Rolfini",          "ATT",  9, 1996, "Italia",      "Vicenza"),

  # ═══════════════════════════════════════════════════════════════════
  # SERIE C 2025/2026 — Girone B (Centro)
  # ═══════════════════════════════════════════════════════════════════

  # ── Arezzo ──
  ("Trombini",         "POR",  1, 1999, "Italia",      "Arezzo"),
  ("Giosa",            "DC",   5, 1991, "Italia",      "Arezzo"),
  ("Damiani",          "CC",   8, 2002, "Italia",      "Arezzo"),
  ("Guccione",         "ATT",  9, 1993, "Italia",      "Arezzo"),

  # ── Ascoli ──
  ("Raffaelli",        "POR",  1, 1998, "Italia",      "Ascoli"),
  ("Quaranta",         "DC",   5, 1997, "Italia",      "Ascoli"),
  ("Caligara",         "CC",   8, 1999, "Italia",      "Ascoli"),
  ("Cangiano A.",      "ATT",  9, 2001, "Italia",      "Ascoli"),

  # ── Perugia ──
  ("Albertoni",        "POR",  1, 1994, "Italia",      "Perugia"),
  ("Angella",          "DC",   5, 1989, "Uganda",      "Perugia"),
  ("Iannoni P.",       "CC",   8, 2001, "Italia",      "Perugia"),
  ("Montevago",        "ATT",  9, 2003, "Italia",      "Perugia"),

  # ── Pianese ──
  ("Boer",             "POR",  1, 1999, "Olanda",      "Pianese"),
  ("Polidori",         "DC",   5, 1996, "Italia",      "Pianese"),
  ("Simeoni",          "CC",   8, 1995, "Italia",      "Pianese"),
  ("Bianchi",          "ATT",  9, 1998, "Italia",      "Pianese"),

  # ── Rimini ──
  ("Colombi",          "POR",  1, 1992, "Italia",      "Rimini"),
  ("Gorelli",          "DC",   5, 1999, "Italia",      "Rimini"),
  ("Garetto",          "CC",   8, 2000, "Italia",      "Rimini"),
  ("Malagrida",        "ATT",  9, 2003, "Italia",      "Rimini"),

  # ── Torres ──
  ("Zaccagno",         "POR",  1, 1997, "Italia",      "Torres"),
  ("Dametto",          "DC",   5, 1996, "Italia",      "Torres"),
  ("Mastinu",          "CC",   8, 1993, "Italia",      "Torres"),
  ("Fischnaller",      "ATT",  9, 1992, "Italia",      "Torres"),

  # ── Campobasso ──
  ("Zamarion",         "POR",  1, 2001, "Italia",      "Campobasso"),
  ("Menna",            "DC",   5, 1993, "Italia",      "Campobasso"),
  ("Prezioso",         "CC",   8, 2000, "Italia",      "Campobasso"),
  ("Emmausso",         "ATT",  9, 1997, "Italia",      "Campobasso"),

  # ── Vis Pesaro ──
  ("Farroni",          "POR",  1, 1996, "Italia",      "Vis Pesaro"),
  ("Ceccacci",         "DC",   5, 1995, "Italia",      "Vis Pesaro"),
  ("Peixoto",          "CC",   8, 1998, "Portogallo",  "Vis Pesaro"),
  ("Cannavò",          "ATT",  9, 1997, "Italia",      "Vis Pesaro"),

  # ── SPAL ──
  ("Galeotti",         "POR",  1, 1998, "Italia",      "SPAL"),
  ("Arena S.",         "DC",   5, 1993, "Italia",      "SPAL"),
  ("Puletto",          "CC",   8, 2000, "Italia",      "SPAL"),
  ("Radrezza",         "ATT",  9, 1997, "Italia",      "SPAL"),

  # ── Gubbio ──
  ("Venturi",          "POR",  1, 1994, "Italia",      "Gubbio"),
  ("Tozzuolo",         "DC",   5, 1996, "Italia",      "Gubbio"),
  ("Rosaia",           "CC",   8, 1994, "Italia",      "Gubbio"),
  ("D'Ursi",           "ATT",  9, 1994, "Italia",      "Gubbio"),

  # ── Sestri Levante ──
  ("Anacoura",         "POR",  1, 2001, "Italia",      "Sestri Levante"),
  ("Pane M.",          "DC",   5, 2000, "Italia",      "Sestri Levante"),
  ("Clemenza",         "CC",   8, 1999, "Italia",      "Sestri Levante"),
  ("Forte",            "ATT",  9, 1994, "Italia",      "Sestri Levante"),

  # ── Pontedera ──
  ("Stancampiano",     "POR",  1, 1996, "Italia",      "Pontedera"),
  ("Espeche",          "DC",   5, 1996, "Argentina",   "Pontedera"),
  ("Ladinetti",        "CC",   8, 1998, "Italia",      "Pontedera"),
  ("Ianesi",           "ATT",  9, 2003, "Italia",      "Pontedera"),

  # ═══════════════════════════════════════════════════════════════════
  # SERIE C 2025/2026 — Girone C (Sud)
  # ═══════════════════════════════════════════════════════════════════

  # ── Benevento ──
  ("Manfredini",       "POR",  1, 1993, "Italia",      "Benevento"),
  ("Capellini",        "DC",   5, 1997, "Italia",      "Benevento"),
  ("Obi",              "CDC",  8, 1991, "Nigeria",     "Benevento"),
  ("Manconi A.B.",     "ATT",  9, 1999, "Italia",      "Benevento"),
  ("Lanini M.",        "ATT", 10, 1996, "Italia",      "Benevento"),

  # ── Catania ──
  ("Furlan C.",        "POR",  1, 1997, "Italia",      "Catania"),
  ("Ierardi",          "DC",   5, 1998, "Svizzera",    "Catania"),
  ("Anastasi",         "CC",   8, 1996, "Italia",      "Catania"),
  ("Lunetta",          "ALD",  7, 2000, "Italia",      "Catania"),
  ("Inglese",          "ATT",  9, 1991, "Italia",      "Catania"),

  # ── Potenza ──
  ("Iacovino",         "POR",  1, 1998, "Italia",      "Potenza"),
  ("Verrengia",        "DC",   5, 1997, "Italia",      "Potenza"),
  ("Vecchi",           "CC",   8, 1999, "Italia",      "Potenza"),
  ("Caturano",         "ATT",  9, 1989, "Italia",      "Potenza"),

  # ── Foggia ──
  ("Perina",           "POR",  1, 1994, "Italia",      "Foggia"),
  ("Camigliano",       "DC",   5, 1994, "Italia",      "Foggia"),
  ("Tascone",          "CC",   8, 1994, "Italia",      "Foggia"),
  ("Sarr A.",          "ATT",  9, 1998, "Senegal",     "Foggia"),

  # ── Audace Cerignola ──
  ("Saracco",          "POR",  1, 1999, "Italia",      "Audace Cerignola"),
  ("Visentin",         "DC",   5, 1995, "Italia",      "Audace Cerignola"),
  ("Capomaggio",       "CC",   8, 2000, "Italia",      "Audace Cerignola"),
  ("Ligi",             "DC",   6, 1993, "Italia",      "Audace Cerignola"),
  ("Salvemini",        "ATT",  9, 1996, "Italia",      "Audace Cerignola"),

  # ── Trapani ──
  ("Ujkaj",            "POR",  1, 2000, "Italia",      "Trapani"),
  ("Celiento",         "DC",   5, 1993, "Italia",      "Trapani"),
  ("Martiniello",      "CC",   8, 1992, "Italia",      "Trapani"),
  ("Bove A.",          "ATT",  9, 2001, "Italia",      "Trapani"),

  # ── Crotone ──
  ("D'Alterio",        "POR",  1, 1991, "Italia",      "Crotone"),
  ("Giron",            "TS",   3, 1994, "Francia",     "Crotone"),
  ("Armini",           "DC",   5, 1999, "Italia",      "Crotone"),
  ("Tumminello",       "ATT",  9, 1998, "Italia",      "Crotone"),
  ("Gomez",            "ATT", 10, 1995, "Argentina",   "Crotone"),

  # ── Messina ──
  ("Curtosi",          "POR",  1, 1989, "Italia",      "Messina"),
  ("Lia",              "DC",   5, 1996, "Italia",      "Messina"),
  ("Cavaliere",        "CC",   8, 1998, "Italia",      "Messina"),
  ("Anatriello",       "ATT",  9, 2003, "Italia",      "Messina"),

  # ── Casertana ──
  ("Baiocco",          "POR",  1, 1997, "Italia",      "Casertana"),
  ("Monteagudo",       "DC",   5, 1996, "Spagna",      "Casertana"),
  ("Tavernelli",       "CC",   8, 2000, "Italia",      "Casertana"),
  ("Damiani D.",       "ATT",  9, 2001, "Italia",      "Casertana"),

  # ── Latina ──
  ("Cardinali",        "POR",  1, 1995, "Italia",      "Latina"),
  ("Tonti",            "DC",   5, 1993, "Italia",      "Latina"),
  ("Ricci D.",         "CC",   8, 2001, "Italia",      "Latina"),
  ("Improta",          "ATT",  9, 1993, "Italia",      "Latina"),

  # ── Giugliano ──
  ("Sassi",            "POR",  1, 1997, "Italia",      "Giugliano"),
  ("Solignani",        "DC",   5, 1994, "Italia",      "Giugliano"),
  ("Nocciolini",       "CC",   8, 1998, "Italia",      "Giugliano"),
  ("Cianci",           "ATT",  9, 1995, "Italia",      "Giugliano"),

  # ── Taranto ──
  ("Vannucchi",        "POR",  1, 1998, "Italia",      "Taranto"),
  ("De Santis",        "DC",   5, 1997, "Italia",      "Taranto"),
  ("Speranza",         "CC",   8, 1997, "Italia",      "Taranto"),
  ("Bifulco",          "ATT",  9, 2001, "Italia",      "Taranto"),

  # ── Monopoli ──
  ("Guido",            "POR",  1, 1994, "Italia",      "Monopoli"),
  ("Fornasier",        "DC",   5, 1995, "Italia",      "Monopoli"),
  ("Bizzotto",         "CC",   8, 1997, "Italia",      "Monopoli"),
  ("Yeboah",           "ATT",  9, 2001, "Ghana",       "Monopoli"),

  # ── Sorrento ──
  ("Del Sorbo",        "POR",  1, 1999, "Italia",      "Sorrento"),
  ("Fusco",            "DC",   5, 1996, "Italia",      "Sorrento"),
  ("Acampora",         "CC",   8, 1992, "Italia",      "Sorrento"),
  ("Musso",            "ATT",  9, 1994, "Italia",      "Sorrento"),

  # ── Altamura ──
  ("Russo M.",         "POR",  1, 1996, "Italia",      "Altamura"),
  ("Hadziosmanovic",   "DC",   5, 2001, "Bosnia",      "Altamura"),
  ("Minesso",          "ATT",  9, 1994, "Italia",      "Altamura"),
  ("Leonetti",         "ATT", 10, 1994, "Italia",      "Altamura"),

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
                name=nome, role=ruolo, number=numero,
                birth_year=anno, nationality=nazione, team_name=squadra,
            ))
            count += 1

        db.commit()
        total = db.query(RegistryPlayer).count()
        print(f"✅ Aggiunti {count} calciatori ({skipped} già presenti ignorati)")
        print(f"   Totale anagrafica: {total} calciatori")
        print(f"   Serie A: 20 squadre")
        print(f"   Serie B: 20 squadre")
        print(f"   Serie C: ~60 squadre (giocatori principali)")

    except Exception as e:
        db.rollback()
        print(f"❌ Errore: {e}")
        import traceback; traceback.print_exc()
    finally:
        db.close()

if __name__ == "__main__":
    populate()