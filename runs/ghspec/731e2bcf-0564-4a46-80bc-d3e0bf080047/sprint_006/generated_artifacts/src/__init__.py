from flask import request, jsonify
from src.models.course import Course
from src.models.teacher import Teacher
from src.app import db
import logging

# Setting up a basic logger
logging.basicConfig(level=logging.INFO)  # Log at INFO level
logger = logging.getLogger(__name__)

@app.route('/courses/<int:course_id>/assign-teacher', methods=['PUT'])
def assign_teacher(course_id):
    course = Course.query.get(course_id)
    
    # Check if the course exists
    if not course:
        logger.error(f"Attempt to assign teacher to a non-existent course ID: {course_id}")
        return jsonify({"error": {"code": "E001", "message": "Invalid course ID."}}), 400

    data = request.json
    teacher_id = data.get('teacher_id')

    # Validate the teacher ID
    if not Teacher.query.get(teacher_id):
        logger.error(f"Invalid teacher ID {teacher_id} attempted for course ID: {course_id}")
        return jsonify({"error": {"code": "E002", "message": "Invalid teacher ID."}}), 400

    # Assign the teacher to the course
    course.teacher_id = teacher_id
    db.session.commit()

    logger.info(f"Teacher ID {teacher_id} successfully assigned to course ID {course_id}")
    return jsonify({
        "message": "Teacher assigned successfully.",
        "course": {
            "id": course.id,
            "name": course.name,
            "level": course.level,
            "teacher_id": course.teacher_id
        }
    }), 200

@app.route('/courses/<int:course_id>', methods=['GET'])
def get_course(course_id):
    course = Course.query.get(course_id)
    
    # Check if the course exists
    if not course:
        logger.error(f"Course not found for ID: {course_id}")
        return jsonify({"error": {"code": "E003", "message": "Course not found."}}), 404

    # Retrieve teacher details if assigned
    teacher = Teacher.query.get(course.teacher_id) if course.teacher_id else None

    response = {
        "id": course.id,
        "name": course.name,
        "level": course.level
    }

    # Include teacher information in the response if available
    if teacher:
        response["teacher"] = {
            "id": teacher.id,
            "name": teacher.name,
            "email": teacher.email
        }

    logger.info(f"Course details retrieved for course ID: {course_id}")
    return jsonify(response), 200