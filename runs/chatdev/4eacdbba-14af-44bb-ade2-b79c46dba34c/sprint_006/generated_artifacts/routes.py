'''
API routes for the application.
'''
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from models import Student, Course, StudentCourse, Teacher  # Ensure Teacher is imported
from database import get_db
from schemas import StudentCreate, StudentResponse, CourseCreate, CourseResponse, TeacherCreate, TeacherResponse  # Ensure TeacherCreate and TeacherResponse are imported
student_router = APIRouter()
course_router = APIRouter()
teacher_router = APIRouter()  # New router for Teacher
@student_router.post("/students/", response_model=StudentResponse)
def create_student(student: StudentCreate, db: Session = Depends(get_db)):
    db_student = Student(name=student.name, email=student.email)  # Include email
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return db_student
@student_router.get("/students/", response_model=list[StudentResponse])
def get_students(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    students = db.query(Student).offset(skip).limit(limit).all()
    return students
@course_router.post("/courses/", response_model=CourseResponse)
def create_course(course: CourseCreate, db: Session = Depends(get_db)):
    db_course = Course(name=course.name, level=course.level, teacher_id=course.teacher_id)  # Update this line
    db.add(db_course)
    db.commit()
    db.refresh(db_course)
    return db_course
@course_router.get("/courses/", response_model=list[CourseResponse])
def get_courses(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    courses = db.query(Course).offset(skip).limit(limit).all()
    return courses
@student_router.post("/students/{student_id}/courses/{course_id}")
def enroll_student_in_course(student_id: int, course_id: int, db: Session = Depends(get_db)):
    student = db.query(Student).filter(Student.id == student_id).first()
    course = db.query(Course).filter(Course.id == course_id).first()
    if not student or not course:
        raise HTTPException(status_code=404, detail="Student or Course not found")
    # Create an association entry in the StudentCourse table
    student_course = StudentCourse(student_id=student.id, course_id=course.id)
    db.add(student_course)
    db.commit()
    return {"message": "Student enrolled in course"}
@teacher_router.post("/teachers/", response_model=TeacherResponse)  # New endpoint for creating Teacher
def create_teacher(teacher: TeacherCreate, db: Session = Depends(get_db)):
    """
    Create a new Teacher in the database.
    - **teacher**: TeacherCreate model containing name and email.
    - **db**: Database session dependency.
    """
    db_teacher = Teacher(name=teacher.name, email=teacher.email)
    db.add(db_teacher)
    db.commit()
    db.refresh(db_teacher)
    return db_teacher
@teacher_router.get("/teachers/", response_model=list[TeacherResponse])  # New endpoint for getting Teachers
def get_teachers(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    """
    Retrieve a list of Teachers from the database.
    - **skip**: Number of records to skip (for pagination).
    - **limit**: Maximum number of records to return.
    - **db**: Database session dependency.
    """
    teachers = db.query(Teacher).offset(skip).limit(limit).all()
    return teachers