```python
from flask import Blueprint, request, jsonify
from src.models import db, Course, Teacher  # Import Course and Teacher models
from sqlalchemy.exc import IntegrityError

routes = Blueprint('routes', __name__)

@routes.route('/courses', methods=['POST'])
def create_course():
    """
    Create a new course with an optional teacher assignment.

    Returns:
        JSON response containing the created course and a success message.
    """
    data = request.json
    title = data.get('title')
    description = data.get('description')
    teacher_id = data.get('teacher_id')  # Optional teacher ID

    new_course = Course(title=title, description=description, teacher_id=teacher_id)

    db.session.add(new_course)
    try:
        db.session.commit()
        return jsonify({"message": "Course created successfully", "course": {
            "id": new_course.id,
            "title": new_course.title,
            "description": new_course.description,
            "teacher_id": new_course.teacher_id
        }}), 201
    except IntegrityError:
        db.session.rollback()
        return jsonify({"error": {"code": "E001", "message": "Invalid teacher ID."}}), 400

@routes.route('/courses/<int:course_id>', methods=['PUT'])
def update_course(course_id):
    """
    Update an existing course, allowing a change of assigned teacher.

    Parameters:
        course_id (int): The ID of the course to update.
    
    Returns:
        JSON response indicating the success or failure of the update operation.
    """
    data = request.json
    title = data.get('title')
    description = data.get('description')
    teacher_id = data.get('teacher_id')  # Optional teacher ID

    course = Course.query.get(course_id)
    if not course:
        return jsonify({"error": {"code": "E002", "message": "Course not found."}}), 404

    course.title = title if title else course.title
    course.description = description if description else course.description
    course.teacher_id = teacher_id if teacher_id is not None else course.teacher_id

    try:
        db.session.commit()
        return jsonify({"message": "Course updated successfully", "course": {
            "id": course.id,
            "title": course.title,
            "description": course.description,
            "teacher_id": course.teacher_id
        }}), 200
    except IntegrityError:
        db.session.rollback()
        return jsonify({"error": {"code": "E001", "message": "Invalid teacher ID."}}), 400

@routes.route('/courses/<int:course_id>', methods=['GET'])
def get_course(course_id):
    """
    Retrieve details of a specific course by ID.

    Parameters:
        course_id (int): The ID of the course to retrieve.
    
    Returns:
        JSON response containing course details or an error message.
    """
    course = Course.query.get(course_id)
    if not course:
        return jsonify({"error": {"code": "E002", "message": "Course not found."}}), 404

    return jsonify({"course": {
        "id": course.id,
        "title": course.title,
        "description": course.description,
        "teacher_id": course.teacher_id
    }}), 200
```