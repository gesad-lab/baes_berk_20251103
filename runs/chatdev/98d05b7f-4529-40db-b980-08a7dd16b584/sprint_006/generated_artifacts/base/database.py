'''
Database connection and session management.
'''
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.ext.declarative import declarative_base
from models import Base, Student, Course, Teacher  # Ensure Teacher is imported
from alembic import command
from alembic.config import Config
DATABASE_URL = "sqlite:///./students.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
def get_db() -> Session:
    '''
    Get a new database session.
    '''
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
def init_db():
    '''
    Initialize the database and create the schema.
    '''
    # Create the tables in the database
    Base.metadata.create_all(bind=engine)  # This will now create Student, Course, and Teacher tables
    # Run Alembic migrations if needed
    alembic_cfg = Config("alembic.ini")
    command.upgrade(alembic_cfg, "head")