from flask import Blueprint, request, jsonify, abort
from src.models.student_model import Student
from src.models.course_model import Course
from src.models.enrollment_model import Enrollment
from src.database import db

student_routes = Blueprint('student_routes', __name__)

@student_routes.route('/students/<int:student_id>/courses', methods=['POST'])
def add_course_to_student(student_id):
    """Enroll a student in a course."""
    data = request.get_json()
    course_id = data.get('course_id')

    # Validate request data
    if not course_id:
        return jsonify({"error": {"code": "E001", "message": "course_id is required."}}), 400

    # Check if the student exists
    student = Student.query.get(student_id)
    if not student:
        return jsonify({"error": {"code": "E002", "message": "Student not found."}}), 404

    # Check if the course exists
    course = Course.query.get(course_id)
    if not course:
        return jsonify({"error": {"code": "E003", "message": "Course not found."}}), 404

    # Create the enrollment entry
    enrollment = Enrollment(student_id=student_id, course_id=course_id)
    db.session.add(enrollment)
    db.session.commit()

    return jsonify({"message": "Course successfully enrolled to student."}), 201

@student_routes.route('/students/<int:student_id>/courses', methods=['GET'])
def get_student_courses(student_id):
    """Retrieve all courses for a given student."""
    student = Student.query.get(student_id)
    if not student:
        return jsonify({"error": {"code": "E002", "message": "Student not found."}}), 404

    # Get courses associated with the student
    courses = Course.query.join(Enrollment).filter(Enrollment.student_id == student_id).all()
    course_list = [{"id": course.id, "name": course.name, "level": course.level} for course in courses]

    return jsonify(course_list), 200

@student_routes.route('/students/<int:student_id>/courses/<int:course_id>', methods=['DELETE'])
def remove_course_from_student(student_id, course_id):
    """Remove a course from a student's enrollment."""
    # Check if the student exists
    student = Student.query.get(student_id)
    if not student:
        return jsonify({"error": {"code": "E002", "message": "Student not found."}}), 404

    # Check if the course exists
    course = Course.query.get(course_id)
    if not course:
        return jsonify({"error": {"code": "E003", "message": "Course not found."}}), 404

    # Remove the enrollment entry
    enrollment = Enrollment.query.filter_by(student_id=student_id, course_id=course_id).first()
    if enrollment:
        db.session.delete(enrollment)
        db.session.commit()
        return '', 204

    # If the enrollment does not exist
    return jsonify({"error": {"code": "E004", "message": "Enrollment record not found."}}), 404