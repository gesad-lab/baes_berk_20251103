```python
# src/error_handling.py

from flask import jsonify
from api.models import Student, Course, Enrollment
from sqlalchemy.exc import IntegrityError

def assign_courses_to_student(student_id, course_ids):
    """Assigns a list of courses to a specific student.

    Args:
        student_id (int): The ID of the student to assign courses to.
        course_ids (List[int]): A list of course IDs to assign.

    Returns:
        dict: Updated student data including enrolled courses or error response.
    """
    # Validate the student exists
    student = Student.query.get(student_id)
    if not student:
        return {"error": {"code": "E001", "message": "Student not found."}}, 404

    # Fetch courses to validate existence
    courses = Course.query.filter(Course.id.in_(course_ids)).all()
    if len(courses) != len(course_ids):
        return {"error": {"code": "E002", "message": "One or more course IDs are invalid."}}, 400
    
    # Clear previous enrollments before assigning new ones
    student.courses.clear()
    student.courses.extend(courses)

    # Persist changes to the database
    try:
        db.session.commit()  # Commit changes to the database
    except IntegrityError:
        db.session.rollback()  # Rollback on error
        return {"error": {"code": "E003", "message": "Failed to assign courses."}}, 500

    # Return updated student data with courses
    return {
        "student_id": student.id,
        "student_name": student.name,
        "courses": [{"id": course.id, "name": course.name} for course in student.courses]
    }, 200

def get_student_with_courses(student_id):
    """Retrieves a student's data along with their enrolled courses.

    Args:
        student_id (int): The ID of the student to retrieve.

    Returns:
        dict: Student data including enrolled courses or error response.
    """
    student = Student.query.get(student_id)
    if not student:
        return {"error": {"code": "E001", "message": "Student not found."}}, 404

    # Build the response with student information and courses
    student_data = {
        "student_id": student.id,
        "student_name": student.name,
        "courses": [{"id": course.id, "name": course.name} for course in student.courses]
    }
    
    return jsonify(student_data), 200
```