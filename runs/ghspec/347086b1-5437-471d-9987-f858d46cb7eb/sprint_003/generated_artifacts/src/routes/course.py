```python
# src/routes/course.py

from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from models.course import Course  # Import the Course model
from database import SessionLocal  # Import the database session
from validators import validate_course_creation  # Import the validation function

router = APIRouter()

# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/courses", response_model=Course, status_code=201)
def create_course(course: Course, db: Session = Depends(get_db)):
    """
    Create a new Course entry in the database.

    :param course: Course instance containing name and level.
    :param db: Database session.
    :return: The created Course details.
    :raises HTTPException: If required fields are missing.
    """
    # Validate the course creation input
    if not course.name or not course.level:
        raise HTTPException(status_code=400, detail="Both 'name' and 'level' are required.")

    db.add(course)
    db.commit()
    db.refresh(course)
    return course

@router.get("/courses", response_model=list[Course], status_code=200)
def retrieve_courses(db: Session = Depends(get_db)):
    """
    Retrieve all Courses from the database.

    :param db: Database session.
    :return: A list of Courses.
    """
    courses = db.query(Course).all()
    return courses
```