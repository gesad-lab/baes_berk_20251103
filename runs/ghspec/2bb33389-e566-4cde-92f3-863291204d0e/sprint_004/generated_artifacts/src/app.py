```python
# src/app.py

from fastapi import FastAPI, HTTPException
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from src.database import init_db, Base, SessionLocal
from src.models import StudentCourses  # Import the StudentCourses model
from src.models import Course, Student  # Assuming these models are defined in src/models.py

DATABASE_URL = "sqlite:///./database.db"  # Update to your actual database connection string

# Create the SQLAlchemy engine
engine = create_engine(DATABASE_URL)
# Create a new session maker
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create the FastAPI app
app = FastAPI()

def verify_database_migrations():
    """Ensure that the database is initialized and the StudentCourses table exists."""
    # Create all tables in the database if they do not exist
    Base.metadata.create_all(bind=engine)

    # Here you can implement additional migration verification logic if needed
    # For instance, checking if the `student_courses` table exists and is properly set up

@app.on_event("startup")
async def startup_event():
    """Startup event handler for the application."""
    verify_database_migrations()

@app.get("/")
def read_root():
    return {"message": "Welcome to the Student Enrollment API"}

# Add additional endpoint implementations for student enrollment and retrieval as needed
# Ensure to catch specific exceptions and handle errors as specified in the guidelines
```