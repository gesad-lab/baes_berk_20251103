```python
from flask import Blueprint, request, jsonify
from models.course import Course  # Assuming Course model is defined in models.course
from models.teacher import Teacher  # Assuming Teacher model is defined in models.teacher
from app import db  # Assuming db is defined in app
from sqlalchemy.exc import IntegrityError, NoResultFound

course_routes = Blueprint('course_routes', __name__)

@course_routes.route('/courses/<int:course_id>', methods=['PATCH'])
def assign_teacher_to_course(course_id):
    """
    Assign a teacher to a course.

    Parameters:
    - course_id: int - The ID of the course to update

    Request JSON Body:
    - teacher_id: int - The ID of the teacher to assign to the course

    Returns:
    - JSON containing the updated course object or error message.
    """
    data = request.get_json()
    teacher_id = data.get('teacher_id')

    # Validate input
    if teacher_id is None:
        return jsonify({"error": {"code": "E400", "message": "Missing teacher_id."}}), 400
    
    # Validate the teacher exists
    teacher = Teacher.query.filter_by(id=teacher_id).one_or_none()
    if not teacher:
        return jsonify({"error": {"code": "E404", "message": "Teacher not found."}}), 404

    # Update the course with the new teacher_id
    try:
        course = Course.query.get(course_id)
        if not course:
            return jsonify({"error": {"code": "E404", "message": "Course not found."}}), 404
        
        course.teacher_id = teacher_id
        db.session.commit()
        return jsonify(course.to_dict()), 200  # Assuming Course has a to_dict method for serialization

    except IntegrityError:
        db.session.rollback()  # Rollback the session on error
        return jsonify({"error": {"code": "E500", "message": "Failed to assign teacher."}}), 500

@course_routes.route('/courses/<int:course_id>', methods=['GET'])
def get_course_information(course_id):
    """
    Retrieve course information, including assigned teacher details.

    Parameters:
    - course_id: int - The ID of the course to retrieve

    Returns:
    - JSON containing course details with teacher information.
    """
    course = Course.query.get(course_id)

    if not course:
        return jsonify({"error": {"code": "E404", "message": "Course not found."}}), 404

    # Prepare response data including teacher information
    response_data = {
        "id": course.id,
        "teacher": {
            "id": course.teacher.id,  # Assuming Course has a relationship to Teacher
            "name": course.teacher.name,
            "email": course.teacher.email
        },
        # Include other course fields as necessary
    }
    
    return jsonify(response_data), 200
```