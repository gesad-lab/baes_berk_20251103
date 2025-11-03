import pytest
from flask import Flask, jsonify, request

# Assuming the app and db have already been set up in your application
app = Flask(__name__)

@app.route('/students/', methods=['POST'])
def create_student():
    data = request.get_json()
    if 'name' not in data or not data['name']:
        return jsonify({"error": {"code": "E001", "message": "Missing name field."}}), 400
    
    # Simulate the creation of a student record
    student_id = 1  # This would normally come from the database
    return jsonify({"id": student_id, "name": data['name']}), 201


# Test cases for error conditions
@pytest.mark.parametrize("data, expected_status, expected_code, expected_message", [
    ({"name": ""}, 400, "E001", "Missing name field."),  # Missing name
    ({}, 400, "E001", "Missing name field.")             # No data provided
])
def test_create_student_invalid(data, expected_status, expected_code, expected_message):
    """Test the student creation endpoint with invalid data."""
    response = app.test_client().post('/students/', json=data)
    
    # Assert the response status code
    assert response.status_code == expected_status

    # Assert that the correct error message is returned
    json_data = response.get_json()
    assert json_data['error']['code'] == expected_code
    assert json_data['error']['message'] == expected_message


@pytest.fixture
def client():
    with app.test_client() as client:
        yield client


def test_create_student_without_name(client):
    """Test the creation of a student without providing a name field."""
    response = client.post('/students/', json={})
    
    assert response.status_code == 400
    json_data = response.get_json()
    assert json_data['error']['code'] == "E001"
    assert json_data['error']['message'] == "Missing name field."


def test_create_student_with_empty_name(client):
    """Test the creation of a student with an empty name."""
    response = client.post('/students/', json={'name': ''})
    
    assert response.status_code == 400
    json_data = response.get_json()
    assert json_data['error']['code'] == "E001"
    assert json_data['error']['message'] == "Missing name field."