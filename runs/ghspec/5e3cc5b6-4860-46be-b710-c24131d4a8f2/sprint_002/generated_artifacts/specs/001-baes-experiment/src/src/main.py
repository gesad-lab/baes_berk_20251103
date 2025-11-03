from fastapi import FastAPI, HTTPException, Body
from pydantic import BaseModel, EmailStr
from typing import List
from src.models.student import Student
from src.database.database import get_db

app = FastAPI()

# Define Pydantic schemas for request and response validation
class StudentCreate(BaseModel):
    name: str
    email: EmailStr  # Updated to include email validation

class StudentResponse(BaseModel):
    id: int
    name: str
    email: str

@app.post("/students", response_model=StudentResponse, status_code=201)
async def create_student(student: StudentCreate):
    """
    Create a new student with a name and email.
    Returns the created student details.
    """
    db = get_db()
    # Logic to save the student to the database
    # Assuming `student` is an instance of a SQLAlchemy model
    new_student = Student(name=student.name, email=student.email)
    db.add(new_student)
    db.commit()
    db.refresh(new_student)
    return new_student

@app.get("/students/{student_id}", response_model=StudentResponse)
async def get_student(student_id: int):
    """
    Retrieve a student by ID.
    Returns the student's details including name and email.
    """
    db = get_db()
    student = db.query(Student).filter(Student.id == student_id).first()
    if student is None:
        raise HTTPException(status_code=404, detail="Student not found")
    return student

@app.put("/students/{student_id}", response_model=StudentResponse)
async def update_student(student_id: int, student: StudentCreate):
    """
    Update an existing student's name and email.
    Returns the updated student details.
    """
    db = get_db()
    existing_student = db.query(Student).filter(Student.id == student_id).first()
    if existing_student is None:
        raise HTTPException(status_code=404, detail="Student not found")
    
    # Update the student's details
    existing_student.name = student.name
    existing_student.email = student.email
    db.commit()
    db.refresh(existing_student)
    return existing_student

# Ensure to include your existing routes and additional configurations as needed

# Error handling is covered by the use of HTTPException for student not found scenarios.