```python
from fastapi import APIRouter, HTTPException, Request
from pydantic import BaseModel, EmailStr, validator
from typing import List
from sqlalchemy.orm import Session
from . import models, database

router = APIRouter()

class StudentCreate(BaseModel):
    name: str
    email: EmailStr

    @validator('email')
    def validate_email(cls, email):
        # Additional custom email validation logic can be placed here if needed.
        return email

@router.post("/students", response_model=models.Student)
async def create_student(student: StudentCreate):
    # Open a database session
    db: Session = database.get_db()
    
    # Check if the email already exists
    existing_student = db.query(models.Student).filter(models.Student.email == student.email).first()
    if existing_student:
        raise HTTPException(status_code=400, detail={"error": {"code": "E002", "message": "Email already exists."}})

    try:
        # Create a new student instance
        new_student = models.Student(name=student.name, email=student.email)
        db.add(new_student)
        db.commit()
        db.refresh(new_student)

        return new_student
    except Exception as e:
        raise HTTPException(status_code=500, detail={"error": {"code": "E003", "message": f"Unexpected error occurred: {str(e)}"}})

@router.get("/students/{student_id}", response_model=models.Student)
async def get_student(student_id: int):
    # Open a database session
    db: Session = database.get_db()
    
    student = db.query(models.Student).filter(models.Student.id == student_id).first()
    if not student:
        raise HTTPException(status_code=404, detail={"error": {"code": "E001", "message": "Student not found."}})

    return student
```