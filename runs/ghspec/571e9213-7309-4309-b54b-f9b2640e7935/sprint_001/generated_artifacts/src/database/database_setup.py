import os
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Define the SQLite database path
DATABASE_URL = "sqlite:///./students.db"

# Create a SQLAlchemy engine
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

# Create a base class for the model
Base = declarative_base()

# Define the Student model
class Student(Base):
    __tablename__ = "students"
    
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String, nullable=False)

def setup_database():
    """Set up the database by creating the necessary tables."""
    # Create all tables in the database
    Base.metadata.create_all(bind=engine)

if __name__ == "__main__":
    # Make sure the database and its tables are created
    setup_database()
    print("Database setup complete.")