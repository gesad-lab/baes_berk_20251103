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
            "details": error.description
        }
    }
    return jsonify(response), 400

# Error handler for duplicate email errors
@app.errorhandler(409)
def handle_conflict(error):
    response = {
        "error": {
            "code": "E409",
            "message": "Conflict",
            "details": "Email address already in use."
        }
    }
    return jsonify(response), 409

# Function to validate teacher creation inputs
def validate_teacher_data(data):
    if 'name' not in data or not data['name']:
        abort(400, description="Missing required field: name")
    
    if 'email' not in data or not data['email']:
        abort(400, description="Missing required field: email")

    if Teacher.query.filter_by(email=data['email']).first() is not None:
        abort(409)

# Test case for creating a teacher
def test_create_teacher_success(client):
    response = client.post('/teachers', json={"name": "John Doe", "email": "john.doe@example.com"})
    assert response.status_code == 201
    assert response.json['name'] == "John Doe"
    assert response.json['email'] == "john.doe@example.com"

# Test case for missing name
def test_create_teacher_missing_name(client):
    response = client.post('/teachers', json={"email": "john.doe@example.com"})
    assert response.status_code == 400
    assert response.json['error']['code'] == "E400"
    assert response.json['error']['message'] == "Bad request"
    assert "Missing required field: name" in response.json['error']['details']

# Test case for duplicate email
def test_create_teacher_duplicate_email(client):
    # Create the initial teacher
    client.post('/teachers', json={"name": "Initial Teacher", "email": "duplicate@example.com"})
    
    # Try to create a second teacher with the same email
    response = client.post('/teachers', json={"name": "Second Teacher", "email": "duplicate@example.com"})
    assert response.status_code == 409
    assert response.json['error']['code'] == "E409"
    assert response.json['error']['message'] == "Conflict"
    assert "Email address already in use." in response.json['error']['details']
```