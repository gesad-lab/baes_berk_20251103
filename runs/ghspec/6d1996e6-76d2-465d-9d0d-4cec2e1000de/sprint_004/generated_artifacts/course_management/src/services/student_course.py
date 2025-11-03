```python
# course_management/src/services/student_course.py

from flask import jsonify, abort
from models.student_course import StudentCourse  # Importing the junction model
from db.database import db_session

def unenroll_student_from_course(student_id: int, course_id: int):
    """
    Unenroll a student from a specific course.

    Parameters:
    - student_id (int): The ID of the student to unenroll.
    - course_id (int): The ID of the course to unenroll from.

    Returns:
    - JSON response with success message or error.
    """
    # Locate the student_course relationship
    enrollment = db_session.query(StudentCourse).filter_by(student_id=student_id, course_id=course_id).first()
    
    if enrollment:
        # Remove the enrollment from the database
        db_session.delete(enrollment)
        db_session.commit()
        return jsonify({"message": "Successfully unenrolled from course."}), 200
    else:
        # Return a 404 if the enrollment does not exist
        abort(404, description=f"Enrollment for student ID {student_id} and course ID {course_id} not found.")
```