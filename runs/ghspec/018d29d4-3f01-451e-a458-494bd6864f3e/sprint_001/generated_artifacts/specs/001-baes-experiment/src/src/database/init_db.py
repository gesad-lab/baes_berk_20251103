from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
import os

# Define the base class for declarative models
Base = declarative_base()

class Student(Base):
    """Model for the student entity."""
    __tablename__ = 'students'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)  # Required field

def init_db():
    """Initialize the database schema."""
    # Fetch the database URL from environment variables
    database_url = os.getenv('DATABASE_URL', 'sqlite:///./test.db')  # Default to SQLite in the local file
    engine = create_engine(database_url)

    # Create all tables in the database which are defined by Base's subclasses
    Base.metadata.create_all(engine)

    # Create a session factory
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

    # Optional: Print initialization success
    print("Database initialized successfully: Student table created.")  

if __name__ == "__main__":
    init_db()  # Run database initialization on startup