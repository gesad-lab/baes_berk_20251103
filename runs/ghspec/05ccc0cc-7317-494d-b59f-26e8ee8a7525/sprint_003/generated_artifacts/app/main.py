from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import Course
from app.schemas import CourseCreate, CourseResponse

router = APIRouter()

@router.post("/courses/", response_model=CourseResponse)
def create_course(course: CourseCreate, db: Session = Depends(get_db)):
    """
    Create a new course with the specified name and level.

    Args:
        course (CourseCreate): The course object containing name and level.
        db (Session): Database session for CRUD operations.

    Returns:
        CourseResponse: The created course details.
    
    Raises:
        HTTPException: If the course could not be created due to validation errors.
    """
    # Ensure that both name and level are provided
    if not course.name or not course.level:
        raise HTTPException(status_code=400, detail="Both name and level are required fields.")

    # Create a new Course object
    new_course = Course(name=course.name, level=course.level)
    
    # Add and commit the new course to the database
    db.add(new_course)
    db.commit()
    db.refresh(new_course)

    return new_course

@router.get("/courses/", response_model=list[CourseResponse])
def read_courses(db: Session = Depends(get_db)):
    """
    Retrieve a list of all available courses.

    Args:
        db (Session): Database session for CRUD operations.

    Returns:
        List[CourseResponse]: A list of course objects.
    """
    courses = db.query(Course).all()
    return courses

# Register the course router with the main application
def register_course_routes(app):
    app.include_router(router)