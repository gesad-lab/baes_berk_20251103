from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, EmailStr
from typing import List

app = FastAPI()

# Database simulation
students_db = []

class Student(BaseModel):
    name: str
    email: EmailStr

@app.post("/students/", response_model=Student)
async def create_student(student: Student):
    """
    Create a new student with name and email.
    
    Args:
        student (Student): The student data with name and email.
        
    Returns:
        Student: The created student object.

    Raises:
        HTTPException: If the email is missing or improperly formatted.
    """
    if not student.email:
        raise HTTPException(status_code=400, detail="E001: Email must be provided.")
    
    # Check for existing student with the same email
    if any(existing_student.email == student.email for existing_student in students_db):
        raise HTTPException(status_code=400, detail="E002: Email already registered.")

    students_db.append(student)
    return student

@app.get("/students/", response_model=List[Student])
async def retrieve_students():
    """
    Retrieve a list of all students.
    
    Returns:
        List[Student]: A list of all student objects.
    """
    return students_db