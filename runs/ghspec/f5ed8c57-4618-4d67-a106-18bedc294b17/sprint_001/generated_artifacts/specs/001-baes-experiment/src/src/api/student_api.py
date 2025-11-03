import logging
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

# Initialize logger
logger = logging.getLogger("student_api")
logger.setLevel(logging.INFO)
handler = logging.StreamHandler()
formatter = logging.Formatter('{"level": "%(levelname)s", "message": "%(message)s", "method": "%(method)s", "url": "%(url)s"}')
handler.setFormatter(formatter)
logger.addHandler(handler)

app = FastAPI()

class Student(BaseModel):
    name: str

students_db = []  # Simulated in-memory database for storing student records

@app.post("/students/", response_model=Student)
async def create_student(student: Student):
    """
    Create a new student record.

    Args:
    - student (Student): The student to be created.

    Returns:
    - Student: The created student data.

    Raises:
    - HTTPException: If the student could not be created.
    """
    logger.info("Creating student", extra={"method": "POST", "url": "/students/"})
    
    # Check if a student with the same name already exists
    if any(s.name == student.name for s in students_db):
        logger.error("Student with this name already exists", extra={"method": "POST", "url": "/students/"})
        raise HTTPException(status_code=400, detail="Student with this name already exists")
    
    students_db.append(student)
    logger.info("Student created successfully", extra={"method": "POST", "url": "/students/", "student": student.dict()})
    return student

@app.get("/students/", response_model=List[Student])
async def get_students():
    """
    Retrieve all student records.

    Returns:
    - List[Student]: A list of all registered students.
    """
    logger.info("Retrieving all students", extra={"method": "GET", "url": "/students/"})
    return students_db

@app.get("/students/{student_name}", response_model=Student)
async def get_student(student_name: str):
    """
    Retrieve a student record by name.

    Args:
    - student_name (str): The name of the student to retrieve.

    Returns:
    - Student: The student data.

    Raises:
    - HTTPException: If the student is not found.
    """
    logger.info("Retrieving student by name", extra={"method": "GET", "url": f"/students/{student_name}"})
    
    student = next((s for s in students_db if s.name == student_name), None)
    if not student:
        logger.error("Student not found", extra={"method": "GET", "url": f"/students/{student_name}"})
        raise HTTPException(status_code=404, detail="Student not found")
    
    logger.info("Student retrieved successfully", extra={"method": "GET", "url": f"/students/{student_name}", "student": student.dict()})
    return student