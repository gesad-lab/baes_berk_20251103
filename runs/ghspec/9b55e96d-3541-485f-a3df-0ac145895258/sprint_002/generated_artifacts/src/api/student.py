```python
# src/api/student.py

from fastapi import APIRouter, HTTPException
from sqlalchemy.orm import Session
from pydantic import BaseModel, EmailStr, ValidationError
from typing import List
from .models import Student
from .database import get_db

router = APIRouter()

class StudentCreate(BaseModel):
    name: str
    email: EmailStr  # This will automatically validate email format

class StudentResponse(BaseModel):
    id: int
    name: str
    email: str

@router.post("/students/", response_model=StudentResponse, status_code=201)
def create_student(student: StudentCreate, db: Session = Depends(get_db)):
    """
    Create a new student and save to the database.

    Parameters:
    - student: StudentCreate: The student data to create.
    - db: Session: The SQLAlchemy database session.
    
    Returns:
    - StudentResponse: The created student's data including ID.
    
    Raises:
    - HTTPException: 400 if the student data is invalid (validation errors).
    """

    # Check for existing student with the same name or email
    existing_student = db.query(Student).filter(
        (Student.name == student.name) | (Student.email == student.email)
    ).first()
    
    if existing_student:
        raise HTTPException(status_code=400, detail="Student with this name or email already exists.")

    new_student = Student(name=student.name, email=student.email)
    
    db.add(new_student)
    db.commit()
    db.refresh(new_student)
    
    return StudentResponse(id=new_student.id, name=new_student.name, email=new_student.email)

@router.get("/students/{student_id}", response_model=StudentResponse)
def read_student(student_id: int, db: Session = Depends(get_db)):
    """
    Retrieve the details of a student by student ID.

    Parameters:
    - student_id: int: The ID of the student to retrieve.
    - db: Session: The SQLAlchemy database session.
    
    Returns:
    - StudentResponse: Student details.
    
    Raises:
    - HTTPException: 404 if student not found.
    """

    student = db.query(Student).filter(Student.id == student_id).first()
    if student is None:
        raise HTTPException(status_code=404, detail="Student not found.")

    return StudentResponse(id=student.id, name=student.name, email=student.email)

@router.put("/students/{student_id}", response_model=StudentResponse)
def update_student(student_id: int, email: EmailStr, db: Session = Depends(get_db)):
    """
    Update a student's email by student ID.

    Parameters:
    - student_id: int: The ID of the student to update.
    - email: EmailStr: The new email to set for the student.
    - db: Session: The SQLAlchemy database session.
    
    Returns:
    - StudentResponse: The updated student's data.
    
    Raises:
    - HTTPException: 400 if the email field is missing or invalid,
                     404 if student not found.
    """

    student = db.query(Student).filter(Student.id == student_id).first()
    if student is None:
        raise HTTPException(status_code=404, detail="Student not found.")
    
    if not email:
        raise HTTPException(status_code=400, detail="Email field is required.")
    
    student.email = email
    
    db.commit()
    db.refresh(student)
    
    return StudentResponse(id=student.id, name=student.name, email=student.email)
```