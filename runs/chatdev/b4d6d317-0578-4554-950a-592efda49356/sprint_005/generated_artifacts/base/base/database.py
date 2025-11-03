'''
Handles database connection and session management.
'''
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from models import Base  # Import Base from models to include new Course table
DATABASE_URL = "sqlite:///./students.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
def create_database():
    '''
    Create the database and tables if they do not exist.
    This function should be modified to handle migrations in production.
    '''
    Base.metadata.create_all(bind=engine)
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