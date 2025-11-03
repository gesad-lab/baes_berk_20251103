'''
Defines the API routes for the application.
'''
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from models import Student, Course
from database import get_db
from schemas import StudentCreate, CourseCreate
router = APIRouter()
@router.post("/students/", response_model=dict)
def create_student(student: StudentCreate, db: Session = Depends(get_db)):
    '''
    Create a new student in the database.
    Parameters:
    - student: StudentCreate - The student data to be created.
    - db: Session - The database session.
    Returns:
    - dict: The created student's id, name, and email.
    '''
    db_student = Student(name=student.name, email=student.email)
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return {"id": db_student.id, "name": db_student.name, "email": db_student.email}
@router.get("/students/", response_model=list)
def get_students(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    '''
    Retrieve a list of students from the database.
    Parameters:
    - skip: int - Number of records to skip.
    - limit: int - Maximum number of records to return.
    - db: Session - The database session.
    Returns:
    - list: A list of students with their id and name.
    '''
    students = db.query(Student).offset(skip).limit(limit).all()
    return [{"id": student.id, "name": student.name, "email": student.email} for student in students]
@router.post("/courses/", response_model=dict)
def create_course(course: CourseCreate, db: Session = Depends(get_db)):
    '''
    Create a new course in the database.
    Parameters:
    - course: CourseCreate - The course data to be created.
    - db: Session - The database session.
    Returns:
    - dict: The created course's id, name, and level.
    '''
    db_course = Course(name=course.name, level=course.level)
    db.add(db_course)
    db.commit()
    db.refresh(db_course)
    return {"id": db_course.id, "name": db_course.name, "level": db_course.level}