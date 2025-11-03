```python
"""Add Course Entity Migration

This script adds the Course entity to the database, allowing for the creation and retrieval of courses.
"""

from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime
from your_app_name import db  # Adjust according to your application structure

class Course(db.Model):
    """Represents a course in the system."""
    
    __tablename__ = 'courses'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    level = Column(String(50), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def __init__(self, name: str, level: str):
        self.name = name
        self.level = level

def create_course(name: str, level: str) -> Course:
    """Create a new course in the database.

    Args:
        name (str): The name of the course.
        level (str): The level of the course.

    Returns:
        Course: The created Course object.
    
    Raises:
        ValueError: If the course name or level is invalid.
    """
    if not name:
        raise ValueError("Course name cannot be empty.")
    if not level:
        raise ValueError("Course level cannot be empty.")

    new_course = Course(name=name, level=level)
    db.session.add(new_course)
    db.session.commit()
    return new_course

def get_courses() -> list:
    """Retrieve all courses from the database.

    Returns:
        list: A list of Course objects.
    """
    return Course.query.all()
```