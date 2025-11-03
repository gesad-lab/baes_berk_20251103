from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session

# Define the SQLite database URL
DATABASE_URL = "sqlite:///./students.db"

# Create an instance of the SQLAlchemy engine
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

# Declare a base class for model definitions
Base = declarative_base()

def get_db() -> Session:
    """
    Dependency that provides a database session to the caller.

    Returns:
        Session: A new SQLAlchemy database session.
    """
    db = sessionmaker(autocommit=False, autoflush=False, bind=engine)()
    try:
        yield db
    finally:
        db.close()