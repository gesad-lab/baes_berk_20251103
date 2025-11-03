'''
Main entry point for the FastAPI application managing students and courses.
'''
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from models import Student, Course
from schemas import StudentCreate, StudentResponse, CourseCreate, CourseResponse
app = FastAPI()
@app.post("/students/", response_model=StudentResponse)
def create_student(student: StudentCreate, db: Session = Depends(get_db)):
    try:
        db_student = Student(name=student.name, email=student.email)
        db.add(db_student)
        db.commit()
        db.refresh(db_student)
        return db_student
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=400, detail=str(e))
@app.get("/students/", response_model=list[StudentResponse])
def get_students(db: Session = Depends(get_db)):
    try:
        return db.query(Student).all()
    except Exception as e:
        raise HTTPException(status_code=500, detail="Error fetching students")
@app.post("/courses/", response_model=CourseResponse)
def create_course(course: CourseCreate, db: Session = Depends(get_db)):
    db_course = Course(name=course.name, level=course.level)
    db.add(db_course)
    db.commit()
    db.refresh(db_course)
    return db_course
@app.get("/courses/", response_model=list[CourseResponse])
def get_courses(db: Session = Depends(get_db)):
    return db.query(Course).all()
@app.post("/students/{student_id}/courses/{course_id}")
def add_course_to_student(student_id: int, course_id: int, db: Session = Depends(get_db)):
    student = db.query(Student).filter(Student.id == student_id).first()
    course = db.query(Course).filter(Course.id == course_id).first()
    if not student or not course:
        raise HTTPException(status_code=404, detail="Student or Course not found")
    student.courses.append(course)
    db.commit()
    return {"message": "Course added to student successfully"}
@app.get("/students/{student_id}/courses", response_model=list[CourseResponse])
def get_student_courses(student_id: int, db: Session = Depends(get_db)):
    student = db.query(Student).filter(Student.id == student_id).first()
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    return student.courses