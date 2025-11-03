```python
import pytest
from flask import json
from student_management_app import create_app
from student_management_app.database import init_db

@pytest.fixture(scope="module")
def test_client():
    app = create_app()
    with app.test_client() as client:
        with app.app_context():
            # Initialize the database and create tables
            init_db()
        yield client

def test_retrieve_all_students(test_client):
    """Test to verify that retrieving all students returns an empty list initially."""
    response = test_client.get('/students')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert isinstance(data, list)
    assert len(data) == 0  # Expecting empty list as no students are created yet

def test_create_student(test_client):
    """Test to verify that a student can be created successfully."""
    response = test_client.post('/students', json={"name": "John Doe"})
    assert response.status_code == 201
    data = json.loads(response.data)
    assert "id" in data
    assert data["name"] == "John Doe"

def test_retrieve_student_by_id(test_client):
    """Test to verify that a student can be retrieved by their ID."""
    # First create a student to retrieve
    create_response = test_client.post('/students', json={"name": "Jane Doe"})
    created_student = json.loads(create_response.data)
    
    response = test_client.get(f'/students/{created_student["id"]}')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data["id"] == created_student["id"]
    assert data["name"] == "Jane Doe"

def test_create_student_without_name(test_client):
    """Test to verify that creating a student without a name returns an error."""
    response = test_client.post('/students', json={})
    assert response.status_code == 400
    error_data = json.loads(response.data)
    assert error_data["error"]["code"] == "E001"  # Example error code for missing name
    assert error_data["error"]["message"] == "Name field is required."
```