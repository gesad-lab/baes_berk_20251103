'''
Database connection management for the application.
'''
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from models import Base
DATABASE_URL = "sqlite:///./students.db"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
def get_db() -> Session:
    '''
    Provides a database session for dependency injection.
    Returns:
    - A Session object.
    '''
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()