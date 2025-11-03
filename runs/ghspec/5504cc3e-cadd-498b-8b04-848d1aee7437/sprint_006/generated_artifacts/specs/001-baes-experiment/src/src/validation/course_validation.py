```python
# src/validation/course_validation.py

from src.models.course import Course  # Importing Course model
from src.models.teacher import Teacher  # Importing Teacher model
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def get_course_with_teacher(course_id: int) -> dict:
    """Retrieve a course along with its associated teacher details.

    Args:
        course_id (int): The ID of the course to retrieve.

    Returns:
        dict: A dictionary containing course details and associated teacher information, or an error message if not found.

    Raises:
        ValueError: If course_id is not a positive integer.
    """

    if not isinstance(course_id, int) or course_id <= 0:
        raise ValueError("Invalid course_id: must be a positive integer.")

    # Query to find the course and join with teacher information
    course = db.session.query(Course).filter(Course.id == course_id).outerjoin(Teacher).one_or_none()

    if course is None:
        return {"error": {"code": "E404", "message": "Course not found."}}

    # Prepare the response to include course and teacher details
    response = {
        "course_id": course.id,
        "course_name": course.name,
        "teacher": {
            "id": course.teacher.id if course.teacher else None,
            "name": course.teacher.name if course.teacher else None
        }
    }

    return response
```