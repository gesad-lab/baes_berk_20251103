from fastapi import FastAPI
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database import Base
from models import Student  # Assuming Student model is in models.py

app = FastAPI()

DATABASE_URL = 'sqlite:///students.db'

# Create the database engine
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def init_db() -> None:
    """Initialize the database and create tables."""
    # Create the database schema
    Base.metadata.create_all(bind=engine)

@app.on_event("startup")
async def startup_event() -> None:
    """Event to run on application startup."""
    init_db()  # Initialize the database when the application starts

@app.get("/")
async def read_root() -> dict:
    """Root endpoint to check if the API is running."""
    return {"message": "Welcome to the Student API!"}

# Include more API endpoints for students as needed, such as CRUD operations.