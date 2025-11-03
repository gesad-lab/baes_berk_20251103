```python
# src/api.py

from fastapi import FastAPI, HTTPException
from sqlalchemy.orm import Session
from pydantic import BaseModel, EmailStr, validator
from src.models import Student, get_db

app = FastAPI()

# Request and response schema for creating/updating a student
class StudentCreate(BaseModel):
    name: str
    email: EmailStr  # Use Pydantic's EmailStr for email validation

class StudentResponse(BaseModel):
    id: int
    name: str
    email: EmailStr

    class Config:
        orm_mode = True

@app.post("/students/", response_model=StudentResponse)
def create_student(student: StudentCreate, db: Session = next(get_db())):
    """Create a new student record."""
    new_student = Student(name=student.name, email=student.email)
    db.add(new_student)
    db.commit()
    db.refresh(new_student)
    return new_student

@app.get("/students/{student_id}", response_model=StudentResponse)
def get_student(student_id: int, db: Session = next(get_db())):
    """Retrieve student details by ID."""
    student = db.query(Student).filter(Student.id == student_id).first()
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    return student

@app.put("/students/{student_id}", response_model=StudentResponse)
def update_student(student_id: int, student: StudentCreate, db: Session = next(get_db())):
    """Update student's email."""
    existing_student = db.query(Student).filter(Student.id == student_id).first()
    if not existing_student:
        raise HTTPException(status_code=404, detail="Student not found")
    
    existing_student.email = student.email
    db.commit()
    db.refresh(existing_student)
    return existing_student

# Database migration-related code would go elsewhere, typically in a migration script.
```
