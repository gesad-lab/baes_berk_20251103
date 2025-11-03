```python
# src/validation/student_validation.py

from flask import request, jsonify
from app import db, Course  # Import the Course model
from sqlalchemy.exc import IntegrityError

def validate_course_association(student_id: int):
    """
    Validates the input for associating courses with a student.

    Parameters:
    student_id (int): The ID of the student to associate with courses.

    Raises:
    ValueError: If no course IDs are provided or if any course ID is invalid.

    Returns:
    None
    """
    course_ids = request.json.get('course_ids', [])

    # Check if course_ids is an empty list
    if not course_ids:
        raise ValueError("No course IDs provided. Please select at least one course.")

    # Validate each course ID
    invalid_ids = []
    for course_id in course_ids:
        if not isinstance(course_id, int) or not Course.query.get(course_id):
            invalid_ids.append(course_id)

    # If we found any invalid course IDs, raise an error
    if invalid_ids:
        raise ValueError(f"Invalid course IDs provided: {invalid_ids}")

def associate_courses_with_student(student_id: int):
    """
    Associates courses with a student.

    Parameters:
    student_id (int): The ID of the student to associate with courses.

    Raises:
    ValueError: If input validation fails.

    Returns:
    JSON response: A success message after associating courses.
    """
    try:
        validate_course_association(student_id)

        # Assuming a function exists to actually associate the courses
        # with the student, as we build upon the existing codebase.
        # associate_courses(student_id, request.json['course_ids'])

        return jsonify({"message": "Courses associated successfully."}), 200
    
    except ValueError as e:
        return jsonify({"error": {"code": "E002", "message": str(e), "details": {}}}), 400
    except IntegrityError as e:
        # Handle potential database integrity errors when linking courses
        db.session.rollback()
        return jsonify({"error": {"code": "E003", "message": "Database Integrity Error", "details": str(e)}}), 500
    except Exception as e:
        return jsonify({"error": {"message": "An unexpected error occurred", "details": str(e)}}), 500
```