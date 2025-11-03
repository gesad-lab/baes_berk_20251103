from flask import Blueprint, request, jsonify
from http import HTTPStatus
from app.models import StudentCourses, Student, Course
from app import db

student_route = Blueprint('student', __name__)

@student_route.route('/students/<int:id>/courses', methods=['POST'])
def assign_courses(id):
    # Validate if the student exists
    student = Student.query.get(id)
    if not student:
        return jsonify({
            "error": {
                "code": "E001",
                "message": "Student not found.",
                "details": {"student_id": id}
            }
        }), HTTPStatus.NOT_FOUND

    # Retrieve the course IDs from the request
    data = request.get_json()
    course_ids = data.get("course_ids", [])

    # Validate course IDs
    if not isinstance(course_ids, list):
        return jsonify({
            "error": {
                "code": "E002",
                "message": "Invalid input: course_ids must be a list.",
                "details": {"received_type": type(course_ids).__name__}
            }
        }), HTTPStatus.BAD_REQUEST

    # Check if provided course IDs exist in the database
    for course_id in course_ids:
        course = Course.query.get(course_id)
        if not course:
            return jsonify({
                "error": {
                    "code": "E003",
                    "message": "Course not found.",
                    "details": {"course_id": course_id}
                }
            }), HTTPStatus.NOT_FOUND

    # Create associations in the junction table
    for course_id in course_ids:
        association = StudentCourses(student_id=id, course_id=course_id)
        db.session.add(association)

    db.session.commit()
    return jsonify(message="Courses successfully assigned."), HTTPStatus.OK

@student_route.route('/students/<int:id>/courses', methods=['GET'])
def get_courses(id):
    # Validate student existence
    student = Student.query.get(id)
    if not student:
        return jsonify({
            "error": {
                "code": "E001",
                "message": "Student not found.",
                "details": {"student_id": id}
            }
        }), HTTPStatus.NOT_FOUND

    # Fetch courses associated with the student
    courses = Course.query.join(StudentCourses).filter(StudentCourses.student_id == id).all()
    
    # Format response
    course_list = [{"id": course.id, "name": course.name, "level": course.level} for course in courses]
    
    return jsonify(courses=course_list), HTTPStatus.OK

@student_route.route('/students/<int:id>/courses', methods=['DELETE'])
def remove_courses(id):
    # Validate if the student exists
    student = Student.query.get(id)
    if not student:
        return jsonify({
            "error": {
                "code": "E001",
                "message": "Student not found.",
                "details": {"student_id": id}
            }
        }), HTTPStatus.NOT_FOUND

    # Retrieve the course IDs from the request
    data = request.get_json()
    course_ids = data.get("course_ids", [])

    # Validate course IDs
    if not isinstance(course_ids, list):
        return jsonify({
            "error": {
                "code": "E002",
                "message": "Invalid input: course_ids must be a list.",
                "details": {"received_type": type(course_ids).__name__}
            }
        }), HTTPStatus.BAD_REQUEST

    # Remove associations from the junction table
    for course_id in course_ids:
        association = StudentCourses.query.filter_by(student_id=id, course_id=course_id).first()
        if association:
            db.session.delete(association)

    db.session.commit()
    return jsonify(message="Courses successfully removed."), HTTPStatus.OK