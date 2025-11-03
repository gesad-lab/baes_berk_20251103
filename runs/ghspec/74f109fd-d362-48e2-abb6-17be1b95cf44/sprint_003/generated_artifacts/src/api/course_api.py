```python
from flask import Blueprint, request, jsonify
from services.course_service import CourseService

course_api = Blueprint('course_api', __name__)
course_service = CourseService()

@course_api.route('/courses/<int:course_id>', methods=['GET'])
def get_course(course_id):
    """
    Retrieve a course by its ID.

    Parameters:
    - course_id (int): The ID of the course to retrieve.

    Returns:
    - JSON response containing course information or error message.
    """
    try:
        course = course_service.get_course(course_id)
        # Return the course details in a JSON response
        return jsonify({
            'id': course.id,
            'name': course.name,
            'level': course.level
        }), 200
    except ValueError as e:
        # Return error message if course not found
        return jsonify({
            'error': {
                'code': 'E404',
                'message': str(e)
            }
        }), 404
    except Exception as e:
        # Handle any unexpected errors
        return jsonify({
            'error': {
                'code': 'E500',
                'message': 'An unexpected error occurred.'
            }
        }), 500
```