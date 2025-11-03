```python
from flask import Blueprint, request, jsonify, abort
from models.student_courses import StudentCourses  # Import the StudentCourses model
from services.enrollment_service import EnrollmentService  # Import the enrollment service
from http import HTTPStatus

enrollment_bp = Blueprint('enrollment', __name__)

@enrollment_bp.route('/api/v1/enrollments', methods=['DELETE'])
def unenroll_student_from_course():
    """
    Remove a student's enrollment from a course.
    
    Request Body:
    {
        "student_id": int,
        "course_id": int
    }

    Returns:
        JSON response indicating the result of the unenrollment.
    """
    data = request.get_json()

    # Validate request body
    if not data or 'student_id' not in data or 'course_id' not in data:
        abort(HTTPStatus.BAD_REQUEST, description="E001: Missing student_id or course_id in request body")

    student_id = data['student_id']
    course_id = data['course_id']

    # Attempt to unenroll the student via the service
    result = EnrollmentService.unenroll_student_from_course(student_id, course_id)

    if result:
        return jsonify({"message": "Successfully unenrolled the student from the course."}), HTTPStatus.OK
    else:
        abort(HTTPStatus.NOT_FOUND, description="E002: Enrollment relationship not found")

# Ensure to register this blueprint in your main app initialization
```