'''
Defines the API routes for student operations.
'''
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import SessionLocal
from models import Student, Course
from schemas import StudentCreate, StudentResponse
router = APIRouter()
# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
@router.post("/students", response_model=StudentResponse)
def create_student(student: StudentCreate, db: Session = Depends(get_db)):
    db_student = Student(name=student.name, email=student.email)  # Include email when creating student
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    # Add courses to the student
    for course_name in student.courses:
        course = db.query(Course).filter(Course.name == course_name).first()
        if course:
            db_student.courses.append(course)
    db.commit()
    return db_student