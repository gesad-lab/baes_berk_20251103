```python
from flask import Blueprint, request, jsonify
from models.course import Course
from schemas.course_schema import CourseSchema
from app import db

course_controller = Blueprint('course_controller', __name__)

@course_controller.route('/courses', methods=['POST'])
def create_course():
    """
    Create a new course with required name and level fields.
    Raises a 400 Bad Request if any required fields are missing.

    Returns:
        Response: JSON representation of the created course or error details.
    """
    # Parse and validate incoming JSON request
    data = request.get_json()

    # Check for missing fields and return error message
    if not data or 'name' not in data or 'level' not in data:
        return jsonify({
            "error": {
                "code": "E400",
                "message": "Missing required fields: 'name' and 'level'."
            }
        }), 400

    course_schema = CourseSchema()
    course_data, errors = course_schema.load(data)

    # If there are validation errors from schemas
    if errors:
        return jsonify({"error": {"code": "E422", "message": "Validation failed.", "details": errors}}), 422

    # Create Course instance and save to database
    new_course = Course(name=course_data['name'], level=course_data['level'])
    db.session.add(new_course)
    db.session.commit()

    return jsonify(course_schema.dump(new_course)), 201

@course_controller.route('/courses', methods=['GET'])
def get_courses():
    """
    Retrieve all courses from the database.

    Returns:
        Response: JSON representation of the list of courses.
    """
    courses = Course.query.all()
    course_schema = CourseSchema(many=True)
    return jsonify(course_schema.dump(courses)), 200
```