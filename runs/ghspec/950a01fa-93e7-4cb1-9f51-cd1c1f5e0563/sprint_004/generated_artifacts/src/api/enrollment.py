```python
# src/api/enrollment.py

from flask import Blueprint, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import logging

# Initialize logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

db = SQLAlchemy()
enrollment_bp = Blueprint('enrollment', __name__)

class Enrollment(db.Model):
    __tablename__ = 'enrollment'
    student_id = db.Column(db.Integer, db.ForeignKey('students.id'), primary_key=True)
    course_id = db.Column(db.Integer, db.ForeignKey('courses.id'), primary_key=True)

    student = db.relationship('Student', back_populates='enrollments')
    course = db.relationship('Course', back_populates='enrolled_students')

@enrollment_bp.route('/enroll', methods=['POST'])
def enroll_student():
    """Enroll a student in a course."""
    data = request.json
    student_id = data.get('student_id')
    course_id = data.get('course_id')

    if not student_id or not course_id:
        logger.error("Enrollment request missing student_id or course_id")
        return jsonify({"error": {"code": "E001", "message": "Both student_id and course_id are required."}}), 400

    enrollment = Enrollment(student_id=student_id, course_id=course_id)
    db.session.add(enrollment)
    try:
        db.session.commit()
        logger.info(f"Student {student_id} enrolled in course {course_id}.")
        return jsonify({"status": "success", "message": "Enrollment successful."}), 201
    except Exception as e:
        db.session.rollback()
        logger.error(f"Failed to enroll student {student_id} in course {course_id}: {str(e)}")
        return jsonify({"error": {"code": "E002", "message": "Enrollment failed."}}), 500

@enrollment_bp.route('/students/<int:student_id>/courses', methods=['GET'])
def get_student_courses(student_id):
    """Retrieve all courses associated with a student."""
    courses = Enrollment.query.filter_by(student_id=student_id).all()
    course_list = [{"course_id": enrollment.course_id} for enrollment in courses]
    
    logger.info(f"Retrieved courses for student {student_id}: {course_list}.")
    return jsonify(course_list), 200

@enrollment_bp.route('/unenroll', methods=['DELETE'])
def unenroll_student():
    """Unenroll a student from a course."""
    data = request.json
    student_id = data.get('student_id')
    course_id = data.get('course_id')

    if not student_id or not course_id:
        logger.error("Unenrollment request missing student_id or course_id")
        return jsonify({"error": {"code": "E001", "message": "Both student_id and course_id are required."}}), 400

    enrollment = Enrollment.query.filter_by(student_id=student_id, course_id=course_id).first()

    if not enrollment:
        logger.warning(f"Student {student_id} not enrolled in course {course_id}.")
        return jsonify({"error": {"code": "E003", "message": "Student is not enrolled in the specified course."}}), 404

    db.session.delete(enrollment)
    try:
        db.session.commit()
        logger.info(f"Student {student_id} unenrolled from course {course_id}.")
        return jsonify({"status": "success", "message": "Unenrollment successful."}), 200
    except Exception as e:
        db.session.rollback()
        logger.error(f"Failed to unenroll student {student_id} from course {course_id}: {str(e)}")
        return jsonify({"error": {"code": "E002", "message": "Unenrollment failed."}}), 500
```