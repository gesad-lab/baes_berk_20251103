```python
from flask import Flask, request, jsonify
from models import Course, db  # Import Course model and database instance

app = Flask(__name__)

@app.route('/courses', methods=['POST'])
def create_course():
    """Create a new Course with a name and level."""
    data = request.get_json()
    name = data.get('name')
    level = data.get('level')

    # Validate input
    if not name or not level:
        return jsonify({"error": {"code": "E001", "message": "Name and Level are required"}}), 400

    # Create and save new Course
    course = Course(name=name, level=level)
    db.session.add(course)
    db.session.commit()

    # Return the created Course details
    return jsonify({"id": course.id, "name": course.name, "level": course.level}), 201

@app.route('/courses/<int:id>', methods=['GET'])
def get_course(id):
    """Retrieve a Course by its ID."""
    course = Course.query.get(id)
    
    # Check if Course exists
    if not course:
        return jsonify({"error": {"code": "E002", "message": "Course not found"}}), 404

    # Return Course details
    return jsonify({"id": course.id, "name": course.name, "level": course.level}), 200
```