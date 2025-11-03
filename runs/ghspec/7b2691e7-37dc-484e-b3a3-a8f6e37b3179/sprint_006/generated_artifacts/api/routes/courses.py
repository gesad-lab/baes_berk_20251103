from flask import Blueprint, request, jsonify
from marshmallow import Schema, fields, ValidationError
from models import Course, Teacher, db  # Importing the Course and Teacher models
from sqlalchemy.exc import IntegrityError

courses_bp = Blueprint('courses', __name__)

class AssignTeacherSchema(Schema):
    """Schema to validate assignment of a teacher to a course."""
    teacher_id = fields.Int(required=True)

@courses_bp.route('/courses/<int:course_id>/assign-teacher', methods=['POST'])
def assign_teacher(course_id):
    """Assign a teacher to a specific course."""
    data = request.json
    schema = AssignTeacherSchema()

    # Validate input data against the schema
    try:
        validated_data = schema.load(data)
    except ValidationError as err:
        return jsonify({"error": {"code": "E001", "message": "Invalid input data", "details": err.messages}}), 400

    teacher_id = validated_data['teacher_id']

    # Validate course existence
    course = Course.query.get(course_id)
    if course is None:
        return jsonify({"error": {"code": "E002", "message": "Course not found"}}), 404

    # Validate teacher existence
    teacher = Teacher.query.get(teacher_id)
    if teacher is None:
        return jsonify({"error": {"code": "E003", "message": "Teacher not found"}}), 404

    # Assign the teacher to the course
    course.teacher_id = teacher_id
    try:
        db.session.commit()
    except IntegrityError:
        db.session.rollback()
        return jsonify({"error": {"code": "E004", "message": "Failed to assign teacher to course"}}), 500

    return jsonify(course.to_dict()), 200  # Assuming to_dict() is defined to serialize Course object

@courses_bp.route('/courses/<int:course_id>', methods=['GET'])
def get_course(course_id):
    """Retrieve course details, including assigned teacher if any."""
    course = Course.query.get(course_id)
    if course is None:
        return jsonify({"error": {"code": "E002", "message": "Course not found"}}), 404
    
    return jsonify(course.to_dict()), 200  # Assuming to_dict() serializes the Course object along with teacher info if present