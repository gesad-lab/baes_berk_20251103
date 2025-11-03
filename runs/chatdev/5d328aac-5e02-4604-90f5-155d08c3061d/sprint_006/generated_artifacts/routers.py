'''
Defines the API routes for the Student, Course, and Teacher entities.
'''
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal
from crud import create_student, get_students, create_course, get_courses, create_teacher, get_teachers
from schemas import StudentCreate, StudentResponse, CourseCreate, CourseResponse, TeacherCreate, TeacherResponse
router = APIRouter()
# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
@router.post("/students/", response_model=StudentResponse)
def add_student(student: StudentCreate, course_ids: list[int] = None, db: Session = Depends(get_db)):
    db_student = create_student(db=db, student=student, course_ids=course_ids)
    return db_student
@router.get("/students/", response_model=list[StudentResponse])
def read_students(db: Session = Depends(get_db)):
    return get_students(db=db)
@router.post("/courses/", response_model=CourseResponse)
def add_course(course: CourseCreate, teacher_id: int, db: Session = Depends(get_db)):
    return create_course(db=db, course=course, teacher_id=teacher_id)
@router.get("/courses/", response_model=list[CourseResponse])
def read_courses(db: Session = Depends(get_db)):
    return get_courses(db=db)
@router.post("/teachers/", response_model=TeacherResponse)
def add_teacher(teacher: TeacherCreate, db: Session = Depends(get_db)):
    return create_teacher(db=db, teacher=teacher)
@router.get("/teachers/", response_model=list[TeacherResponse])
def read_teachers(db: Session = Depends(get_db)):
    return get_teachers(db=db)