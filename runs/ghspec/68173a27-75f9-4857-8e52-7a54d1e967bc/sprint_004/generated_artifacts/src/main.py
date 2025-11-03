```python
import logging
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from src.services.student_course_service import enroll_student, get_student_courses

app = FastAPI()

# Setup logging configuration
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class EnrollmentRequest(BaseModel):
    student_id: int
    course_id: int

@app.post("/enroll")
async def enroll(enrollment: EnrollmentRequest):
    """
    Enroll a student in a course.

    Args:
        enrollment (EnrollmentRequest): Enrollment information including student_id and course_id.

    Returns:
        dict: Confirmation message on successful enrollment.

    Raises:
        HTTPException: If the input is invalid or enrollment fails.
    """
    try:
        result = await enroll_student(enrollment.student_id, enrollment.course_id)
        logger.info(f"Student {enrollment.student_id} enrolled in course {enrollment.course_id}.")
        return {"message": "Enrollment successful", "result": result}
    except ValueError as e:
        logger.error(f"Enrollment failed: {str(e)}")
        raise HTTPException(status_code=400, detail=str(e))


@app.get("/students/{student_id}/courses")
async def get_courses(student_id: int):
    """
    Retrieve courses for a given student.

    Args:
        student_id (int): ID of the student.

    Returns:
        list: List of courses the student is enrolled in.
    
    Raises:
        HTTPException: If the student ID is invalid or retrieval fails.
    """
    try:
        courses = await get_student_courses(student_id)
        if not courses:
            logger.warning(f"No courses found for student ID {student_id}.")
            return {"message": "No courses found", "courses": []}
        
        logger.info(f"Retrieved courses for student ID {student_id}.")
        return {"courses": courses}
    except Exception as e:
        logger.error(f"Error retrieving courses for student ID {student_id}: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal server error")
```