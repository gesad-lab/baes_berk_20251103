from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, EmailStr
import logging

# Initialize FastAPI app
app = FastAPI()

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Sample in-memory database for demonstration purposes
students_db = {}

# Pydantic model for Student data
class Student(BaseModel):
    name: str
    email: EmailStr  # Ensures email is in valid format

@app.post("/students")
async def create_student(student: Student):
    """
    Create a new student record with name and email.
    
    Parameters:
    - student: Student model containing name and email fields.

    Returns:
    - Created student object in JSON format.
    """
    if student.email in students_db:
        logger.error(f"Email already exists: {student.email}")
        raise HTTPException(status_code=400, detail="Email already exists")
    
    student_id = len(students_db) + 1
    students_db[student_id] = student
    logger.info(f"Created student {student_id}: {student.name}, {student.email}")
    
    return {"id": student_id, "name": student.name, "email": student.email}

@app.get("/students/{student_id}")
async def get_student(student_id: int):
    """
    Retrieve details of a specific student by ID.

    Parameters:
    - student_id: ID of the student to retrieve.

    Returns:
    - Student object in JSON format.
    
    Raises:
    - HTTP 404 if student ID is not found.
    """
    student = students_db.get(student_id)
    if not student:
        logger.warning(f"Student ID not found: {student_id}")
        raise HTTPException(status_code=404, detail="Student not found")
    
    logger.info(f"Retrieved student {student_id}: {student.name}, {student.email}")
    return {"id": student_id, "name": student.name, "email": student.email}

@app.put("/students/{student_id}")
async def update_student(student_id: int, student: Student):
    """
    Update a student's email address by ID.

    Parameters:
    - student_id: ID of the student to update.
    - student: Student model containing updated email field.

    Returns:
    - Updated student object in JSON format.
    
    Raises:
    - HTTP 404 if student ID is not found.
    """
    if student_id not in students_db:
        logger.error(f"Attempted to update non-existent student ID: {student_id}")
        raise HTTPException(status_code=404, detail="Student not found")
    
    students_db[student_id] = student
    logger.info(f"Updated student {student_id}: {student.name}, {student.email}")
    
    return {"id": student_id, "name": student.name, "email": student.email}