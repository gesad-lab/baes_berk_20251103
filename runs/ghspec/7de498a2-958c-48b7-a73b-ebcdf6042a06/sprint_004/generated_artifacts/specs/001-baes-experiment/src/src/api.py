from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session
from src.services import remove_student_from_course, get_student_by_id, get_course_by_id
from src.database import get_db

router = APIRouter()

class CourseUnenroll(BaseModel):
    course_id: int

@router.delete("/students/{student_id}/enroll", response_model=dict)
async def unenroll_student(student_id: int, course: CourseUnenroll, db: Session = Depends(get_db)):
    """
    Remove a student from a course.

    - student_id: ID of the student to unenroll
    - course: Contains the course_id to remove
    """
    # Check if the student exists
    student = get_student_by_id(db, student_id)
    if student is None:
        raise HTTPException(status_code=404, detail="Student not found")

    # Check if the course exists
    course_entity = get_course_by_id(db, course.course_id)
    if course_entity is None:
        raise HTTPException(status_code=404, detail="Course not found")

    # Attempt to remove the student from the course
    success = remove_student_from_course(db, student_id, course.course_id)
    if not success:
        raise HTTPException(status_code=400, detail="Failed to remove student from course")

    # Return a success message
    return {"success": True, "message": "Student successfully removed from course"}