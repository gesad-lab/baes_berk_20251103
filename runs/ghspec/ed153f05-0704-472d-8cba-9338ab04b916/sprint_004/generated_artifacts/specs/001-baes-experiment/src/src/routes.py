```python
from flask import request, jsonify, abort
from src.database import get_db
from src.models import Student, Course, StudentCourse
from src.schemas import StudentCourseSchema

@app.route('/students/<int:id>/courses', methods=['POST'])
def enroll_student_in_course(id):
    """Enroll a student in a specified course.

    Args:
        id (int): The ID of the student.

    Returns:
        JSON response with success or error message.
    """
    db = get_db()
    
    # Check if the student exists in the database
    student = db.session.query(Student).filter(Student.id == id).first()
    if not student:
        # If the student does not exist, return a structured error response
        return jsonify({"error": {"code": "E001", "message": "Student does not exist."}}), 404

    # Extract course ID from the request
    data = request.get_json()
    course_id = data.get("course_id")
    
    # Check for valid course ID in the database
    course = db.session.query(Course).filter(Course.id == course_id).first()
    if not course:
        return jsonify({"error": {"code": "E002", "message": "Course does not exist."}}), 404
    
    # Associate student with course
    student_course = StudentCourse(student_id=id, course_id=course_id)
    db.session.add(student_course)
    db.session.commit()
    
    return jsonify({"message": "Student successfully enrolled in the course."}), 201

@app.route('/students/<int:id>/courses', methods=['GET'])
def get_student_courses(id):
    """Retrieve all courses associated with a student.

    Args:
        id (int): The ID of the student.

    Returns:
        JSON response with the list of courses or error message.
    """
    db = get_db()
    
    # Check if the student exists in the database
    student = db.session.query(Student).filter(Student.id == id).first()
    if not student:
        return jsonify({"error": {"code": "E001", "message": "Student does not exist."}}), 404

    # Retrieve all courses associated with the student
    student_courses = db.session.query(StudentCourse).filter(StudentCourse.student_id == id).all()
    course_ids = [student_course.course_id for student_course in student_courses]

    # From course_ids, get detailed course information
    courses = db.session.query(Course).filter(Course.id.in_(course_ids)).all()
    course_list = [{"id": course.id, "name": course.name, "level": course.level} for course in courses]

    return jsonify(course_list)
```