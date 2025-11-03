```python
from fastapi import APIRouter, HTTPException
from models import Course, AssignTeacherRequest, CourseDetailsResponse
from db_setup import SessionLocal
from sqlalchemy.orm import Session

router = APIRouter()

@router.post("/courses/{course_id}/assign-teacher", response_model=dict)
def assign_teacher(course_id: int, request: AssignTeacherRequest):
    """Assign a teacher to a course."""
    session: Session = SessionLocal()
    try:
        course = session.query(Course).filter(Course.id == course_id).first()
        if not course:
            raise HTTPException(status_code=404, detail="Course not found")

        course.teacher_id = request.teacher_id
        session.commit()
        return {"message": "Teacher assigned successfully to course."}
    except Exception as e:
        session.rollback()  # Rollback changes on error
        raise HTTPException(status_code=500, detail="Failed to assign teacher") from e
    finally:
        session.close()  # Ensure session is closed after operation

@router.delete("/courses/{course_id}/remove-teacher", response_model=dict)
def remove_teacher(course_id: int):
    """Remove a teacher from a course."""
    session: Session = SessionLocal()
    try:
        course = session.query(Course).filter(Course.id == course_id).first()
        if not course:
            raise HTTPException(status_code=404, detail="Course not found")

        course.teacher_id = None  # Setting to None to reflect removal
        session.commit()
        return {"message": "Teacher removed successfully from the course."}
    except Exception as e:
        session.rollback()  # Rollback changes on error
        raise HTTPException(status_code=500, detail="Failed to remove teacher") from e
    finally:
        session.close()  # Ensure session is closed after operation
```