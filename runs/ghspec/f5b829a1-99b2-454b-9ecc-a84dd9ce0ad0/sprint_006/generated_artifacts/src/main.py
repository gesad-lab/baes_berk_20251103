from fastapi import FastAPI, HTTPException, Path
from pydantic import BaseModel
from src.services.course_service import CourseService

app = FastAPI()
course_service = CourseService()

class TeacherAssignment(BaseModel):
    teacher_id: int

class UnassignmentResponse(BaseModel):
    id: int
    message: str

@app.put('/courses/{course_id}/assign-teacher', response_model=dict)
async def assign_teacher(course_id: int = Path(..., title="The ID of the course"), assignment: TeacherAssignment):
    """
    Assign a teacher to a course.
    
    Parameters:
    - course_id: The ID of the course to which a teacher will be assigned.
    - assignment: JSON body containing the teacher_id.

    Returns:
    - A JSON response with the course details.
    
    Raises:
    - HTTPException: if the course or teacher does not exist.
    """
    try:
        course = course_service.assign_teacher(course_id, assignment.teacher_id)
        return {"id": course.id, "name": course.name, "teacher_id": course.teacher_id}
    except ValueError as e:  # Change this to specific exception type as needed
        raise HTTPException(status_code=404, detail=str(e))

@app.delete('/courses/{course_id}/unassign-teacher', response_model=UnassignmentResponse)
async def unassign_teacher(course_id: int = Path(..., title="The ID of the course")):
    """
    Remove a teacher from a course.
    
    Parameters:
    - course_id: The ID of the course from which a teacher will be unassigned.

    Returns:
    - A JSON response confirming the teacher has been unassigned.
    
    Raises:
    - HTTPException: if the course does not exist.
    """
    try:
        course = course_service.unassign_teacher(course_id)
        return {"id": course.id, "message": "Teacher unassigned successfully"}
    except ValueError as e:  # Change this to specific exception type as needed
        raise HTTPException(status_code=404, detail=str(e))