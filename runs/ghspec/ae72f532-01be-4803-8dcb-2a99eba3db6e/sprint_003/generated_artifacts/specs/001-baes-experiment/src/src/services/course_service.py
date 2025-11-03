```python
# src/services/course_service.py

from typing import List, Dict, Optional
from fastapi import HTTPException
from src.models.course import Course  # Assuming you will implement this model
from src.dal.course_dal import CourseDAL  # Data access layer for Course

class CourseService:
    """Service for managing Course entities."""

    def __init__(self):
        self.course_dal = CourseDAL()

    def create_course(self, name: str, level: str) -> Dict[str, str]:
        """Create a new course with the given name and level.

        Args:
            name (str): The name of the course.
            level (str): The level of the course.

        Returns:
            Dict[str, str]: A dictionary containing the created course's ID, name, and level.

        Raises:
            HTTPException: If name or level is missing.
        """
        # Validate input
        if not name:
            raise HTTPException(status_code=400, detail={"code": "E001", "message": "Course name is required"})
        if not level:
            raise HTTPException(status_code=400, detail={"code": "E002", "message": "Course level is required"})

        # Create the course in DAL (data access layer)
        course_id = self.course_dal.create_course(name, level)
        return {"id": course_id, "name": name, "level": level}

    def get_all_courses(self) -> List[Dict[str, str]]:
        """Retrieve all courses from the database.

        Returns:
            List[Dict[str, str]]: A list of courses with their names and levels.
        """
        courses = self.course_dal.get_all_courses()
        return [{"id": course.id, "name": course.name, "level": course.level} for course in courses]

# You can extend this class with more methods as needed for update, delete, etc.
```