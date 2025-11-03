```python
from flask import jsonify, request
from src.models import Course
from src.database import db

class CourseService:
    """Service for managing Course-related operations such as creation and retrieval."""

    @staticmethod
    def create_course(course_data):
        """Creates a new course with the provided data.
        
        Args:
            course_data (dict): A dictionary containing 'name' and 'level' of the course.

        Returns:
            tuple: A tuple containing the course data for successful creation, or an error message for failure, along with relevant HTTP status code.
        """
        # Validate required fields
        name = course_data.get('name')
        level = course_data.get('level')

        if not name or not level:
            error_response = {
                "error": {
                    "code": "E001",
                    "message": "Missing required fields: 'name' and 'level' must be provided."
                }
            }
            return jsonify(error_response), 400

        # Create a new course instance
        new_course = Course(name=name, level=level)
        db.session.add(new_course)
        
        try:
            db.session.commit()  # Commit the new course to the database
            return jsonify({"id": new_course.id, "name": new_course.name, "level": new_course.level}), 201
        except Exception as e:  # Handle potential database errors
            db.session.rollback()  # Rollback in case of an error during commit
            error_response = {
                "error": {
                    "code": "E002",
                    "message": "An error occurred while creating the course."
                }
            }
            return jsonify(error_response), 500

    @staticmethod
    def get_course(course_id):
        """Retrieves a course by its ID.
        
        Args:
            course_id (int): The ID of the course to retrieve.

        Returns:
            tuple: A tuple containing the course data for successful retrieval, or an error message for failure, along with relevant HTTP status code.
        """
        course = Course.query.get(course_id)  # Query the database for the course
        
        # Check if the course exists
        if course is None:
            error_response = {
                "error": {
                    "code": "E003",
                    "message": "Course not found."
                }
            }
            return jsonify(error_response), 404

        # If found, return course details
        return jsonify({"id": course.id, "name": course.name, "level": course.level}), 200
```