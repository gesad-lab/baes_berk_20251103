```python
from flask import Blueprint, request, jsonify
from app.models import Student, Course, student_courses
from app import db

bp = Blueprint('students', __name__)

@bp.route('/students/<int:student_id>/courses', methods=['POST'])
def enroll_student_in_course(student_id):
    """Enroll a student in a specific course.
    
    Args:
        student_id (int): The ID of the student to enroll.
        course_id (int): The ID of the course to enroll the student in.
    
    Returns:
        Response: JSON confirmation of the enrollment including student and course details.
                  Returns 201 Created on success.
    """
    data = request.json
    course_id = data.get('course_id')

    if not course_id:
        return jsonify({"error": {"code": "E001", "message": "course_id is required."}}), 400

    # Adding the student-course relationship
    student = Student.query.get(student_id)
    course = Course.query.get(course_id)

    if not student or not course:
        return jsonify({"error": {"code": "E002", "message": "Invalid student or course ID."}}), 404

    # Only proceed if the relationship does not already exist
    if student_courses.query.filter_by(student_id=student_id, course_id=course_id).first():
        return jsonify({"error": {"code": "E003", "message": "Student is already enrolled in this course."}}), 400

    # Enroll the student
    new_enrollment = student_courses(student_id=student_id, course_id=course_id)
    db.session.add(new_enrollment)
    db.session.commit()
    
    return jsonify({
        "message": "Student enrolled successfully.",
        "student_id": student.id,
        "course_id": course.id,
        "course_name": course.name,
        "course_level": course.level
    }), 201

@bp.route('/students/<int:student_id>/courses', methods=['GET'])
def list_students_courses(student_id):
    """List all courses that a student is enrolled in.
    
    Args:
        student_id (int): The ID of the student whose courses are to be listed.
    
    Returns:
        Response: JSON array of course records associated with the student.
                  Returns 200 OK on success.
    """
    student = Student.query.get(student_id)

    if not student:
        return jsonify({"error": {"code": "E002", "message": "Invalid student ID."}}), 404

    courses = db.session.query(Course).join(student_courses).filter(student_courses.c.student_id == student_id).all()

    course_list = [{"course_id": course.id, "course_name": course.name, "course_level": course.level} for course in courses]
    
    return jsonify(course_list), 200

@bp.route('/students/<int:student_id>/courses/<int:course_id>', methods=['DELETE'])
def unenroll_student_from_course(student_id, course_id):
    """Unenroll a student from a specific course.
    
    Args:
        student_id (int): The ID of the student to unenroll.
        course_id (int): The ID of the course to remove from the student's enrollments.
    
    Returns:
        Response: 204 No Content when the unenrollment is successful.
    """
    student = Student.query.get(student_id)

    if not student:
        return jsonify({"error": {"code": "E002", "message": "Invalid student ID."}}), 404

    enrollment = student_courses.query.filter_by(student_id=student_id, course_id=course_id).first()

    if not enrollment:
        return jsonify({"error": {"code": "E004", "message": "This student is not enrolled in the specified course."}}), 404

    db.session.delete(enrollment)
    db.session.commit()
    
    return '', 204
```