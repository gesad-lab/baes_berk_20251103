```python
from typing import List, Optional
from sqlalchemy.orm import Session
from src.models.course import Course  # Assuming the Course model exists in this path
from src.database import get_db  # Assuming a function exists to get the DB session

def create_course(db: Session, name: str, level: str) -> Course:
    """Create a new course in the database.
    
    Args:
        db (Session): The database session.
        name (str): The name of the course.
        level (str): The level of the course.

    Returns:
        Course: The created course.
    """
    course = Course(name=name, level=level)
    db.add(course)
    db.commit()
    db.refresh(course)
    return course

def get_course(db: Session, course_id: int) -> Optional[Course]:
    """Retrieve a course from the database using its ID.
    
    Args:
        db (Session): The database session.
        course_id (int): The ID of the course to retrieve.

    Returns:
        Course: The retrieved course, or None if not found.
    """
    return db.query(Course).filter(Course.id == course_id).first()

def update_course(db: Session, course_id: int, name: Optional[str] = None, level: Optional[str] = None) -> Optional[Course]:
    """Update an existing course's details.
    
    Args:
        db (Session): The database session.
        course_id (int): The ID of the course to update.
        name (Optional[str]): The new name of the course.
        level (Optional[str]): The new level of the course.

    Returns:
        Course: The updated course, or None if not found.
    """
    course = get_course(db, course_id)
    
    if course:
        if name is not None:
            course.name = name
        if level is not None:
            course.level = level
            
        db.commit()
        db.refresh(course)
        return course
    
    return None

def list_courses(db: Session) -> List[Course]:
    """Retrieve a list of all courses in the database.
    
    Args:
        db (Session): The database session.

    Returns:
        List[Course]: A list of all courses.
    """
    return db.query(Course).all()
```