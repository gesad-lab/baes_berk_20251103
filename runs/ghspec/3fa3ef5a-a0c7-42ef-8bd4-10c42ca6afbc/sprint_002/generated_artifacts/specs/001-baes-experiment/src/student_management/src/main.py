```python
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, EmailStr
from typing import List
from models.student import Student  # Assuming Student model exists with SQLAlchemy
from services.student_service import create_student, get_students  # Assuming these service functions exist
from database.db import SessionLocal  # Assuming you have a session management for database

app = FastAPI()

# Pydantic model for Student input validation
class StudentCreate(BaseModel):
    name: str
    email: EmailStr  # Validate email format

class StudentResponse(BaseModel):
    id: int
    name: str
    email: EmailStr

@app.post("/students/", response_model=StudentResponse)
def add_student(student: StudentCreate):
    """
    Create and return a new student.
    
    :param student: The student data including name and email.
    :return: The created student data.
    :raises HTTPException: If there is an issue with saving the student.
    """
    try:
        # Create the student using the service layer
        created_student = create_student(student.name, student.email)
        return created_student
    except Exception as e:
        # Log error (consider using a proper logger)
        print(f"Error creating student: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")

@app.get("/students/", response_model=List[StudentResponse])
def read_students():
    """
    Retrieve a list of all students.
    
    :return: A list of all students with their details.
    :raises HTTPException: If there is an error fetching students.
    """
    try:
        students = get_students()
        return students
    except Exception as e:
        # Log error (consider using a proper logger)
        print(f"Error fetching students: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")
```