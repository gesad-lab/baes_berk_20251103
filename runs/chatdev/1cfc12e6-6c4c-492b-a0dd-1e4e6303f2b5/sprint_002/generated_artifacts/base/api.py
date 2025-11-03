'''
API endpoints for managing students.
'''
from fastapi import HTTPException, Depends
from sqlalchemy.orm import Session
from models import Student
from database import get_db
from typing import List
async def create_student(student_data: dict, db: Session):
    '''
    Create a new student in the database.
    Parameters:
    - student_data: A dictionary containing the student's name.
    - db: The database session.
    Returns:
    - The created Student object.
    '''
    if not student_data.get('name'):
        raise HTTPException(status_code=400, detail="Name is required")
    student = Student(name=student_data['name'])
    db.add(student)
    db.commit()
    db.refresh(student)
    return student
async def get_students(db: Session):
    '''
    Retrieve all students from the database.
    Parameters:
    - db: The database session.
    Returns:
    - A list of Student objects.
    '''
    return db.query(Student).all()