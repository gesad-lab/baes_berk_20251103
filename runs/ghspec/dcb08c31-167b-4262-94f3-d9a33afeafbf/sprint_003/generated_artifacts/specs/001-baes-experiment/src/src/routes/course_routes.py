```python
import json
from flask import Blueprint, jsonify, request, abort
from flask_sqlalchemy import SQLAlchemy

# Initialize a blueprint for course routes
course_routes = Blueprint('course_routes', __name__)
db = SQLAlchemy()

# Define the Course model
class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    level = db.Column(db.String, nullable=False)

@course_routes.route('/courses', methods=['POST'])
def create_course():
    """
    Create a new course.

    Request JSON body should include:
        - name (str): The name of the course (required)
        - level (str): The level of the course (required)

    Returns:
        - 201: Created course object
        - 400: Validation error
    """
    data = request.get_json()

    # Validate input
    if not data or 'name' not in data or 'level' not in data:
        return jsonify({
            "error": {
                "code": "E001",
                "message": "Validation error. 'name' and 'level' are required fields."
            }
        }), 400
    
    name = data['name']
    level = data['level']

    # Additional validation for empty strings
    if not name.strip() or not level.strip():
        return jsonify({
            "error": {
                "code": "E002",
                "message": "Validation error. 'name' and 'level' cannot be empty."
            }
        }), 400

    # Create new Course instance
    new_course = Course(name=name, level=level)
    db.session.add(new_course)
    db.session.commit()

    # Return the created course
    return jsonify({
        "id": new_course.id,
        "name": new_course.name,
        "level": new_course.level
    }), 201

@course_routes.route('/courses', methods=['GET'])
def get_courses():
    """
    Retrieve a list of all courses.

    Returns:
        - 200: A list of courses including name and level.
    """
    courses = Course.query.all()
    course_list = [{"id": course.id, "name": course.name, "level": course.level} for course in courses]
    
    return jsonify(course_list), 200
```