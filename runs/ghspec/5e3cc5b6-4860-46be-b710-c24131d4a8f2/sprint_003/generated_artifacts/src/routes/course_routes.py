```python
from fastapi import APIRouter, HTTPException, status
from typing import List
from src.models.course import Course
from src.schemas.course_schema import CourseCreate, CourseResponse
from src.database.database import get_db
from sqlalchemy.orm import Session

router = APIRouter()

@router.post("/courses", response_model=CourseResponse, status_code=status.HTTP_201_CREATED)
async def create_course(course: CourseCreate, db: Session = next(get_db())):
    """
    Create a new course.

    Parameters:
    - course: CourseCreate object containing the course details.

    Returns:
    - CourseResponse object with the created course details.
    """
    db_course = Course(name=course.name, level=course.level)
    db.add(db_course)
    db.commit()
    db.refresh(db_course)
    return db_course

@router.get("/courses/{course_id}", response_model=CourseResponse, status_code=status.HTTP_200_OK)
async def retrieve_course(course_id: int, db: Session = next(get_db())):
    """
    Retrieve a course by its ID.

    Parameters:
    - course_id: ID of the course to retrieve.

    Returns:
    - CourseResponse object with the course details.
    """
    course = db.query(Course).filter(Course.id == course_id).first()
    if course is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Course not found")
    return course

@router.put("/courses/{course_id}", response_model=CourseResponse, status_code=status.HTTP_200_OK)
async def update_course(course_id: int, course: CourseCreate, db: Session = next(get_db())):
    """
    Update an existing course's name or level.

    Parameters:
    - course_id: ID of the course to update.
    - course: CourseCreate object containing the new values for the course.

    Returns:
    - CourseResponse object with the updated course details.
    """
    db_course = db.query(Course).filter(Course.id == course_id).first()
    if db_course is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Course not found")
    
    db_course.name = course.name
    db_course.level = course.level
    db.commit()
    db.refresh(db_course)
    return db_course

# Register the router in the main application file
def init_routes(app):
    app.include_router(router, prefix="/api/v1", tags=["courses"])
```