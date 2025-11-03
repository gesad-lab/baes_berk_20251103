```python
# src/routes/student.py

from fastapi import APIRouter, HTTPException
from sqlalchemy.orm import Session
from pydantic import BaseModel, EmailStr, constr
from typing import List
from src.models.student import Student
from src.database import get_db
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

router = APIRouter()

# Pydantic model for request body
class StudentCreate(BaseModel):
    name: str
    email: EmailStr  # Validate email format

class StudentResponse(BaseModel):
    id: int
    name: str
    email: str

@router.post("/students", response_model=StudentResponse, status_code=201)
def create_student(student: StudentCreate, db: Session = Depends(get_db)):
    # Check if email already exists
    if db.query(Student).filter(Student.email == student.email).first():
        logger.warning(f"Attempt to create a student with an existing email: {student.email}")
        raise HTTPException(status_code=400, detail="Email already exists")

    db_student = Student(name=student.name, email=student.email)
    db.add(db_student)
    db.commit()
    db.refresh(db_student)

    logger.info(f"Created student: {db_student.name} with email: {db_student.email}")
    return db_student

@router.get("/students/{student_id}", response_model=StudentResponse)
def get_student(student_id: int, db: Session = Depends(get_db)):
    db_student = db.query(Student).filter(Student.id == student_id).first()
    if db_student is None:
        logger.error(f"Student not found with id: {student_id}")
        raise HTTPException(status_code=404, detail="Student not found")

    logger.info(f"Retrieved student: {db_student.name} with email: {db_student.email}")
    return db_student

# Add additional routes and logic as necessary...
```