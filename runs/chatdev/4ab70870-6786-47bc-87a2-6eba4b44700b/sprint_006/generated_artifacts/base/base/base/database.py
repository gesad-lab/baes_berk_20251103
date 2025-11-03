'''
Database connection and session management.
'''
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
SQLALCHEMY_DATABASE_URL = "sqlite:///./students.db"
# Create the database engine
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
# Create a configured "Session" class
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
# Create a base class for declarative models
Base = declarative_base()
def get_db() -> Session:
    '''
    Dependency that provides a database session.
    '''
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()