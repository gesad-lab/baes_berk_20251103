```python
from flask import Blueprint, jsonify, request
from src.models import Course
from src.database import get_db
from sqlalchemy.exc import IntegrityError

# Create a new Blueprint for the routes
bp = Blueprint('courses', __name__)

@bp.route('/courses', methods=['GET'])
def get_all_courses():
    """Retrieve a list of all courses."""
    try:
        db = get_db()
        courses = db.session.query(Course).all()  # Retrieve all courses
        result = [{"id": course.id, "name": course.name, "level": course.level} for course in courses]
        return jsonify(result), 200
    except Exception as e:
        return jsonify({"error": {"code": "E500", "message": "Internal Server Error", "details": str(e)}}), 500

@bp.route('/courses/<int:id>', methods=['GET'])
def get_course(id):
    """Retrieve a course by ID."""
    db = get_db()
    course = db.session.query(Course).get(id)  # Retrieve the course with the given ID
    if course:
        return jsonify({"id": course.id, "name": course.name, "level": course.level}), 200
    else:
        return jsonify({"error": {"code": "E404", "message": "Course not found"}}), 404

# Ensure the Blueprint is registered in the main application file
def register_routes(app):
    app.register_blueprint(bp)
```