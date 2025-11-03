'''
Database connection and session management.
'''
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from base import Base  # Updated import
from alembic import command
from alembic.config import Config
DATABASE_URL = "sqlite:///./students.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
def create_database():
    """
    Create the database and apply migrations if needed.
    """
    alembic_cfg = Config("alembic.ini")
    command.upgrade(alembic_cfg, "head")
def get_db() -> Session:
    """
    Provide a database session for dependency injection.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()