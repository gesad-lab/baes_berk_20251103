'''
Contains the API endpoints for creating and retrieving Student entities.
'''
from fastapi import APIRouter, HTTPException
from sqlalchemy.orm import Session
from models import Student
from database import SessionLocal
from schemas import StudentCreate
router = APIRouter()
@router.post("/students/", response_model=dict)
async def create_student(student: StudentCreate):
    db: Session = SessionLocal()
    try:
        new_student = Student(name=student.name, email=student.email)  # Include email when creating a new student
        db.add(new_student)
        db.commit()
        db.refresh(new_student)
        return {"id": new_student.id, "name": new_student.name, "email": new_student.email}  # Return email in response
    finally:
        db.close()
@router.get("/students/", response_model=list)
async def read_students():
    db: Session = SessionLocal()
    try:
        students = db.query(Student).all()
        return [{"id": student.id, "name": student.name, "email": student.email} for student in students]  # Include email in response
    finally:
        db.close()