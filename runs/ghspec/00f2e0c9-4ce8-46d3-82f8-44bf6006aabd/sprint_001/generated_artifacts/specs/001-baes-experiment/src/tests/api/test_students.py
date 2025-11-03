import pytest
import json

# Sample data for testing
students = []

@pytest.fixture
def client():
    from main import app  # Assuming your Flask app is in main.py
    with app.test_client() as client:
        yield client

def test_create_student_success(client):
    response = client.post('/students', json={'name': 'John Doe'})
    assert response.status_code == 201
    assert 'id' in response.json
    assert response.json['name'] == 'John Doe'

def test_create_student_missing_name(client):
    response = client.post('/students', json={})
    assert response.status_code == 400
    assert response.json == {"error": {"code": "E001", "message": "Name is required."}}

def test_get_student_success(client):
    response = client.post('/students', json={'name': 'Jane Doe'})
    student_id = response.json['id']

    response = client.get(f'/students/{student_id}')
    assert response.status_code == 200
    assert response.json['name'] == 'Jane Doe'

def test_get_student_not_found(client):
    response = client.get('/students/999')
    assert response.status_code == 404
    assert response.json == {"error": {"code": "E002", "message": "Student not found."}}

def test_update_student_success(client):
    response = client.post('/students', json={'name': 'Alice Smith'})
    student_id = response.json['id']

    response = client.put(f'/students/{student_id}', json={'name': 'Alice Johnson'})
    assert response.status_code == 200
    assert response.json['name'] == 'Alice Johnson'

def test_update_student_missing_name(client):
    response = client.post('/students', json={'name': 'Bob Brown'})
    student_id = response.json['id']

    response = client.put(f'/students/{student_id}', json={})
    assert response.status_code == 400
    assert response.json == {"error": {"code": "E001", "message": "Name is required."}}

def test_delete_student_success(client):
    response = client.post('/students', json={'name': 'Charlie Black'})
    student_id = response.json['id']

    response = client.delete(f'/students/{student_id}')
    assert response.status_code == 200
    assert response.json == {"message": "Student deleted successfully."}

def test_delete_student_not_found(client):
    response = client.delete('/students/999')
    assert response.status_code == 404
    assert response.json == {"error": {"code": "E002", "message": "Student not found."}}