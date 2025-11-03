```python
from flask import Blueprint, request, jsonify
from models.student import Student  # Assuming the Student model is in models/student.py
from models.course import Course  # Assuming the Course model is in models/course.py
from database import session  # Assuming the database session is managed in database.py
from sqlalchemy import delete  # Importing delete for removing course associations

students_bp = Blueprint('students', __name__)

# Existing routes...

@students_bp.route('/students/<int:student_id>/courses/<int:course_id>', methods=['DELETE'])
def remove_course_from_student(student_id, course_id):
    """
    Remove a specific course from a student's course associations.
    
    Parameters:
        student_id (int): The ID of the student.
        course_id (int): The ID of the course to remove.
    
    Returns:
        JSON response with a confirmation message or an error message if the student does not exist.
    """
    # Fetch the student from the database
    student = session.query(Student).filter_by(id=student_id).first()
    
    if not student:
        return jsonify({"error": {"code": "E002", "message": "Student does not exist."}}), 404

    # Delete the association from the junction table
    stmt = delete(student_courses).where(student_courses.c.student_id == student_id, student_courses.c.course_id == course_id)
    result = session.execute(stmt)

    # Check if any row was deleted to confirm if the course was removed
    if result.rowcount == 0:
        return jsonify({"message": "No association found for this course."}), 404

    session.commit()

    return jsonify({"message": "Course removed successfully."}), 200
```