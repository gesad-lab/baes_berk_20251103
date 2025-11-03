```python
from flask import Blueprint, request, jsonify, abort
from sqlalchemy.exc import NoResultFound
from src.models import db, Student, Course, StudentCourses
from src.schemas import EnrollmentSchema

# Create a Blueprint for the API routes
api_bp = Blueprint('api', __name__)

@api_bp.route('/students/<int:student_id>/enroll', methods=['POST'])
def enroll_in_courses(student_id):
    """Enroll a student in specified courses.
    
    Args:
        student_id (int): The ID of the student to enroll.

    Request body:
        JSON with an array of course IDs, e.g., {"course_ids": [1, 2, 3]}

    Returns:
        JSON representation of the updated Student including their courses.
    """
    # Validate the request body
    data = request.get_json()
    course_ids = data.get('course_ids')
    
    if not course_ids or not isinstance(course_ids, list):
        return abort(400, description="Invalid format: 'course_ids' must be a list.")

    # Check if the student exists
    student = Student.query.get(student_id)
    
    if not student:
        return abort(400, description=f"Student with ID {student_id} does not exist.")

    # Fetch and validate the courses
    courses = Course.query.filter(Course.id.in_(course_ids)).all()
    if len(courses) != len(course_ids):
        return abort(400, description="One or more course IDs are invalid.")

    # Enroll the student in the valid courses
    for course in courses:
        association = StudentCourses(student_id=student.id, course_id=course.id)
        db.session.add(association)

    db.session.commit()

    # Prepare the response data
    student_courses = [{'id': course.id, 'name': course.name} for course in courses]
    response_data = {
        'id': student.id,
        'name': student.name,
        'courses': student_courses
    }

    return jsonify(response_data), 200

@api_bp.route('/students/<int:student_id>', methods=['GET'])
def get_student_details(student_id):
    """Retrieve details of a specified student along with their enrolled courses.
    
    Args:
        student_id (int): The ID of the student to retrieve.

    Returns:
        JSON representation of the student with their courses.
    """
    # Get the student record
    student = Student.query.get(student_id)
    
    if not student:
        return abort(404, description=f"Student with ID {student_id} not found.")

    # Fetch enrolled courses
    enrolled_courses = db.session.query(Course).join(StudentCourses).filter(StudentCourses.student_id == student.id).all()
    courses_list = [{'id': course.id, 'name': course.name} for course in enrolled_courses]

    # Prepare the response data
    response_data = {
        'id': student.id,
        'name': student.name,
        'courses': courses_list
    }

    return jsonify(response_data), 200
```