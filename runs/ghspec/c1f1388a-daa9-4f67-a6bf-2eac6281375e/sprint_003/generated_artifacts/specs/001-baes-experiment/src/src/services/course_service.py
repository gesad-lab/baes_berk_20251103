```python
# src/services/course_service.py

from typing import List, Optional
from sqlalchemy.orm import Session
from src.models.course import Course  # Assuming the Course model is defined here
from src.schemas.course import CourseCreate, CourseResponse  # Importing schemas for input/output
from fastapi import HTTPException, status

class CourseService:
    """Service for managing Course entities."""

    @staticmethod
    def create_course(course_data: CourseCreate, db: Session) -> CourseResponse:
        """Create a new course entity in the database.

        Args:
            course_data (CourseCreate): Schema containing course details.
            db (Session): Database session for transactions.

        Returns:
            CourseResponse: The created course details.

        Raises:
            HTTPException: If the course creation fails (e.g., duplicate name).
        """
        # Check if course with the same name already exists
        existing_course = db.query(Course).filter(Course.name == course_data.name).first()
        if existing_course:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Course with name '{course_data.name}' already exists."
            )
        
        # Create a new Course instance and add it to the session
        new_course = Course(name=course_data.name, level=course_data.level)
        db.add(new_course)
        db.commit()
        db.refresh(new_course)

        return CourseResponse(id=new_course.id, name=new_course.name, level=new_course.level)

    @staticmethod
    def get_courses(db: Session, skip: int = 0, limit: int = 10) -> List[CourseResponse]:
        """Retrieve a list of courses.

        Args:
            db (Session): Database session for transactions.
            skip (int): The number of records to skip for pagination.
            limit (int): The maximum number of records to return.

        Returns:
            List[CourseResponse]: A list of course details.
        """
        courses = db.query(Course).offset(skip).limit(limit).all()
        return [CourseResponse(id=course.id, name=course.name, level=course.level) for course in courses]

    @staticmethod
    def get_course(course_id: int, db: Session) -> Optional[CourseResponse]:
        """Retrieve a specific course by its ID.

        Args:
            course_id (int): The ID of the course to retrieve.
            db (Session): Database session for transactions.

        Returns:
            CourseResponse: The course details if found.

        Raises:
            HTTPException: If the course is not found.
        """
        course = db.query(Course).filter(Course.id == course_id).first()
        if course is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Course with id '{course_id}' not found."
            )
        return CourseResponse(id=course.id, name=course.name, level=course.level)
```