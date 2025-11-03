'''
Database connection and initialization.
'''
from sqlalchemy import create_engine, Column, Integer, String, inspect
from sqlalchemy.orm import sessionmaker, Session
from models import Base
DATABASE_URL = "sqlite:///./students.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
def get_db() -> Session:
    '''
    Dependency to get the database session.
    '''
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
def init_db():
    '''
    Initialize the database and create tables.
    '''
    # Check if the 'courses' table exists before creating it
    inspector = inspect(engine)
    if 'courses' not in inspector.get_table_names():
        Base.metadata.create_all(bind=engine)