'''
Main application entry point for the Student Management system.
'''
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db, create_database
from models import Student, Course, Teacher
from schemas import StudentCreate, StudentResponse, CourseCreate, CourseResponse, TeacherCreate, TeacherResponse
from typing import List
app = FastAPI()
@app.on_event("startup")
def startup_event():
    create_database()
@app.post("/students/", response_model=StudentResponse)
def create_student(student: StudentCreate, course_ids: List[int] = None, db: Session = Depends(get_db)):
    db_student = Student(name=student.name, email=student.email)
    if course_ids:
        db_student.courses = db.query(Course).filter(Course.id.in_(course_ids)).all()
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
@app.post("/teachers/", response_model=TeacherResponse)
def create_teacher(teacher: TeacherCreate, db: Session = Depends(get_db)):
    db_teacher = Teacher(name=teacher.name, email=teacher.email)
    db.add(db_teacher)
    db.commit()
    db.refresh(db_teacher)
    return db_teacher