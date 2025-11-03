```python
from flask import Blueprint, request, jsonify
from app.models import Student, Course
from app import db

students_bp = Blueprint('students', __name__)

@students_bp.route('/students/<int:student_id>/courses', methods=['POST'])
def enroll_student_course(student_id):
    data = request.get_json()
    course_id = data.get('courseId')
    
    # Check if courseId is provided
    if not course_id:
        return jsonify({"error": {"code": "E001", "message": "Course ID is required."}}), 400
    
    # Verify if the course exists in the database
    course = Course.query.get(course_id)
    if not course:
        return jsonify({"error": {"code": "E002", "message": "Course does not exist."}}), 400  # Changed to 400 for consistent error handling
    
    # Find the student in the database
    student = Student.query.get(student_id)
    if student:
        # Enroll the student in the course
        student.courses.append(course)
        db.session.commit()
        # Return the updated student details
        return jsonify({"id": student.id, "name": student.name, "email": student.email, "course_ids": [c.id for c in student.courses]}), 201
    
    # If student not found, return an error
    return jsonify({"error": {"code": "E003", "message": "Student not found."}}), 404

@students_bp.route('/students/<int:student_id>/courses', methods=['GET'])
def get_enrolled_courses(student_id):
    student = Student.query.get(student_id)
    
    # If student not found, return an error
    if not student:
        return jsonify({"error": {"code": "E003", "message": "Student not found."}}), 404
    
    # Return the list of enrolled courses
    return jsonify([{"id": course.id, "name": course.name, "level": course.level} for course in student.courses]), 200
```