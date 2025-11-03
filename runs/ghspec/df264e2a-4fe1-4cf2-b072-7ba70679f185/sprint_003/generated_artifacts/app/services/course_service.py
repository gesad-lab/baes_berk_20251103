```python
# app/api/course.py

from flask import Blueprint, request, jsonify
from app.services.course_service import CourseService
from app.models.course import Course  # Assuming there's a Course model to interact with the database

course_bp = Blueprint("course", __name__)
course_service = CourseService()

@course_bp.route("/courses/<int:id>", methods=["GET"])
def get_course(id):
    """
    Retrieve course details by ID.

    Args:
        id (int): The unique identifier of the course.

    Returns:
        JSON response with course details or a 404 error if not found.
    """
    try:
        course = course_service.get_course_by_id(id)
        if course:
            return jsonify(course), 200
        else:
            return jsonify({"error": {"code": "E404", "message": "Course not found."}}), 404
    except Exception as e:
        # Log the exception for debugging purposes
        print(f"Error retrieving course: {e}")  # Replace with proper logging
        return jsonify({"error": {"code": "E500", "message": "Internal server error."}}), 500
```