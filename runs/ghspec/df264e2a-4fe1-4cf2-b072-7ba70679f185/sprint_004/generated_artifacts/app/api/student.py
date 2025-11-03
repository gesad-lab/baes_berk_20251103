```python
# app/api/student.py

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.services.student_service import assign_course_to_student, get_student_with_courses

router = APIRouter()

class CourseAssignmentRequest(BaseModel):
    course_id: int


@router.post("/students/{id}/courses")
async def add_course_to_student(id: int, request: CourseAssignmentRequest):
    """
    Assign a course to a student based on their ID.

    :param id: The ID of the student.
    :param request: JSON body with course_id to be assigned.
    :return: Confirmation message in JSON format.
    """
    try:
        response = await assign_course_to_student(student_id=id, course_id=request.course_id)
        return {"message": response}
    except HTTPException as e:
        # Raising an HTTP exception if the course ID is invalid
        raise HTTPException(status_code=e.status_code, detail=e.detail)


@router.get("/students/{id}")
async def fetch_student(id: int):
    """
    Retrieve a student's details along with their enrolled courses.

    :param id: The ID of the student to retrieve.
    :return: JSON response containing the student's details and courses.
    """
    student_info = await get_student_with_courses(student_id=id)
    if not student_info:
        raise HTTPException(status_code=404, detail="Student not found")

    return student_info
```