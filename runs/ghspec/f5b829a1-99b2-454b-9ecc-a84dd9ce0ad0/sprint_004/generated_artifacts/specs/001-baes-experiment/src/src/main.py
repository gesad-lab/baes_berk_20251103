```python
import logging
from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from src.models import Student, Course
from src.services.enrollment_service import EnrollmentService
from src.database import get_db  # Assuming there is a database module for session management

# Set up structured logging
logging.basicConfig(
    level=logging.INFO,
    format='{"time": "%(asctime)s", "level": "%(levelname)s", "message": "%(message)s"}'
)
logger = logging.getLogger(__name__)

app = FastAPI()

@app.post("/students/{student_id}/enroll")
async def enroll_student(student_id: int, course_id: int, db: Session = Depends(get_db)):
    """
    Enroll a student into a course.

    Args:
        student_id (int): The ID of the student.
        course_id (int): The ID of the course.
        db (Session): The database session dependency.

    Returns:
        dict: Confirmation message if enrollment is successful.

    Raises:
        HTTPException: If the student or course is invalid or already enrolled.
    """
    try:
        enrollment_service = EnrollmentService()
        await enrollment_service.enroll_student(db, student_id, course_id)
        logger.info(f"Student {student_id} successfully enrolled in course {course_id}.")
        return {"message": "Enrollment successful"}
    except ValueError as e:
        logger.error(f"Enrollment failed: {str(e)}")
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        logger.exception("An unexpected error occurred during enrollment.")
        raise HTTPException(status_code=500, detail="Internal server error")

@app.get("/students/{student_id}/courses")
async def get_courses(student_id: int, db: Session = Depends(get_db)):
    """
    Retrieve a list of courses for a given student.

    Args:
        student_id (int): The ID of the student.
        db (Session): The database session dependency.

    Returns:
        list: A list of courses the student is enrolled in.

    Raises:
        HTTPException: If the student is invalid.
    """
    try:
        enrollment_service = EnrollmentService()
        courses = await enrollment_service.get_courses_for_student(db, student_id)
        logger.info(f"Retrieved courses for student {student_id}.")
        return courses
    except ValueError as e:
        logger.error(f"Failed to retrieve courses for student {student_id}: {str(e)}")
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        logger.exception("An unexpected error occurred while retrieving courses.")
        raise HTTPException(status_code=500, detail="Internal server error")
```