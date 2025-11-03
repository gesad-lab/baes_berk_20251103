from flask import Blueprint, request, jsonify
from src.models import Course  # Assuming Course model is defined in models.py
from src import db  # Assuming db is the SQLAlchemy instance

routes_bp = Blueprint('routes', __name__)

@routes_bp.route('/courses', methods=['POST'])
def create_course():
    """
    Endpoint to create a new course.
    Expects a JSON payload with `name` and `level`.

    Returns:
        JSON response with a success message and created course details or error message.
    """
    data = request.get_json()

    # Validate input
    if not data or 'name' not in data or 'level' not in data:
        return jsonify({"error": {"code": "E001", "message": "Invalid input: 'name' and 'level' are required fields."}}), 400

    # Create a new course instance
    new_course = Course(name=data['name'], level=data['level'])

    # Add to session and commit to the database
    try:
        db.session.add(new_course)
        db.session.commit()
    except Exception as e:
        db.session.rollback()  # Rollback the session in case of error
        return jsonify({"error": {"code": "E002", "message": "Failed to create course.", "details": str(e)}}), 500

    # Return success response with created course details
    return jsonify({
        "message": "Course created successfully.",
        "course": {
            "id": new_course.id,
            "name": new_course.name,
            "level": new_course.level
        }
    }), 201


@routes_bp.route('/courses', methods=['GET'])
def get_courses():
    """
    Endpoint to retrieve a list of all courses.

    Returns:
        JSON response with an array of courses or an error message.
    """
    try:
        courses = Course.query.all()
        course_list = [{"id": course.id, "name": course.name, "level": course.level} for course in courses]

        return jsonify(course_list), 200

    except Exception as e:
        return jsonify({"error": {"code": "E003", "message": "Failed to retrieve courses.", "details": str(e)}}), 500