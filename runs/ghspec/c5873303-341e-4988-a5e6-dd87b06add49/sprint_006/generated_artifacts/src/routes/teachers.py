import { APIRouter, HTTPException, status }
from fastapi import Depends, Body
from sqlalchemy.orm import Session
from src.database import get_db
from src.models import Course, Teacher
from src.schemas import AssignTeacher, CourseResponse

router = APIRouter()

@router.post("/courses/{course_id}/assign_teacher", response_model=CourseResponse)
async def assign_teacher_to_course(
    course_id: int,
    assign_teacher: AssignTeacher,
    db: Session = Depends(get_db)
):
    """
    Assign a teacher to the specified course.

    Parameters:
    - course_id: The ID of the course to which the teacher will be assigned.
    - assign_teacher: The request body containing the teacher_id.

    Returns:
    - A JSON object containing the updated course details, including teacher info.
    """
    # Fetch the course by ID
    course = db.query(Course).filter(Course.id == course_id).first()
    if course is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Course with ID {course_id} not found."
        )

    # Fetch the teacher by ID
    teacher = db.query(Teacher).filter(Teacher.id == assign_teacher.teacher_id).first()
    if teacher is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Teacher with ID {assign_teacher.teacher_id} not found."
        )

    # Assign teacher to the course
    course.teacher_id = assign_teacher.teacher_id
    db.commit()
    db.refresh(course)

    return course