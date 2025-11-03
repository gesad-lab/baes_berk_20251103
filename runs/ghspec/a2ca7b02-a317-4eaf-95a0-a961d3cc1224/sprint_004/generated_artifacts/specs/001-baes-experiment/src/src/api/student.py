from fastapi import APIRouter, HTTPException, Body
from services.student_service import StudentService
from pydantic import BaseModel

router = APIRouter()

class CourseEnrollmentRequest(BaseModel):
    course_id: int

@router.post("/students/{student_id}/courses")
async def enroll_student_in_course(student_id: int, course_data: CourseEnrollmentRequest):
    """
    Enroll a student in a course.
    
    Args:
        student_id (int): The ID of the student.
        course_data (CourseEnrollmentRequest): Contains the course_id for enrollment.

    Returns:
        dict: Confirmation of enrollment.
    
    Raises:
        HTTPException: If the student or course is not found, or enrollment fails.
    """
    # Attempt to enroll the student in the specified course
    try:
        return await StudentService.enroll_student_in_course(student_id, course_data.course_id)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail="An error occurred while enrolling the student.")

@router.get("/students/{student_id}")
async def retrieve_student_with_courses(student_id: int):
    """
    Retrieve a student's information along with enrolled courses.
    
    Args:
        student_id (int): The ID of the student.

    Returns:
        dict: Student information along with enrolled courses.

    Raises:
        HTTPException: If the student is not found.
    """
    # Attempt to retrieve student data with courses
    try:
        student_data = await StudentService.get_student_with_courses(student_id)
        if not student_data:
            raise HTTPException(status_code=404, detail="Student not found.")
        return student_data
    except Exception as e:
        raise HTTPException(status_code=500, detail="An error occurred while retrieving student data.")