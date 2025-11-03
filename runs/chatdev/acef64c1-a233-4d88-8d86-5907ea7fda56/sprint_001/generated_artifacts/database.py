'''
Database connection and session management.
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
    Create the database and tables if they don't exist.
    '''
    Base.metadata.create_all(bind=engine)
def get_db() -> Session:
    '''
    Dependency to get the database session.
    '''
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()