from flask import Blueprint, request, jsonify
from services.course_service import assign_teacher_to_course
from db import get_db_session
from sqlalchemy.orm.exc import NoResultFound
from models.course import Course

course_bp = Blueprint('course', __name__)

@course_bp.route('/courses/<int:course_id>/assign-teacher/<int:teacher_id>', methods=['POST'])
def assign_teacher(course_id, teacher_id):
    """
    Assign a teacher to a course.

    :param course_id: ID of the course to which the teacher should be assigned
    :param teacher_id: ID of the teacher to assign to the course
    :return: JSON response with success or error message
    """
    try:
        assign_teacher_to_course(get_db_session(), course_id, teacher_id)
        return jsonify({"message": "Teacher successfully assigned to course."}), 200
    except NoResultFound:
        return jsonify({"error": {"code": "E004", "message": "Course not found."}}), 404

@course_bp.route('/courses/<int:course_id>', methods=['GET'])
def get_course(course_id):
    """
    Retrieve course information including its assigned teacher.

    :param course_id: ID of the course to retrieve
    :return: JSON response with course details or error message
    """
    course = get_db_session().query(Course).filter(Course.id == course_id).one_or_none()
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