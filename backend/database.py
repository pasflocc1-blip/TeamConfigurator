from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
import sys


def get_db_path():
    """
    In sviluppo: db nella cartella backend/
    Con PyInstaller (.app Mac): db in ~/.myapp/ (persiste tra aggiornamenti)
    """
    if getattr(sys, "frozen", False):
        home = os.path.expanduser("~")
        app_dir = os.path.join(home, ".myapp")
        os.makedirs(app_dir, exist_ok=True)
        return os.path.join(app_dir, "myapp.db")
    else:
        return os.path.join(os.path.dirname(os.path.abspath(__file__)), "myapp.db")


DATABASE_URL = f"sqlite:///{get_db_path()}"

engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False},
    # Forza SQLite a restituire datetime come stringhe ISO (compatibile Mac/Win)
    json_serializer=None,
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()