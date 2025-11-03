```python
from flask import Blueprint, request, jsonify
from your_application.models import db, Student, Course, StudentCourse
from sqlalchemy.exc import IntegrityError

students_bp = Blueprint('students', __name__)

@students_bp.route('/students/<int:student_id>/courses', methods=['POST'])
def associate_course(student_id):
    """
    Associate a course with a student.

    Parameters:
    - student_id: ID of the student to associate courses with

    Request Body:
    - JSON Object with the following properties:
        - course_id: ID of the course to be associated

    Returns:
    - 201: Course successfully associated
    - 400: Bad request if course ID is invalid
    - 404: Not found if student or course does not exist
    """
    data = request.get_json()
    course_id = data.get("course_id")

    # Validate input
    if not course_id:
        return jsonify({"error": {"code": "E001", "message": "course_id is required"}}), 400

    student = Student.query.get(student_id)
    course = Course.query.get(course_id)

    if not student:
        return jsonify({"error": {"code": "E002", "message": "Student not found"}}), 404
    if not course:
        return jsonify({"error": {"code": "E003", "message": "Course not found"}}), 404

    # Create association
    student_course = StudentCourse(student_id=student_id, course_id=course_id)

    try:
        db.session.add(student_course)
        db.session.commit()
        return jsonify({"message": "Course successfully associated"}), 201
    except IntegrityError:
        db.session.rollback()
        return jsonify({"error": {"code": "E004", "message": "Course already associated with student"}}), 400

@students_bp.route('/students/<int:student_id>/courses', methods=['GET'])
def get_courses_for_student(student_id):
    """
    Retrieve all courses associated with a specific student.

    Parameters:
    - student_id: ID of the student to fetch courses for

    Returns:
    - 200: List of courses associated with the student
    - 404: Not found if the student does not exist
    """
    student = Student.query.get(student_id)

    if not student:
        return jsonify({"error": {"code": "E002", "message": "Student not found"}}), 404

    # Query for courses associated with the student
    courses = db.session.query(Course).join(StudentCourse).filter(StudentCourse.student_id == student_id).all()

    course_details = [{"id": course.id, "name": course.name} for course in courses]
    return jsonify(course_details), 200
```