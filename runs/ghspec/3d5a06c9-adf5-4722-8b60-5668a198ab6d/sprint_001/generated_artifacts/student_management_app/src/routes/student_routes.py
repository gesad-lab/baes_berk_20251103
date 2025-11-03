# Content for /student_management_app/src/routes/student_routes.py

"""
student_routes.py

This module contains the route handler definitions for managing student records
within the Student Management Web Application. It provides endpoints for
creating, reading, updating, and deleting student information.

Endpoints:
- POST /students: Create a new student
- GET /students: Retrieve a list of students
- GET /students/{id}: Retrieve a specific student by ID
- PUT /students/{id}: Update a student by ID
- DELETE /students/{id}: Delete a student by ID
"""

from fastapi import APIRouter, HTTPException
from sqlalchemy.orm import Session
from ..models import Student
from ..schemas import StudentCreate, StudentResponse

router = APIRouter()

@router.post("/students", response_model=StudentResponse)
def create_student(student: StudentCreate, db: Session):
    """
    Create a new student record in the database.

    Parameters:
    - student: An instance of StudentCreate containing the student's data.

    Returns:
    - A StudentResponse instance representing the created student.
    """
    db_student = Student(name=student.name)
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return db_student

@router.get("/students")
def read_students(db: Session):
    """
    Retrieve a list of all student records.

    Returns:
    - A list of StudentResponse instances representing the stored students.
    """
    return db.query(Student).all()

@router.get("/students/{id}", response_model=StudentResponse)
def read_student(id: int, db: Session):
    """
    Retrieve a specific student record by ID.

    Parameters:
    - id: The ID of the student to retrieve.

    Returns:
    - A StudentResponse instance representing the retrieved student.

    Raises:
    - HTTPException: If no student with the given ID exists.
    """
    student = db.query(Student).filter(Student.id == id).first()
    if student is None:
        raise HTTPException(status_code=404, detail="Student not found")
    return student

@router.put("/students/{id}", response_model=StudentResponse)
def update_student(id: int, student: StudentCreate, db: Session):
    """
    Update a specific student record by ID.

    Parameters:
    - id: The ID of the student to update.
    - student: An instance of StudentCreate containing the updated student's data.

    Returns:
    - A StudentResponse instance representing the updated student.

    Raises:
    - HTTPException: If no student with the given ID exists.
    """
    db_student = db.query(Student).filter(Student.id == id).first()
    if db_student is None:
        raise HTTPException(status_code=404, detail="Student not found")
    
    db_student.name = student.name
    db.commit()
    db.refresh(db_student)
    return db_student

@router.delete("/students/{id}")
def delete_student(id: int, db: Session):
    """
    Delete a specific student record by ID.

    Parameters:
    - id: The ID of the student to delete.

    Raises:
    - HTTPException: If no student with the given ID exists.
    """
    db_student = db.query(Student).filter(Student.id == id).first()
    if db_student is None:
        raise HTTPException(status_code=404, detail="Student not found")
    
    db.delete(db_student)
    db.commit()
    return {"message": "Student deleted successfully"}
    
# No additional content needs to be modified in this file for the task given. 
# We need to implement the required change in the README.md.
