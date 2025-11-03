```python
# src/services/course_service.py

from sqlalchemy.orm import Session
from src.models import Course  # Ensure the Course model is imported
from fastapi import HTTPException

class CourseService:
    """Service class for managing Course entities."""

    def __init__(self, db: Session):
        self.db = db  # Database session for interacting with Course models

    def create_course(self, name: str, level: str) -> Course:
        """
        Create a new course.
        
        Args:
            name (str): The name of the course.
            level (str): The level of the course.

        Returns:
            Course: The created course instance.

        Raises:
            HTTPException: If required fields are missing.
        """
        # Validate the input fields
        if not name:
            raise HTTPException(status_code=400, detail="E001: Name field is required.")
        if not level:
            raise HTTPException(status_code=400, detail="E002: Level field is required.")

        # Create a new Course instance
        course = Course(name=name, level=level)

        # Add the course to the database and commit the transaction
        self.db.add(course)
        self.db.commit()
        self.db.refresh(course)  # Refresh to get updated data including generated fields

        return course

    def get_course(self, course_id: int) -> Course:
        """
        Retrieve a course by its ID.

        Args:
            course_id (int): The ID of the course.

        Returns:
            Course: The course instance if found.

        Raises:
            HTTPException: If the course is not found.
        """
        course = self.db.query(Course).filter(Course.id == course_id).first()
        if not course:
            raise HTTPException(status_code=404, detail="E003: Course not found.")
        
        return course
```