from flask import Blueprint, jsonify, request
from models import Student, Course, db  # Importing Student and Course models
from sqlalchemy.exc import IntegrityError
from marshmallow import Schema, fields, ValidationError

students_bp = Blueprint('students', __name__)

class CourseAssociationSchema(Schema):
    """Schema to validate course association with a student."""
    courseIds = fields.List(fields.Int(required=True), required=True)

@students_bp.route('/students/<int:student_id>/courses', methods=['POST'])
def associate_courses(student_id):
    """Associate courses with a student."""
    data = request.json
    try:
        # Validate request data against the schema
        CourseAssociationSchema().load(data)
    except ValidationError as err:
        return jsonify({"error": {"code": "E003", "message": "Invalid input.", "details": err.messages}}), 400

    course_ids = data.get('courseIds', [])
    existing_student = Student.query.get(student_id)

    if not existing_student:
        return jsonify({"error": {"code": "E002", "message": "Student not found."}}), 404

    for course_id in course_ids:
        existing_course = Course.query.get(course_id)
        if not existing_course:
            return jsonify({"error": {"code": "E001", "message": f"Course with ID {course_id} does not exist."}}), 404
        existing_student.courses.append(existing_course)

    try:
        db.session.commit()
    except IntegrityError:
        db.session.rollback()  # Rollback if there is an integrity error
        return jsonify({"error": {"code": "E004", "message": "Failed to associate courses due to integrity issues."}}), 400

    return jsonify({"message": "Courses associated successfully.", "courses": [course.name for course in existing_student.courses]}), 200

# Assuming tests/test_students.py will be updated in the next steps.