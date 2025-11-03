```python
# src/services.py

from flask import jsonify
from src.models import Course  # Assuming Course model is defined in models.py
from src.database import db  # Importing the database instance


class CourseService:
    """Service for managing course-related operations."""

    @staticmethod
    def create_course(name: str, level: str) -> dict:
        """
        Create a new course with the provided name and level.

        Args:
            name (str): The name of the course.
            level (str): The level of the course.

        Returns:
            dict: The created course data or an error response.

        Raises:
            ValueError: If name or level is missing.
        """
        # Validate input
        if not name or not level:
            error_response = {
                "error": {
                    "code": "E001",
                    "message": "Name and level are required."
                }
            }
            return jsonify(error_response), 400  # Return a 400 Bad Request response

        # Create and save the new course
        new_course = Course(name=name, level=level)
        db.session.add(new_course)
        db.session.commit()

        # Prepare the successful response
        response_data = {
            "id": new_course.id,
            "name": new_course.name,
            "level": new_course.level
        }
        return jsonify(response_data), 201  # Return a 201 Created response

    @staticmethod
    def get_course_by_id(course_id: int) -> dict:
        """
        Retrieve a course by its ID.

        Args:
            course_id (int): The unique identifier of the course.

        Returns:
            dict: The course data or an error response.
        """
        course = Course.query.get(course_id)
        if not course:
            error_response = {
                "error": {
                    "code": "E002",
                    "message": "Course not found."
                }
            }
            return jsonify(error_response), 404  # Return a 404 Not Found response

        # Prepare the successful response
        response_data = {
            "id": course.id,
            "name": course.name,
            "level": course.level
        }
        return jsonify(response_data), 200  # Return a 200 OK response
```