'''
Main entry point for the application.
'''
from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from database import get_db
from models import Student, Course, Teacher
from schemas import StudentCreate, StudentResponse, CourseCreate, CourseResponse, TeacherCreate, TeacherResponse
app = FastAPI()
@app.post("/students/", response_model=StudentResponse)
def create_student(student: StudentCreate, db: Session = Depends(get_db)):
    db_student = Student(name=student.name, email=student.email)
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    # Associate courses
    for course_id in student.course_ids:
        course = db.query(Course).filter(Course.id == course_id).first()
        if course:
            db_student.courses.append(course)
    db.commit()
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