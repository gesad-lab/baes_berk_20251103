```python
# src/routes/course_routes.py

from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from src.database.database import get_db
from src.models.course import Course
from src.models.teacher import Teacher
from src.schemas.course import CourseResponse
from src.schemas.teacher import TeacherResponse

router = APIRouter()

@router.get("/courses", response_model=list[CourseResponse])
def list_courses(db: Session = Depends(get_db)):
    """
    Retrieve all courses along with their assigned teachers.

    Parameters:
    - db: Database session dependency.

    Returns:
    - List[CourseResponse]: List of courses with associated teacher information.
    """
    courses = db.query(Course).all()
    
    if not courses:
        raise HTTPException(status_code=404, detail="No courses found.")

    return [
        {
            "id": course.id,
            "name": course.name,
            "teacher": {
                "id": course.teacher.id,
                "name": course.teacher.name
            } if course.teacher else None
        } for course in courses
    ]
```