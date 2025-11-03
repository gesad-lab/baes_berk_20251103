from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import List

app = FastAPI()

# Define the Student model with Pydantic
class Student(BaseModel):
    name: str = Field(..., min_length=1, max_length=100, description="The name of the student. Required and must be between 1 and 100 characters.")

# In-memory storage for students (for demonstration purposes)
students_db = []

@app.post("/students", response_model=Student, status_code=201)
async def create_student(student: Student):
    """
    Create a new student entity.

    :param student: Student object containing the student's name
    :return: The created Student object
    :raises HTTPException: If the name is not provided or invalid
    """
    # Validate the name field
    if not student.name:
        raise HTTPException(status_code=400, detail={"error": {"code": "E001", "message": "The name field is required."}})

    # Add student to the database
    students_db.append(student)
    return student

@app.get("/students", response_model=List[Student], status_code=200)
async def get_students():
    """
    Retrieve all student entities.

    :return: List of Student objects
    """
    return students_db

@app.get("/students/{student_id}", response_model=Student, status_code=200)
async def get_student(student_id: int):
    """
    Retrieve a student entity by its ID.

    :param student_id: The ID of the student
    :return: The Student object
    :raises HTTPException: If the student is not found
    """
    if student_id < 0 or student_id >= len(students_db):
        raise HTTPException(status_code=404, detail={"error": {"code": "E002", "message": "Student not found."}})
    return students_db[student_id]