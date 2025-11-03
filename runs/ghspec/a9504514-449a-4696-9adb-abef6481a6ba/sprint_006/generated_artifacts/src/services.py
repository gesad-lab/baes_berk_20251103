```python
# src/services.py

from flask import jsonify, request, abort
from src.models import Course, Teacher
from src.database import db

def assign_teacher_to_course(course_id: str, teacher_id: str) -> tuple:
    """Assign a teacher to a specific course by course ID.

    Args:
        course_id (str): The ID of the course to which the teacher will be assigned.
        teacher_id (str): The ID of the teacher who will be assigned to the course.

    Returns:
        tuple: A JSON response with the status and updated course details or an error message.
    """
    # Retrieve the course by ID
    course = Course.query.get(course_id)
    if course is None:
        abort(404, description="Course not found")

    # Retrieve the teacher by ID
    teacher = Teacher.query.get(teacher_id)
    if teacher is None:
        abort(404, description="Teacher not found")

    # Assign the teacher to the course
    course.teacher_id = teacher.id
    db.session.commit()
    
    return jsonify({
        'message': 'Teacher assigned successfully',
        'course': {
            'id': course.id,
            'title': course.title,
            'description': course.description,
            'teacher': {
                'id': teacher.id,
                'name': teacher.name
            }
        }
    }), 200

def get_course_by_id(course_id: str) -> tuple:
    """Retrieve the details of a specific course, including the assigned teacher.

    Args:
        course_id (str): The ID of the course to retrieve.

    Returns:
        tuple: A JSON response containing the course details or an error message.
    """
    # Retrieve course by ID
    course = Course.query.get(course_id)
    if course is None:
        abort(404, description="Course not found")

    # Prepare course details along with teacher information
    teacher_info = {
        'id': course.teacher.id if course.teacher else None,
        'name': course.teacher.name if course.teacher else None
    }

    return jsonify({
        'id': course.id,
        'title': course.title,
        'description': course.description,
        'teacher': teacher_info
    }), 200
```