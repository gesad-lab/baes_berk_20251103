from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field
from sqlalchemy.orm import Session
from src.repository import get_course, assign_teacher_to_course, Course, Teacher  # Ensure models and repository functions are imported
from typing import List

router = APIRouter()

class AssignTeacherRequest(BaseModel):
    teacher_id: int = Field(..., description="The ID of the teacher to assign")
    
class CourseResponse(BaseModel):
    id: int
    name: str
    teacher: str

@router.post("/courses/{course_id}/assign-teacher", response_model=CourseResponse)
async def assign_teacher(course_id: int, request: AssignTeacherRequest, db: Session):
    """
    Assign a teacher to a course by course ID.
    
    Args:
        course_id (int): The ID of the course to which the teacher is being assigned.
        request (AssignTeacherRequest): The request body containing the teacher ID.

    Returns:
        CourseResponse: The updated course details with the assigned teacher.
    
    Raises:
        HTTPException: If the course or teacher ID is invalid.
    """
    course = get_course(db, course_id)
    if not course:
        raise HTTPException(status_code=404, detail="Course not found")
    
    teacher = get_teacher(db, request.teacher_id)  # Assumes this function is defined in the repository
    if not teacher:
        raise HTTPException(status_code=404, detail="Teacher not found")
    
    updated_course = assign_teacher_to_course(db, course_id, request.teacher_id)
    
    return CourseResponse(id=updated_course.id, name=updated_course.name, teacher=teacher.name)

@router.get("/courses/{course_id}", response_model=CourseResponse)
async def get_course_with_teacher(course_id: int, db: Session):
    """
    Retrieve a course with its assigned teacher by course ID.
    
    Args:
        course_id (int): The ID of the course to retrieve.

    Returns:
        CourseResponse: The course details including the assigned teacher.
    
    Raises:
        HTTPException: If the course ID is invalid.
    """
    course = get_course(db, course_id)
    if not course:
        raise HTTPException(status_code=404, detail="Course not found")
    
    # Assume there's a method to get the teacher details if assigned
    teacher_name = course.teacher.name if course.teacher else None
    
    return CourseResponse(id=course.id, name=course.name, teacher=teacher_name) 

# Include the new router into the main application file (not shown here) to register these endpoints.