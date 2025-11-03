```python
# src/api/courses.py
import json
from flask import Blueprint, request, jsonify
from app.models import Course
from app import db

courses_bp = Blueprint('courses', __name__)

@courses_bp.route('/courses', methods=['POST'])
def create_course():
    """Create a new course.

    Args:
        name (str): The name of the course. Must not be empty.
        level (str): The level of the course. Must not be empty.

    Returns:
        JSON response with the created course details and a HTTP 201 status code on success.
        HTTP 400 status code with error details if validation fails.
    """
    data = request.json
    name = data.get('name')
    level = data.get('level')

    if not name or not level:
        return jsonify({'error': {'code': 'E001', 'message': 'Name and level are required.'}}), 400

    new_course = Course(name=name, level=level)
    db.session.add(new_course)
    db.session.commit()

    return jsonify({'id': new_course.id, 'name': new_course.name, 'level': new_course.level}), 201

@courses_bp.route('/courses', methods=['GET'])
def list_courses():
    """Retrieve a list of all courses.

    Returns:
        JSON response containing an array of course records, each including name and level.
        HTTP 200 status code on success.
    """
    courses = Course.query.all()
    return jsonify([{'id': course.id, 'name': course.name, 'level': course.level} for course in courses]), 200

@courses_bp.route('/courses/<int:course_id>', methods=['PUT'])
def update_course(course_id):
    """Update an existing course by ID.

    Args:
        course_id (int): The ID of the course to update.
        name (str, optional): The new name of the course. If provided, must not be empty.
        level (str, optional): The new level of the course. If provided, must not be empty.

    Returns:
        JSON response with the updated course details and HTTP 200 status code on success.
        HTTP 404 status code if the course is not found, or HTTP 400 for validation errors.
    """
    data = request.json
    course = Course.query.get(course_id)

    if course is None:
        return jsonify({'error': {'code': 'E002', 'message': 'Course not found.'}}), 404
    
    if 'name' in data and not data['name']:
        return jsonify({'error': {'code': 'E001', 'message': 'Name cannot be empty.'}}), 400
    
    if 'level' in data and not data['level']:
        return jsonify({'error': {'code': 'E001', 'message': 'Level cannot be empty.'}}), 400

    course.name = data.get('name', course.name)
    course.level = data.get('level', course.level)

    db.session.commit()

    return jsonify({'id': course.id, 'name': course.name, 'level': course.level}), 200
```