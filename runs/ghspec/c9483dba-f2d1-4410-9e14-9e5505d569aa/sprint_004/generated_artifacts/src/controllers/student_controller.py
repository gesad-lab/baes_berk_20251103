```python
from flask import request, jsonify
from models import Student, Course, db

def assign_course(student_id):
    """Assign a course to a student given their IDs.

    Args:
        student_id (int): The ID of the student to whom the course will be assigned.

    Returns:
        Response: JSON response indicating the result of the operation.
    """
    data = request.get_json()  # Retrieve JSON data from the request
    course_id = data.get('course_id')

    # Validate that a course ID has been provided
    if not course_id:
        return jsonify({"error": {"code": "E001", "message": "Course ID is required"}}), 400

    student = Student.query.get(student_id)  # Get the student by ID
    if not student:
        return jsonify({"error": {"code": "E002", "message": "Student not found"}}), 404  # Handle a non-existent student

    course = Course.query.get(course_id)  # Get the course by ID
    if not course:
        return jsonify({"error": {"code": "E003", "message": "Course not found"}}), 404  # Handle a non-existent course

    # Establish the relationship by adding the course to the student's courses
    student.courses.append(course)
    db.session.commit()  # Commit the changes to the database

    # Prepare the response with the updated student details
    return jsonify({
        "student_id": student.id,
        "courses": [course.name for course in student.courses]
    }), 200

def retrieve_student_with_courses(student_id):
    """Retrieve a student's details along with their associated courses.

    Args:
        student_id (int): The ID of the student whose details are to be fetched.

    Returns:
        Response: JSON response with the student details and their courses.
    """
    student = Student.query.get(student_id)  # Get the student by ID
    if not student:
        return jsonify({"error": {"code": "E002", "message": "Student not found"}}), 404  # Handle a non-existent student

    # Prepare the response with the student's details
    return jsonify({
        "student_id": student.id,
        "name": student.name,
        "courses": [course.name for course in student.courses]
    }), 200
```