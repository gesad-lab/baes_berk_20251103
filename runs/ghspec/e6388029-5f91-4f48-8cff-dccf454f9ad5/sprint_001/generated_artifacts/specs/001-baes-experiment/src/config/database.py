from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import IntegrityError
import os

# Define the SQLite database URL
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./students.db")

# Create the SQLAlchemy engine
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

# Declare a base class for declarative models
Base = declarative_base()

class Student(Base):
    """Model representing a student in the database."""
    
    __tablename__ = "students"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)

# Create a new session factory
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def init_db():
    """Initialize the database by creating the schema."""
    try:
        # Create the database tables
        Base.metadata.create_all(bind=engine)
    except Exception as e:
        print(f"Error creating database: {e}")  # Log error but don't expose PII or internal details

# Call the initialization function
if __name__ == "__main__":
    init_db()  # Creates the database schema on startup if run as a script