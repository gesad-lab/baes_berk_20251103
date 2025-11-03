```python
from flask import Flask, jsonify, request, abort
from src.models import Course  # Importing the Course model from models.py
from src.repositories import CourseRepository  # Assuming a repository exists for data operations
from sqlalchemy.exc import IntegrityError

app = Flask(__name__)

# Initialize repository
course_repository = CourseRepository()

@app.route('/courses', methods=['POST'])
def create_course():
    """Create a new course with name and level.
    
    Request must contain:
    - name: str (Course name, cannot be empty)
    - level: str (Course level, cannot be empty)
    
    Returns:
    - JSON response with the created course's data and status code 201.
    """
    data = request.get_json()
    
    # Validate input
    if not data or not 'name' in data or not data['name'] or not 'level' in data or not data['level']:
        abort(400, 'E001: Invalid request body. Name and level are required.')
    
    # Create the Course object
    new_course = Course(name=data['name'], level=data['level'])
    
    try:
        # Save the course to the repository
        course_repository.add(new_course)
        return jsonify(new_course.to_dict()), 201  # Assuming there's a method to convert Course to a dict
    except IntegrityError:
        abort(500, 'E002: Database error. Course could not be created.')

@app.route('/courses/<int:id>', methods=['GET', 'PUT'])
def course_operations(id):
    """Get course by ID or update existing course by ID.
    
    Returns course details for GET method with status code 200.
    Updates course details for PUT method with status code 204 on success.
    
    For PUT request, the request must contain:
    - name: str (Course name)
    - level: str (Course level)
    """
    if request.method == 'GET':
        course = course_repository.get_by_id(id)
        if course is None:
            abort(404, 'E003: Course not found.')
        return jsonify(course.to_dict()), 200
    
    elif request.method == 'PUT':
        data = request.get_json()
        
        # Validate input
        if not data or not 'name' in data or not 'level' in data:
            abort(400, 'E004: Invalid request body. Name and level are required.')

        course = course_repository.get_by_id(id)
        if course is None:
            abort(404, 'E003: Course not found.')

        # Update course attributes
        course.name = data['name']
        course.level = data['level']
        
        try:
            course_repository.update(course)
            return '', 204  # No content on successful update
        except IntegrityError:
            abort(500, 'E002: Database error. Course could not be updated.')

# Ensure to handle potential exceptions and log errors when necessary.
```