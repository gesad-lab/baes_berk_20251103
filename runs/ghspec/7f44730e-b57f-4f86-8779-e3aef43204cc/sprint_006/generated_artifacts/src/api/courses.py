# src/api/courses.py
from fastapi import APIRouter, HTTPException
from sqlalchemy.orm import Session
from pydantic import BaseModel
from db.database import SessionLocal
from models.course import Course
from models.teacher import Teacher

router = APIRouter()

class AssignTeacher(BaseModel):
    teacher_id: str

@router.post("/courses/{course_id}/assign_teacher")
def assign_teacher(course_id: str, assign_teacher: AssignTeacher):
    db = SessionLocal()
    course = db.query(Course).filter(Course.id == course_id).first()
    teacher = db.query(Teacher).filter(Teacher.id == assign_teacher.teacher_id).first()

    if not course:
        raise HTTPException(status_code=404, detail={"error": {"code": "E002", "message": "Course does not exist"}})
    if not teacher:
        raise HTTPException(status_code=404, detail={"error": {"code": "E003", "message": "Teacher does not exist"}})

    course.teacher_id = assign_teacher.teacher_id
    db.commit()
    db.refresh(course)

    return {"message": "Teacher assigned to course successfully"}

@router.get("/courses/{course_id}")
def get_course_details(course_id: str):
    db = SessionLocal()
    course = db.query(Course).filter(Course.id == course_id).first()
    
    if not course:
        raise HTTPException(status_code=404, detail={"error": {"code": "E002", "message": "Course does not exist"}})

    # Prepare response structure to include course details with assigned teacher info
    return {
        "course": {
            "name": course.name,
            "teacher": {
                "name": course.teacher.name if course.teacher else None,
                "email": course.teacher.email if course.teacher else None
            }
        }
    }