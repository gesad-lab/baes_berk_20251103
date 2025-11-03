```python
from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from src.database import get_db
from src.service.student_course_service import associate_courses, get_student_courses
from src.model.student_course import StudentCourse

router = APIRouter()

@router.post("/students/{id}/courses")
async def enroll_courses(id: int, course_ids: list[int], db: Session = Depends(get_db)):
    """
    Enroll a student in one or more courses.

    Parameters:
    - id: The ID of the student to enroll.
    - course_ids: A list of course IDs to associate with the student.

    Returns:
    - A success message upon successful enrollment.
    """
    try:
        associate_courses(db, id, course_ids)
        return {"message": "Courses associated successfully with the student."}
    except HTTPException as e:
        raise HTTPException(status_code=e.status_code, detail=e.detail)
    except Exception as e:
        # Log error details (except sensitive information)
        raise HTTPException(status_code=500, detail="An unexpected error occurred.")

@router.get("/students/{id}/courses")
async def retrieve_student_courses(id: int, db: Session = Depends(get_db)):
    """
    Retrieve all courses associated with a student.

    Parameters:
    - id: The ID of the student to retrieve courses for.

    Returns:
    - A list of courses associated with the student.
    """
    try:
        courses = get_student_courses(db, id)
        return courses
    except HTTPException as e:
        raise HTTPException(status_code=e.status_code, detail=e.detail)
    except Exception as e:
        # Log error details (except sensitive information)
        raise HTTPException(status_code=500, detail="An unexpected error occurred.")
```