# api/students.py

from flask import Blueprint, request, jsonify
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, ForeignKey
from sqlalchemy.exc import IntegrityError

students_bp = Blueprint('students', __name__)

# Database setup - adjust connection as needed
engine = create_engine('sqlite:///courses.db')
metadata = MetaData(bind=engine)

# Define the join table for student-course relationships
student_courses_table = Table('student_courses', metadata,
    Column('student_id', Integer, ForeignKey('students.id'), primary_key=True),
    Column('course_id', Integer, ForeignKey('courses.id'), primary_key=True)
)

# Create the table if it doesn't exist
metadata.create_all(engine)

def validate_student_and_course(student_id: int, course_id: int) -> bool:
    """Validate that both the student and course exist in the database."""
    # Assume these functions exist to check existence
    from services.student_service import student_exists
    from services.course_service import course_exists
    
    if not student_exists(student_id):
        return False
    if not course_exists(course_id):
        return False
    return True

@students_bp.route('/students/<int:student_id>/courses', methods=['POST'])
def enroll_student_in_course(student_id: int):
    """
    Enroll a student in a course.

    Path Parameter:
        student_id: int (required)
    
    Request Body:
        course_id: int (required)

    Response:
        JSON object with success message and updated student data.
    """
    request_data = request.get_json()
    
    # Validate request data
    if 'course_id' not in request_data:
        return jsonify({"error": {"code": "E001", "message": "course_id is required"}}), 400

    course_id = request_data['course_id']

    # Validate student and course existence
    if not validate_student_and_course(student_id, course_id):
        return jsonify({"error": {"code": "E002", "message": "Student or Course does not exist"}}), 404

    # Perform enrollment logic - Insert relationship to DB
    with engine.connect() as connection:
        try:
            connection.execute(student_courses_table.insert().values(student_id=student_id, course_id=course_id))
            return jsonify({"message": "Student enrolled in course successfully."}), 201
        except IntegrityError:
            return jsonify({"error": {"code": "E003", "message": "Enrollment already exists."}}), 409

@students_bp.route('/students/<int:student_id>/courses', methods=['GET'])
def get_student_courses(student_id: int):
    """
    Retrieve a list of courses a student is enrolled in.

    Path Parameter:
        student_id: int (required)

    Response:
        JSON array of course objects associated with the student.
    """
    # Assume this function exists to retrieve courses
    from services.course_service import get_courses_for_student
    
    courses = get_courses_for_student(student_id)
    if courses is None:
        return jsonify({"error": {"code": "E004", "message": "Student not found."}}), 404

    return jsonify(courses), 200