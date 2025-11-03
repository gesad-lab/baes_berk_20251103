'''
Defines the API routes for the Student, Course, and Teacher entities.
'''
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import SessionLocal
from models import Student, Course, Teacher
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
def create_student(student: StudentCreate, db: Session = Depends(get_db)):
    db_student = Student(name=student.name, email=student.email)
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    # Assign courses to the student with validation
    for course_id in student.course_ids:
        db_course = db.query(Course).filter(Course.id == course_id).first()
        if db_course:
            db_student.courses.append(db_course)
        else:
            print(f"Course ID {course_id} does not exist. Skipping.")
    db.commit()
    db.refresh(db_student)
    return db_student
# Course routes
@router.post("/courses/", response_model=CourseResponse)
def create_course(course: CourseCreate, db: Session = Depends(get_db)):
    # Create a new course with an optional teacher assignment
    db_course = Course(name=course.name, level=course.level, teacher_id=course.teacher_id)  # Updated to include teacher_id
    db.add(db_course)
    db.commit()
    db.refresh(db_course)
    return db_course
# Teacher routes
@router.post("/teachers/", response_model=TeacherResponse)
def create_teacher(teacher: TeacherCreate, db: Session = Depends(get_db)):
    db_teacher = Teacher(name=teacher.name, email=teacher.email)
    db.add(db_teacher)
    db.commit()
    db.refresh(db_teacher)
    return db_teacher