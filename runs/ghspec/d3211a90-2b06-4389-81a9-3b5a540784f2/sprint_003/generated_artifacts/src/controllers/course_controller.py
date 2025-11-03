```python
# src/controllers/course_controller.py

from flask import Blueprint, request, jsonify
from models.course import Course  # Assuming the Course model is in models/course.py
from database import session  # Assuming database session is managed in database.py

courses_bp = Blueprint('courses', __name__)

@courses_bp.route('/courses', methods=['POST'])
def create_course():
    data = request.json
    validate_course_data(data)

    new_course = Course(name=data['name'], level=data['level'])
    session.add(new_course)
    session.commit()

    return jsonify({
        "id": new_course.id,
        "name": new_course.name,
        "level": new_course.level
    }), 201

@courses_bp.route('/courses/<int:id>', methods=['GET'])
def get_course(id):
    course = session.query(Course).filter_by(id=id).first()
    if not course:
        return jsonify({"error": {"code": "E004", "message": "Course not found."}}), 404

    return jsonify({
        "name": course.name,
        "level": course.level
    }), 200

def validate_course_data(data):
    """
    Validate the input data for course creation.
    
    Parameters:
    - data (dict): The input data containing course details.

    Raises:
    - ValueError: If required fields are missing or of invalid type.
    """
    # Check if 'name' field is present
    if 'name' not in data or not isinstance(data['name'], str) or not data['name']:
        raise ValueError("Name field is required.")

    # Check if 'level' field is present
    if 'level' not in data or not isinstance(data['level'], str) or not data['level']:
        raise ValueError("Level field is required.")
```