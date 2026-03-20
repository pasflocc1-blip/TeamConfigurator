from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
import sys

def get_db_path():
    if getattr(sys, "frozen", False):
        home = os.path.expanduser("~")
        app_dir = os.path.join(home, ".myapp")
        os.makedirs(app_dir, exist_ok=True)
        db_path = os.path.join(app_dir, "myapp.db")
        # Se il db esiste ma è corrotto/da bundle, eliminalo
        return db_path
    else:
        return os.path.join(os.path.dirname(__file__), "myapp.db")

DATABASE_URL = f"sqlite:///{get_db_path()}"

engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False}  # necessario per SQLite + FastAPI
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    """Dependency FastAPI per ottenere la sessione DB"""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()