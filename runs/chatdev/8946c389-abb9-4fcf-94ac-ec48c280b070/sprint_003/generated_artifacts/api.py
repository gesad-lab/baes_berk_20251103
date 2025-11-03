'''
Defines the API endpoints for the Student and Course entities.
'''
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from models import Student, Course
from database import get_db
from schemas import StudentCreate, StudentResponse, CourseCreate, CourseResponse
router = APIRouter()
@router.post("/students/", response_model=StudentResponse)
def create_student(student: StudentCreate, db: Session = Depends(get_db)):
    '''
    Creates a new student with the given name and email.
    '''
    db_student = Student(name=student.name, email=student.email)  # Include email
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return {"id": db_student.id, "name": db_student.name, "email": db_student.email}  # Return email
@router.get("/students/", response_model=list[StudentResponse])
def get_students(db: Session = Depends(get_db)):
    '''
    Retrieves all students from the database.
    '''
    return db.query(Student).all()
@router.post("/courses/", response_model=CourseResponse)
def create_course(course: CourseCreate, db: Session = Depends(get_db)):
    '''
    Creates a new course with the given name and level.
    '''
    db_course = Course(name=course.name, level=course.level)
    db.add(db_course)
    db.commit()
    db.refresh(db_course)
    return {"id": db_course.id, "name": db_course.name, "level": db_course.level}
@router.get("/courses/", response_model=list[CourseResponse])
def get_courses(db: Session = Depends(get_db)):
    '''
    Retrieves all courses from the database.
    '''
    return db.query(Course).all()