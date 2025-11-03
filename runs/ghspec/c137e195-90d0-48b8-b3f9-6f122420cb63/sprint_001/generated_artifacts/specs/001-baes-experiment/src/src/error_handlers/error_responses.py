```python
from fastapi import APIRouter, HTTPException
from models.student import Student
from database.db import SessionLocal
from typing import List

router = APIRouter()

@router.post("/students", response_model=Student, status_code=201)
def create_student(student: Student):
    """
    Create a new student.

    Args:
        student (Student): The student data to create.

    Raises:
        HTTPException: If the student name is missing.

    Returns:
        Student: The created student object.
    """
    # Validate that the name field is provided
    if not student.name:
        raise HTTPException(status_code=400, detail="Name is required")
    
    db = SessionLocal()
    # Add the new student to the database session
    db.add(student)
    db.commit()
    db.refresh(student)  # Refresh the student instance with the new data
    return student

@router.get("/students", response_model=List[Student], status_code=200)
def get_students():
    """
    Retrieve a list of all students.

    Returns:
        List[Student]: A list of student objects.
    """
    db = SessionLocal()
    students = db.query(Student).all()  # Query all students from the database
    return students
```