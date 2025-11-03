from fastapi import APIRouter, HTTPException, Body
from pydantic import BaseModel, EmailStr
from typing import List
from models.student import Student  # Assuming this is where the Student model is defined
from database import SessionLocal  # Importing the database session
from sqlalchemy.orm import Session

router = APIRouter()

# Pydantic model for request validation and data formatting
class StudentCreateUpdate(BaseModel):
    name: str
    email: EmailStr  # Using Pydantic's EmailStr for email validation

# Response model to format the output
class StudentResponse(BaseModel):
    id: int
    name: str
    email: str

# Dependency for getting the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/students", response_model=StudentResponse, status_code=201)
def create_student(student: StudentCreateUpdate, db: Session = next(get_db())):
    """Create a new student with the provided name and email."""
    db_student = Student(name=student.name, email=student.email)
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return db_student

@router.get("/students/{student_id}", response_model=StudentResponse)
def read_student(student_id: int, db: Session = next(get_db())):
    """Retrieve a student by ID."""
    db_student = db.query(Student).filter(Student.id == student_id).first()
    if db_student is None:
        raise HTTPException(status_code=404, detail="Student not found")
    return db_student

@router.put("/students/{student_id}", response_model=StudentResponse)
def update_student(student_id: int, student: StudentCreateUpdate, db: Session = next(get_db())):
    """Update an existing student's information identified by the student ID."""
    db_student = db.query(Student).filter(Student.id == student_id).first()
    if db_student is None:
        raise HTTPException(status_code=404, detail="Student not found")
    
    # Update student's attributes
    db_student.name = student.name
    db_student.email = student.email
    db.commit()
    db.refresh(db_student)
    return db_student