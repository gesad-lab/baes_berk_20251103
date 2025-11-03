'''
Defines the API routes for the application.
'''
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from models import Student as StudentModel, Course as CourseModel, Teacher as TeacherModel
from database import get_db
from pydantic import BaseModel, EmailStr
from typing import List
# Pydantic model for request validation
class Student(BaseModel):
    name: str
    email: EmailStr
    course_ids: List[int] = []  # New field for course IDs
class Course(BaseModel):
    name: str
    level: str
class Teacher(BaseModel):
    name: str
    email: EmailStr
router = APIRouter()
@router.post("/students/", response_model=dict)
def create_student(student: Student, db: Session = Depends(get_db)):
    '''
    Creates a new student with the given name, email, and associated courses.
    '''
    new_student = StudentModel(name=student.name, email=student.email)
    db.add(new_student)
    db.commit()
    db.refresh(new_student)
    # Add courses to the student
    if student.course_ids:
        courses = db.query(CourseModel).filter(CourseModel.id.in_(student.course_ids)).all()
        new_student.courses.extend(courses)
    db.commit()  # Commit the changes after adding courses
    return {"id": new_student.id, "name": new_student.name, "email": new_student.email}
@router.get("/students/", response_model=list)
def get_students(db: Session = Depends(get_db)):
    '''
    Retrieves all students.
    '''
    return db.query(StudentModel).all()
@router.post("/courses/", response_model=dict)
def create_course(course: Course, db: Session = Depends(get_db)):
    '''
    Creates a new course with the given name and level.
    '''
    new_course = CourseModel(name=course.name, level=course.level)
    db.add(new_course)
    db.commit()
    db.refresh(new_course)
    return {"id": new_course.id, "name": new_course.name, "level": new_course.level}
@router.get("/courses/", response_model=list)
def get_courses(db: Session = Depends(get_db)):
    '''
    Retrieves all courses.
    '''
    return db.query(CourseModel).all()
@router.post("/teachers/", response_model=dict)
def create_teacher(teacher: Teacher, db: Session = Depends(get_db)):
    '''
    Creates a new teacher with the given name and email.
    '''
    new_teacher = TeacherModel(name=teacher.name, email=teacher.email)
    db.add(new_teacher)
    db.commit()
    db.refresh(new_teacher)
    return {"id": new_teacher.id, "name": new_teacher.name, "email": new_teacher.email}
@router.get("/teachers/", response_model=list)
def get_teachers(db: Session = Depends(get_db)):
    '''
    Retrieves all teachers.
    '''
    return db.query(TeacherModel).all()
@router.post("/courses/{course_id}/assign_teacher/{teacher_id}", response_model=dict)
def assign_teacher_to_course(course_id: int, teacher_id: int, db: Session = Depends(get_db)):
    '''
    Assigns a teacher to a course.
    '''
    course = db.query(CourseModel).filter(CourseModel.id == course_id).first()
    teacher = db.query(TeacherModel).filter(TeacherModel.id == teacher_id).first()
    if not course or not teacher:
        raise HTTPException(status_code=404, detail="Course or Teacher not found")
    if course.teacher_id is not None:
        raise HTTPException(status_code=400, detail="Course already has a teacher assigned")
    course.teacher = teacher
    db.commit()
    return {"course_id": course.id, "teacher_id": teacher.id}