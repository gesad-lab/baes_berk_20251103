```python
# File: src/repositories/course_repository.py

from typing import Optional, List
from sqlalchemy.orm import Session
from src.models.course import Course
from src.database import get_db  # Assuming there's a get_db function for database sessions

class CourseRepository:
    """Repository for managing Course entities in the database."""
    
    def __init__(self, db: Session):
        self.db = db

    def create_course(self, name: str, level: str) -> Course:
        """
        Create a new course in the database.
        
        Parameters:
            name (str): The name of the course.
            level (str): The level of the course.

        Returns:
            Course: The created Course instance.
        
        Raises:
            ValueError: If the name or level is invalid.
        """
        if not name or not level:
            raise ValueError("Both name and level must be provided.")

        new_course = Course(name=name, level=level)
        self.db.add(new_course)
        self.db.commit()
        self.db.refresh(new_course)  # Refresh to get the new id and other defaults
        return new_course

    def get_course(self, course_id: int) -> Optional[Course]:
        """
        Retrieve a course by its ID.

        Parameters:
            course_id (int): The ID of the course to retrieve.

        Returns:
            Course: The retrieved Course instance or None if not found.
        """
        return self.db.query(Course).filter(Course.id == course_id).first()

    def list_courses(self) -> List[Course]:
        """
        List all courses in the database.

        Returns:
            List[Course]: A list of Course instances.
        """
        return self.db.query(Course).all()
```
