```python
# File: api.py

from flask import Flask, jsonify, request
from models.student import init_db  # Importing existing function for DB initialization
from models.course import Course   # Assuming the new Course model will be defined in models/course.py

app = Flask(__name__)

# Database initialization code
@app.before_first_request
def setup():
    init_db()

@app.route('/courses', methods=['POST'])
def create_course():
    """
    Create a new course.
    
    Request Body: 
    {
        "name": "string", 
        "level": "string"
    }
    
    Returns:
    JSON response with course information or error message if validation fails.
    """
    data = request.get_json()
    
    # Validate input
    if not data or 'name' not in data or 'level' not in data:
        return jsonify({"error": {"code": "E001", "message": "Invalid input data. Both 'name' and 'level' are required."}}), 400

    # Create a new course instance
    new_course = Course(name=data['name'], level=data['level'])
    
    # Assuming we have a method to save the new course to the database
    try:
        new_course.save()  # Method to save course to the database
        return jsonify({"message": "Course created", "course": {"name": new_course.name, "level": new_course.level}}), 201
    except Exception as e:
        return jsonify({"error": {"code": "E002", "message": "Failed to create course", "details": str(e)}}), 500

@app.route('/courses', methods=['GET'])
def get_courses():
    """
    Retrieve all courses.
    
    Returns:
    JSON list of courses.
    """
    try:
        courses = Course.query.all()  # Assuming we can query all courses from the database
        return jsonify([{"name": course.name, "level": course.level} for course in courses]), 200
    except Exception as e:
        return jsonify({"error": {"code": "E003", "message": "Failed to retrieve courses", "details": str(e)}}), 500

# Add a placeholder for app.run() if needed in the actual execution context
```