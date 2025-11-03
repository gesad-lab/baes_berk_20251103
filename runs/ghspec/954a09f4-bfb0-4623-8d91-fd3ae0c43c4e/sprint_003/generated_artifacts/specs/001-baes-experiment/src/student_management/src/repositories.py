```python
# src/repositories.py

from typing import Optional
from sqlalchemy.exc import IntegrityError
from src.models import Course
from src.database import db  # Assuming db is the SQLAlchemy instance

class CourseRepository:
    """Repository for managing Course entities in the database."""

    @staticmethod
    def create_course(name: str, level: str) -> Course:
        """Creates a new Course with the given name and level.

        Args:
            name (str): The name of the course.
            level (str): The level of the course.

        Raises:
            ValueError: If name or level is missing.
            IntegrityError: If a database integrity error occurs.

        Returns:
            Course: The created Course entity.
        """
        if not name or not level:
            raise ValueError("Both name and level fields are required.")

        new_course = Course(name=name, level=level)
        db.session.add(new_course)

        try:
            db.session.commit()
        except IntegrityError:
            db.session.rollback()
            raise

        return new_course

    @staticmethod
    def get_course(course_id: int) -> Optional[Course]:
        """Retrieves a Course entity by its ID.

        Args:
            course_id (int): The ID of the course.

        Returns:
            Optional[Course]: The Course entity if found, otherwise None.
        """
        return Course.query.get(course_id)
```