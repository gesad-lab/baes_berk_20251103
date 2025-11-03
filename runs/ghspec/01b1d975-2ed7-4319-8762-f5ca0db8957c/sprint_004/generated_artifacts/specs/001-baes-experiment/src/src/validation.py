```python
# src/validation.py

from werkzeug.exceptions import BadRequest
from src.models import db, Course

def validate_course_exists(course_id: int) -> None:
    """Validate that a course exists in the database.

    Args:
        course_id (int): The ID of the course to validate.

    Raises:
        BadRequest: If the course ID is not found in the database.
    """
    # Check if the Course with the given ID exists
    course = db.session.query(Course).filter(Course.id == course_id).first()
    if course is None:
        # Raise an error if the Course does not exist
        raise BadRequest(f"E001: Course with ID {course_id} does not exist.")
```