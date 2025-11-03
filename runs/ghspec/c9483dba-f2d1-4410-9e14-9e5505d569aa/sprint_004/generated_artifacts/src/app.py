```python
from flask import request, jsonify
from models import Student, Course, db

def assign_course(student_id):
    """
    Assign a course to a student.
    
    Args:
        student_id (int): The ID of the student to whom the course will be assigned.

    Returns:
        JSON response with the updated Student details and status code.
    """
    data = request.get_json()
    course_id = data.get('course_id')

    # Validate input
    if not course_id:
        return jsonify({"error": {"code": "E001", "message": "Course ID is required"}}), 400

    student = Student.query.get(student_id)
    if not student:
        return jsonify({"error": {"code": "E002", "message": "Student not found"}}), 404

    course = Course.query.get(course_id)
    if not course:
        return jsonify({"error": {"code": "E003", "message": "Course not found"}}), 404

    # Assign the course to the student
    student.courses.append(course)
    db.session.commit()

    # Prepare response data
    response_data = {
        "student_id": student.id,
        "courses": [course.id for course in student.courses]
    }
    
    return jsonify(response_data), 200


def retrieve_student(student_id):
    """
    Retrieve a student's details along with their enrolled courses.
    
    Args:
        student_id (int): The ID of the student to retrieve.

    Returns:
        JSON response with the student's details and status code.
    """
    student = Student.query.get(student_id)
    if not student:
        return jsonify({"error": {"code": "E002", "message": "Student not found"}}), 404

    response_data = {
        "student_id": student.id,
        "name": student.name,
        "email": student.email,
        "courses": [course.id for course in student.courses]
    }
    
    return jsonify(response_data), 200
```