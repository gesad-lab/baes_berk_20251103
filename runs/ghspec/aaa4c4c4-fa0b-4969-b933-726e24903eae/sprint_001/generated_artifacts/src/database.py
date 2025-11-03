from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

# Define the SQLite database URL from an environment variable or a default
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./students.db")

# Create a SQLAlchemy engine
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

# Create a declarative base class
Base = declarative_base()

class Student(Base):
    """Represents the Student entity."""
    __tablename__ = 'students'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)

def create_database():
    """Create the SQLite database and tables."""
    Base.metadata.create_all(bind=engine)

# Create a session local class to interact with the database
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    """Dependency to get a database session."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Run the database creation on startup
if __name__ == "__main__":
    create_database()