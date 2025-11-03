'''
Defines the API routes for student management.
'''
from fastapi import APIRouter, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal
from models import Student, Course
from schemas import StudentCreate, StudentResponse
from typing import List
router = APIRouter()
@router.post("/students", response_model=StudentResponse, status_code=201)
def create_student(student: StudentCreate):
    with SessionLocal() as db:
        db_student = Student(name=student.name, email=student.email)
        if student.course_ids:
            db_student.courses = db.query(Course).filter(Course.id.in_(student.course_ids)).all()
        db.add(db_student)
        db.commit()
        db.refresh(db_student)
        return db_student