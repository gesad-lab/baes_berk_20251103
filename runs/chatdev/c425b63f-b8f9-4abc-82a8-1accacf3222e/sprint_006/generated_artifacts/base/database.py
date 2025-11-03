'''
Database connection and session management.
'''
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from .models import Base
DATABASE_URL = "sqlite:///./students.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
def get_db() -> Session:
    '''
    Provides a database session for dependency injection.
    '''
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
# Create the database schema on startup
Base.metadata.create_all(bind=engine)