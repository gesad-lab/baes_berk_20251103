```python
# src/api/student_api.py
from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel, EmailStr, Field
from typing import List, Optional
from src.models import Student
from src.database import SessionLocal

router = APIRouter()

class StudentCreate(BaseModel):
    name: str
    email: EmailStr  # Using Pydantic's built-in email validation

class StudentUpdate(BaseModel):
    name: Optional[str] = None
    email: Optional[EmailStr] = None  # Optional for updates, can be None

class StudentResponse(BaseModel):
    id: int
    name: str
    email: EmailStr

@router.post("/students", response_model=StudentResponse, status_code=status.HTTP_201_CREATED)
def create_student(student: StudentCreate):
    """Create a new student with a valid name and email."""
    db = SessionLocal()
    new_student = Student(name=student.name, email=student.email)
    db.add(new_student)
    db.commit()
    db.refresh(new_student)
    db.close()
    return new_student

@router.put("/students/{student_id}", response_model=StudentResponse)
def update_student(student_id: int, student: StudentUpdate):
    """Update an existing student's details, including email."""
    db = SessionLocal()
    existing_student = db.query(Student).filter(Student.id == student_id).first()

    if not existing_student:
        db.close()
        raise HTTPException(status_code=404, detail="Student not found")

    if student.name is not None:
        existing_student.name = student.name
    if student.email is not None:
        existing_student.email = student.email

    db.commit()
    db.refresh(existing_student)
    db.close()
    
    return existing_student

@router.get("/students/{student_id}", response_model=StudentResponse)
def get_student(student_id: int):
    """Retrieve a student's details by ID."""
    db = SessionLocal()
    student = db.query(Student).filter(Student.id == student_id).first()
    
    if student is None:
        db.close()
        raise HTTPException(status_code=404, detail="Student not found")
    
    db.close()
    return student
```