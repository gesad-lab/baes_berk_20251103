'''
Defines the API routes for the Student and Course entities.
'''
from fastapi import APIRouter, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal
from models import Student, Course
from schemas import StudentCreate, StudentResponse, CourseCreate, CourseResponse
student_router = APIRouter()
course_router = APIRouter()
@student_router.post("/students", response_model=StudentResponse)
def create_student(student: StudentCreate):
    db: Session = SessionLocal()
    db_student = Student(name=student.name, email=student.email)
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    db.close()
    return db_student
@student_router.get("/students/{student_id}", response_model=StudentResponse)
def read_student(student_id: int):
    db: Session = SessionLocal()
    db_student = db.query(Student).filter(Student.id == student_id).first()
    db.close()
    if db_student is None:
        raise HTTPException(status_code=404, detail="Student not found")
    return db_student
@course_router.post("/courses", response_model=CourseResponse)
def create_course(course: CourseCreate):
    db: Session = SessionLocal()
    db_course = Course(name=course.name, level=course.level)
    db.add(db_course)
    db.commit()
    db.refresh(db_course)
    db.close()
    return db_course
@course_router.get("/courses/{course_id}", response_model=CourseResponse)
def read_course(course_id: int):
    db: Session = SessionLocal()
    db_course = db.query(Course).filter(Course.id == course_id).first()
    db.close()
    if db_course is None:
        raise HTTPException(status_code=404, detail="Course not found")
    return db_course