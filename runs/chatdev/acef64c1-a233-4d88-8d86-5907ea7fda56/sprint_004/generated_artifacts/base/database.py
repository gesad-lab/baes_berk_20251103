'''
Database connection and session management.
'''
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from models import Student, Course  # Import Course model
DATABASE_URL = "sqlite:///./students.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
def create_database():
    '''
    Create the database and tables if they don't exist.
    '''
    from models import Base  # Import Base here to avoid circular import
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