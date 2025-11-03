```python
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from src.models.course import Course  # Importing the Course model
from src.models.teacher import Teacher  # Importing the Teacher model
from sqlalchemy.orm import joinedload

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
db = SQLAlchemy(app)

@app.route('/courses/<int:course_id>', methods=['GET'])
def get_course_info(course_id):
    """
    Retrieve course information based on course_id.
    
    Args:
        course_id (int): The ID of the course to retrieve.

    Returns:
        JSON: Course details including course ID, name, level, teacher 
              ID, teacher name, and teacher email or error message if 
              the course is not found.
    """
    # Attempt to retrieve the course with the associated teacher details
    course = db.session.query(Course).options(joinedload(Course.teacher)).filter(Course.id == course_id).first()

    if not course:
        return jsonify({"error": {"code": "E404", "message": "Course not found."}}), 404

    # Construct response data
    course_details = {
        "course_id": course.id,
        "name": course.name,
        "level": course.level,
        "teacher_id": course.teacher.id if course.teacher else None,
        "teacher_name": course.teacher.name if course.teacher else None,
        "teacher_email": course.teacher.email if course.teacher else None
    }
    
    return jsonify(course_details), 200
```