```python
# src/app.py

from flask import Flask, jsonify, request
from services.course import create_course, get_course_by_id, update_course
from models.course import Course  # Assuming this model exists
from db.database import db_session

app = Flask(__name__)

# Route for creating a new course
@app.route('/courses', methods=['POST'])
def add_course():
    """
    Create a new course.

    Expected JSON payload:
    {
        "name": "Course Name",
        "level": "Course Level"
    }

    :return: JSON response with course details or error message
    """
    return create_course()

# Route for retrieving course information by ID
@app.route('/courses/<int:course_id>', methods=['GET'])
def get_course(course_id):
    """
    Retrieve a course by ID.

    :param course_id: ID of the course to retrieve
    :return: JSON response with course details or error message
    """
    return get_course_by_id(course_id)

# Route for updating course information
@app.route('/courses/<int:course_id>', methods=['PUT'])
def update_course_info(course_id):
    """
    Update a course's name or level.

    Expected JSON payload:
    {
        "name": "New Course Name",
        "level": "New Course Level"
    }

    :param course_id: ID of the course to update
    :return: JSON response indicating success or failure
    """
    return update_course(course_id)

if __name__ == '__main__':
    app.run(debug=True)
```