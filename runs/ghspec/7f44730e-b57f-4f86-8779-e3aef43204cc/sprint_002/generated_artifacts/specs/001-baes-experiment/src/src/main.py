```python
# src/main.py
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, EmailStr
from db.database import init_db
from models.student import Student
from sqlalchemy.orm import Session
from db.database import SessionLocal

app = FastAPI()

@app.on_event("startup")
def startup_event():
    init_db()

class StudentCreate(BaseModel):
    name: str
    email: EmailStr

@app.post("/students")
def create_student(student: StudentCreate):
    """Create a new student record with name and email."""
    db: Session = SessionLocal()
    new_student = Student(name=student.name, email=student.email)
    db.add(new_student)
    db.commit()
    db.refresh(new_student)
    return {"message": "Student created successfully", "student": {"name": new_student.name, "email": new_student.email}}

@app.get("/students")
def get_students():
    """Retrieve a list of all students and their emails."""
    db: Session = SessionLocal()
    students = db.query(Student).all()
    return [{"name": student.name, "email": student.email} for student in students]
```