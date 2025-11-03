'''
Contains the API endpoints for creating and retrieving Student, Course, and Teacher entities.
'''
from fastapi import APIRouter, HTTPException
from sqlalchemy.orm import Session
from models import Student, Course, Teacher
from database import SessionLocal
from schemas import StudentCreate, CourseCreate, TeacherCreate
from typing import List
router = APIRouter()
@router.post("/students/", response_model=dict)
async def create_student(student: StudentCreate):
    db: Session = SessionLocal()
    try:
        new_student = Student(name=student.name, email=student.email)
        db.add(new_student)
        db.commit()
        db.refresh(new_student)
        return {"id": new_student.id, "name": new_student.name, "email": new_student.email}
    finally:
        db.close()
@router.get("/students/", response_model=list)
async def read_students():
    db: Session = SessionLocal()
    try:
        students = db.query(Student).all()
        return [{"id": student.id, "name": student.name, "email": student.email} for student in students]
    finally:
        db.close()
@router.post("/courses/", response_model=dict)
async def create_course(course: CourseCreate):
    db: Session = SessionLocal()
    try:
        new_course = Course(name=course.name, level=course.level)
        db.add(new_course)
        db.commit()
        db.refresh(new_course)
        return {"id": new_course.id, "name": new_course.name, "level": new_course.level}
    finally:
        db.close()
@router.get("/courses/", response_model=list)
async def read_courses():
    db: Session = SessionLocal()
    try:
        courses = db.query(Course).all()
        return [{"id": course.id, "name": course.name, "level": course.level} for course in courses]
    finally:
        db.close()
@router.post("/students/{student_id}/courses/{course_id}", response_model=dict)
async def add_course_to_student(student_id: int, course_id: int):
    db: Session = SessionLocal()
    try:
        student = db.query(Student).filter(Student.id == student_id).first()
        course = db.query(Course).filter(Course.id == course_id).first()
        if not student or not course:
            raise HTTPException(status_code=404, detail="Student or Course not found")
        student.courses.append(course)
        db.commit()
        return {"message": "Course added to student successfully"}
    finally:
        db.close()
@router.post("/teachers/", response_model=dict)
async def create_teacher(teacher: TeacherCreate):
    db: Session = SessionLocal()
    try:
        new_teacher = Teacher(name=teacher.name, email=teacher.email)
        db.add(new_teacher)
        db.commit()
        db.refresh(new_teacher)
        return {"id": new_teacher.id, "name": new_teacher.name, "email": new_teacher.email}
    finally:
        db.close()
@router.get("/teachers/", response_model=list)
async def read_teachers():
    db: Session = SessionLocal()
    try:
        teachers = db.query(Teacher).all()
        return [{"id": teacher.id, "name": teacher.name, "email": teacher.email} for teacher in teachers]
    finally:
        db.close()