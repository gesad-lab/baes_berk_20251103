'''
Handles database connection and session management.
'''
from sqlalchemy import create_engine, inspect
from sqlalchemy.orm import sessionmaker, Session
from base import Base  # Import Base from the new base.py
DATABASE_URL = "sqlite:///./students.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
def create_database():
    '''
    Create the database and tables if they do not exist.
    This function checks for existing tables to prevent data loss.
    '''
    Base.metadata.create_all(bind=engine)  # Create all tables defined in Base
def get_db() -> Session:
    '''
    Get a database session.
    Returns:
    - Session: The database session.
    '''
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()