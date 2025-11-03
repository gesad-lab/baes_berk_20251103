```python
# src/app.py
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, EmailStr
from sqlalchemy.orm import Session
from src.models import Student  # Assuming Student model is in models.py
from src.db import get_db  # Import the dependency to obtain database sessions

app = FastAPI()

class StudentCreate(BaseModel):
    name: str
    email: EmailStr  # Use EmailStr to enforce proper email formatting

@app.post("/students/", response_model=Student)
def create_student(student: StudentCreate, db: Session = next(get_db())):
    """
    Create a new student with name and email.
    
    :param student: StudentCreate object with name and email.
    :param db: Database session.
    :return: The created student object.
    :raises HTTPException: If email is missing or invalid.
    """
    # Check if the email field is present
    if not student.email:
        raise HTTPException(status_code=400, detail="Email field is required.")

    new_student = Student(name=student.name, email=student.email)
    db.add(new_student)
    db.commit()
    db.refresh(new_student)
    return new_student

@app.get("/students/{student_id}", response_model=Student)
def get_student(student_id: int, db: Session = next(get_db())):
    """
    Retrieve a student's information by ID.
    
    :param student_id: The unique identifier for the student.
    :param db: Database session.
    :return: The student's details in JSON format.
    :raises HTTPException: If student not found.
    """
    student = db.query(Student).filter(Student.id == student_id).first()
    if student is None:
        raise HTTPException(status_code=404, detail="Student not found.")
    return student
```