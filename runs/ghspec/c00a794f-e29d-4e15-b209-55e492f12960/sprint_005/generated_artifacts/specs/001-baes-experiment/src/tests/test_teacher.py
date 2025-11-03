```python
# tests/test_teacher.py
import pytest
from fastapi import status
from src.models import Teacher
from src.database import SessionLocal

@pytest.fixture
def client():
    from fastapi.testclient import TestClient
    from src.main import app
    return TestClient(app)

def test_create_teacher(client):
    response = client.post("/teachers", json={"name": "John Doe", "email": "john.doe@example.com"})
    assert response.status_code == 201
    assert response.json() == {"message": "Teacher created successfully"}

def test_create_teacher_without_name(client):
    response = client.post("/teachers", json={"email": "john.doe@example.com"})
    assert response.status_code == 400
    assert response.json() == {"error": {"code": "E001", "message": "Name is required."}}

def test_create_teacher_without_email(client):
    response = client.post("/teachers", json={"name": "John Doe"})
    assert response.status_code == 400
    assert response.json() == {"error": {"code": "E002", "message": "Email is required."}}

def test_get_teacher(client):
    # Assume we have a teacher with ID 1 in the db
    response = client.get("/teachers/1")
    assert response.status_code == 200
    assert "name" in response.json()
    assert "email" in response.json()
```