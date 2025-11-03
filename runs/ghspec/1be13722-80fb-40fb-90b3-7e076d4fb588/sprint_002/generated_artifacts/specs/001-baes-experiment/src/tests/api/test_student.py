from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, EmailStr
from typing import List, Optional
from sqlalchemy.orm import Session
from models import Student  # Assuming this is the model for the Student entity
from services import student_service  # Assuming this is where create and fetch logic is handled

app = FastAPI()

class StudentCreate(BaseModel):
    name: str
    email: EmailStr  # Using EmailStr for automatic email validation


class StudentResponse(BaseModel):
    id: int
    name: str
    email: str


@app.post("/students/", response_model=StudentResponse)
def create_student(student: StudentCreate, db: Session):
    """
    Create a new student entity with the provided name and email.
    If the email format is invalid or email is not provided, raise an HTTP exception.
    """
    if not student_service.validate_email(student.email):
        raise HTTPException(status_code=400, detail="Invalid email format")
    
    # Call service to create student
    new_student = student_service.create_student(db=db, name=student.name, email=student.email)
    return StudentResponse(id=new_student.id, name=new_student.name, email=new_student.email)


@app.get("/students/", response_model=List[StudentResponse])
def get_students(db: Session):
    """
    Retrieve a list of all students including their emails.
    """
    students = student_service.get_students(db=db)
    return [StudentResponse(id=student.id, name=student.name, email=student.email) for student in students]