```python
import json
import pytest
from flask import Flask, request, jsonify, abort
from your_app import create_app, db  # Adjust import based on your app structure
from your_app.models import Student, Course  # Adjust import for your Course model
from your_app.errors import handle_missing_email  # Centralized error handling

app = create_app()

# Centralized error handling for missing course data
@app.errorhandler(400)
def handle_bad_request(error):
    response = {
        "error": {
            "code": "E001",
            "message": error.description
        }
    }
    return jsonify(response), 400

# New Course creation route
@app.route('/courses', methods=['POST'])
def create_course():
    data = request.get_json()

    # Check if 'name' or 'level' is missing
    if 'name' not in data or not data['name']:
        abort(400, 'Name is required.')
    if 'level' not in data or not data['level']:
        abort(400, 'Level is required.')

    new_course = Course(name=data['name'], level=data['level'])
    db.session.add(new_course)
    db.session.commit()

    return jsonify({"message": "Course created successfully.", "id": new_course.id}), 201


# Testing for the create course functionality
@pytest.mark.parametrize("input_data, expected_status, expected_message", [
    ({"name": "Introduction to Python", "level": "Beginner"}, 201, "Course created successfully."),
    ({"name": "", "level": "Beginner"}, 400, "Name is required."),
    ({"name": "Introduction to Python", "level": ""}, 400, "Level is required."),
    ({"level": "Beginner"}, 400, "Name is required."),
    ({"name": "Introduction to Python"}, 400, "Level is required."),
])
def test_create_course(input_data, expected_status, expected_message):
    client = app.test_client()
    response = client.post('/courses', json=input_data)
    
    assert response.status_code == expected_status
    assert response.get_json()['error']['message'] == expected_message if expected_status == 400 else response.get_json()['message'] == expected_message
```