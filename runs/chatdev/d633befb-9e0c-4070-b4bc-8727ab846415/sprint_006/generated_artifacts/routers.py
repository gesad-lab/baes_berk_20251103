'''
Defines the API routes for the Student, Course, and Teacher entities.
'''
from fastapi import APIRouter, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal
from models import Student, Course, Teacher
from schemas import StudentCreate, StudentResponse, CourseCreate, CourseResponse, TeacherCreate, TeacherResponse
student_router = APIRouter()
course_router = APIRouter()
teacher_router = APIRouter()
@student_router.post("/students", response_model=StudentResponse)
def create_student(student: StudentCreate):
    db: Session = SessionLocal()
    db_student = Student(name=student.name, email=student.email)
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    db.close()
    return db_student
@course_router.post("/courses", response_model=CourseResponse)
def create_course(course: CourseCreate):
    db: Session = SessionLocal()
    # Check if the teacher exists
    teacher = db.query(Teacher).filter(Teacher.id == course.teacher_id).first()
    if not teacher:
        db.close()
        raise HTTPException(status_code=404, detail="Teacher not found")
    db_course = Course(name=course.name, level=course.level, teacher_id=course.teacher_id)
    db.add(db_course)
    db.commit()
    db.refresh(db_course)
    db.close()
    return db_course
@teacher_router.post("/teachers", response_model=TeacherResponse)
def create_teacher(teacher: TeacherCreate):
    db: Session = SessionLocal()
    db_teacher = Teacher(name=teacher.name, email=teacher.email)
    db.add(db_teacher)
    db.commit()
    db.refresh(db_teacher)
    db.close()
    return db_teacher