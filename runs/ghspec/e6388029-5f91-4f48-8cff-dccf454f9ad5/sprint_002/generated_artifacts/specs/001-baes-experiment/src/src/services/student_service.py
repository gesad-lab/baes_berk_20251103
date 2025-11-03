```python
# File: src/services/student_service.py

from sqlalchemy.orm import Session
from src.models import Student
from src.schemas import StudentCreate, StudentUpdate
from typing import List
from fastapi import HTTPException

def create_student(db: Session, student: StudentCreate) -> Student:
    """
    Create a new student record in the database.
    
    Parameters:
    - db: SQLAlchemy session.
    - student: StudentCreate model containing student details.
    
    Returns:
    - The created student instance.
    
    Raises:
    - HTTPException if the email is invalid or already exists.
    """
    # Check if the email already exists
    existing_student = db.query(Student).filter(Student.email == student.email).first()
    if existing_student:
        raise HTTPException(status_code=400, detail="E001: Email already exists.")
    
    # Create a new student instance
    new_student = Student(name=student.name, email=student.email)
    db.add(new_student)
    db.commit()
    db.refresh(new_student)
    return new_student

def get_student(db: Session, student_id: int) -> Student:
    """
    Retrieve a student record by its ID.
    
    Parameters:
    - db: SQLAlchemy session.
    - student_id: ID of the student to retrieve.
    
    Returns:
    - The student instance if found.
    
    Raises:
    - HTTPException if the student does not exist.
    """
    student = db.query(Student).filter(Student.id == student_id).first()
    if not student:
        raise HTTPException(status_code=404, detail="Student not found.")
    return student

def update_student(db: Session, student_id: int, student_update: StudentUpdate) -> Student:
    """
    Update an existing student's record.
    
    Parameters:
    - db: SQLAlchemy session.
    - student_id: ID of the student to update.
    - student_update: StudentUpdate model containing fields to update.
    
    Returns:
    - The updated student instance.
    
    Raises:
    - HTTPException if the student does not exist or email is invalid.
    """
    student = db.query(Student).filter(Student.id == student_id).first()
    if not student:
        raise HTTPException(status_code=404, detail="Student not found.")
    
    # Update fields if they are provided
    if student_update.name is not None:
        student.name = student_update.name
    if student_update.email is not None:
        existing_email_student = db.query(Student).filter(Student.email == student_update.email).first()
        if existing_email_student and existing_email_student.id != student_id:
            raise HTTPException(status_code=400, detail="E001: Email already exists.")
        student.email = student_update.email
    
    db.commit()
    db.refresh(student)
    return student

def delete_student(db: Session, student_id: int) -> None:
    """
    Delete a student record by its ID.
    
    Parameters:
    - db: SQLAlchemy session.
    - student_id: ID of the student to delete.
    
    Raises:
    - HTTPException if the student does not exist.
    """
    student = db.query(Student).filter(Student.id == student_id).first()
    if not student:
        raise HTTPException(status_code=404, detail="Student not found.")
    
    db.delete(student)
    db.commit()
```