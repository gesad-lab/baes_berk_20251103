```python
from flask import Blueprint, jsonify, request
from src.models import Student, Course, StudentCourse  # Importing necessary models
from src.extensions import db  # Assuming you have a database extension initialized
from sqlalchemy.exc import IntegrityError

routes = Blueprint('routes', __name__)

@routes.route('/api/v1/students/<int:student_id>/courses', methods=['GET'])
def get_student_courses(student_id):
    """Retrieve the list of courses for a specific student.

    Args:
        student_id (int): The ID of the student.

    Returns:
        JSON response with list of courses or error message.
    """
    student = Student.query.get(student_id)
    if student is None:
        return jsonify({'error': {'code': 'E001', 'message': 'Student not found'}}), 404

    # Get the courses associated with the student
    courses = student.course_associations
    course_list = [{"id": course.course.id, "name": course.course.name, "level": course.course.level}
                   for course in courses]

    return jsonify(course_list), 200

@routes.route('/api/v1/students/<int:student_id>/courses', methods=['POST'])
def associate_student_with_course(student_id):
    """Associate a student with a course.

    Args:
        student_id (int): The ID of the student.
        course_id (int): The ID of the course provided in the request body.

    Returns:
        JSON response indicating success or failure.
    """
    student = Student.query.get(student_id)
    if student is None:
        return jsonify({'error': {'code': 'E001', 'message': 'Student not found'}}), 404

    data = request.json
    course_id = data.get('course_id')
    if not course_id:
        return jsonify({'error': {'code': 'E002', 'message': 'Course ID is required'}}), 400

    course = Course.query.get(course_id)
    if course is None:
        return jsonify({'error': {'code': 'E003', 'message': 'Course not found'}}), 404

    # Associate the student with the course
    try:
        new_association = StudentCourse(student_id=student_id, course_id=course_id)
        db.session.add(new_association)
        db.session.commit()
        return jsonify({'message': 'Course successfully added to student'}), 201
    except IntegrityError:
        db.session.rollback()
        return jsonify({'error': {'code': 'E004', 'message': 'Association already exists'}}), 400

```