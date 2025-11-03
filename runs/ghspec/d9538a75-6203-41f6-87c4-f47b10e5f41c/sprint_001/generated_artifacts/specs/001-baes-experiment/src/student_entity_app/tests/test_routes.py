```python
import json
import pytest
from src.app import app  # Importing the main application
from unittest.mock import patch

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

# Scenario 1: Create a Student
def test_create_student_with_valid_name(client):
    response = client.post('/students', json={'name': 'John Doe'})
    assert response.status_code == 201  # HTTP 201 Created
    data = json.loads(response.data)
    assert data['student']['name'] == 'John Doe'

# Scenario 2: Retrieve All Students
def test_get_students(client):
    # First, create a student to ensure there's at least one student in the database
    client.post('/students', json={'name': 'Jane Doe'})
    
    response = client.get('/students')
    assert response.status_code == 200  # HTTP 200 OK
    data = json.loads(response.data)
    assert isinstance(data, list)  # Response should be a list
    assert len(data) > 0  # There should be at least one student

# Scenario 3: Handle Missing Name
def test_create_student_without_name(client):
    response = client.post('/students', json={})
    assert response.status_code == 400  # HTTP 400 Bad Request
    data = json.loads(response.data)
    assert data['error']['code'] == 'E001'  # Error code for missing name
    assert data['error']['message'] == 'Name is required.'  # Error message should be clear
```