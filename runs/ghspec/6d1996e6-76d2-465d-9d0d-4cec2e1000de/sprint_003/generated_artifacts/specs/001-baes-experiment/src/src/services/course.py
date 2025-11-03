```python
# src/services/course.py

from models.course import Course
from db.database import db_session
from flask import jsonify, request, abort

def create_course():
    """
    Create a new course record.

    :return: JSON response with course details or error message
    """
    data = request.get_json()

    # Extract name and level from the request data
    name = data.get("name")
    level = data.get("level")

    # Validate course name and level
    if not name or not isinstance(name, str) or len(name.strip()) == 0:
        abort(400, jsonify({"error": {"code": "E001", "message": "Invalid course name. It cannot be empty."}}))
    
    if not level or not isinstance(level, str) or len(level.strip()) == 0:
        abort(400, jsonify({"error": {"code": "E002", "message": "Invalid course level. It cannot be empty."}}))

    # Create a new course instance
    new_course = Course(name=name.strip(), level=level.strip())

    # Add the new course to the database session
    db_session.add(new_course)
    db_session.commit()

    # Return the created course as JSON
    return jsonify({"id": new_course.id, "name": new_course.name, "level": new_course.level}), 201
```