```python
# src/controllers/students.py

from flask import Blueprint, request, jsonify, abort
from sqlalchemy.exc import IntegrityError
from your_app_name.models import Student, Course, StudentCourse, db

students_bp = Blueprint('students', __name__)

@students_bp.route('/students/<int:student_id>/courses', methods=['GET'])
def retrieve_courses_for_student(student_id):
    """Retrieve courses for a specific student.
    
    Args:
        student_id (int): The ID of the student for whom to retrieve courses.
    
    Returns:
        JSON response containing a list of course objects related to the student.
        Returns 404 if the student is not found.
    """
    student = Student.query.get(student_id)
    if not student:
        abort(404, description="Student not found")
    
    # Retrieve all courses associated with the student
    courses = Course.query.join(StudentCourse).filter(StudentCourse.student_id == student.id).all()
    
    # Serialize the course data
    course_data = [{"id": course.id, "name": course.name} for course in courses]
    
    return jsonify(course_data), 200

@students_bp.route('/students/<int:student_id>/courses', methods=['POST'])
def associate_courses_with_student(student_id):
    """Associate courses with a specific student.
    
    Args:
        student_id (int): The ID of the student with whom to associate courses.
    
    Request Body:
        {
            "course_ids": [array_of_integers]
        }
    
    Returns:
        JSON response indicating success or an error message.
        Returns 404 if the student is not found.
    """
    student = Student.query.get(student_id)
    if not student:
        abort(404, description="Student not found")
    
    data = request.get_json()
    course_ids = data.get('course_ids', [])
    
    if not course_ids:
        abort(400, description="No course IDs provided")

    try:
        # Associate each course ID with the student
        for course_id in course_ids:
            course = Course.query.get(course_id)
            if course:
                # Create the association only if it doesn't already exist
                existing_association = StudentCourse.query.filter_by(student_id=student_id, course_id=course_id).first()
                if not existing_association:
                    new_association = StudentCourse(student_id=student_id, course_id=course_id)
                    db.session.add(new_association)
        
        db.session.commit()
        return jsonify({"message": "Courses associated successfully"}), 201
    
    except IntegrityError:
        db.session.rollback()
        abort(400, description="Invalid course ID provided")  # Handles foreign key constraint errors
    except Exception as e:
        db.session.rollback()
        abort(500, description="An unexpected error occurred: " + str(e))
```