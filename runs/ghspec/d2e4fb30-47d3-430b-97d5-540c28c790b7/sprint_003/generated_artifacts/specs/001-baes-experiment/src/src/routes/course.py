from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session
from ..models.course import Course
from ..database import get_db

router = APIRouter()

class CourseCreate(BaseModel):
    name: str
    level: str

@router.post("/courses", response_model=CourseCreate)
async def create_course(course: CourseCreate, db: Session = Depends(get_db)):
    """
    Create a new course in the database.

    Args:
        course (CourseCreate): Course data containing name and level to be created.
        db (Session): The database session to be used for creating the course.

    Raises:
        HTTPException: If course creation fails due to validation errors.

    Returns:
        CourseCreate: The details of the created course.
    """
    if not course.name or not course.level:
        raise HTTPException(
            status_code=400,
            detail="Both 'name' and 'level' are required fields."
        )

    # Create a new course instance
    new_course = Course(name=course.name, level=course.level)

    # Add the course to the database
    db.add(new_course)
    db.commit()
    db.refresh(new_course)  # Refresh the instance to get the generated ID

    return new_course

@router.get("/courses", response_model=list[CourseCreate])
async def get_courses(db: Session = Depends(get_db)):
    """
    Retrieve all courses from the database.

    Args:
        db (Session): The database session to be used for querying courses.

    Returns:
        list[CourseCreate]: A list of all courses in the database.
    """
    courses = db.query(Course).all()  # Fetch all courses from the database
    return courses  # Return the list of courses