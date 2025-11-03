'''
Contains the API endpoints for creating and retrieving Student and Course entities.
'''
from fastapi import APIRouter, HTTPException
from sqlalchemy.orm import Session
from models import Student, Course
from database import SessionLocal
from schemas import StudentCreate, CourseCreate
router = APIRouter()
@router.post("/students/", response_model=dict)
async def create_student(student: StudentCreate):
    db: Session = SessionLocal()
    try:
        new_student = Student(name=student.name, email=student.email)
        db.add(new_student)
        db.commit()
        db.refresh(new_student)
        return {"id": new_student.id, "name": new_student.name, "email": new_student.email}
    finally:
        db.close()
@router.get("/students/", response_model=list)
async def read_students():
    db: Session = SessionLocal()
    try:
        students = db.query(Student).all()
        return [{"id": student.id, "name": student.name, "email": student.email} for student in students]
    finally:
        db.close()
@router.post("/courses/", response_model=dict)
async def create_course(course: CourseCreate):
    db: Session = SessionLocal()
    try:
        new_course = Course(name=course.name, level=course.level)
        db.add(new_course)
        db.commit()
        db.refresh(new_course)
        return {"id": new_course.id, "name": new_course.name, "level": new_course.level}
    finally:
        db.close()
@router.get("/courses/", response_model=list)
async def read_courses():
    db: Session = SessionLocal()
    try:
        courses = db.query(Course).all()
        return [{"id": course.id, "name": course.name, "level": course.level} for course in courses]
    finally:
        db.close()