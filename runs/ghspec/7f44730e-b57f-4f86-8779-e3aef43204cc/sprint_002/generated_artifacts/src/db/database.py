# src/db/database.py

from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.exc import ProgrammingError

Base = declarative_base()

class Student(Base):
    __tablename__ = 'students'
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)  # New email field added

# Configure the SQLite database connection
DATABASE_URL = "sqlite:///./students.db"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def init_db():
    """Initialize the database and update the schema, adding the email column if it doesn't exist."""
    # Create tables if they do not exist
    Base.metadata.create_all(bind=engine)

    # Attempt to add email column if it doesn't already exist
    try:
        with engine.connect() as connection:
            connection.execute('ALTER TABLE students ADD COLUMN email TEXT NOT NULL')
    except ProgrammingError:
        # The column already exists; do nothing
        pass

# Ensure the database is initialized on startup
init_db()