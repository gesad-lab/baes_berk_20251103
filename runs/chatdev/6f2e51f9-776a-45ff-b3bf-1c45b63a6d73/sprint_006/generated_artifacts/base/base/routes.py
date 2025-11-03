'''
API routes for the Student and Course entities.
'''
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from models import Student, Course
from database import get_db
from schemas import StudentCreate, CourseCreate  # Import the Pydantic models
student_router = APIRouter()
@student_router.post("/students/", response_model=dict)
def create_student(student: StudentCreate, db: Session = Depends(get_db)):
    db_student = Student(name=student.name, email=student.email)  # Added email to Student creation
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return {"id": db_student.id, "name": db_student.name, "email": db_student.email}  # Return email
@student_router.get("/students/", response_model=list)
def get_students(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    students = db.query(Student).offset(skip).limit(limit).all()
    return [{"id": student.id, "name": student.name, "email": student.email} for student in students]  # Return email
@student_router.post("/courses/", response_model=dict)
def create_course(course: CourseCreate, db: Session = Depends(get_db)):
    db_course = Course(name=course.name, level=course.level)
    db.add(db_course)
    db.commit()
    db.refresh(db_course)
    return {"id": db_course.id, "name": db_course.name, "level": db_course.level}
@student_router.get("/courses/", response_model=list)
def get_courses(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    courses = db.query(Course).offset(skip).limit(limit).all()
    return [{"id": course.id, "name": course.name, "level": course.level} for course in courses]
@student_router.post("/students/{student_id}/courses/{course_id}", response_model=dict)
def enroll_student_in_course(student_id: int, course_id: int, db: Session = Depends(get_db)):
    db_student = db.query(Student).filter(Student.id == student_id).first()
    db_course = db.query(Course).filter(Course.id == course_id).first()
    if not db_student or not db_course:
        raise HTTPException(status_code=404, detail="Student or Course not found")
    db_student.courses.append(db_course)
    db.commit()
    return {"student_id": db_student.id, "course_id": db_course.id}