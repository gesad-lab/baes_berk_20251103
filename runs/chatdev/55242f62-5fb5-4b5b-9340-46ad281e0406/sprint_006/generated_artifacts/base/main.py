'''
Main entry point for the FastAPI application.
'''
from fastapi import FastAPI, HTTPException
from models import Base, Student, Course, Teacher
from database import engine
from schemas import StudentCreate, StudentResponse, CourseCreate, CourseResponse, TeacherCreate, TeacherResponse
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
@app.post("/teachers/", response_model=TeacherResponse)
def create_teacher(teacher: TeacherCreate):
    db: Session = Session(bind=engine)
    db_teacher = Teacher(name=teacher.name, email=teacher.email)
    db.add(db_teacher)
    db.commit()
    db.refresh(db_teacher)
    return db_teacher
@app.post("/students/{student_id}/enroll/")
def enroll_student_in_course(student_id: int, course_id: int):  # Add course_id parameter
    db: Session = Session(bind=engine)
    student = db.query(Student).filter(Student.id == student_id).first()
    course = db.query(Course).filter(Course.id == course_id).first()
    if not student or not course:
        raise HTTPException(status_code=404, detail="Student or Course not found")
    student.courses.append(course)
    db.commit()
    return {"message": "Student enrolled in course successfully"}