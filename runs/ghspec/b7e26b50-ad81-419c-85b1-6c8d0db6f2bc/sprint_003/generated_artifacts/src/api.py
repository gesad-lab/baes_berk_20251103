```python
# src/api.py

from flask import Flask, request, jsonify, abort
from your_app import create_app, db  # Import your app and db instance
from your_app.models import Course  # Import the Course model
from your_app.errors import handle_bad_request  # Import centralized error handling

app = create_app()

@app.route('/courses', methods=['POST'])
def create_course():
    """Create a new course with the specified name and level."""
    data = request.get_json()

    if not data:
        abort(400, description="Request body must be JSON.")

    name = data.get('name')
    level = data.get('level')

    if not name:
        abort(400, description="Name is required.")
    if not level:
        abort(400, description="Level is required.")

    # Create a new Course instance
    new_course = Course(name=name, level=level)

    # Add the new course to the database session and commit
    db.session.add(new_course)
    db.session.commit()

    # Construct response
    response = {
        'id': new_course.id,
        'name': new_course.name,
        'level': new_course.level
    }

    return jsonify(response), 201

@app.route('/courses/<int:id>', methods=['GET'])
def get_course(id):
    """Retrieve details of a specific course by ID."""
    course = Course.query.get(id)

    if course is None:
        abort(404, description="Course not found.")

    response = {
        'id': course.id,
        'name': course.name,
        'level': course.level
    }

    return jsonify(response), 200


# Add any other necessary routes or functions below
```