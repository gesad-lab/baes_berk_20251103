from flask import Flask, request, jsonify
from models import db, Course
from services.course_service import create_course, get_course_by_id, list_courses

app = Flask(__name__)

@app.route('/api/v1/courses', methods=['POST'])
def add_course():
    """Create a new course."""
    data = request.get_json()
    
    # Validate request data
    course_name = data.get('name')
    course_level = data.get('level')

    if not course_name or not isinstance(course_name, str):
        return jsonify({"error": {"code": "E001", "message": "Invalid course name; it must be a non-empty string."}}), 400
    
    if not course_level or not isinstance(course_level, str):
        return jsonify({"error": {"code": "E002", "message": "Invalid course level; it must be a non-empty string."}}), 400
    
    # Call service to create course
    try:
        course = create_course(course_name, course_level)
    except Exception as e:
        return jsonify({"error": {"code": "E003", "message": str(e)}}), 500

    return jsonify(course.to_dict()), 201  # Return the created course data

@app.route('/api/v1/courses/<int:course_id>', methods=['GET'])
def get_course(course_id):
    """Retrieve a course by its ID."""
    course = get_course_by_id(course_id)
    
    if not course:
        return jsonify({"error": {"code": "E004", "message": "Course not found."}}), 404
    
    return jsonify(course.to_dict()), 200  # Return course data

@app.route('/api/v1/courses', methods=['GET'])
def get_courses():
    """Retrieve a list of courses."""
    courses = list_courses()
    return jsonify([course.to_dict() for course in courses]), 200  # Return list of courses

if __name__ == '__main__':
    app.run(debug=True)