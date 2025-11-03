from fastapi import FastAPI, HTTPException
from sqlalchemy.orm import Session
from pydantic import BaseModel, Field
from typing import List
from models import Student
from services import create_student, get_students
from database import SessionLocal, init_db

app = FastAPI()

# Initialize the database
init_db()

class StudentCreate(BaseModel):
    name: str = Field(..., description="The name of the student, required.")

@app.post("/students", response_model=Student, status_code=201)
def add_student(student: StudentCreate):
    # Validate that the student has a name
    if not student.name:
        raise HTTPException(status_code=400, detail="Name field is required.")
    
    # Create the student and return the created object
    return create_student(session=SessionLocal(), name=student.name)

@app.get("/students", response_model=List[Student])
def read_students():
    # Retrieve and return all students
    return get_students(session=SessionLocal())