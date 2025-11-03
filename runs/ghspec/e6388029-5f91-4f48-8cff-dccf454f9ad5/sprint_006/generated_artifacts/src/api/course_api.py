from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from src.database import get_db
from src.models import Course, Teacher

router = APIRouter()

@router.patch("/courses/{course_id}/assign-teacher", response_model=None)
async def assign_teacher_to_course(course_id: int, teacher_id: int, db: Session = Depends(get_db)):
    """
    Assign a teacher to a course by updating the course record with the teacher's ID.

    Args:
    - course_id: The ID of the course to update.
    - teacher_id: The ID of the teacher to assign to the course.
    - db: The database session.

    Returns:
    - None: Returns 204 No Content on success.

    Raises:
    - HTTPException: 404 if the course is not found, 400 if the teacher is not found.
    """
    course = db.query(Course).filter(Course.id == course_id).first()
    if course is None:
        raise HTTPException(status_code=404, detail="Course not found.")
    
    teacher = db.query(Teacher).filter(Teacher.id == teacher_id).first()
    if teacher is None:
        raise HTTPException(status_code=400, detail="Teacher not found.")
    
    # Assign the teacher to the course
    course.teacher_id = teacher_id
    db.commit()
    return None  # Returns 204 No Content