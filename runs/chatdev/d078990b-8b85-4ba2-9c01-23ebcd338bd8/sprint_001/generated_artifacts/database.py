'''
Database connection and initialization.
'''
from sqlalchemy import create_engine
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
    Base.metadata.create_all(bind=engine)