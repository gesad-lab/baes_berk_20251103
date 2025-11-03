```python
import pytest
import json
from src.app import create_app

@pytest.fixture
def client():
    """Create a test client for the application."""
    app = create_app(testing=True)
    with app.test_client() as client:
        yield client

def test_create_student(client):
    """Test creating a student with valid input."""
    response = client.post('/students', json={'name': 'John Doe'})
    assert response.status_code == 201
    data = json.loads(response.data)
    assert 'id' in data
    assert data['name'] == 'John Doe'

def test_create_student_invalid(client):
    """Test creating a student with no name."""
    response = client.post('/students', json={'name': ''})
    assert response.status_code == 400
    error_data = json.loads(response.data)
    assert error_data == {"error": {"code": "E001", "message": "Name field cannot be empty."}}

def test_retrieve_student(client):
    """Test retrieving an existing student."""
    # First create a student to retrieve
    create_response = client.post('/students', json={'name': 'John Doe'})
    student_id = json.loads(create_response.data)['id']

    # Now retrieve the student
    response = client.get(f'/students/{student_id}')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data['name'] == 'John Doe'

def test_retrieve_student_not_found(client):
    """Test retrieving a student that does not exist."""
    response = client.get('/students/999')
    assert response.status_code == 404
    error_data = json.loads(response.data)
    assert error_data == {"error": {"code": "E002", "message": "Student not found."}}

def test_update_student(client):
    """Test updating an existing student."""
    # Create a student first
    create_response = client.post('/students', json={'name': 'John Doe'})
    student_id = json.loads(create_response.data)['id']

    # Update the student's name
    response = client.put(f'/students/{student_id}', json={'name': 'Jane Doe'})
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data['name'] == 'Jane Doe'

def test_update_student_not_found(client):
    """Test updating a student that does not exist."""
    response = client.put('/students/999', json={'name': 'Jane Doe'})
    assert response.status_code == 404
    error_data = json.loads(response.data)
    assert error_data == {"error": {"code": "E002", "message": "Student not found."}}

def test_delete_student(client):
    """Test deleting an existing student."""
    # Create a student first
    create_response = client.post('/students', json={'name': 'John Doe'})
    student_id = json.loads(create_response.data)['id']

    # Delete the student
    response = client.delete(f'/students/{student_id}')
    assert response.status_code == 204

def test_delete_student_not_found(client):
    """Test deleting a student that does not exist."""
    response = client.delete('/students/999')
    assert response.status_code == 404
    error_data = json.loads(response.data)
    assert error_data == {"error": {"code": "E002", "message": "Student not found."}}
```