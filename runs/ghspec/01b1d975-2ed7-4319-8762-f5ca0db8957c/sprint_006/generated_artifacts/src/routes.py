```python
from flask import Blueprint, jsonify, request
from src.models import db, Course, Teacher  # Importing models
from src.validation import validate_course_exists, validate_teacher_exists

# Create a Blueprint for routes
routes = Blueprint('routes', __name__)

@routes.route('/courses/<int:course_id>', methods=['GET'])
def get_course_details(course_id):
    """
    Retrieve details of a specific Course including its assigned Teacher.
    
    Parameters:
    - course_id: ID of the Course to retrieve details for
    
    Returns:
    - JSON response with Course details and associated Teacher info or 404 Not Found.
    """
    # Validate Course existence
    course = validate_course_exists(course_id)
    if not course:
        return jsonify({'error': {'code': 'E404', 'message': 'Course not found'}}), 404
    
    # Prepare response data
    course_data = {
        'id': course.id,
        'name': course.name,
        'description': course.description,
    }
    
    # Include Teacher info if assigned
    if course.teacher_id:
        teacher = Teacher.query.get(course.teacher_id)
        if teacher:
            course_data['teacher'] = {
                'name': teacher.name,
                'email': teacher.email
            }

    return jsonify(course_data), 200

# Other routes for assigning teachers can be added here similarly
```