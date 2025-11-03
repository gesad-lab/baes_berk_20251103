```python
from flask import Blueprint, request, jsonify
from app.models import Course  # Importing the Course model
from app import db

courses_bp = Blueprint('courses', __name__)

@courses_bp.route('/courses', methods=['POST'])
def create_course():
    data = request.get_json()
    # Validate that 'name' and 'level' are present in the request
    if not data or not data.get('name') or not data.get('level'):
        error_message = {}
        if not data or not data.get('name'):
            error_message["name"] = "Name is required."
        if not data or not data.get('level'):
            error_message["level"] = "Level is required."
        
        return jsonify({"error": {"code": "E001", "message": "Validation error", "details": error_message}}), 400
    
    course = Course(name=data['name'], level=data['level'])
    db.session.add(course)
    db.session.commit()
    return jsonify({"id": course.id, "name": course.name, "level": course.level}), 201

@courses_bp.route('/courses', methods=['GET'])
def get_courses():
    courses = Course.query.all()
    return jsonify([{"id": course.id, "name": course.name, "level": course.level} for course in courses]), 200
```