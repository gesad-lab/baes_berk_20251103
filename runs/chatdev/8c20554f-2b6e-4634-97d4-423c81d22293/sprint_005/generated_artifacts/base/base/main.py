'''
Main application file for the FastAPI backend.
'''
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import engine, get_db
from models import Student, Course
from schemas import StudentCreate, StudentResponse, CourseCreate, CourseResponse
from sqlalchemy import inspect
app = FastAPI()
# Create the database tables only if they do not exist
if not inspect(engine).has_table("students"):
    from database import Base
    Base.metadata.create_all(bind=engine)
if not inspect(engine).has_table("courses"):
    Base.metadata.create_all(bind=engine)
@app.post("/students/", response_model=StudentResponse)
def create_student(student: StudentCreate, db: Session = Depends(get_db)):
    '''
    Create a new student in the database.
    '''
    existing_student = db.query(Student).filter(Student.name == student.name).first()
    if existing_student:
        raise HTTPException(status_code=400, detail="Student with this name already exists.")
    db_student = Student(name=student.name, email=student.email)  # Updated to include email
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return StudentResponse(id=db_student.id, name=db_student.name, email=db_student.email)  # Updated return statement
@app.get("/students/", response_model=list[StudentResponse])
def read_students(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    '''
    Retrieve a list of students from the database.
    '''
    students = db.query(Student).offset(skip).limit(limit).all()
    return students
@app.post("/courses/", response_model=CourseResponse)
def create_course(course: CourseCreate, db: Session = Depends(get_db)):
    '''
    Create a new course in the database.
    '''
    db_course = Course(name=course.name, level=course.level)
    db.add(db_course)
    db.commit()
    db.refresh(db_course)
    return CourseResponse(id=db_course.id, name=db_course.name, level=db_course.level)
@app.get("/courses/", response_model=list[CourseResponse])
def read_courses(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    '''
    Retrieve a list of courses from the database.
    '''
    courses = db.query(Course).offset(skip).limit(limit).all()
    return courses