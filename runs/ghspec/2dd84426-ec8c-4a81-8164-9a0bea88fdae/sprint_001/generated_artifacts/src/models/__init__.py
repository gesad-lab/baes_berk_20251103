from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Database configuration
DATABASE_URL = "sqlite:///students.db"

# Initialize the SQLAlchemy engine
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

# Base class for declarative models
Base = declarative_base()

# Create a new session maker
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def init_db():
    """Create the database schema on application startup."""
    # Import all models here to register them with SQLAlchemy
    from .student import Student  # Ensure the Student model is imported
    Base.metadata.create_all(bind=engine)  # Create tables in the database

# Call the database initialization function
init_db()