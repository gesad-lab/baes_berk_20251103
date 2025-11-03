'''
Defines the API routes for the Student and Course entities.
'''
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from models import Student as StudentModel, Course as CourseModel  # Import Course model
from database import get_db
from pydantic import BaseModel
from typing import List
# Pydantic model for request validation
class Student(BaseModel):
    name: str
    email: str  # Added email field
    course_ids: List[int] = []  # List of course IDs associated with the student
class StudentResponse(BaseModel):
    id: int
    name: str
    email: str  # Added email field
    course_ids: List[int]  # List of course IDs associated with the student
class Course(BaseModel):  # Pydantic model for Course
    name: str
    level: str
class CourseResponse(BaseModel):  # Pydantic model for Course response
    id: int
    name: str
    level: str
student_router = APIRouter()
@student_router.post("/students/", response_model=StudentResponse)
def create_student(student: Student, db: Session = Depends(get_db)):
    db_student = StudentModel(name=student.name, email=student.email)  # Updated to include email
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    # Associate courses with the student
    for course_id in student.course_ids:
        course = db.query(CourseModel).filter(CourseModel.id == course_id).first()
        if course:
            db_student.courses.append(course)  # Add course to student's courses
    db.commit()  # Commit changes
    return {"id": db_student.id, "name": db_student.name, "email": db_student.email, "course_ids": student.course_ids}
@student_router.get("/students/", response_model=list[StudentResponse])
def get_students(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    students = db.query(StudentModel).offset(skip).limit(limit).all()
    return [{"id": student.id, "name": student.name, "email": student.email, "course_ids": [course.id for course in student.courses]} for student in students]  # Updated to include course_ids
@student_router.post("/courses/", response_model=CourseResponse)  # Route to create a course
def create_course(course: Course, db: Session = Depends(get_db)):
    db_course = CourseModel(name=course.name, level=course.level)
    db.add(db_course)
    db.commit()
    db.refresh(db_course)
    return {"id": db_course.id, "name": db_course.name, "level": db_course.level}
@student_router.get("/courses/", response_model=list[CourseResponse])  # Route to get courses
def get_courses(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    courses = db.query(CourseModel).offset(skip).limit(limit).all()
    return [{"id": course.id, "name": course.name, "level": course.level} for course in courses]