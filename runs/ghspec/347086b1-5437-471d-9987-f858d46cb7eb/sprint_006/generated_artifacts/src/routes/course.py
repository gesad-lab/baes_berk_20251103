from fastapi import APIRouter, HTTPException
from sqlalchemy.orm import Session
from pydantic import BaseModel
from .models import Course, Teacher
from .database import get_db
import logging

logger = logging.getLogger(__name__)
router = APIRouter()

class AssignTeacherRequest(BaseModel):
    teacher_id: int

@router.put("/courses/{course_id}/assign_teacher")
def assign_teacher_to_course(course_id: int, request: AssignTeacherRequest, db: Session = Depends(get_db)):
    """
    Assign a teacher to a course.

    Parameters:
    course_id (int): The ID of the course to which the teacher will be assigned.
    request (AssignTeacherRequest): The request body containing the teacher_id.
    db (Session): The database session.

    Returns:
    JSON: Success message or error details.
    """
    # Retrieve the course from the database
    course = db.query(Course).filter(Course.id == course_id).first()
    if not course:
        raise HTTPException(status_code=404, detail="Course not found")

    # Validate teacher ID
    teacher = db.query(Teacher).filter(Teacher.id == request.teacher_id).first()
    if not teacher:
        logger.error("Invalid teacher ID %s provided for course ID %s", request.teacher_id, course_id)
        raise HTTPException(status_code=400, detail="Invalid teacher ID")

    # Assign the teacher to the course
    course.teacher_id = request.teacher_id
    db.commit()
    
    logger.info("Assigned teacher ID %s to course ID %s", request.teacher_id, course_id)
    
    return {"message": "Teacher assigned successfully"}