'''
Handles database connections and session management.
'''
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
DATABASE_URL = "sqlite:///./students.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
def create_database():
    '''
    Creates the database and tables if they do not exist.
    '''
    from models import Course, Teacher  # Moved import here to avoid circular import
    Base.metadata.create_all(bind=engine)
def get_db() -> Session:
    '''
    Provides a database session for each request.
    '''
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()