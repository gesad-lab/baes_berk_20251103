from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, EmailStr
from typing import List
from .models import Student  # Assuming the Student model is defined in models.py
from .database import get_db  # Assuming a function to get the DB session is defined in database.py
from sqlalchemy.orm import Session

router = APIRouter()

# Pydantic model for creating a new student
class StudentCreate(BaseModel):
    name: str
    email: EmailStr  # Email validation handled by Pydantic

# Pydantic model for retrieving student information
class StudentResponse(BaseModel):
    id: int
    name: str
    email: EmailStr

    class Config:
        orm_mode = True  # Enable ORM mode to read data as dictionaries

@router.post("/students", response_model=StudentResponse)
def create_student(student: StudentCreate, db: Session = Depends(get_db)):
    """
    Create a new student with name and email.
    
    Args:
        student (StudentCreate): The student data to create.
        db (Session): Database session.
    
    Returns:
        StudentResponse: The created student's details.
    
    Raises:
        HTTPException: If the email or name is missing.
    """
    if not (student.name and student.email):
        raise HTTPException(status_code=400, detail="Name and email are required.")
    
    db_student = Student(name=student.name, email=student.email)
    db.add(db_student)
    db.commit()
    db.refresh(db_student)

    return db_student

@router.get("/students", response_model=List[StudentResponse])
def get_students(db: Session = Depends(get_db)):
    """
    Retrieve a list of all students.
    
    Args:
        db (Session): Database session.
    
    Returns:
        List[StudentResponse]: List of students with their details.
    """
    students = db.query(Student).all()
    return students