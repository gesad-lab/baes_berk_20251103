from flask import Flask, jsonify, request, abort
from src.models import Student, Course  # Assuming these models exist in models.py
from src.repositories import StudentRepository, CourseRepository  # Assume repositories are defined
from sqlalchemy.exc import IntegrityError

app = Flask(__name__)

# Create a repository instance
student_repository = StudentRepository()
course_repository = CourseRepository()

@app.route('/students/<int:student_id>/enroll', methods=['POST'])
def enroll_student(student_id):
    """
    Enroll a student in specified courses.

    Params:
    - student_id (int): The ID of the student
    - Request Body: { "course_ids": [integer] } 

    Returns:
    - Response: { "student_id": "integer", "enrolled_courses": [...] }
    """
    data = request.get_json()

    if not data or 'course_ids' not in data:
        abort(400, description='E001: Invalid input, expected {"course_ids": [...]}')

    course_ids = data['course_ids']

    # Validate course_ids is a list of integers
    if not isinstance(course_ids, list) or not all(isinstance(course_id, int) for course_id in course_ids):
        abort(400, description='E002: course_ids must be an array of integers')

    # Logic to enroll the student into the provided courses
    try:
        enrolled_courses = student_repository.enroll_student(student_id, course_ids)
    except IntegrityError as e:
        abort(400, description=f'E003: Enrollment error - {str(e)}')

    return jsonify({
        "student_id": student_id,
        "enrolled_courses": [{"course_id": course.id, "name": course.name, "level": course.level} for course in enrolled_courses]
    }), 201

@app.route('/students/<int:student_id>/courses', methods=['GET'])
def get_student_courses(student_id):
    """
    Retrieve a list of courses a student is enrolled in.

    Params:
    - student_id (int): The ID of the student

    Returns:
    - Response: [{ "course_id": "integer", "name": "string", "level": "string" }]
    """
    courses = student_repository.get_student_courses(student_id)
    
    if courses is None:
        abort(404, description='E004: Student not found')

    return jsonify([{"course_id": course.id, "name": course.name, "level": course.level} for course in courses])

@app.route('/students/<int:student_id>/enroll', methods=['PUT'])
def update_student_enrollment(student_id):
    """
    Update a student's course enrollment.

    Params:
    - student_id (int): The ID of the student
    - Request Body: { "course_ids": [integer] }

    Returns:
    - Response: { "student_id": "integer", "enrolled_courses": [...] }
    """
    data = request.get_json()

    if not data or 'course_ids' not in data:
        abort(400, description='E001: Invalid input, expected {"course_ids": [...]}')

    course_ids = data['course_ids']

    # Validate course_ids is a list of integers
    if not isinstance(course_ids, list) or not all(isinstance(course_id, int) for course_id in course_ids):
        abort(400, description='E002: course_ids must be an array of integers')

    # Logic to update the student's enrollment
    try:
        enrolled_courses = student_repository.update_student_courses(student_id, course_ids)
    except IntegrityError as e:
        abort(400, description=f'E003: Update error - {str(e)}')

    return jsonify({
        "student_id": student_id,
        "enrolled_courses": [{"course_id": course.id, "name": course.name, "level": course.level} for course in enrolled_courses]
    })