```python
from flask import Blueprint, jsonify, request
from src.models import StudentCourses, Student, Course  # Import relevant models
from sqlalchemy.exc import IntegrityError, NoResultFound

student_courses_bp = Blueprint('student_courses', __name__)

@student_courses_bp.route('/students/<int:student_id>/courses', methods=['POST'])
def enroll_student(student_id):
    """Enroll a student in a course.

    Request Body:
    {
        "course_id": <integer>  # Required
    }

    Response:
    - 200 OK with confirmation: {"student_id": <student_id>, "course_id": <course_id>}
    - 400 Bad Request if course ID is invalid.
    """
    data = request.json
    course_id = data.get('course_id')

    if not course_id:
        return jsonify({'error': {'code': 'E001', 'message': 'Missing course_id in request.'}}), 400

    try:
        # Check if student exists
        student = Student.query.get(student_id)
        if not student:
            return jsonify({'error': {'code': 'E002', 'message': 'Student not found.'}}), 404
        
        # Logic to associate the student with the course
        student_course = StudentCourses(student_id=student_id, course_id=course_id)
        db.session.add(student_course)
        db.session.commit()

        return jsonify({"student_id": student_id, "course_id": course_id}), 200
        
    except IntegrityError:
        db.session.rollback()
        return jsonify({'error': {'code': 'E003', 'message': 'Invalid course association.'}}), 400
    
    except Exception as e:
        return jsonify({'error': {'code': 'E004', 'message': str(e)}}), 500


@student_courses_bp.route('/students/<int:student_id>/courses', methods=['GET'])
def get_student_courses(student_id):
    """Retrieve courses for a student.

    Response:
    - 200 OK with list of courses: [{"course_id": <course_id>, "name": <course_name>, "level": <course_level>}, ...]
    - 404 Not Found if student does not exist.
    """
    try:
        # Logic to retrieve courses
        student = Student.query.get(student_id)
        if not student:
            return jsonify({'error': {'code': 'E002', 'message': 'Student not found.'}}), 404
        
        courses = Course.query.join(StudentCourses).filter(StudentCourses.student_id == student_id).all()
        course_details = [{"course_id": course.id, "name": course.name, "level": course.level} for course in courses]
        
        return jsonify(course_details), 200
    
    except Exception as e:
        return jsonify({'error': {'code': 'E004', 'message': str(e)}}), 500


@student_courses_bp.route('/students/<int:student_id>/courses/<int:course_id>', methods=['DELETE'])
def remove_student_from_course(student_id, course_id):
    """Remove a student from a course.

    Response:
    - 200 OK with confirmation of removal: {"message": "Successfully removed."}
    - 404 Not Found if student or course does not exist.
    """
    try:
        # Logic to remove the student from the course
        student_course = StudentCourses.query.filter_by(student_id=student_id, course_id=course_id).first()
        if not student_course:
            return jsonify({'error': {'code': 'E005', 'message': 'Student or course not found.'}}), 404

        db.session.delete(student_course)
        db.session.commit()

        return jsonify({"message": "Successfully removed."}), 200

    except Exception as e:
        return jsonify({'error': {'code': 'E004', 'message': str(e)}}), 500
```