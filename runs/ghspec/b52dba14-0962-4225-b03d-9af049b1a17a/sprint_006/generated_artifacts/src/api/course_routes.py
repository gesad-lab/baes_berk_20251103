```python
from flask import Blueprint, jsonify, request
from src.models.course_model import Course
from src.services.course_service import CourseService
from src.models.teacher_model import Teacher
from sqlalchemy.exc import NoResultFound, IntegrityError

course_routes = Blueprint('course_routes', __name__)

@course_routes.route('/courses/<int:course_id>/assign_teacher', methods=['PUT'])
def assign_teacher(course_id):
    """
    Assign a teacher to a course.
    
    Parameters:
    - course_id: ID of the course to which the teacher is to be assigned.
    
    Request body should contain:
    - teacher_id (int): ID of the teacher to be assigned.
    
    Returns:
    - 200 OK with a confirmation message if the assignment is successful.
    - 400 Bad Request if the teacher_id is missing or does not exist.
    """
    data = request.get_json()
    teacher_id = data.get('teacher_id')

    if not teacher_id:
        return jsonify({"error": {"code": "E001", "message": "teacher_id is required"}}), 400

    try:
        # Check if the teacher exists
        teacher = Teacher.query.filter_by(id=teacher_id).one()
    except NoResultFound:
        return jsonify({"error": {"code": "E002", "message": "Teacher not found"}}), 400

    try:
        # Assign the teacher to the course
        course = Course.query.filter_by(id=course_id).one()
        course.teacher_id = teacher_id
        CourseService.update_course(course)  # Assuming this method handles the db commit
        return jsonify({"message": "Teacher assigned successfully"}), 200
    except NoResultFound:
        return jsonify({"error": {"code": "E003", "message": "Course not found"}}), 404
    except IntegrityError as e:
        # Catch any integrity issues that might arise
        return jsonify({"error": {"code": "E004", "message": "Could not assign teacher to course"}}), 500

@course_routes.route('/courses/<int:course_id>', methods=['GET'])
def get_course(course_id):
    """
    Retrieve course details along with the assigned teacher's information.
    
    Parameters:
    - course_id: ID of the course to retrieve.
    
    Returns:
    - 200 OK with course details including the teacher's name if assigned.
    - 404 Not Found if the course does not exist.
    """
    try:
        course = Course.query.filter_by(id=course_id).one()
        teacher_name = None
        if course.teacher_id:
            teacher = Teacher.query.filter_by(id=course.teacher_id).one()
            teacher_name = teacher.name

        return jsonify({
            "course_id": course.id,
            "course_name": course.name,
            "description": course.description,
            "teacher_name": teacher_name
        }), 200
    except NoResultFound:
        return jsonify({"error": {"code": "E003", "message": "Course not found"}}), 404
```