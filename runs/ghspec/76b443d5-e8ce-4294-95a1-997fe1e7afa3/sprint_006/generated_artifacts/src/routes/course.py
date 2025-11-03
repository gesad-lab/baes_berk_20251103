```python
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, constr
from sqlalchemy.orm import Session
from src.database import get_db
from src.models import Course, Teacher
from typing import Any

router = APIRouter()

class TeacherAssignment(BaseModel):
    teacher_id: int

@router.patch("/courses/{course_id}/assign-teacher")
def assign_teacher_to_course(course_id: int, teacher_assignment: TeacherAssignment, db: Session = Depends(get_db)) -> dict:
    """
    Assign a teacher to a course.

    Args:
        course_id (int): The ID of the course to assign the teacher to.
        teacher_assignment (TeacherAssignment): The teacher assignment details containing teacher_id.
        db (Session): The database session dependency.

    Returns:
        dict: Success message and assigned IDs.

    Raises:
        HTTPException: If the course or teacher does not exist.
    """
    # Validate that the course exists
    course = db.query(Course).filter(Course.id == course_id).first()
    if not course:
        raise HTTPException(status_code=404, detail={"code": "E001", "message": "Course not found."})

    # Validate that the teacher exists
    teacher = db.query(Teacher).filter(Teacher.id == teacher_assignment.teacher_id).first()
    if not teacher:
        raise HTTPException(status_code=404, detail={"code": "E002", "message": "Teacher not found."})

    # Assign the teacher to the course
    course.teacher_id = teacher_assignment.teacher_id
    db.commit()

    return {
        "message": "Teacher assigned successfully.",
        "course_id": course_id,
        "teacher_id": teacher_assignment.teacher_id
    }
```