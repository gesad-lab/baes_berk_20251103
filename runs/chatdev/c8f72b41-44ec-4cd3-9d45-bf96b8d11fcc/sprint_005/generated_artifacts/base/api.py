'''
Contains the API endpoints for managing Student and Course entities.
'''
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from models import Student, Course
from database import get_db
from pydantic import BaseModel, EmailStr  # Import EmailStr for email validation
class StudentCreate(BaseModel):
    name: str
    email: EmailStr  # Added email field with validation
class CourseCreate(BaseModel):
    name: str
    level: str
class StudentCoursesUpdate(BaseModel):
    course_ids: list[int]  # List of course IDs to associate with the student
router = APIRouter()
@router.post("/students/", response_model=StudentCreate)
def create_student(student: StudentCreate, db: Session = Depends(get_db)):
    db_student = Student(name=student.name, email=student.email)  # Include email in creation
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return StudentCreate(name=db_student.name, email=db_student.email)  # Return email
@router.get("/students/", response_model=list[StudentCreate])
def get_students(db: Session = Depends(get_db)):
    students = db.query(Student).all()
    return [StudentCreate(name=student.name, email=student.email) for student in students]  # Return email
@router.post("/courses/", response_model=CourseCreate)
def create_course(course: CourseCreate, db: Session = Depends(get_db)):
    db_course = Course(name=course.name, level=course.level)
    db.add(db_course)
    db.commit()
    db.refresh(db_course)
    return CourseCreate(name=db_course.name, level=db_course.level)
@router.get("/courses/", response_model=list[CourseCreate])
def get_courses(db: Session = Depends(get_db)):
    courses = db.query(Course).all()
    return [CourseCreate(name=course.name, level=course.level) for course in courses]
@router.put("/students/{student_id}/courses/", response_model=StudentCreate)
def add_courses_to_student(student_id: int, course_ids: StudentCoursesUpdate, db: Session = Depends(get_db)):
    db_student = db.query(Student).filter(Student.id == student_id).first()
    if not db_student:
        raise HTTPException(status_code=404, detail="Student not found")
    courses = db.query(Course).filter(Course.id.in_(course_ids.course_ids)).all()
    # Check for duplicates and add only if not already associated
    for course in courses:
        if course not in db_student.courses:
            db_student.courses.append(course)  # Add course to the student if not already present
    db.commit()
    db.refresh(db_student)
    return StudentCreate(name=db_student.name, email=db_student.email)