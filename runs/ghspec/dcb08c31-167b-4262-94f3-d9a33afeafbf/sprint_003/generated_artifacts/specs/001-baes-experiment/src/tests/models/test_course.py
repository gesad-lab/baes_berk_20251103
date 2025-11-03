```python
from flask import Blueprint, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from models.course import Course  # Assuming Course model is defined in models.course

# Initialize the blueprint for course routes
course_bp = Blueprint('course', __name__)

# Initialize SQLAlchemy
db = SQLAlchemy()

@course_bp.route('/courses', methods=['GET'])
def get_courses():
    """
    Retrieve all courses from the database.
    
    Returns:
        JSON response containing a list of courses with name and level.
    """
    try:
        # Query all courses
        courses = Course.query.all()
        
        # Format response
        course_list = [{"name": course.name, "level": course.level} for course in courses]
        
        return jsonify(course_list), 200
    except Exception as e:
        # Log the error and return a 500 status with error message
        app.logger.error(f"Error retrieving courses: {e}")
        return jsonify({"error": {"code": "E500", "message": "Internal server error"}}), 500
```