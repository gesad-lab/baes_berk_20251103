'''
API routes for managing students, courses, and teachers.
'''
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from models import Student, Course, Teacher
from schemas import StudentCreate, StudentResponse, CourseCreate, CourseResponse, TeacherCreate, TeacherResponse
from database import get_db
student_router = APIRouter()
course_router = APIRouter()
teacher_router = APIRouter()
@student_router.post("/students/", response_model=StudentResponse)
def create_student(student: StudentCreate, db: Session = Depends(get_db)):
    db_student = Student(name=student.name, email=student.email)  # Include email when creating student
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return db_student
@teacher_router.post("/teachers/", response_model=TeacherResponse)
def create_teacher(teacher: TeacherCreate, db: Session = Depends(get_db)):
    db_teacher = Teacher(name=teacher.name, email=teacher.email)  # Create teacher instance
    db.add(db_teacher)
    db.commit()
    db.refresh(db_teacher)
    return db_teacher
@student_router.get("/students/", response_model=list[StudentResponse])
def get_students(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    students = db.query(Student).offset(skip).limit(limit).all()
    return [
        {
            "id": student.id,
            "name": student.name,
            "email": student.email,
            "courses": [{"id": course.id, "name": course.name, "level": course.level} for course in student.courses]
        }
        for student in students
    ]
@course_router.post("/courses/", response_model=CourseResponse)
def create_course(course: CourseCreate, db: Session = Depends(get_db)):
    db_course = Course(name=course.name, level=course.level, teacher_id=course.teacher_id)  # Associate teacher with course
    db.add(db_course)
    db.commit()
    db.refresh(db_course)
    return db_course
@course_router.get("/courses/", response_model=list[CourseResponse])
def get_courses(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    courses = db.query(Course).offset(skip).limit(limit).all()
    return courses