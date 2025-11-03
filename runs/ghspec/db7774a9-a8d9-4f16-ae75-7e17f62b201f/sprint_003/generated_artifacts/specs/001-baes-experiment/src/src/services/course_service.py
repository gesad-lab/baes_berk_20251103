```python
# src/services/course_service.py

from typing import List, Optional
from fastapi import HTTPException
from src.models.course import Course  # Assuming the Course model is defined in models/course.py
from src.schemas.course import CourseCreate, CourseOut  # Assuming relevant schemas are defined in schemas/course.py
from src.database.database import Database  # Assuming a Database class exists for data operations

class CourseService:
    """Service logic for managing courses."""

    def __init__(self, db: Database):
        self.db = db

    def create_course(self, course_data: CourseCreate) -> CourseOut:
        """Create a new course using the provided data.

        Args:
            course_data (CourseCreate): The data needed to create a new course.

        Returns:
            CourseOut: The created course object including an ID.

        Raises:
            HTTPException: If name or level is missing from the course data.
        """
        if not course_data.name or not course_data.level:
            raise HTTPException(
                status_code=422,
                detail="Course name and level must be provided."
            )

        # Create a course instance and save it in the database
        new_course = Course(name=course_data.name, level=course_data.level)
        self.db.add(new_course)
        
        # Return the created course object
        return CourseOut.from_orm(new_course)

    def get_course(self, course_id: int) -> Optional[CourseOut]:
        """Retrieve a course by its ID.

        Args:
            course_id (int): The ID of the course to retrieve.

        Returns:
            Optional[CourseOut]: The retrieved course object or None if not found.
        """
        course = self.db.get_by_id(Course, course_id)
        if course is None:
            raise HTTPException(status_code=404, detail="Course not found.")
        
        return CourseOut.from_orm(course)

    def list_courses(self) -> List[CourseOut]:
        """List all courses.

        Returns:
            List[CourseOut]: A list of all course objects.
        """
        courses = self.db.get_all(Course)
        return [CourseOut.from_orm(course) for course in courses]
```