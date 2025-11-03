```python
# src/services.py
from flask import jsonify
from src.models import Course
from src.db import db

def create_course(name: str, level: str) -> dict:
    """Create a new course entity in the database.
    
    Args:
        name (str): The name of the course.
        level (str): The level of the course.
    
    Returns:
        dict: The created course with its data or an error message.
    """
    if not name or not level:
        return {"error": {"code": "E001", "message": "Name and level are required."}}, 400
    
    new_course = Course(name=name, level=level)
    db.session.add(new_course)
    db.session.commit()
    return jsonify({"name": new_course.name, "level": new_course.level}), 201

def get_all_courses() -> list:
    """Retrieve all courses from the database.
    
    Returns:
        list: A list of all courses, including their name and level.
    """
    courses = Course.query.all()
    return jsonify([{"name": course.name, "level": course.level} for course in courses])
```