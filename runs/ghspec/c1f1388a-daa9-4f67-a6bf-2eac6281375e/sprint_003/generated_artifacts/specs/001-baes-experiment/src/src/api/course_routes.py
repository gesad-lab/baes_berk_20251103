from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from src.models.course import Course
from src.schemas.course import CourseCreate, CourseResponse
from src.db.database import get_db

router = APIRouter()

@router.post("/courses", response_model=CourseResponse)
async def create_course(course: CourseCreate, db: Session = Depends(get_db)):
    """
    Create a new course with the provided name and level.
    
    Args:
        course (CourseCreate): The course data containing the name and level.
        db (Session): The database session.

    Returns:
        CourseResponse: The created course's details.
    
    Raises:
        HTTPException: If the course could not be created.
    """
    new_course = Course(name=course.name, level=course.level)
    db.add(new_course)
    try:
        db.commit()
        db.refresh(new_course)
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail="Could not create course") from e

    return new_course

@router.get("/courses/{course_id}", response_model=CourseResponse)
async def get_course(course_id: int, db: Session = Depends(get_db)):
    """
    Retrieve a course by its ID.
    
    Args:
        course_id (int): The ID of the course to retrieve.
        db (Session): The database session.

    Returns:
        CourseResponse: The details of the requested course.

    Raises:
        HTTPException: If the course is not found.
    """
    course = db.query(Course).filter(Course.id == course_id).first()
    if not course:
        raise HTTPException(status_code=404, detail="Course not found")
    
    return course

@router.get("/courses", response_model=list[CourseResponse])
async def get_courses(db: Session = Depends(get_db)):
    """
    Retrieve a list of all courses.
    
    Args:
        db (Session): The database session.

    Returns:
        List[CourseResponse]: A list of all courses.
    """
    courses = db.query(Course).all()
    return courses