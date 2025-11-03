'''
Contains the API routes for the Student, Course, and Teacher entities.
'''
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from models import Student as StudentModel, Course as CourseModel, Teacher as TeacherModel  # Import Teacher model
from database import get_db
from pydantic import BaseModel, EmailStr
# Pydantic model for Student request validation
class Student(BaseModel):
    name: str
    email: EmailStr  # New email field added with validation
    course_ids: list[int] = []  # List of course IDs for enrollment
# Pydantic model for Course request validation
class Course(BaseModel):
    name: str
    level: str
# Pydantic model for Teacher request validation
class Teacher(BaseModel):
    name: str
    email: EmailStr  # New email field added with validation
router = APIRouter()
@router.post("/students/", response_model=dict)
def create_student(student: Student, db: Session = Depends(get_db)):
    '''
    Endpoint to create a new student.
    '''
    db_student = StudentModel(name=student.name, email=student.email)  # Include email in creation
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    # Initialize courses relationship to an empty list if no course_ids are provided
    if student.course_ids:
        courses = db.query(CourseModel).filter(CourseModel.id.in_(student.course_ids)).all()
        db_student.courses.extend(courses)
        db.commit()
    return {"id": db_student.id, "name": db_student.name, "email": db_student.email}
@router.get("/students/", response_model=list)
def get_students(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    '''
    Endpoint to retrieve all students.
    '''
    students = db.query(StudentModel).offset(skip).limit(limit).all()
    return [{"id": student.id, "name": student.name, "email": student.email} for student in students]
@router.post("/courses/", response_model=dict)
def create_course(course: Course, db: Session = Depends(get_db)):
    '''
    Endpoint to create a new course.
    '''
    db_course = CourseModel(name=course.name, level=course.level)
    db.add(db_course)
    db.commit()
    db.refresh(db_course)
    return {"id": db_course.id, "name": db_course.name, "level": db_course.level}
@router.get("/courses/", response_model=list)
def get_courses(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    '''
    Endpoint to retrieve all courses.
    '''
    courses = db.query(CourseModel).offset(skip).limit(limit).all()
    return [{"id": course.id, "name": course.name, "level": course.level} for course in courses]
@router.post("/teachers/", response_model=dict)
def create_teacher(teacher: Teacher, db: Session = Depends(get_db)):
    '''
    Endpoint to create a new teacher.
    '''
    db_teacher = TeacherModel(name=teacher.name, email=teacher.email)
    db.add(db_teacher)
    db.commit()
    db.refresh(db_teacher)
    return {"id": db_teacher.id, "name": db_teacher.name, "email": db_teacher.email}
@router.get("/teachers/", response_model=list)
def get_teachers(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    '''
    Endpoint to retrieve all teachers.
    '''
    teachers = db.query(TeacherModel).offset(skip).limit(limit).all()
    return [{"id": teacher.id, "name": teacher.name, "email": teacher.email} for teacher in teachers]