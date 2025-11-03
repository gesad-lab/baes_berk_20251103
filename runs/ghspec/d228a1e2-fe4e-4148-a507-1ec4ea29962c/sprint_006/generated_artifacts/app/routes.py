```python
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from app.models import Course, Teacher  # Import the models (assumed existing)

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'  # In-memory database for testing
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

@app.route('/courses/<int:course_id>/assign-teacher', methods=['POST'])
def assign_teacher_to_course(course_id):
    """Assign a teacher to a specific course."""
    data = request.get_json()
    
    # Validate input
    if 'teacher_id' not in data or not isinstance(data['teacher_id'], int):
        return jsonify({"error": {"code": "E001", "message": "Invalid input: teacher_id is required and must be an integer."}}), 400
    
    course = Course.query.get(course_id)
    if course is None:
        return jsonify({"error": {"code": "E404", "message": "Course not found."}}), 404

    # Assign the teacher to the course
    course.teacher_id = data['teacher_id']
    db.session.commit()
    
    return jsonify({"message": "Teacher assigned successfully.", "course_id": course_id}), 200

@app.route('/courses/<int:course_id>', methods=['GET'])
def get_course_details(course_id):
    """Get details of a specific course."""
    course = Course.query.get(course_id)
    if course is None:
        return jsonify({"error": {"code": "E404", "message": "Course not found."}}), 404
    
    response_data = {
        "course_id": course.id,
        "title": course.title,
        "teacher_id": course.teacher_id,
        # Assume Teacher model has attributes name and email
        "teacher": {
            "id": course.teacher_id,
            "name": course.teacher.name if course.teacher else None,
            "email": course.teacher.email if course.teacher else None
        }
    }
    return jsonify(response_data), 200

@app.route('/teachers/<int:teacher_id>/courses', methods=['GET'])
def list_courses_by_teacher(teacher_id):
    """List all courses assigned to a specific teacher."""
    courses = Course.query.filter_by(teacher_id=teacher_id).all()
    response_data = [{"course_id": course.id, "title": course.title} for course in courses]
    
    return jsonify(response_data), 200

# Remember to set up error handling, logging, or additional middleware as required for production use.
```