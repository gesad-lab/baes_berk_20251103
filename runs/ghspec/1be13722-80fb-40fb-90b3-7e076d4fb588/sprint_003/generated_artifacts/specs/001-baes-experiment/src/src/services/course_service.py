```python
# src/services/course_service.py

from models.course import Course  # Importing the Course model
from sqlalchemy.orm import Session
from fastapi import HTTPException

class CourseService:
    """Service for managing course-related operations."""

    @staticmethod
    def create_course(db: Session, course_data: dict) -> Course:
        """
        Create a new course in the database.

        Args:
            db (Session): The database session.
            course_data (dict): A dictionary containing course attributes.

        Returns:
            Course: The created Course object.

        Raises:
            HTTPException: If the course data is invalid or cannot be saved.
        """
        # Validate required fields
        if 'name' not in course_data or not course_data['name']:
            raise HTTPException(status_code=400, detail="E001: Course name is required")
        if 'level' not in course_data or not course_data['level']:
            raise HTTPException(status_code=400, detail="E002: Course level is required")

        # Create a new course instance
        new_course = Course(name=course_data['name'], level=course_data['level'])

        # Add and commit the course to the session
        db.add(new_course)
        try:
            db.commit()
            db.refresh(new_course)  # Refresh to get the updated instance
        except Exception as e:
            db.rollback()  # Rollback in case of error
            raise HTTPException(status_code=500, detail=str(e))  # Raise HTTP exception if save fails
        
        return new_course

    @staticmethod
    def get_courses(db: Session) -> list:
        """
        Retrieve all courses from the database.

        Args:
            db (Session): The database session.

        Returns:
            list: A list of Course objects.
        """
        return db.query(Course).all()  # Query to get all courses
```