```python
from fastapi import APIRouter, HTTPException
from sqlalchemy.orm import Session
from db_setup import SessionLocal
from models import CourseCreate, CourseResponse, Course  # Ensure Course model and schemas are imported

router = APIRouter()

@router.post("/courses", response_model=CourseResponse, status_code=201)
def create_course(course: CourseCreate):
    """
    Create a new course with the provided details.

    Args:
        course (CourseCreate): Course details containing name and level.

    Returns:
        CourseResponse: The newly created course including its ID.
    """
    session: Session = SessionLocal()
    new_course = Course(name=course.name, level=course.level)
    
    # Add the new course to the session and commit the transaction
    session.add(new_course)
    session.commit()
    session.refresh(new_course)  # Refresh the instance with the new data from the DB
    session.close()  # Ensure to close the session to release resources
    
    return new_course

@router.get("/courses/{id}", response_model=CourseResponse)
def get_course(id: int):
    """
    Retrieve a course by its ID.

    Args:
        id (int): The ID of the course to retrieve.

    Returns:
        CourseResponse: The requested course details.
    
    Raises:
        HTTPException: If the course is not found.
    """
    session: Session = SessionLocal()
    course = session.query(Course).filter(Course.id == id).first()
    session.close()
    
    if course is None:
        raise HTTPException(status_code=404, detail="Course not found")
    
    return course

@router.put("/courses/{id}", response_model=CourseResponse)
def update_course(id: int, course: CourseCreate):
    """
    Update an existing course's details.

    Args:
        id (int): The ID of the course to update.
        course (CourseCreate): The new details for the course.

    Returns:
        CourseResponse: The updated course details.

    Raises:
        HTTPException: If the course is not found.
    """
    session: Session = SessionLocal()
    existing_course = session.query(Course).filter(Course.id == id).first()
    
    if existing_course is None:
        session.close()
        raise HTTPException(status_code=404, detail="Course not found")
    
    # Update course details
    existing_course.name = course.name
    existing_course.level = course.level
    session.commit()
    session.refresh(existing_course)
    session.close()
    
    return existing_course
```