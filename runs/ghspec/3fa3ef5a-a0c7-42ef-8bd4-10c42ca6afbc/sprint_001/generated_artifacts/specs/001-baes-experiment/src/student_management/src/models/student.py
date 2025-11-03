from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
import logging

# Initialize logging
logging.basicConfig(level=logging.INFO)

# Create FastAPI instance
app = FastAPI(title="Student Management API")

# Define the Student model
class Student(BaseModel):
    name: str

# In-memory storage for students (replace with database in future)
students_db = []

@app.post("/students/", response_model=Student, status_code=201)
async def create_student(student: Student):
    """
    Create a new student.

    Args:
        student: Student object containing the name.

    Returns:
        The created Student object.
    """
    students_db.append(student)
    logging.info(f"Created student: {student.name}")
    return student

@app.get("/students/", response_model=List[Student])
async def get_students():
    """
    Retrieve the list of students.

    Returns:
        A list of Student objects.
    """
    return students_db

@app.exception_handler(Exception)
async def validation_exception_handler(request, exc):
    """
    Handle validation exceptions.

    Args:
        request: The request object.
        exc: The exception object.

    Returns:
        JSON response with error details.
    """
    logging.error(f"An error occurred: {exc}")
    return {"error": {"code": "E001", "message": str(exc)}}

# Run the application with: uvicorn main:app --reload