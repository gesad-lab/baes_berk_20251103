```python
# src/services/course_service.py

from src.models import Course  # Import the Course model for database operations
from flask import jsonify, request
from sqlalchemy.exc import IntegrityError

def create_course(name: str, level: str) -> dict:
    """Creates a new course with the specified name and level.

    Args:
        name (str): The name of the course.
        level (str): The level of the course.

    Returns:
        dict: The created course's details including ID, name, and level.
    
    Raises:
        ValueError: If required fields are missing or invalid.
    """
    if not name or not level:
        raise ValueError("Both name and level are required to create a course.")

    new_course = Course(name=name, level=level)  # Create a course instance
    
    try:
        # Persist the new course to the database
        new_course.save()
    except IntegrityError:
        # Handle errors related to unique constraints or other database issues
        raise ValueError("An error occurred while creating the course. Please try again.")
    
    return {
        "id": new_course.id,
        "name": new_course.name,
        "level": new_course.level
    }

def get_course_by_id(course_id: int) -> dict:
    """Retrieves details of a course by its unique identifier.

    Args:
        course_id (int): The unique identifier for the course.

    Returns:
        dict: The course details, including name and level.

    Raises:
        ValueError: If the course is not found.
    """
    course = Course.query.get(course_id)  # Fetch the course instance from the database
    
    if not course:
        raise ValueError("Course not found.")
    
    return {
        "id": course.id,
        "name": course.name,
        "level": course.level
    }
```