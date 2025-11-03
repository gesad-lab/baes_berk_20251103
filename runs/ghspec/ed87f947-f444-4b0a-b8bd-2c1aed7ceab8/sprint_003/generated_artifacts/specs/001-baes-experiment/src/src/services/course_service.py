```python
# src/services/course_service.py

from typing import List, Optional
from fastapi import HTTPException
from sqlalchemy.orm import Session
from .models import Course  # Assuming you have a Course model defined in src/models.py

class CourseService:
    """Service class to handle business logic related to Course entities."""

    @staticmethod
    def create_course(db: Session, name: str, level: str) -> Course:
        """Create a new Course entity in the database.

        Args:
            db (Session): Database session.
            name (str): The name of the course.
            level (str): The level of the course.

        Returns:
            Course: The created course instance.
        
        Raises:
            HTTPException: If course creation fails due to validation errors.
        """
        if not name or not level:
            raise HTTPException(status_code=400, detail="E001: Missing name or level")

        # Create a new course instance
        course = Course(name=name, level=level)
        db.add(course)
        db.commit()
        db.refresh(course)

        return course

    @staticmethod
    def get_course(db: Session, course_id: int) -> Optional[Course]:
        """Retrieve an existing Course by its ID.

        Args:
            db (Session): Database session.
            course_id (int): The ID of the course to retrieve.

        Returns:
            Optional[Course]: The course instance if found, else None.
        
        Raises:
            HTTPException: If course does not exist.
        """
        course = db.query(Course).filter(Course.id == course_id).first()
        if not course:
            raise HTTPException(status_code=404, detail="E002: Course not found")
        return course

    @staticmethod
    def update_course(db: Session, course_id: int, name: Optional[str], level: Optional[str]) -> Course:
        """Update an existing Course's name and/or level.

        Args:
            db (Session): Database session.
            course_id (int): The ID of the course to update.
            name (Optional[str]): New name for the course (if any).
            level (Optional[str]): New level for the course (if any).

        Returns:
            Course: The updated course instance.

        Raises:
            HTTPException: If course does not exist or validation fails.
        """
        course = db.query(Course).filter(Course.id == course_id).first()
        if not course:
            raise HTTPException(status_code=404, detail="E002: Course not found")

        if name is not None:
            course.name = name
        if level is not None:
            course.level = level

        db.commit()
        db.refresh(course)
        return course

    @staticmethod
    def get_all_courses(db: Session) -> List[Course]:
        """Retrieve all Course entities.

        Args:
            db (Session): Database session.

        Returns:
            List[Course]: A list of all courses.
        """
        return db.query(Course).all()
```