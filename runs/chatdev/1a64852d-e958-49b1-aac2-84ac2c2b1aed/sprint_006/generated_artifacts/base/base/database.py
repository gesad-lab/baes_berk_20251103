'''
Database connection and session management.
'''
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from models import Base  # Import Base to create tables
from alembic import command
from alembic.config import Config
DATABASE_URL = "sqlite:///./students.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
# Create the database tables if they don't exist
Base.metadata.create_all(bind=engine)
# Alembic migration setup
def run_migrations():
    alembic_cfg = Config("alembic.ini")
    command.upgrade(alembic_cfg, "head")
def get_db() -> Session:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()