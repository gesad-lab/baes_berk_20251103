```python
# services/course_service.py
from sqlalchemy.exc import IntegrityError
from typing import List, Dict, Any
from models.course import Course
from models.database import db  # Assuming db is your SQLAlchemy instance

def create_course(name: str, level: str) -> Course:
    """Create a new course entity in the database.

    Args:
        name (str): The name of the course.
        level (str): The level of the course.

    Returns:
        Course: The created Course object.

    Raises:
        ValueError: If the course name or level is empty.
    """
    if not name:
        raise ValueError("Course name is required.")
    if not level:
        raise ValueError("Course level is required.")

    new_course = Course(name=name, level=level)
    db.session.add(new_course)
    try:
        db.session.commit()
    except IntegrityError:
        db.session.rollback()
        raise ValueError("An error occurred while creating the course.")

    return new_course

def get_all_courses() -> List[Dict[str, Any]]:
    """Retrieve all courses from the database.

    Returns:
        List[Dict[str, Any]]: A list of dictionaries containing course details.
    """
    courses = Course.query.all()
    return [{"id": course.id, "name": course.name, "level": course.level} for course in courses]
```