```python
# src/api/courses.py

from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
import logging
from src.database import get_db  # Assuming you have this for database session management
from src.models import Course, Teacher  # Assuming these models exist and are structured correctly

# Create a logger for this module
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

router = APIRouter()

@router.put("/courses/{course_id}/assign-teacher")
async def assign_teacher_to_course(course_id: int, teacher_data: dict, db: Session = Depends(get_db)):
    """
    Assign a teacher to a course.
    
    Parameters:
    - course_id: The ID of the course to which the teacher will be assigned.
    - teacher_data: Dictionary containing the `teacher_id`.
    
    Returns:
    - JSON response with a success message and updated Course details.
    """
    teacher_id = teacher_data.get("teacher_id")
    
    # Log the attempt to assign a teacher
    logger.info(f"Attempting to assign teacher {teacher_id} to course {course_id}")

    course = db.query(Course).filter(Course.id == course_id).first()
    if not course:
        logger.error(f"Course with id {course_id} not found")
        raise HTTPException(status_code=404, detail="Course not found")
    
    teacher = db.query(Teacher).filter(Teacher.id == teacher_id).first()
    if not teacher:
        logger.error(f"Teacher with id {teacher_id} not found")
        raise HTTPException(status_code=404, detail="Teacher not found")
    
    course.teacher_id = teacher_id
    db.commit()
    logger.info(f"Successfully assigned teacher {teacher_id} to course {course_id}")
    
    return {
        "message": "Teacher assigned successfully",
        "course": {
            "id": course.id,
            "name": course.name,
            "teacher_id": course.teacher_id,
            "teacher_name": teacher.name,
            "teacher_email": teacher.email
        }
    }

@router.get("/courses/{course_id}")
async def retrieve_course_details(course_id: int, db: Session = Depends(get_db)):
    """
    Retrieve details of a specific course along with its assigned teacher.
    
    Parameters:
    - course_id: The ID of the course to retrieve.
    
    Returns:
    - JSON object containing the Course's details and assigned Teacher's information.
    """
    logger.info(f"Retrieving details for course {course_id}")
    
    course = db.query(Course).filter(Course.id == course_id).first()
    if not course:
        logger.error(f"Course with id {course_id} not found")
        raise HTTPException(status_code=404, detail="Course not found")

    teacher = db.query(Teacher).filter(Teacher.id == course.teacher_id).first() if course.teacher_id else None
    
    return {
        "id": course.id,
        "name": course.name,
        "teacher": {
            "name": teacher.name if teacher else None,
            "email": teacher.email if teacher else None
        } if teacher else None
    }
```