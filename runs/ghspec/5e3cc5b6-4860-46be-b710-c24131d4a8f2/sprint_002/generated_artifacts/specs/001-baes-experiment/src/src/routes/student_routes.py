```python
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, EmailStr, Field
from typing import List
from src.models.student import Student
from src.database.database import get_db
from sqlalchemy.orm import Session

router = APIRouter()

class StudentCreate(BaseModel):
    name: str
    email: EmailStr  # Email is required and validated

class StudentUpdate(BaseModel):
    name: str = Field(None, description="Name of the student")
    email: EmailStr = Field(None, description="Email of the student")

class StudentResponse(BaseModel):
    id: int
    name: str
    email: EmailStr

@router.post("/students", response_model=StudentResponse, status_code=201)
def create_student(student: StudentCreate, db: Session = next(get_db())):
    """
    Create a new student with a name and email address.
    """
    db_student = Student(name=student.name, email=student.email)
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return db_student

@router.get("/students/{student_id}", response_model=StudentResponse)
def read_student(student_id: int, db: Session = next(get_db())):
    """
    Retrieve a student by ID.
    """
    student = db.query(Student).filter(Student.id == student_id).first()
    if student is None:
        raise HTTPException(status_code=404, detail="Student not found")
    return student

@router.put("/students/{student_id}", response_model=StudentResponse)
def update_student(student_id: int, student: StudentUpdate, db: Session = next(get_db())):
    """
    Update a student's information by ID.
    """
    db_student = db.query(Student).filter(Student.id == student_id).first()
    if db_student is None:
        raise HTTPException(status_code=404, detail="Student not found")

    # Update fields if provided in the request
    if student.name is not None:
        db_student.name = student.name
    if student.email is not None:
        db_student.email = student.email
    
    db.commit()
    db.refresh(db_student)
    return db_student
```