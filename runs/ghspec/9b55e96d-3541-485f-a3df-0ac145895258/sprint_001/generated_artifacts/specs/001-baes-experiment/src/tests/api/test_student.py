```python
import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

@pytest.fixture(scope="module")
def student_data():
    return {
        "name": "John Doe",
        "age": 20,
        "email": "johndoe@example.com"
    }

def test_create_student_success(student_data):
    response = client.post("/students/", json=student_data)
    assert response.status_code == 201  # Check for successful creation
    assert "id" in response.json()  # Ensure the response contains a student ID
    assert response.json()["name"] == student_data["name"]  # Check the name matches

def test_update_student_success(student_data):
    # First, create a student to update
    create_response = client.post("/students/", json=student_data)
    student_id = create_response.json()["id"]
    
    # Prepare new data for update
    updated_data = {**student_data, "name": "John Smith"}
    
    update_response = client.put(f"/students/{student_id}", json=updated_data)
    assert update_response.status_code == 200  # Check for successful update
    assert update_response.json()["name"] == "John Smith"  # Ensure the name was updated

def test_update_student_validation_error():
    invalid_data = {
        "name": "",  # Invalid: empty name
        "age": 25,
        "email": "invalidemail.com"  # Invalid email format
    }
    
    response = client.put("/students/100", json=invalid_data)  # Trying to update a non-existing student
    assert response.status_code == 404  # Check for not found
    assert response.json() == {"error": {"code": "E404", "message": "Student not found", "details": {}}}  # Proper error format

    invalid_email_response = client.post("/students/", json={"name": "Jane Doe", "age": 20, "email": "invalidemail.com"})
    assert invalid_email_response.status_code == 422  # Check for unprocessable entity
    assert "detail" in invalid_email_response.json()  # Ensure response contains validation details

def test_read_student_not_found():
    response = client.get("/students/999")  # Attempt to retrieve a non-existing student
    assert response.status_code == 404  # Check for not found
    assert response.json() == {"error": {"code": "E404", "message": "Student not found", "details": {}}}  # Proper error format
```