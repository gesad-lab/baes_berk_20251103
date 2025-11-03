```python
from flask import Blueprint, jsonify
from flask_sqlalchemy import SQLAlchemy

# Set up the database instance (assumes it is already created in app)
db = SQLAlchemy()

# Define Course model
class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)  # Required field
    level = db.Column(db.String, nullable=False)  # Required field

# Create a blueprint for the courses API
courses_bp = Blueprint('courses', __name__)

@courses_bp.route('/courses', methods=['GET'])
def get_courses():
    """
    Retrieve all course records.

    Returns:
        JSON response with a list of courses including id, name, and level.
    """
    try:
        # Query all courses from the database
        courses = Course.query.all()

        # Transform course data into a list of dictionaries
        course_list = [{
            'id': course.id,
            'name': course.name,
            'level': course.level
        } for course in courses]

        # Return the course list as a JSON response
        return jsonify(course_list), 200  # 200 OK
    except Exception as e:
        # Log the exception for debugging (avoid logging sensitive data)
        print(f"Error retrieving courses: {str(e)}")
        return jsonify({"error": {"code": "E500", "message": "Internal Server Error"}}), 500  # 500 Internal Server Error
```