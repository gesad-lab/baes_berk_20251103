'''
Defines the API routes for the Student and Course entities.
'''
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from models import Student, Course
from database import get_db
from schemas import StudentCreate, CourseCreate  # Import the Pydantic models
router = APIRouter()
@router.post("/students/", response_model=StudentCreate)
def create_student(student: StudentCreate, db: Session = Depends(get_db)):
    if not student.name:
        raise HTTPException(status_code=400, detail="Student name is required.")
    if not student.email:
        raise HTTPException(status_code=400, detail="Student email is required.")
    db_student = Student(name=student.name, email=student.email)
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return {"id": db_student.id, "name": db_student.name, "email": db_student.email}
@router.get("/students/", response_model=list)
def get_students(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    students = db.query(Student).offset(skip).limit(limit).all()
    return [{"id": student.id, "name": student.name, "email": student.email} for student in students]
@router.post("/courses/", response_model=CourseCreate)
def create_course(course: CourseCreate, db: Session = Depends(get_db)):
    if not course.name:
        raise HTTPException(status_code=400, detail="Course name is required.")
    if not course.level:
        raise HTTPException(status_code=400, detail="Course level is required.")
    db_course = Course(name=course.name, level=course.level)
    db.add(db_course)
    db.commit()
    db.refresh(db_course)
    return {"id": db_course.id, "name": db_course.name, "level": db_course.level}
@router.get("/courses/", response_model=list)
def get_courses(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    courses = db.query(Course).offset(skip).limit(limit).all()
    return [{"id": course.id, "name": course.name, "level": course.level} for course in courses]