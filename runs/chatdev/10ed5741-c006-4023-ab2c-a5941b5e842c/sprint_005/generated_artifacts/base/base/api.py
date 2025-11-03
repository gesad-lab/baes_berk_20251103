'''
Contains the API endpoints for the Student and Course entities.
'''
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from models import Student, Course
from database import get_db
from pydantic import BaseModel
router = APIRouter()
class StudentCreate(BaseModel):
    name: str
    email: str  # Added email field
class StudentResponse(BaseModel):
    id: int
    name: str
    email: str  # Added email field
@router.post("/students/", response_model=StudentResponse)
def create_student(student: StudentCreate, db: Session = Depends(get_db)):
    '''
    Endpoint to create a new student.
    '''
    new_student = Student(name=student.name, email=student.email)  # Updated to include email
    db.add(new_student)
    db.commit()
    db.refresh(new_student)
    return {"id": new_student.id, "name": new_student.name, "email": new_student.email}  # Updated to include email
@router.get("/students/", response_model=list[StudentResponse])
def get_students(db: Session = Depends(get_db)):
    '''
    Endpoint to retrieve all students.
    '''
    return [{"id": student.id, "name": student.name, "email": student.email} for student in db.query(Student).all()]  # Updated to include email
class CourseCreate(BaseModel):
    name: str
    level: str
class CourseResponse(BaseModel):
    id: int
    name: str
    level: str
@router.post("/courses/", response_model=CourseResponse)
def create_course(course: CourseCreate, db: Session = Depends(get_db)):
    '''
    Endpoint to create a new course.
    '''
    new_course = Course(name=course.name, level=course.level)
    db.add(new_course)
    db.commit()
    db.refresh(new_course)
    return {"id": new_course.id, "name": new_course.name, "level": new_course.level}
@router.get("/courses/", response_model=list[CourseResponse])
def get_courses(db: Session = Depends(get_db)):
    '''
    Endpoint to retrieve all courses.
    '''
    return [{"id": course.id, "name": course.name, "level": course.level} for course in db.query(Course).all()]