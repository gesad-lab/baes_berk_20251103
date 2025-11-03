```python
from flask import Blueprint, request, jsonify
from src.models import db, Course, Student  # Import necessary models
from sqlalchemy.exc import NoResultFound  # Import exception for handling no results

routes = Blueprint('routes', __name__)

@routes.route('/enroll', methods=['POST'])
def enroll_student():
    """Enroll a student in a course."""
    data = request.get_json()
    student_id = data.get('student_id')
    course_id = data.get('course_id')

    # Validate that both student_id and course_id are provided
    if not student_id or not course_id:
        return jsonify({"error": {"code": "E001", "message": "Student ID and Course ID must be provided."}}), 400

    try:
        # Fetch the student and course from the database
        student = Student.query.filter_by(id=student_id).one()
        course = Course.query.filter_by(id=course_id).one()

        # Check if the course already exists for this student to prevent duplicates
        if course in student.courses:
            return jsonify({"error": {"code": "E002", "message": "Student is already enrolled in this course."}}), 400
        
        # Enroll the student in the course
        student.courses.append(course)
        db.session.commit()

        return jsonify({
            "message": "Student successfully enrolled in course.",
            "student_id": student.id,
            "course_id": course.id
        }), 200

    except NoResultFound:
        # Handle case where the course does not exist
        return jsonify({"error": {"code": "E003", "message": "Course not found."}}), 404

    except Exception as e:
        # Log the exception and return a generic error message
        db.session.rollback()
        return jsonify({"error": {"code": "E004", "message": "An unexpected error occurred."}}), 500

@routes.route('/student_courses/<int:student_id>', methods=['GET'])
def get_student_courses(student_id):
    """Retrieve all courses for a specific student."""
    student = Student.query.get_or_404(student_id)
    courses = [course.name for course in student.courses]  # Assuming Course has a 'name' attribute

    return jsonify({"student_id": student.id, "courses": courses}), 200
```