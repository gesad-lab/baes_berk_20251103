```python
# src/api/student_course_api.py

from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel
from src.models.student import Student
from src.models.course import Course
from src.services.student_course_service import associate_student_with_course, get_student_courses

router = APIRouter()

class CourseAssociationRequest(BaseModel):
    """
    Schema for associating a student with a course.
    """
    course_id: str

@router.post("/students/{student_id}/courses", status_code=status.HTTP_200_OK)
async def associate_course(student_id: int, request: CourseAssociationRequest):
    """
    Associate a student with a course.

    Parameters:
    - student_id: int, the ID of the student
    - request: CourseAssociationRequest, the course association request body

    Returns:
    - Confirmation message upon successful association.

    Raises:
    - HTTPException if student or course cannot be found.
    """
    # Associate the student with the course using the service layer
    try:
        await associate_student_with_course(student_id, request.course_id)
        return {"message": "Course associated successfully."}
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))

@router.get("/students/{student_id}/courses", status_code=status.HTTP_200_OK)
async def retrieve_courses(student_id: int):
    """
    Retrieve all courses associated with a student.

    Parameters:
    - student_id: int, the ID of the student

    Returns:
    - List of course objects associated with the specified student.

    Raises:
    - HTTPException if student cannot be found.
    """
    # Retrieve the courses associated with the student from the service layer
    try:
        courses = await get_student_courses(student_id)
        return courses
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))
```