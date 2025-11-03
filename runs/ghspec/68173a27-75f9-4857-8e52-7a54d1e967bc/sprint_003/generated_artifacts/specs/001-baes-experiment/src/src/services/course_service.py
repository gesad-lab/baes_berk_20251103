```python
# src/services/course_service.py

from src.models.course import Course  # Import Course model
from src.repositories.course_repository import (
    create_course as save_course,
    get_courses,
)  # Import repository functions
from fastapi import HTTPException

def create_course(course_data: dict) -> Course:
    """Create a new course in the system.

    Args:
        course_data (dict): A dictionary containing course information including
                            title and description.

    Returns:
        Course: The created Course entity.

    Raises:
        HTTPException: If the input validation fails.
    """
    # Validate required fields
    title = course_data.get("title")
    description = course_data.get("description")

    if not title or not description:
        raise HTTPException(
            status_code=400,
            detail="Both title and description are required fields."
        )

    # Create the Course instance
    new_course = Course(title=title, description=description)

    # Save the course using the repository function
    saved_course = save_course(new_course)

    return saved_course

def retrieve_courses() -> list[Course]:
    """Retrieve all courses from the system.

    Returns:
        list[Course]: A list of Course entities.
    """
    return get_courses()
```