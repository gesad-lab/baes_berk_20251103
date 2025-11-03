```python
from flask import Blueprint, request, jsonify
from marshmallow import ValidationError
from src.schemas import CourseSchema  # Import the CourseSchema for validation

courses_bp = Blueprint('courses', __name__)

# Initialize the Course schema
course_schema = CourseSchema()

@courses_bp.route('/courses', methods=['POST'])
def create_course():
    """Create a new Course with provided name and level."""
    try:
        # Validate and deserialize input data
        course_data = course_schema.load(request.json)
        
        # Here, you would typically add the course to the database
        # For demonstration, we'll just return the validated data
        return jsonify({"message": "Course created successfully", "course": course_data}), 201
    
    except ValidationError as err:
        # Return a 400 error with details if validation fails
        return jsonify({"error": {"code": "E001", "message": "Invalid input", "details": err.messages}}), 400

@courses_bp.route('/courses/<int:id>', methods=['GET'])
def get_course(id):
    """Retrieve a Course by its unique identifier."""
    # Here, you would fetch the course from the database using the provided ID
    # For demonstration, we assume the course is found
    # course = fetch_course_from_db(id) # Placeholder for actual database query
    
    # Example response (you would replace this with actual fetched data)
    course = {"id": id, "name": "Sample Course", "level": "Beginner"}
    return jsonify(course), 200
```