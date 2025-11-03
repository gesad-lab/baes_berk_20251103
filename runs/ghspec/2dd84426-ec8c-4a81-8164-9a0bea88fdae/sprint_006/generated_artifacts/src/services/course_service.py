from flask import Blueprint, request, jsonify
from src.models.course import Course
from sqlalchemy.orm.exc import NoResultFound
from src.services.course_service import assign_teacher_to_course
from src.db import get_db_session

course_bp = Blueprint('course', __name__)

@course_bp.route('/courses/<int:course_id>/assign-teacher/<int:teacher_id>', methods=['POST'])
def assign_teacher(course_id, teacher_id):
    """
    Assign a teacher to a course.

    Parameters:
        course_id (int): ID of the course to which the teacher will be assigned.
        teacher_id (int): ID of the teacher who will be assigned.

    Returns:
        JSON response with a success message or error code if the course is not found.
    """
    try:
        assign_teacher_to_course(get_db_session(), course_id, teacher_id)
        return jsonify({"message": "Teacher successfully assigned to course."}), 200
    except NoResultFound:
        return jsonify({"error": {"code": "E004", "message": "Course not found."}}), 404

@course_bp.route('/courses/<int:course_id>', methods=['GET'])
def get_course(course_id):
    """
    Retrieve course information, including teacher details.

    Parameters:
        course_id (int): ID of the course to retrieve.

    Returns:
        JSON response with course details, including teacher information, or error code if not found.
    """
    session = get_db_session()
    course = session.query(Course).filter(Course.id == course_id).one_or_none()  # Fetch course or None
    if course:
        return jsonify({
            "id": course.id,
            "name": course.name,
            "teacher": {
                "id": course.teacher.id if course.teacher else None,
                "name": course.teacher.name if course.teacher else None,
                "email": course.teacher.email if course.teacher else None
            }
        }), 200
    else:
        return jsonify({"error": {"code": "E004", "message": "Course not found."}}), 404