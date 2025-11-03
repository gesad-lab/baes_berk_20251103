'''
Defines the API routes for the Student, Course, and Teacher entities.
'''
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from models import Student as StudentModel, Course as CourseModel, Teacher as TeacherModel  # Import Teacher model
from database import get_db
from pydantic import BaseModel
from typing import List, Optional
# Pydantic model for request validation
class Student(BaseModel):
    name: str
    email: str
    course_ids: List[int] = []
class StudentResponse(BaseModel):
    id: int
    name: str
    email: str
    course_ids: List[int]
class Course(BaseModel):
    name: str
    level: str
    teacher_id: Optional[int] = None  # Add teacher_id to the Course model
class CourseResponse(BaseModel):
    id: int
    name: str
    level: str
    teacher_id: Optional[int] = None  # Add teacher_id to the Course response model
class Teacher(BaseModel):  # Pydantic model for Teacher
    name: str
    email: str
class TeacherResponse(BaseModel):  # Pydantic model for Teacher response
    id: int
    name: str
    email: str
student_router = APIRouter()
@student_router.post("/students/", response_model=StudentResponse)
def create_student(student: Student, db: Session = Depends(get_db)):
    db_student = StudentModel(name=student.name, email=student.email)
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    for course_id in student.course_ids:
        course = db.query(CourseModel).filter(CourseModel.id == course_id).first()
        if course:
            db_student.courses.append(course)
    db.commit()
    return {"id": db_student.id, "name": db_student.name, "email": db_student.email, "course_ids": student.course_ids}
@student_router.get("/students/", response_model=list[StudentResponse])
def get_students(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    students = db.query(StudentModel).offset(skip).limit(limit).all()
    return [{"id": student.id, "name": student.name, "email": student.email, "course_ids": [course.id for course in student.courses]} for student in students]
@student_router.post("/courses/", response_model=CourseResponse)
def create_course(course: Course, db: Session = Depends(get_db)):
    db_course = CourseModel(name=course.name, level=course.level, teacher_id=course.teacher_id)  # Include teacher_id
    db.add(db_course)
    db.commit()
    db.refresh(db_course)
    return {"id": db_course.id, "name": db_course.name, "level": db_course.level, "teacher_id": db_course.teacher_id}
@student_router.get("/courses/", response_model=list[CourseResponse])
def get_courses(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    courses = db.query(CourseModel).offset(skip).limit(limit).all()
    return [{"id": course.id, "name": course.name, "level": course.level, "teacher_id": course.teacher_id} for course in courses]
@student_router.post("/teachers/", response_model=TeacherResponse)  # Route to create a teacher
def create_teacher(teacher: Teacher, db: Session = Depends(get_db)):
    db_teacher = TeacherModel(name=teacher.name, email=teacher.email)
    db.add(db_teacher)
    db.commit()
    db.refresh(db_teacher)
    return {"id": db_teacher.id, "name": db_teacher.name, "email": db_teacher.email}
@student_router.get("/teachers/", response_model=list[TeacherResponse])  # Route to get teachers
def get_teachers(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    teachers = db.query(TeacherModel).offset(skip).limit(limit).all()
    return [{"id": teacher.id, "name": teacher.name, "email": teacher.email} for teacher in teachers]