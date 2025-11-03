```python
from flask import Flask, request, jsonify
from src.models import Course  # Assuming there's a Course model defined in models.py
from src.database import db  # Assuming SQLAlchemy session is managed here

app = Flask(__name__)

@app.route('/courses', methods=['POST'])
def create_course():
    """Create a new course with validation for name and level."""
    data = request.json

    # Validate required fields
    if 'name' not in data or not data['name']:
        return jsonify({"error": {"code": "E001", "message": "Course name is required."}}), 400
    if 'level' not in data or not data['level']:
        return jsonify({"error": {"code": "E002", "message": "Course level is required."}}), 400

    # Create and save new course instance
    new_course = Course(name=data['name'], level=data['level'])
    db.session.add(new_course)

    try:
        db.session.commit()  # Commit the new course to the database
        return jsonify({"message": "Course created successfully.", "course": {"name": new_course.name, "level": new_course.level}}), 201
    except Exception as e:
        db.session.rollback()  # Rollback session on error
        return jsonify({"error": {"code": "E003", "message": "Failed to create course.", "details": str(e)}}), 500

@app.route('/courses', methods=['GET'])
def get_courses():
    """Retrieve all courses from the database."""
    courses = Course.query.all()  # Fetch all courses
    return jsonify([{"name": course.name, "level": course.level} for course in courses]), 200
```