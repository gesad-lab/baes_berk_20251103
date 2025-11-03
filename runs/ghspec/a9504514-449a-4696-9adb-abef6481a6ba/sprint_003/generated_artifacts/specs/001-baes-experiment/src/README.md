```python
# src/services.py

from flask import request, jsonify
from src.models import Course
from src.database import db

def create_course():
    """
    Create a new course with the provided name and level.
    
    Expects a JSON body with 'name' and 'level'. If both fields are present, 
    adds the course to the database and returns the course details.
    
    Returns:
        A response with a success message and course details or an error message.
    """
    data = request.get_json()
    
    # Input validation
    name = data.get('name')
    level = data.get('level')
    
    if not name:
        return jsonify({"error": {"code": "E001", "message": "Name field is required."}}), 400
    if not level:
        return jsonify({"error": {"code": "E002", "message": "Level field is required."}}), 400

    try:
        # Create a new course instance
        new_course = Course(name=name, level=level)
        
        # Add course to the database
        db.session.add(new_course)
        db.session.commit()
        
        return jsonify({
            "id": new_course.id,
            "name": new_course.name,
            "level": new_course.level
        }), 201

    except Exception as e:
        # Log and return a generic error message
        db.session.rollback()  # Rollback the session in case of an error
        return jsonify({"error": {"code": "E003", "message": "Failed to create course."}}), 500

def retrieve_courses():
    """
    Retrieve all courses from the database.
    
    Returns:
        A JSON array of all courses with their name and level.
    """
    try:
        # Query all courses from the database
        courses = Course.query.all()
        
        # Serialize course data
        courses_data = [{"id": course.id, "name": course.name, "level": course.level} for course in courses]
        
        return jsonify(courses_data), 200
    
    except Exception as e:
        # Log and return a generic error message
        return jsonify({"error": {"code": "E004", "message": "Failed to retrieve courses."}}), 500
```