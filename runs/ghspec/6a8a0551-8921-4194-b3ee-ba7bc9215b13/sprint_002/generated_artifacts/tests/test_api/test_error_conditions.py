```python
import pytest
from flask import Flask, jsonify, request

# Setup the Flask app and database context
app = Flask(__name__)

@app.route('/students/', methods=['POST'])
def create_student():
    data = request.get_json()
    if 'name' not in data or not data['name']:
        return jsonify({"error": {"code": "E001", "message": "Missing name field."}}), 400
    
    if 'email' not in data or not data['email'] or '@' not in data['email']:
        return jsonify({"error": {"code": "E002", "message": "Invalid email format."}}), 400

    # Simulate the creation of a student record (implementation omitted for brevity)
    student_id = 1  # This would normally come from the database
    return jsonify({"id": student_id, "name": data['name'], "email": data['email']}), 201


def test_create_student_without_email(test_client):
    """Test creating a student without an email field."""
    response = test_client.post('/students/', json={'name': 'Jane Doe'})
    assert response.status_code == 400
    assert response.get_json() == {"error": {"code": "E002", "message": "Invalid email format."}}


def test_create_student_with_invalid_email(test_client):
    """Test creating a student with an invalid email format."""
    response = test_client.post('/students/', json={'name': 'Jane Doe', 'email': 'jane.doe@'})
    assert response.status_code == 400
    assert response.get_json() == {"error": {"code": "E002", "message": "Invalid email format."}}


def test_create_student_with_valid_email(test_client):
    """Test creating a student with a valid email."""
    response = test_client.post('/students/', json={'name': 'Jane Doe', 'email': 'jane.doe@example.com'})
    assert response.status_code == 201
    assert response.get_json() == {
        "id": 1,
        "name": "Jane Doe",
        "email": "jane.doe@example.com"
    }
```