```python
from flask import Blueprint, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from src.models import Student, Course
from src.services.student_course_service import (
    enroll_student_in_course,
    unenroll_student_from_course,
)
from sqlalchemy.exc import IntegrityError

student_api = Blueprint('student_api', __name__)
db = SQLAlchemy()

@student_api.route('/students/<int:student_id>/courses', methods=['POST'])
def enroll_course(student_id):
    """Enroll a student in a course."""
    body = request.get_json()

    # Validate input
    if not body or 'course_id' not in body:
        return jsonify({'error': {'code': 'E001', 'message': 'Invalid input: course_id is required'}}), 400

    course_id = body['course_id']

    try:
        enroll_student_in_course(student_id, course_id)
        return jsonify({'message': 'Student enrolled successfully'}), 201
    except IntegrityError:
        # Handle enrollment to a non-existing course or duplicate enrollment
        db.session.rollback()  # Rollback the session to maintain integrity
        return jsonify({'error': {'code': 'E002', 'message': 'Enrollment failed: Course may not exist or student is already enrolled'}}), 400
    except Exception as e:
        # Log the error for debugging purposes (not exposed to user)
        db.session.rollback()
        return jsonify({'error': {'code': 'E003', 'message': 'An unexpected error occurred', 'details': str(e)}}), 500


@student_api.route('/students/<int:student_id>/courses/<int:course_id>', methods=['DELETE'])
def unenroll_course(student_id, course_id):
    """Unenroll a student from a course."""
    try:
        unenroll_student_from_course(student_id, course_id)
        return jsonify({'message': 'Student unenrolled successfully'}), 200
    except IntegrityError:
        db.session.rollback()
        return jsonify({'error': {'code': 'E004', 'message': 'Unenrollment failed: Student may not be enrolled in this course'}}), 400
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': {'code': 'E005', 'message': 'An unexpected error occurred', 'details': str(e)}}), 500


@student_api.route('/students/<int:student_id>/courses', methods=['GET'])
def get_courses(student_id):
    """Retrieve courses for a student."""
    courses = Course.query.join(Student.courses).filter(Student.id == student_id).all()
    # Format courses into a JSON serializable format
    return jsonify({'courses': [course.to_dict() for course in courses]}), 200
```