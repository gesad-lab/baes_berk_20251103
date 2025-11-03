import json
import pytest
from flask import Flask, request, jsonify, abort
from your_app import create_app, db  # Adjust import based on your app structure
from your_app.models import Student  # Adjust import for your Student model
from your_app.errors import handle_missing_email  # Centralized error handling

app = create_app()

# Centralized error handling for missing email
@app.errorhandler(400)
def handle_bad_request(error):
    response = {
        "error": {
            "code": "E001",
            "message": "Email is required."
        }
    }
    return jsonify(response), 400

@app.route('/students', methods=['POST'])
def add_student():
    # Validate incoming data
    data = request.get_json() or {}
    name = data.get('name')
    email = data.get('email')

    if not email:
        return handle_bad_request(None)  # Centralized error handling

    student = Student(name=name, email=email)
    db.session.add(student)
    db.session.commit()

    return jsonify({"id": student.id, "email": student.email}), 201

@app.route('/students/<int:id>', methods=['PUT'])
def update_student(id):
    # Validate incoming data
    data = request.get_json() or {}
    email = data.get('email')

    if not email:
        return handle_bad_request(None)  # Centralized error handling

    student = Student.query.get_or_404(id)
    student.email = email
    db.session.commit()

    return jsonify({"id": student.id, "email": student.email})

# Tests for the /students endpoints
def test_add_student_missing_email(client):
    response = client.post('/students', json={"name": "John Doe"})
    assert response.status_code == 400
    assert response.json == {"error": {"code": "E001", "message": "Email is required."}}

def test_update_student_missing_email(client):
    # First create a student
    post_response = client.post('/students', json={"name": "John Doe", "email": "john.doe@example.com"})
    student_id = post_response.json['id']

    # Attempt to update without an email
    response = client.put(f'/students/{student_id}', json={"email": ""})
    assert response.status_code == 400
    assert response.json == {"error": {"code": "E001", "message": "Email is required."}}