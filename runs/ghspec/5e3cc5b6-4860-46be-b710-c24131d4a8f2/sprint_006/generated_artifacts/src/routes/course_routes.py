```python
from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from src.database.database import get_db
from src.models.course import Course
from src.models.teacher import Teacher
from src.schemas.course_schema import CourseResponse

router = APIRouter()

@router.get("/courses/{course_id}", response_model=CourseResponse)
def get_course(course_id: int, db: Session = Depends(get_db)):
    """
    Retrieve the details of a specific course by ID, including associated Teacher information.

    Args:
        course_id (int): The ID of the course to retrieve.
        db (Session): The database session dependency.

    Returns:
        CourseResponse: The details of the course, including teacher information.

    Raises:
        HTTPException: If the course is not found or any other error occurs.
    """
    course = db.query(Course).filter(Course.id == course_id).first()

    if not course:
        raise HTTPException(status_code=404, detail="Course not found")

    return course
```