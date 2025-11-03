```python
from flask import Blueprint, jsonify, request
from models import Course  # Assuming models.py contains the Course model
from extensions import db  # Assuming extensions.py handles the database initialization

course_api = Blueprint('course_api', __name__)

@course_api.route('/courses', methods=['POST'])
def create_course():
    """Create a new course.

    Request Body:
        - name (string): The name of the course.
        - level (string): The level of the course.

    Responses:
        - 201 Created: Course successfully created.
            {
                "id": <int>,       // The ID of the newly created course
                "name": <string>,  // The name of the course
                "level": <string>  // The level of the course
            }
        - 400 Bad Request: Missing or invalid parameters.
            {
                "error": {
                    "code": "E001",
                    "message": "Invalid input provided.",
                    "details": {}
                }
            }
    """
    data = request.get_json()
    name = data.get('name')
    level = data.get('level')

    if not name or not level:
        return jsonify({
            "error": {
                "code": "E001",
                "message": "Invalid input provided.",
                "details": {
                    "name": "Name is required.",
                    "level": "Level is required."
                }
            }
        }), 400

    # Create a new course and save to the database
    new_course = Course(name=name, level=level)
    db.session.add(new_course)
    db.session.commit()
    
    return jsonify({"id": new_course.id, "name": new_course.name, "level": new_course.level}), 201


@course_api.route('/courses/<int:id>', methods=['GET'])
def get_course(id):
    """Retrieve details of a specific course by its ID.

    Responses:
        - 200 OK: Course found.
            {
                "id": <int>,       // The ID of the course
                "name": <string>,  // The name of the course
                "level": <string>  // The level of the course
            }
        - 404 Not Found: Course does not exist.
            {
                "error": {
                    "code": "E002",
                    "message": "Course not found.",
                    "details": {}
                }
            }
    """
    course = Course.query.get(id)
    if not course:
        return jsonify({
            "error": {
                "code": "E002",
                "message": "Course not found.",
                "details": {}
            }
        }), 404

    return jsonify({"id": course.id, "name": course.name, "level": course.level}), 200


@course_api.route('/courses', methods=['GET'])
def list_courses():
    """List all available courses.

    Responses:
        - 200 OK: Successfully retrieved list of courses.
            [
                {
                    "id": <int>,       // The ID of the course
                    "name": <string>,  // The name of the course
                    "level": <string>  // The level of the course
                },
                ...
            ]
    """
    courses = Course.query.all()
    return jsonify([{"id": course.id, "name": course.name, "level": course.level} for course in courses]), 200
```