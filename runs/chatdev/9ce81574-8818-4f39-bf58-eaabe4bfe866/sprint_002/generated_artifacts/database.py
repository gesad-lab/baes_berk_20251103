'''
Handles database connections and session management.
'''
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
DATABASE_URL = "sqlite:///./students.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
def create_database():
    '''
    Create the database tables.
    '''
    Base.metadata.create_all(bind=engine)
def get_db():
    '''
    Get a database session.
    Yields:
    - db: Session - The database session.
    '''
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()