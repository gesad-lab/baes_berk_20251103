'''
Main entry point for the FastAPI application.
'''
from fastapi import FastAPI
from models import Base, Student, Course
from database import engine
from schemas import StudentCreate, StudentResponse, CourseCreate, CourseResponse
from sqlalchemy.orm import Session
app = FastAPI()
# Create the database tables
Base.metadata.create_all(bind=engine)
@app.post("/students/", response_model=StudentResponse)
def create_student(student: StudentCreate):
    db: Session = Session(bind=engine)
    db_student = Student(name=student.name, email=student.email)
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return db_student
@app.post("/courses/", response_model=CourseResponse)
def create_course(course: CourseCreate):
    db: Session = Session(bind=engine)
    db_course = Course(name=course.name, level=course.level)
    db.add(db_course)
    db.commit()
    db.refresh(db_course)
    return db_course