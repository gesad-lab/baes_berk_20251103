from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.exc import SQLAlchemyError
import os

# Define the base for SQLAlchemy models
Base = declarative_base()

# Create a new SQLite database (or connect to an existing one)
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./test.db")

# Create an engine instance
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

# Create a configured "Session" class
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def init_db() -> None:
    """Initialize the database schema by creating the required tables."""
    try:
        # Import all models here (to ensure they are registered)
        # e.g. from .models import Student
        # This is where you would do `Base.metadata.create_all(bind=engine)`
        Base.metadata.create_all(bind=engine)
    except SQLAlchemyError as e:
        # Handle database connection errors
        print(f"Error initializing the database: {str(e)}")

# Dependency to get the database session
def get_db() -> Session:
    """Generate a new database session."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()