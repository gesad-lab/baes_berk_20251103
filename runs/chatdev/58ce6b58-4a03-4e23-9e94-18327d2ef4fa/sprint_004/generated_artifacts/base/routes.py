'''
Defines the API routes for the application.
'''
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from models import Student as StudentModel, Course as CourseModel
from database import get_db
from pydantic import BaseModel, EmailStr
# Pydantic model for request validation
class Student(BaseModel):
    name: str
    email: EmailStr
class Course(BaseModel):
    name: str
    level: str
router = APIRouter()
@router.post("/students/", response_model=dict)
def create_student(student: Student, db: Session = Depends(get_db)):
    '''
    Creates a new student with the given name and email.
    '''
    new_student = StudentModel(name=student.name, email=student.email)
    db.add(new_student)
    db.commit()
    db.refresh(new_student)
    return {"id": new_student.id, "name": new_student.name, "email": new_student.email}
@router.get("/students/", response_model=list)
def get_students(db: Session = Depends(get_db)):
    '''
    Retrieves all students.
    '''
    return db.query(StudentModel).all()
@router.post("/courses/", response_model=dict)
def create_course(course: Course, db: Session = Depends(get_db)):
    '''
    Creates a new course with the given name and level.
    '''
    new_course = CourseModel(name=course.name, level=course.level)
    db.add(new_course)
    db.commit()
    db.refresh(new_course)
    return {"id": new_course.id, "name": new_course.name, "level": new_course.level}
@router.get("/courses/", response_model=list)
def get_courses(db: Session = Depends(get_db)):
    '''
    Retrieves all courses.
    '''
    return db.query(CourseModel).all()