import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, String
from sqlalchemy.exc import SQLAlchemyError
from fastapi import FastAPI, HTTPException

# SQLAlchemy Database configuration
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./test.db")  # Default SQLite database
Base = declarative_base()

class Student(Base):
    """Database model for student."""
    __tablename__ = "students"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)

# Create SQLAlchemy engine
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def init_db() -> None:
    """Initialize the database by creating all tables."""
    try:
        Base.metadata.create_all(bind=engine)  # Create tables according to the defined models
    except SQLAlchemyError as e:
        print(f"Database initialization error: {e}")  # Log specific errors for debugging

# FastAPI application instance
app = FastAPI()

@app.on_event("startup")
def startup_event():
    """Event to run on application startup; initializes the database."""
    init_db()

# Note: Additional routes for handling student operations will be implemented in a later task.