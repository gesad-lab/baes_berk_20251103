'''
Defines the API endpoints for CRUD operations on the Student, Course, and Teacher entities.
'''
from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from models import Student, Course, Teacher
from database import SessionLocal
student_router = APIRouter()
course_router = APIRouter()
teacher_router = APIRouter()
# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
@student_router.post("/students/", response_model=dict)
async def create_student(name: str, email: str, db: Session = Depends(get_db)):
    '''
    Creates a new student with the provided name and email.
    '''
    student = Student(name=name, email=email)
    db.add(student)
    db.commit()
    db.refresh(student)
    return {"id": student.id, "name": student.name, "email": student.email}
@course_router.post("/courses/", response_model=dict)
async def create_course(name: str, level: str, db: Session = Depends(get_db)):
    '''
    Creates a new course with the provided name and level.
    '''
    course = Course(name=name, level=level)
    db.add(course)
    db.commit()
    db.refresh(course)
    return {"id": course.id, "name": course.name, "level": course.level}
@teacher_router.post("/teachers/", response_model=dict)
async def create_teacher(name: str, email: str, db: Session = Depends(get_db)):
    '''
    Creates a new teacher with the provided name and email.
    '''
    teacher = Teacher(name=name, email=email)
    db.add(teacher)
    db.commit()
    db.refresh(teacher)
    return {"id": teacher.id, "name": teacher.name, "email": teacher.email}
# Include the teacher router in the main application