from flask import request, jsonify
from src.models.course import Course
from src import db

@app.route('/courses', methods=['POST'])
def create_course():
    """Create a new course entity."""
    data = request.json
    name = data.get('name')
    level = data.get('level')

    # Validate input fields
    if not name:
        return jsonify({"error": {"code": "E001", "message": "Name field is required."}}), 400
    if not level:
        return jsonify({"error": {"code": "E002", "message": "Level field is required."}}), 400

    # Create and save the new course
    new_course = Course(name=name, level=level)
    db.session.add(new_course)
    db.session.commit()

    # Return success response with the created course data
    return jsonify({"id": new_course.id, "name": new_course.name, "level": new_course.level}), 201

@app.route('/courses', methods=['GET'])
def get_courses():
    """Retrieve all course records."""
    courses = Course.query.all()
    # Return a list of course objects in JSON format
    return jsonify([{"id": course.id, "name": course.name, "level": course.level} for course in courses])