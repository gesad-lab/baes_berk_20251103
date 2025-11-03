```python
from fastapi import APIRouter, HTTPException, Query
from sqlalchemy.orm import Session
from typing import Optional
from database import get_db
from models import Student
from pydantic import BaseModel, Field

router = APIRouter()

# Pydantic model for student creation
class StudentCreate(BaseModel):
    name: str = Field(..., example="John Doe")  # Required field with an example

# Pydantic model for student response
class StudentResponse(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True  # Allows reading data from SQLAlchemy models

@router.post("/students", response_model=StudentResponse, status_code=201)
async def create_student(student: StudentCreate, db: Session = next(get_db())):
    """
    Create a new student in the database.

    Parameters:
    - student: StudentCreate - the student data to create
    - db: Session - the database session

    Returns:
    - StudentResponse - the created student data
    """
    db_student = Student(name=student.name)
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return db_student

@router.get("/students/{student_id}", response_model=StudentResponse)
async def get_student(student_id: int, db: Session = next(get_db())):
    """
    Retrieve a student by ID from the database.

    Parameters:
    - student_id: int - the ID of the student to retrieve
    - db: Session - the database session

    Returns:
    - StudentResponse - the student data if found
    - HTTPException - 404 if student not found
    """
    db_student = db.query(Student).filter(Student.id == student_id).first()
    if db_student is None:
        raise HTTPException(status_code=404, detail="Student not found")
    return db_student
```