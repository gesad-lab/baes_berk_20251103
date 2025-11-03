```python
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session
from src.database import Base

Base = declarative_base()

class Course(Base):
    """Course model representing the courses in the system."""
    
    __tablename__ = 'courses'
    
    id = Column(Integer, primary_key=True, index=True)  # Unique identifier for the course
    name = Column(String, nullable=False)  # Name of the course
    level = Column(String, nullable=False)  # Level of the course (e.g., beginner, intermediate, etc.)

    def __repr__(self):
        """String representation of the Course instance for debugging."""
        return f"<Course(id={self.id}, name='{self.name}', level='{self.level}')>"

def create_course(db: Session, name: str, level: str):
    """Create a new course in the database.

    Args:
        db: Database session for making changes.
        name: Name of the course.
        level: Level of the course.

    Returns:
        The created Course instance if successful.
    
    Raises:
        ValueError: If name or level is invalid (empty).
    """
    if not name or not level:
        raise ValueError("Both name and level fields are required.")

    course = Course(name=name, level=level)
    db.add(course)  # Add new course to the session
    db.commit()     # Commit session to save changes
    db.refresh(course)  # Refresh to get the newly created course data
    return course  # Return the created course object
```