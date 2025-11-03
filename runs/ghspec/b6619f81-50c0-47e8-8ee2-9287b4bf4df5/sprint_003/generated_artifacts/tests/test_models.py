```python
from flask import jsonify, request, abort
from src.models import Course  # Assuming that a Course model exists in models.py
from src.repositories import CourseRepository  # Assuming there's a repository for course data operations

@app.route('/courses', methods=['POST'])
def create_course():
    """
    Create a new course with the provided name and level.

    Request Body:
    - name (str): The name of the course, must be non-empty.
    - level (str): The level of the course, must be non-empty.

    Returns:
    - 201 Created with course details on success
    - 400 Bad Request if name or level is missing
    """
    data = request.get_json()

    # Validate input
    name = data.get('name')
    level = data.get('level')

    if not name or not isinstance(name, str) or not name.strip():
        abort(400, description="E001: Course name is required and must be a non-empty string.")
    
    if not level or not isinstance(level, str) or not level.strip():
        abort(400, description="E002: Course level is required and must be a non-empty string.")

    # Create a new course
    course = Course(name=name, level=level)
    course_repository = CourseRepository()
    course_repository.add(course)  # Assuming add handles database logic

    return jsonify({
        'id': course.id,
        'name': course.name,
        'level': course.level
    }), 201

@app.route('/courses/<int:id>', methods=['PUT'])
def update_course(id):
    """
    Update an existing course's name and level.

    Request Body:
    - name (str): The new name of the course, must be non-empty.
    - level (str): The new level of the course, must be non-empty.

    Returns:
    - 200 OK with updated course details on success
    - 404 Not Found if the course doesn't exist
    - 400 Bad Request if name or level is invalid
    """
    data = request.get_json()

    name = data.get('name')
    level = data.get('level')

    if name is not None and (not isinstance(name, str) or not name.strip()):
        abort(400, description="E001: Course name must be a non-empty string.")
    
    if level is not None and (not isinstance(level, str) or not level.strip()):
        abort(400, description="E002: Course level must be a non-empty string.")

    course_repository = CourseRepository()
    course = course_repository.get_by_id(id)  # Assuming this retrieves the course

    if course is None:
        abort(404, description="Course not found.")

    if name is not None:
        course.name = name
    if level is not None:
        course.level = level

    course_repository.update(course)  # Assuming update handles database logic

    return jsonify({
        'id': course.id,
        'name': course.name,
        'level': course.level
    }), 200
```