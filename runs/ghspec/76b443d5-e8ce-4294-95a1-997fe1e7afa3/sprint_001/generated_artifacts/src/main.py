from fastapi import FastAPI, HTTPException, Request
from pydantic import BaseModel
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session

# Define the database URL (using SQLite for development)
DATABASE_URL = "sqlite:///./test.db"

# Initialize SQLAlchemy components
engine = create_engine(DATABASE_URL)
Base = declarative_base()

# Database model for Student
class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)

# Pydantic model for student request body
class StudentCreate(BaseModel):
    name: str

# FastAPI application
app = FastAPI()

@app.on_event("startup")
async def startup():
    # Create the database schema if it doesn't exist
    Base.metadata.create_all(bind=engine)

@app.post("/students", response_model=StudentCreate)
async def create_student(student: StudentCreate):
    if not student.name:
        raise HTTPException(status_code=400, detail="E001: Missing name")
    
    # This would typically include the logic to add the student to the database
    # For now, we will simulate an in-memory structure only for demonstration
    new_student = Student(name=student.name)
    # Logic to save the student to the database would go here

    return new_student

@app.get("/students/{id}", response_model=StudentCreate)
async def read_student(id: int):
    # This would typically include the logic to retrieve a student from the database
    # Simulating a student retrieval for demonstration purposes
    student_data = {"id": id, "name": "Example Student"}  # Replace with actual DB call

    if student_data:
        return student_data
    else:
        raise HTTPException(status_code=404, detail="Student not found")