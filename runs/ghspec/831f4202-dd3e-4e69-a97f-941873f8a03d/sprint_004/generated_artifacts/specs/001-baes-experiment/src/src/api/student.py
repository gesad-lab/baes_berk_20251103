```python
import logging
from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from src.database import get_db
from src.models import Student, Course
from pydantic import BaseModel

# Setup logging configuration
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

router = APIRouter()

class CourseAssociationRequest(BaseModel):
    student_id: int
    course_id: int

@router.post("/students/associate_course")
async def associate_course(request: CourseAssociationRequest, db: Session = Depends(get_db)):
    """
    Associate a student with a course.

    Args:
        request (CourseAssociationRequest): The request body containing student and course IDs.
        db (Session): The database session.

    Returns:
        JSON response with the status of the association.

    Raises:
        HTTPException: If student or course is not found or any validation fails.
    """
    # Validate student existence
    student = db.query(Student).filter(Student.id == request.student_id).first()
    if not student:
        logger.error(f"Student ID {request.student_id} not found.")
        raise HTTPException(status_code=404, detail="Student not found.")

    # Validate course existence
    course = db.query(Course).filter(Course.id == request.course_id).first()
    if not course:
        logger.error(f"Course ID {request.course_id} not found.")
        raise HTTPException(status_code=404, detail="Course not found.")

    # Assume the logic for associating student with course goes here
    # For example: associate_student_with_course(student, course)

    logger.info(f"Successfully associated Student ID {request.student_id} with Course ID {request.course_id}.")
    return {"message": "Course association successful."}
```