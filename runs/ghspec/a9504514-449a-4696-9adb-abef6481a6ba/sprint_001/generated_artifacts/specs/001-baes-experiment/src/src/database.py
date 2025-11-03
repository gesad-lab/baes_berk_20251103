import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Define the SQLite database file location
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///students.db")

# Create a SQLAlchemy engine
engine = create_engine(DATABASE_URL)

# Create a declarative base class for the models
Base = declarative_base()

def init_db():
    """
    Initializes the database by creating all tables if they don't already exist.
    """
    Base.metadata.create_all(engine)

# Create a new session factory
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    """
    Dependency that provides a database session to be used in API route handlers.
    Ensures that the session is correctly closed after use.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()