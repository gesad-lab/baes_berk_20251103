from flask import request, jsonify
from models import Course, db  # Importing the Course model and database session

def create_course():
    """Create a new Course with a name and level."""
    data = request.get_json()
    
    # Extracting name and level from the JSON payload
    name = data.get('name')
    level = data.get('level')
    
    # Input validation: both fields are required
    if not name or not level:
        return jsonify({"error": {"code": "E001", "message": "Name and Level are required"}}), 400
    
    # Creating a new Course instance
    course = Course(name=name, level=level)
    
    try:
        # Adding to the database session and committing
        db.session.add(course)
        db.session.commit()
    except Exception as e:
        # Handle any errors during database commit, return an error message
        db.session.rollback()  # Rollback session on error
        return jsonify({"error": {"code": "E002", "message": "Failed to create course", "details": str(e)}}), 500
    
    # Successful creation response
    return jsonify({"id": course.id, "name": course.name, "level": course.level}), 201

def get_course(id):
    """Retrieve a Course by ID."""
    course = Course.query.get(id)
    
    # If the course does not exist, return a 404 error
    if not course:
        return jsonify({"error": {"code": "E003", "message": "Course not found"}}), 404
    
    # Return the course details in JSON format
    return jsonify({"id": course.id, "name": course.name, "level": course.level}), 200