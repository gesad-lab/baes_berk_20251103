```python
from fastapi import APIRouter, HTTPException, Body
from pydantic import BaseModel, EmailStr
from typing import List
from src.models.student import Student  # Assuming you have a Student model defined
from src.database import SessionLocal  # Assuming you are using a session for DB
from sqlalchemy.orm import Session

router = APIRouter()

# Pydantic schema for creating and retrieving a student
class StudentCreate(BaseModel):
    name: str
    email: EmailStr  # Using Pydantic's EmailStr for validation

class StudentResponse(BaseModel):
    id: int
    name: str
    email: str

@router.post("/students", response_model=StudentResponse, status_code=201)
def create_student(student: StudentCreate):
    """Create a new student with a name and email."""
    db: Session = SessionLocal()
    new_student = Student(name=student.name, email=student.email)
    db.add(new_student)
    db.commit()
    db.refresh(new_student)
    return StudentResponse(id=new_student.id, name=new_student.name, email=new_student.email)

@router.get("/students/{student_id}", response_model=StudentResponse)
def get_student(student_id: int):
    """Retrieve a student by ID."""
    db: Session = SessionLocal()
    student = db.query(Student).filter(Student.id == student_id).first()
    if student is None:
        raise HTTPException(status_code=404, detail="Student not found")
    return StudentResponse(id=student.id, name=student.name, email=student.email)

@router.get("/students", response_model=List[StudentResponse])
def list_students():
    """List all students."""
    db: Session = SessionLocal()
    students = db.query(Student).all()
    return [StudentResponse(id=student.id, name=student.name, email=student.email) for student in students]
```