```python
from flask import Blueprint, request, jsonify
from models.course import Course
from models.teacher import Teacher
from app import db

course_bp = Blueprint('course_bp', __name__)

@course_bp.route('/courses/<int:course_id>/assign_teacher/<int:teacher_id>', methods=['POST'])
def assign_teacher_to_course(course_id, teacher_id):
    """
    Assign a teacher to a course.

    Parameters:
    - course_id: The ID of the course
    - teacher_id: The ID of the teacher to assign
   
    Returns:
    - JSON response with course details on success, or error message on failure.
    """
    
    # Verify the course exists
    course = Course.query.get(course_id)
    if not course:
        return jsonify({"error": {"code": "E404", "message": "Course not found"}}), 404
    
    # Verify the teacher exists
    teacher = Teacher.query.get(teacher_id)
    if not teacher:
        return jsonify({"error": {"code": "E400", "message": "Invalid teacher ID"}}), 400
    
    # Assign the teacher to the course
    course.teacher_id = teacher_id
    db.session.commit()

    # Return updated course details
    return jsonify({
        "course_id": course.id,
        "title": course.title,
        "teacher": {
            "id": teacher.id,
            "name": teacher.name,
            "email": teacher.email
        }
    }), 200

@course_bp.route('/courses/<int:course_id>', methods=['GET'])
def get_course_details(course_id):
    """
    Retrieve course details including the assigned teacher.

    Parameters:
    - course_id: The ID of the course

    Returns:
    - JSON response with course details including teacher information.
    """
    
    # Verify the course exists
    course = Course.query.get(course_id)
    if not course:
        return jsonify({"error": {"code": "E404", "message": "Course not found"}}), 404
    
    # Prepare response
    response = {
        "course_id": course.id,
        "title": course.title
    }

    # Check if there's an assigned teacher
    if course.teacher_id:
        teacher = Teacher.query.get(course.teacher_id)
        if teacher:
            response["teacher"] = {
                "id": teacher.id,
                "name": teacher.name,
                "email": teacher.email
            }
    
    return jsonify(response), 200

@course_bp.route('/courses/<int:course_id>/remove_teacher', methods=['POST'])
def remove_teacher_from_course(course_id):
    """
    Remove the teacher assigned to a course.

    Parameters:
    - course_id: The ID of the course

    Returns:
    - JSON response indicating success or failure.
    """
    
    # Verify the course exists
    course = Course.query.get(course_id)
    if not course:
        return jsonify({"error": {"code": "E404", "message": "Course not found"}}), 404

    # Remove the teacher assignment
    course.teacher_id = None
    db.session.commit()

    return jsonify({"message": "Teacher assignment removed."}), 200
```