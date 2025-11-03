'''
Handles database connection and session management.
'''
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from base import Base  # Updated import
from alembic import command
from alembic.config import Config
import os  # Importing os to check for directory existence
DATABASE_URL = "sqlite:///./students.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
def create_database():
    '''
    Creates the database and tables using Alembic for migrations.
    Initializes Alembic if the directory does not exist.
    '''
    alembic_dir = "alembic"
    if not os.path.exists(alembic_dir):
        os.makedirs(alembic_dir)  # Create the Alembic directory if it doesn't exist
        command.init(alembic_dir)  # Initialize Alembic
    alembic_cfg = Config("alembic.ini")
    command.upgrade(alembic_cfg, "head")  # Run migrations to the latest version
def get_db() -> Session:
    '''
    Provides a database session.
    '''
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()