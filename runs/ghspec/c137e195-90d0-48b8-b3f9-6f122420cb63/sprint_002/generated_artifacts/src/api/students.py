from fastapi import APIRouter, HTTPException
from models.student import Student
from database.db import SessionLocal
from pydantic import BaseModel, EmailStr
from typing import List

router = APIRouter()

class StudentCreate(BaseModel):
    name: str
    email: EmailStr  # Use Pydantic for email validation

@router.post("/students", response_model=StudentCreate, status_code=201)
def create_student(student: StudentCreate):
    """Create a new student in the database."""
    db = SessionLocal()
    new_student = Student(name=student.name, email=student.email)
    
    # Add the new student to the database
    db.add(new_student)
    
    try:
        db.commit()  # Commit the transaction
        db.refresh(new_student)  # Refresh instance to get the ID
    except Exception as e:
        db.rollback()  # Rollback in case of error
        raise HTTPException(status_code=400, detail=str(e))  # Return error response
    
    return new_student  # Return the created student

@router.get("/students", response_model=List[StudentCreate], status_code=200)
def get_students():
    """Retrieve all students from the database."""
    db = SessionLocal()
    students = db.query(Student).all()  # Query to get all students
    return students  # Return list of students