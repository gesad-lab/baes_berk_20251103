'''
Main entry point for the application.
'''
# Import necessary modules
from fastapi import FastAPI, Depends
from database import init_db, get_db, migrate_db
from models import Student, Course
from schemas import StudentCreate, StudentResponse, CourseCreate, CourseResponse
from sqlalchemy.orm import Session
app = FastAPI()
@app.on_event("startup")
def startup_event():
    '''
    Initialize the database on startup.
    '''
    init_db()
    migrate_db()  # Ensure migration is called on startup
@app.post("/students/", response_model=StudentResponse)
def create_student(student: StudentCreate, db: Session = Depends(get_db)):
    '''
    Create a new student in the database.
    '''
    db_student = Student(name=student.name, email=student.email)
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return db_student
@app.post("/courses/", response_model=CourseResponse)
def create_course(course: CourseCreate, db: Session = Depends(get_db)):
    '''
    Create a new course in the database.
    '''
    db_course = Course(name=course.name, level=course.level)
    db.add(db_course)
    db.commit()
    db.refresh(db_course)
    return db_course