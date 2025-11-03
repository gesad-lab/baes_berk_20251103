from flask import Blueprint, request, jsonify
from marshmallow import Schema, fields, ValidationError
from src.models import Course
from src.services.course_service import create_course, get_course_by_id

bp = Blueprint('courses', __name__)

# Define a schema for course validation using Marshmallow
class CourseSchema(Schema):
    name = fields.String(required=True)
    level = fields.String(required=True)

course_schema = CourseSchema()

@bp.route('/courses', methods=['POST'])
def create_course_endpoint():
    """Handle course creation requests."""
    try:
        # Validate and deserialize the incoming request data
        course_data = course_schema.load(request.json)
        
        # Create the course using service layer
        new_course = create_course(course_data['name'], course_data['level'])
        
        # Respond with the created course details
        return jsonify({"id": new_course.id, "name": new_course.name, "level": new_course.level}), 201
    except ValidationError as err:
        # Handle validation errors and return them in a structured format
        return jsonify({"error": {"code": "E001", "message": "Validation error", "details": err.messages}}), 400

@bp.route('/courses/<int:id>', methods=['GET'])
def get_course_endpoint(id):
    """Retrieve course details by ID."""
    course = get_course_by_id(id)
    if course:
        return jsonify({"id": course.id, "name": course.name, "level": course.level}), 200
    else:
        return jsonify({"error": {"code": "E002", "message": "Course not found"}}), 404

# Ensure to register this blueprint in your main application file
# Example: app.register_blueprint(bp)