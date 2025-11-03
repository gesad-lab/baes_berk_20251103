```python
from flask import Blueprint, request, jsonify
from app.models import Student, Course, StudentCourse
from app import db

routes = Blueprint('routes', __name__)

@routes.route('/associate_courses', methods=['POST'])
def associate_courses():
    """
    Associate courses with a student.
    Expects a JSON body containing student ID and a list of course IDs.
    Responds with a success message and the updated student record or error messages on validation failures.
    """
    data = request.get_json()

    # Validate input data
    if not data or 'student_id' not in data or 'course_ids' not in data:
        return jsonify({"error": {"code": "E001", "message": "Student ID and course IDs are required."}}), 400

    student_id = data['student_id']
    course_ids = data['course_ids']

    # Validate student existence
    student = Student.query.get(student_id)
    if not student:
        return jsonify({"error": {"code": "E002", "message": "Invalid student ID provided."}}), 404

    # Validate course IDs
    valid_courses = []
    for course_id in course_ids:
        course = Course.query.get(course_id)
        if course:
            valid_courses.append(course)
        else:
            return jsonify({"error": {"code": "E003", "message": f"Invalid course ID {course_id} provided."}}), 404

    # Associate courses with the student
    for course in valid_courses:
        student_course = StudentCourse(student_id=student.id, course_id=course.id)
        db.session.add(student_course)

    db.session.commit()

    return jsonify({
        "message": "Courses associated successfully.",
        "student": {
            "id": student.id,
            "name": student.name,
            "courses": [{"id": c.id, "name": c.name} for c in valid_courses]
        }
    }), 200

@routes.route('/students/<int:student_id>', methods=['GET'])
def get_student_with_courses(student_id):
    """
    Retrieve a student record along with their associated courses.
    Responds with the student record or an error message if the student does not exist.
    """
    student = Student.query.get(student_id)
    if not student:
        return jsonify({"error": {"code": "E002", "message": "Student not found."}}), 404

    courses = student.courses  # Assuming a relationship is defined in the Model
    return jsonify({
        "id": student.id,
        "name": student.name,
        "courses": [{"id": course.id, "name": course.name} for course in courses]
    }), 200
```