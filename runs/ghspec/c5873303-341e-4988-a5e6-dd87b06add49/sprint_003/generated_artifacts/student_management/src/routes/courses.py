from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from src.models import Course
from src.schemas import CourseResponse
from src.database import get_db

router = APIRouter()

@router.get("/courses", response_model=list[CourseResponse])
def get_all_courses(db: Session = Depends(get_db)):
    """
    Retrieve all courses from the database.

    Args:
        db (Session): Database session for querying.

    Returns:
        List[CourseResponse]: A list of course objects containing name and level.
    """
    courses = db.query(Course).all()  # Query all courses from the database
    return courses  # Return the list of courses as response

# Make sure to include the router in your main application file as well.