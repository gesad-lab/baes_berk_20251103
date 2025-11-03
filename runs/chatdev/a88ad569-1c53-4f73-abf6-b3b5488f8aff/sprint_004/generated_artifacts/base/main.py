'''
Main application entry point for the Student Management system.
'''
from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from database import get_db, create_database
from models import Student, Course
from schemas import StudentCreate, StudentResponse, CourseCreate, CourseResponse
app = FastAPI()
@app.on_event("startup")
def startup_event():
    create_database()
    with engine.connect() as connection:
        with open("migration.sql") as f:
            migration_script = f.read()
            connection.execute(migration_script)
@app.post("/students/", response_model=StudentResponse)
def create_student(student: StudentCreate, db: Session = Depends(get_db)):
    db_student = Student(name=student.name, email=student.email)
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return db_student
@app.post("/courses/", response_model=CourseResponse)
def create_course(course: CourseCreate, db: Session = Depends(get_db)):
    db_course = Course(name=course.name, level=course.level)
    db.add(db_course)
    db.commit()
    db.refresh(db_course)
    return db_course