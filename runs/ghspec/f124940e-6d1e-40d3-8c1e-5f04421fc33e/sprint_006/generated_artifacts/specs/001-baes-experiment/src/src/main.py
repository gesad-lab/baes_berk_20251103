```python
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional
from src.models import Course  # Assuming Course model exists in models.py
from src.services.courses_service import assign_teacher_to_course, get_course_details, unassign_teacher_from_course  # Assuming these service functions exist

app = FastAPI()

class TeacherAssignmentRequest(BaseModel):
    teacher_id: int  # Request body to assign a teacher

class CourseResponse(BaseModel):
    id: int
    name: str
    teacher: Optional[dict]  # To hold teacher's details if assigned


@app.post("/courses/{course_id}/assign_teacher", response_model=CourseResponse)
async def assign_teacher(course_id: int, request: TeacherAssignmentRequest):
    """Assign a teacher to a course.

    - course_id: ID of the course to assign a teacher to.
    - request: Contains the teacher_id to assign.
    
    Returns the updated course details upon successful assignment.
    """
    try:
        updated_course = await assign_teacher_to_course(course_id, request.teacher_id)
        return updated_course
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))  # Handle invalid teacher assignment


@app.get("/courses/{course_id}", response_model=CourseResponse)
async def retrieve_course(course_id: int):
    """Retrieve course details including assigned teacher.

    - course_id: ID of the course to retrieve.
    
    Returns course details with assigned teacher info.
    """
    try:
        course_details = await get_course_details(course_id)
        return course_details
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))  # Course not found


@app.delete("/courses/{course_id}/unassign_teacher", response_model=CourseResponse)
async def unassign_teacher(course_id: int):
    """Unassign the teacher from the course.

    - course_id: ID of the course to unassign the teacher from.
    
    Returns the updated course details after unassignment.
    """
    try:
        updated_course = await unassign_teacher_from_course(course_id)
        return updated_course
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))  # Course not found


# Note: Ensure that the functions assign_teacher_to_course, get_course_details, and unassign_teacher_from_course are implemented in the courses_service.py file.
```