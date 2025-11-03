```python
from flask import Blueprint, request, jsonify
from src.models import Course, db
import logging

# Initialize logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

course_routes = Blueprint('course_routes', __name__)

@course_routes.route('/courses', methods=['POST'])
def create_course():
    """Create a new Course entity.
    
    Expected JSON payload:
    {
        "name": "Course Name",
        "level": "Course Level"
    }
    Returns a success response with course details or an error message.
    """
    data = request.get_json()

    # Validate required fields
    if 'name' not in data:
        logger.error("Attempt to create course without a name.")
        return jsonify({"error": {"code": "E001", "message": "Name is required."}}), 400
    
    if 'level' not in data:
        logger.error("Attempt to create course without a level.")
        return jsonify({"error": {"code": "E002", "message": "Level is required."}}), 400

    # Create and save the new course
    new_course = Course(name=data['name'], level=data['level'])
    db.session.add(new_course)

    try:
        db.session.commit()
        logger.info("Course created successfully: %s", new_course.id)
        return jsonify({"id": new_course.id, "name": new_course.name, "level": new_course.level}), 201
    except Exception as e:
        db.session.rollback()
        logger.exception("Failed to create course: %s", str(e))
        return jsonify({"error": {"code": "E003", "message": "Failed to create course."}}), 500

@course_routes.route('/courses', methods=['GET'])
def get_courses():
    """Retrieve all Course entities.
    
    Returns a list of all courses in JSON format.
    """
    courses = Course.query.all()
    course_list = [{"id": course.id, "name": course.name, "level": course.level} for course in courses]
    logger.info("Retrieved %d courses.", len(course_list))
    return jsonify(course_list)
```