```python
# src/services.py

from src.models import Course  # Import the Course model
from src.database import get_db_session  # Import the database session handler
from flask import abort

def create_course(name: str, level: str) -> Course:
    """
    Create a new course in the database.

    Parameters:
    - name (str): The name of the course.
    - level (str): The level of the course (e.g., beginner, intermediate, advanced).

    Returns:
    - Course: The created course instance.

    Raises:
    - ValueError: If name or level are not provided or are invalid.
    """
    if not name or not level:
        raise ValueError("Both 'name' and 'level' are required fields.")

    with get_db_session() as session:
        course = Course(name=name, level=level)  # Create a new course instance
        session.add(course)  # Add course to the session
        session.commit()  # Commit the transaction to save course
        return course

def get_course_by_id(course_id: int) -> Course:
    """
    Retrieve a course by its ID.

    Parameters:
    - course_id (int): The ID of the course to retrieve.

    Returns:
    - Course: The course instance with the specified ID.

    Raises:
    - NotFound: If no course is found with the provided ID.
    """
    with get_db_session() as session:
        course = session.query(Course).get(course_id)  # Query for the course by ID
        if course is None:  # Check if course exists
            abort(404, description="Course not found.")  # 404 if not found
        return course
```