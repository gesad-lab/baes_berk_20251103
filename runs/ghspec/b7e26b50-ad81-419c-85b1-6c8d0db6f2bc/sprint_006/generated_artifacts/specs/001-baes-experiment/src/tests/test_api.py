```python
import json
import pytest
from flask import Flask, request, jsonify, abort
from your_app import create_app, db  # Adjust import based on your app structure
from your_app.models import Student, Course, Teacher  # Import the Teacher model for validation

app = create_app()

# Centralized error handling for missing course data
@app.errorhandler(400)
def handle_bad_request(error):
    response = {
        "error": {
            "code": "E400",
            "message": "Bad request",
        }
    }
    return jsonify(response), 400

@app.route('/courses/<int:course_id>', methods=['PATCH'])
def assign_teacher_to_course(course_id):
    """Assigns a teacher to a course based on the course ID and the provided teacher ID."""
    data = request.get_json()
    teacher_id = data.get('teacher_id')

    if not teacher_id:
        return jsonify({"error": {"code": "E001", "message": "Teacher ID is required"}}), 400

    course = Course.query.get(course_id)
    if not course:
        return jsonify({"error": {"code": "E404", "message": "Course not found"}}), 404

    teacher = Teacher.query.get(teacher_id)
    if not teacher:
        return jsonify({"error": {"code": "E404", "message": "Teacher not found"}}), 404

    course.teacher_id = teacher.id  # Assign the teacher
    db.session.commit()

    return jsonify({"message": "Teacher assigned successfully", "course_id": course.id, "teacher_id": teacher.id}), 200

# Unit tests for teacher assignment functionality
def test_assign_teacher_to_course(client):
    """Test case to assign a teacher to a course successfully."""
    teacher = Teacher(name="Test Teacher")
    course = Course(name="Test Course")
    db.session.add(teacher)
    db.session.add(course)
    db.session.commit()

    response = client.patch(f'/courses/{course.id}', json={"teacher_id": teacher.id})
    assert response.status_code == 200
    assert response.json == {
        "message": "Teacher assigned successfully",
        "course_id": course.id,
        "teacher_id": teacher.id
    }

def test_assign_teacher_to_invalid_course(client):
    """Test case to handle assigning a teacher to a non-existent course."""
    response = client.patch('/courses/999', json={"teacher_id": 1})
    assert response.status_code == 404
    assert response.json == {
        "error": {
            "code": "E404",
            "message": "Course not found"
        }
    }

def test_assign_invalid_teacher_to_course(client):
    """Test case to handle assigning an invalid teacher to a course."""
    course = Course(name="Test Course")
    db.session.add(course)
    db.session.commit()

    response = client.patch(f'/courses/{course.id}', json={"teacher_id": 999})
    assert response.status_code == 404
    assert response.json == {
        "error": {
            "code": "E404",
            "message": "Teacher not found"
        }
    }

def test_assign_teacher_without_teacher_id(client):
    """Test case to handle request without teacher_id."""
    course = Course(name="Test Course")
    db.session.add(course)
    db.session.commit()

    response = client.patch(f'/courses/{course.id}', json={})
    assert response.status_code == 400
    assert response.json == {
        "error": {
            "code": "E001",
            "message": "Teacher ID is required"
        }
    }
```