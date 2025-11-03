```python
from flask import Blueprint, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from src.services.course_service import create_course, get_all_courses, update_course_level

# Create a blueprint for course API
course_api = Blueprint('course_api', __name__)

@course_api.route('/courses', methods=['POST'])
def api_create_course():
    """
    Create a new Course.
    
    Request Body:
        - name (string): The name of the Course.
        - level (string): The level of the Course.
        
    Response:
        - 201 Created with JSON representation of the created Course.
    """
    data = request.get_json()
    
    # Validate the request body
    if not data or 'name' not in data or 'level' not in data:
        return jsonify({"error": {"code": "E001", "message": "Invalid input. 'name' and 'level' are required."}}), 400
    
    # Call the service to create course
    course = create_course(data['name'], data['level'])
    
    return jsonify(course), 201


@course_api.route('/courses', methods=['GET'])
def api_get_all_courses():
    """
    Retrieve all Courses.
    
    Response:
        - 200 OK with JSON array of Course objects including name and level.
    """
    courses = get_all_courses()
    return jsonify(courses), 200


@course_api.route('/courses/<int:id>', methods=['PUT'])
def api_update_course_level(id):
    """
    Update an existing Course's level.
    
    Request Body:
        - level (string): The new level of the Course.
        
    Response:
        - 200 OK with JSON representation of the updated Course.
    """
    data = request.get_json()
    
    # Validate the request body
    if not data or 'level' not in data:
        return jsonify({"error": {"code": "E001", "message": "Invalid input. 'level' is required."}}), 400
    
    # Call the service to update course level
    updated_course = update_course_level(id, data['level'])
    
    return jsonify(updated_course), 200
```