```python
# tests/api/test_teacher_api.py

import pytest
from flask import Flask
from src.api.teacher_api import teacher_bp

@pytest.fixture()
def app():
    app = Flask(__name__)
    app.register_blueprint(teacher_bp)
    return app

def test_create_teacher(client):
    # Test successful creation of a teacher
    response = client.post('/teachers', json={"name": "John Doe", "email": "john@example.com"})
    assert response.status_code == 201
    assert response.json["message"] == "Teacher successfully created."

def test_create_teacher_missing_name(client):
    # Test creation of a teacher with missing name
    response = client.post('/teachers', json={"email": "john@example.com"})
    assert response.status_code == 400
    assert response.json["error"]["name"] == "The name field is required."

def test_create_teacher_invalid_email(client):
    # Test creation of a teacher with invalid email format
    response = client.post('/teachers', json={"name": "Jane Doe", "email": "invalid-email"})
    assert response.status_code == 400
    assert response.json["error"]["email"] == "The email must have a valid format."
```