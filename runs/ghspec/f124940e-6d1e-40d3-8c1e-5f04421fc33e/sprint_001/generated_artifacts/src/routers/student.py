from fastapi import APIRouter, HTTPException, Status
from sqlalchemy.orm import Session
from typing import List
from src.models import Student
from src.database import get_db

router = APIRouter()

@router.get("/students", response_model=List[Student])
def get_students(db: Session = next(get_db())):
    """
    Retrieve all students from the database.

    Args:
        db (Session): Database session object

    Returns:
        List[Student]: A list of student records in JSON format
    """
    students = db.query(Student).all()
    return students  # Response will automatically return 200 OK with JSON payload


@router.post("/students", response_model=Student, status_code=201)
def create_student(student: Student, db: Session = next(get_db())):
    """
    Create a new student in the database.

    Args:
        student (Student): The student data to be created

    Returns:
        Student: The created student record in JSON format
    """
    db.add(student)
    db.commit()
    db.refresh(student)
    return student  # Response will return 201 Created with student data


@router.put("/students/{student_id}", response_model=Student)
def update_student(student_id: int, student_data: Student, db: Session = next(get_db())):
    """
    Update an existing student's name in the database.

    Args:
        student_id (int): The ID of the student to update
        student_data (Student): The new student data

    Returns:
        Student: The updated student record in JSON format
    """
    student = db.query(Student).filter(Student.id == student_id).first()
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    
    student.name = student_data.name
    db.commit()
    db.refresh(student)
    return student  # Response will return 200 OK with updated student data


@router.delete("/students/{student_id}", status_code=204)
def delete_student(student_id: int, db: Session = next(get_db())):
    """
    Delete a student from the database.

    Args:
        student_id (int): The ID of the student to delete

    Returns:
        None: 204 No Content on successful deletion
    """
    student = db.query(Student).filter(Student.id == student_id).first()
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    
    db.delete(student)
    db.commit()
    return  # Response will return 204 No Content on successful deletion