'''
Defines the API endpoints for the Student and Course entities.
'''
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from models import Student as StudentModel, Course as CourseModel
from database import get_db
from pydantic import BaseModel
# Pydantic models for request validation
class Student(BaseModel):
    name: str
    email: str  # Added email field
    course_ids: list[int] = []  # List of course IDs
class Course(BaseModel):
    name: str
    level: str
class StudentResponse(BaseModel):
    id: int
    name: str
    email: str  # Added email field
    courses: list[Course] = []  # List of courses
class CourseResponse(BaseModel):
    id: int
    name: str
    level: str
router = APIRouter()
@router.post("/students/", response_model=StudentResponse)
def create_student(student: Student, db: Session = Depends(get_db)):
    db_student = StudentModel(name=student.name, email=student.email)
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    # Add courses to the student
    for course_id in student.course_ids:
        course = db.query(CourseModel).filter(CourseModel.id == course_id).first()
        if course:
            db_student.courses.append(course)
        else:
            raise HTTPException(status_code=400, detail=f"Course with ID {course_id} does not exist.")
    db.commit()
    return {"id": db_student.id, "name": db_student.name, "email": db_student.email, "courses": db_student.courses}
@router.get("/students/", response_model=list[StudentResponse])
def get_students(db: Session = Depends(get_db)):
    students = db.query(StudentModel).all()
    return [{"id": student.id, "name": student.name, "email": student.email, "courses": student.courses} for student in students]
@router.post("/courses/", response_model=CourseResponse)
def create_course(course: Course, db: Session = Depends(get_db)):
    db_course = CourseModel(name=course.name, level=course.level)
    db.add(db_course)
    db.commit()
    db.refresh(db_course)
    return {"id": db_course.id, "name": db_course.name, "level": db_course.level}
@router.get("/courses/", response_model=list[CourseResponse])
def get_courses(db: Session = Depends(get_db)):
    return db.query(CourseModel).all()