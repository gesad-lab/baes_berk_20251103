```python
from flask import current_app
from src.models.course import Course  # Import the Course model
from src import db  # Import the SQLAlchemy instance

def create_course(name: str, level: str):
    """
    Create a new course with the specified name and level.

    :param name: The name of the course.
    :param level: The level of the course.
    :return: The created Course object.
    :raises ValueError: If name or level is empty.
    """
    if not name or not level:
        raise ValueError("Both 'name' and 'level' must be provided.")
    
    new_course = Course(name=name, level=level)
    
    try:
        db.session.add(new_course)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        current_app.logger.error(f"Failed to create course: {e}")
        raise
    
    return new_course

def get_all_courses():
    """
    Retrieve all courses from the database.

    :return: List of Course objects.
    """
    try:
        courses = Course.query.all()
    except Exception as e:
        current_app.logger.error(f"Failed to retrieve courses: {e}")
        return []  # Return an empty list in case of failure
    
    return courses
```