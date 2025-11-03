```python
from flask import Blueprint, jsonify, request
from src.models.course import Course
from src import db

course_routes = Blueprint('course_routes', __name__)

@course_routes.route('/courses', methods=['POST'])
def create_course():
    """
    Create a new course with the provided name and level.
    
    Request Format:
    {
        "name": "Course Name",
        "level": "Course Level"
    }
    
    Returns:
    - 201 Created with course details if successful.
    - 400 Bad Request if validation fails.
    """
    data = request.json

    # Validate required fields
    name = data.get('name')
    level = data.get('level')
    
    if not name or not level:
        return jsonify({"error": {"code": "E002", "message": "Name and level are required"}}), 400
    
    # Additional validation for level (example: restricting to specific values)
    valid_levels = ["beginner", "intermediate", "advanced"]  # Define valid levels as per requirement
    if level not in valid_levels:
        return jsonify({"error": {"code": "E003", "message": f"Invalid level provided. Must be one of {valid_levels}"}}), 400

    # Create a new course object and save to the database
    try:
        new_course = Course(name=name, level=level)
        db.session.add(new_course)
        db.session.commit()
        return jsonify({"id": new_course.id, "name": new_course.name, "level": new_course.level}), 201
    except IntegrityError:
        db.session.rollback()
        return jsonify({"error": {"code": "E004", "message": "Database integrity error occurred."}}), 500
```