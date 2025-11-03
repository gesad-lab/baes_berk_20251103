# src/api.py

from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from models import Course, Teacher  # Import models
from database import get_db  # Import database session from a separate module
import logging

app = FastAPI()

# Configure logging for error handling
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class ErrorResponse:
    """Standard error response format."""
    def __init__(self, code: str, message: str):
        self.error = {
            "code": code,
            "message": message
        }

@app.post("/courses/{course_id}/assign-teacher")
async def assign_teacher(course_id: int, teacher_id: int, db: Session = Depends(get_db)):
    """Assign a teacher to a course."""
    # Validate that the course exists
    course = db.query(Course).filter(Course.id == course_id).first()
    if not course:
        logger.error(f"Assign Teacher Error: Course with id {course_id} not found.")
        raise HTTPException(status_code=404, detail=ErrorResponse("E404", "Course not found."))

    # Validate that the teacher exists
    teacher = db.query(Teacher).filter(Teacher.id == teacher_id).first()
    if not teacher:
        logger.error(f"Assign Teacher Error: Teacher with id {teacher_id} not found.")
        raise HTTPException(status_code=404, detail=ErrorResponse("E404", "Teacher not found."))

    # Assign teacher to the course
    course.teacher_id = teacher_id
    db.commit()
    logger.info(f"Teacher with id {teacher_id} assigned to Course with id {course_id}.")
    return {"message": "Teacher successfully assigned to the course."}

@app.get("/courses/{course_id}")
async def get_course(course_id: int, db: Session = Depends(get_db)):
    """Retrieve course details, including the assigned teacher."""
    course = db.query(Course).filter(Course.id == course_id).first()
    if not course:
        logger.error(f"Get Course Error: Course with id {course_id} not found.")
        raise HTTPException(status_code=404, detail=ErrorResponse("E404", "Course not found."))

    # Build response with course details
    response = {
        "id": course.id,
        "name": course.name,
        "teacher": {"name": course.teacher.name} if course.teacher else None
    }
    return response