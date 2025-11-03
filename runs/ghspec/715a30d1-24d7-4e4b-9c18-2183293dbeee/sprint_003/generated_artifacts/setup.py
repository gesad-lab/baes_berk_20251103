from fastapi import FastAPI
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from models import Course  # Import the Course model
import os

# Database configuration
SQLALCHEMY_DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./database.db")

# Set up the database engine and session
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create the base class for the SQLAlchemy models
Base = declarative_base()

# Initialize the FastAPI application
app = FastAPI()

@app.on_event("startup")
def startup_event():
    # Create the database tables if they don't exist
    Base.metadata.create_all(bind=engine)

@app.on_event("shutdown")
def shutdown_event():
    # Optional: Cleanup actions if necessary
    pass

# Example FastAPI route to create a Course
@app.post("/courses/")
async def create_course(course: Course):
    # This function would typically call a service layer to handle business logic
    return {"message": "Course created successfully", "course": course}

# Example route to retrieve courses (to be implemented)
@app.get("/courses/")
async def get_courses():
    # This function would typically call a service layer to retrieve courses
    # This is a placeholder response
    return {"courses": []}  # Replace with actual retrieval logic

# Example placeholder for other routes (as needed)
# @app.get("/courses/{course_id}")
# async def read_course(course_id: int):
#     pass

# Run the application with `uvicorn main:app --reload` if needed for development.