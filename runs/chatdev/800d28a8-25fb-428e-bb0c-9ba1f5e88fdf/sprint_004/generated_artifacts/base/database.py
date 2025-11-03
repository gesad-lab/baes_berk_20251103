'''
Handles database connection and session management.
'''
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from models import Base  # Import Base to create tables
from alembic import command
from alembic.config import Config
DATABASE_URL = "sqlite:///./students.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
def create_database():
    '''
    Creates the database and tables if they do not exist and applies migrations.
    '''
    # Create tables if they do not exist
    Base.metadata.create_all(bind=engine)
    # Apply migrations using Alembic
    alembic_cfg = Config("alembic.ini")
    command.upgrade(alembic_cfg, "head")
def get_db() -> Session:
    '''
    Provides a database session for each request.
    '''
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()