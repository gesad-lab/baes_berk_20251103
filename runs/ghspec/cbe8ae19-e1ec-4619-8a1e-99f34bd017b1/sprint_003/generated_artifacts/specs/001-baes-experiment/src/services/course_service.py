```python
# services/course_service.py

from models import db, Course
from werkzeug.exceptions import BadRequest

def create_course(name: str, level: str) -> Course:
    """Create a course record with validated name and level.

    Args:
        name (str): The name of the course.
        level (str): The level of the course (e.g., Beginner, Intermediate).

    Returns:
        Course: The created Course object.
    
    Raises:
        BadRequest: If name or level are invalid.
    """
    # Input validation to ensure name and level are not empty
    if not isinstance(name, str) or not name.strip():
        raise BadRequest('E001: Invalid name format. Name must be a non-empty string.')
    
    if not isinstance(level, str) or not level.strip():
        raise BadRequest('E002: Invalid level format. Level must be a non-empty string.')

    # Create a new course instance
    course = Course(name=name, level=level)
    
    # Add to the database session and commit
    db.session.add(course)
    db.session.commit()
    
    return course

def get_course_by_id(course_id: int) -> Course:
    """Fetch a course record by its ID.

    Args:
        course_id (int): The ID of the course to fetch.

    Returns:
        Course: The Course object if found, else None.
    """
    return Course.query.get(course_id)

def list_courses() -> list[Course]:
    """List all course records.

    Returns:
        list: A list of Course objects.
    """
    return Course.query.all()
```