'''
Database connection and session management.
'''
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from models import Course, Teacher  # Import Course and Teacher models
DATABASE_URL = "sqlite:///./students.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
def get_db() -> Session:
    '''
    Create a new database session.
    '''
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
def init_db() -> None:
    '''
    Initialize the database and create tables.
    '''
    Base.metadata.create_all(bind=engine)