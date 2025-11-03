'''
API endpoints for managing students and courses.
'''
from fastapi import HTTPException, Depends
from sqlalchemy.orm import Session
from models import Student, Course
from database import get_db
from typing import List
async def create_student(student_data: dict, db: Session):
    '''
    Create a new student in the database.
    Parameters:
    - student_data: A dictionary containing the student's name and email.
    - db: The database session.
    Returns:
    - The created Student object.
    '''
    if not student_data.get('name'):
        raise HTTPException(status_code=400, detail="Name is required")
    if not student_data.get('email'):
        raise HTTPException(status_code=400, detail="Email is required")  # Check for email
    student = Student(name=student_data['name'], email=student_data['email'])  # Include email
    db.add(student)
    db.commit()
    db.refresh(student)
    return student
async def create_course(course_data: dict, db: Session):
    '''
    Create a new course in the database.
    Parameters:
    - course_data: A dictionary containing the course's name and level.
    - db: The database session.
    Returns:
    - The created Course object.
    '''
    if not course_data.get('name'):
        raise HTTPException(status_code=400, detail="Course name is required")
    if not course_data.get('level'):
        raise HTTPException(status_code=400, detail="Course level is required")
    course = Course(name=course_data['name'], level=course_data['level'])
    db.add(course)
    db.commit()
    db.refresh(course)
    return course
async def get_students(db: Session):
    '''
    Retrieve all students from the database.
    Parameters:
    - db: The database session.
    Returns:
    - A list of Student objects.
    '''
    return db.query(Student).all()
async def get_courses(db: Session):
    '''
    Retrieve all courses from the database.
    Parameters:
    - db: The database session.
    Returns:
    - A list of Course objects.
    '''
    return db.query(Course).all()