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
    # Enroll the student in courses if course_ids are provided
    for course_id in student.course_ids:
        db_course = db.query(Course).filter(Course.id == course_id).first()
        if db_course:
            db_student.courses.append(db_course)
    db.commit()  # Commit changes after enrolling in courses
    db.refresh(db_student)
    return db_student
@router.post("/courses/", response_model=CourseResponse)
def create_course(course: CourseCreate, db: Session = Depends(get_db)):
    db_course = Course(name=course.name, level=course.level, teacher_id=course.teacher_id)  # Updated line
    db.add(db_course)
    db.commit()
    db.refresh(db_course)
    return db_course
@router.post("/teachers/", response_model=TeacherResponse)
def create_teacher(teacher: TeacherCreate, db: Session = Depends(get_db)):
    db_teacher = Teacher(name=teacher.name, email=teacher.email)
    db.add(db_teacher)
    db.commit()
    db.refresh(db_teacher)
    return db_teacher
@router.post("/students/{student_id}/courses/{course_id}/", response_model=StudentResponse)
def enroll_student_in_course(student_id: int, course_id: int, db: Session = Depends(get_db)):
    db_student = db.query(Student).filter(Student.id == student_id).first()
    db_course = db.query(Course).filter(Course.id == course_id).first()
    if db_student and db_course:
        db_student.courses.append(db_course)
        db.commit()
        db.refresh(db_student)
        return db_student
    return {"error": "Student or Course not found"}