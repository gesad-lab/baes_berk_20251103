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

@pytest.fixture()
def client(app):
    return app.test_client()

def test_create_teacher(client):
    response = client.post('/teachers', json={"name": "John Doe", "email": "john@example.com"})
    assert response.status_code == 201
    assert response.json["message"] == "Teacher successfully created."

def test_create_teacher_missing_name(client):
    response = client.post('/teachers', json={"email": "john@example.com"})
    assert response.status_code == 400
    assert response.json["error"]["code"] == "E001"
    assert response.json["error"]["message"] == "The name field is required."

def test_create_teacher_missing_email(client):
    response = client.post('/teachers', json={"name": "John Doe"})
    assert response.status_code == 400
    assert response.json["error"]["code"] == "E002"
    assert response.json["error"]["message"] == "The email field is required."

def test_create_teacher_invalid_email_format(client):
    response = client.post('/teachers', json={"name": "John Doe", "email": "johnexample.com"})
    assert response.status_code == 400
    assert response.json["error"]["code"] == "E003"
    assert response.json["error"]["message"] == "Email format is invalid."
```