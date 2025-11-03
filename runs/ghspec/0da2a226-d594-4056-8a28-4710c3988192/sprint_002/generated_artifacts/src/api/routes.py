```python
from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel, EmailStr
from sqlalchemy.orm import Session
from database import get_db
from models import Student
from student_service import create_student, get_student, update_student

router = APIRouter()

class StudentCreate(BaseModel):
    name: str
    email: EmailStr  # Enforcing email format

class StudentResponse(BaseModel):
    id: int
    name: str
    email: str

@router.post("/students", response_model=StudentResponse)
def create_new_student(student: StudentCreate, db: Session = Depends(get_db)):
    if not student.email:
        # Raise an error if email is not provided
        raise HTTPException(status_code=400, detail="E001: Email is a required field")
    
    # Call the service to create a new student
    new_student = create_student(student.name, student.email)
    return new_student

@router.get("/students/{student_id}", response_model=StudentResponse)
def read_student(student_id: int, db: Session = Depends(get_db)):
    student = get_student(student_id)
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    return student

@router.put("/students/{student_id}", response_model=StudentResponse)
def update_student_email(student_id: int, email: EmailStr, db: Session = Depends(get_db)):
    updated_student = update_student(student_id, email)
    if not updated_student:
        raise HTTPException(status_code=404, detail="Student not found")
    return updated_student
```