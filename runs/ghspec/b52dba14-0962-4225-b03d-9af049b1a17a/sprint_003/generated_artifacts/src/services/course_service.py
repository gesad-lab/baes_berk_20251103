```python
# src/services/course_service.py

from src.models.course_model import Course  # Import the Course model for database interactions
from typing import List, Dict, Any, Optional

class CourseService:
    """Service to manage Course entities in the application."""

    @staticmethod
    def create_course(name: str, level: str) -> Dict[str, Any]:
        """Create a new course with the given name and level.

        Args:
            name (str): The name of the course.
            level (str): The level of the course.

        Returns:
            Dict[str, Any]: A dictionary containing the created course details.
        """
        # Validate input
        if not name or not level:
            raise ValueError("Both 'name' and 'level' are required to create a course.")

        course = Course(name=name, level=level)  # Instantiate the Course model
        course.save()  # Save the course to the database (assuming save method exists)
        
        return {
            "message": "Course created successfully",
            "course": {
                "id": course.id,
                "name": course.name,
                "level": course.level
            }
        }

    @staticmethod
    def get_course(course_id: int) -> Optional[Dict[str, Any]]:
        """Retrieve a course by its ID.

        Args:
            course_id (int): The ID of the course to retrieve.

        Returns:
            Optional[Dict[str, Any]]: A dictionary containing course details or None if not found.
        """
        course = Course.get_by_id(course_id)  # Assuming method exists to fetch by ID
        if course is None:
            return None  # Course not found
        
        return {
            "id": course.id,
            "name": course.name,
            "level": course.level
        }

    @staticmethod
    def update_course(course_id: int, name: str, level: str) -> Dict[str, Any]:
        """Update an existing course with new name and level.

        Args:
            course_id (int): The ID of the course to update.
            name (str): The new name of the course.
            level (str): The new level of the course.

        Returns:
            Dict[str, Any]: A dictionary containing updated course details.
        """
        course = Course.get_by_id(course_id)  # Assuming method exists
        if not course:
            raise ValueError(f"Course with ID {course_id} does not exist.")

        # Update fields
        course.name = name
        course.level = level
        course.save()  # Save the updated course
        
        return {
            "message": "Course updated successfully",
            "course": {
                "id": course.id,
                "name": course.name,
                "level": course.level
            }
        }
```