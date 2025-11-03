```python
import logging
from flask import Flask, request, jsonify
from models.course import Course  # Assuming the Course model exists in models/course.py
from your_database_module import db  # Replace with your actual database module

app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s %(message)s')
logger = logging.getLogger(__name__)

@app.route('/courses', methods=['POST'])
def create_course():
    """Creates a new course with the provided name and level."""
    data = request.get_json()
    name = data.get('name')
    level = data.get('level')
    
    # Validate input
    if not name or not isinstance(name, str):
        logger.error("Validation error: 'name' is required and must be a string.")
        return jsonify({"error": {"code": "E001", "message": "'name' is required and must be a string."}}), 400
    if not level or not isinstance(level, str):
        logger.error("Validation error: 'level' is required and must be a string.")
        return jsonify({"error": {"code": "E002", "message": "'level' is required and must be a string."}}), 400
    
    # Create course
    new_course = Course(name=name, level=level)
    db.session.add(new_course)
    
    try:
        db.session.commit()
        logger.info(f"Course created: {new_course.id} - {new_course.name} ({new_course.level})")
        return jsonify({"id": new_course.id, "name": new_course.name, "level": new_course.level}), 201
    except Exception as e:
        db.session.rollback()
        logger.error(f"Error creating course: {str(e)}")
        return jsonify({"error": {"code": "E003", "message": "Failed to create course."}}), 500

@app.route('/courses/<int:id>', methods=['GET'])
def get_course(id):
    """Retrieves a course by ID."""
    course = Course.query.get(id)
    if course is None:
        logger.warning(f"Course not found: {id}")
        return jsonify({"error": {"code": "E004", "message": "Course not found."}}), 404

    logger.info(f"Course retrieved: {course.id} - {course.name} ({course.level})")
    return jsonify({"id": course.id, "name": course.name, "level": course.level}), 200

@app.route('/courses/<int:id>', methods=['PUT'])
def update_course(id):
    """Updates a course's name and/or level by ID."""
    data = request.get_json()
    course = Course.query.get(id)
    
    if course is None:
        logger.warning(f"Attempt to update non-existing course: {id}")
        return jsonify({"error": {"code": "E004", "message": "Course not found."}}), 404
    
    name = data.get('name')
    level = data.get('level')
    
    # Validate the presence of at least one field for update
    if not name and not level:
        logger.error("Validation error: At least one of 'name' or 'level' must be provided for update.")
        return jsonify({"error": {"code": "E005", "message": "At least one of 'name' or 'level' must be provided."}}), 400
    
    if name:
        if not isinstance(name, str):
            logger.error("Validation error: 'name' must be a string.")
            return jsonify({"error": {"code": "E001", "message": "'name' must be a string."}}), 400
        course.name = name

    if level:
        if not isinstance(level, str):
            logger.error("Validation error: 'level' must be a string.")
            return jsonify({"error": {"code": "E002", "message": "'level' must be a string."}}), 400
        course.level = level
    
    try:
        db.session.commit()
        logger.info(f"Course updated: {course.id} - {course.name} ({course.level})")
        return jsonify({"id": course.id, "name": course.name, "level": course.level}), 200
    except Exception as e:
        db.session.rollback()
        logger.error(f"Error updating course {id}: {str(e)}")
        return jsonify({"error": {"code": "E006", "message": "Failed to update course."}}), 500
```