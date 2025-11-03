```python
import pytest
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from your_project.models import Course, Teacher  # Import relevant models
from your_project.validations import validate_teacher_id  # Import validation logic

# Assuming the app and db have been initialized in your main application code
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)

# Sample API endpoint to create a course
@app.route('/api/v1/students/<int:student_id>/courses', methods=['POST'])
def associate_course(student_id):
    data = request.json
    course_id = data.get('course_id')
    teacher_id = data.get('teacher_id')

    # Perform validation for teacher_id
    if teacher_id and not validate_teacher_id(teacher_id):
        return jsonify({"error": {"code": "E001", "message": "Invalid teacher ID"}}), 400

    # Fetch the course using the provided course_id
    course = Course.query.filter_by(id=course_id, student_id=student_id).first()
    if not course:
        return jsonify({"error": {"code": "E002", "message": "Course not found"}}), 404

    # Assign teacher if provided
    if teacher_id:
        course.teacher_id = teacher_id

    # Save changes to the database
    db.session.commit()
    return jsonify({"message": "Course updated successfully"}), 200

# Test routes to validate teacher_id assignment
def test_associate_course_with_valid_teacher():
    # Assuming setup code to create a test student and course
    
    response = app.test_client().post('/api/v1/students/1/courses', json={
        'course_id': 1,
        'teacher_id': 1  # Assuming teacher with ID 1 exists
    })
    assert response.status_code == 200
    assert response.json['message'] == "Course updated successfully"

def test_associate_course_with_invalid_teacher():
    response = app.test_client().post('/api/v1/students/1/courses', json={
        'course_id': 1,
        'teacher_id': 9999  # Assuming teacher with ID 9999 does not exist
    })
    assert response.status_code == 400
    assert response.json['error']['code'] == "E001"
    assert response.json['error']['message'] == "Invalid teacher ID"
```