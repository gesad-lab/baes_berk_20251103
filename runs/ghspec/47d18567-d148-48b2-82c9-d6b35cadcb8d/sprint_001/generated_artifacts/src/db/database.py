from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

# Setting up the SQLite database URL from environment variables
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./students.db")

# Create the SQLAlchemy engine
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

# Base class for declarative models
Base = declarative_base()

class Student(Base):
    """Model for the Student entity."""
    __tablename__ = 'students'

    id = Column(Integer, primary_key=True, index=True)  # Unique identifier
    name = Column(String, nullable=False)  # Student's name should not be null

def init_db() -> None:
    """Create the database tables if they do not exist."""
    # Create all tables in the engine
    Base.metadata.create_all(bind=engine)

# Create a new session local for database interactions
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Call this function to initialize the database on startup
init_db()