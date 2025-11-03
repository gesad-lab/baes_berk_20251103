```python
# src/services/course_service.py

from typing import List, Optional
from sqlalchemy.orm import Session
from src.models.course import Course  # Assuming the Course model is defined in this file
from sqlalchemy.exc import IntegrityError

def create_course(db: Session, name: str, level: str) -> Course:
    """
    Creates a new course in the database.
    
    Parameters:
        db (Session): The SQLAlchemy database session.
        name (str): The name of the course.
        level (str): The level of the course.
        
    Returns:
        Course: The created Course object.
    
    Raises:
        ValueError: If required fields are missing.
    """
    if not name or not level:
        raise ValueError("Both name and level must be provided to create a course.")
    
    new_course = Course(name=name, level=level)
    try:
        db.add(new_course)
        db.commit()
        db.refresh(new_course)
    except IntegrityError as e:
        db.rollback()
        raise ValueError("Error occurred while creating the course.") from e
    
    return new_course


def get_all_courses(db: Session) -> List[Course]:
    """
    Retrieves all courses from the database.
    
    Parameters:
        db (Session): The SQLAlchemy database session.
        
    Returns:
        List[Course]: A list of Course objects.
    """
    return db.query(Course).all()
```