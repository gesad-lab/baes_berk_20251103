'''
Contains the FastAPI routes for the application.
'''
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from models import Student, Course  # Import Course model
from database import get_db
router = APIRouter()
@router.post("/students/", response_model=dict)
def create_student(name: str, email: str, db: Session = Depends(get_db)):
    db_student = Student(name=name, email=email)
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return {"id": db_student.id, "name": db_student.name, "email": db_student.email}
@router.get("/students/", response_model=list)
def get_students(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    students = db.query(Student).offset(skip).limit(limit).all()
    return [{"id": student.id, "name": student.name, "email": student.email} for student in students]
@router.post("/courses/", response_model=dict)
def create_course(name: str, level: str, db: Session = Depends(get_db)):
    db_course = Course(name=name, level=level)
    db.add(db_course)
    db.commit()
    db.refresh(db_course)
    return {"id": db_course.id, "name": db_course.name, "level": db_course.level}
@router.get("/courses/", response_model=list)
def get_courses(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    courses = db.query(Course).offset(skip).limit(limit).all()
    return [{"id": course.id, "name": course.name, "level": course.level} for course in courses]
@router.post("/students/{student_id}/courses/{course_id}")
def enroll_student_in_course(student_id: int, course_id: int, db: Session = Depends(get_db)):
    student = db.query(Student).filter(Student.id == student_id).first()
    course = db.query(Course).filter(Course.id == course_id).first()
    if not student or not course:
        raise HTTPException(status_code=404, detail="Student or Course not found")
    student.courses.append(course)
    db.commit()
    return {"message": "Student enrolled in course successfully."}
@router.get("/students/{student_id}/courses/")
def get_student_courses(student_id: int, db: Session = Depends(get_db)):
    student = db.query(Student).filter(Student.id == student_id).first()
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    return [{"id": course.id, "name": course.name, "level": course.level} for course in student.courses]