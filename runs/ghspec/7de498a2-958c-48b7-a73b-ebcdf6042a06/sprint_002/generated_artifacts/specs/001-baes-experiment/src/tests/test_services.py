```python
import pytest
from fastapi.testclient import TestClient
from src.main import app

@pytest.fixture(scope="module")
def test_client():
    """Create a test client for the FastAPI application."""
    client = TestClient(app)
    yield client

def test_create_student_with_invalid_email_format(test_client):
    """Test that creating a student with an invalid email format returns a 400 error."""
    # Sample payload with an invalid email format
    payload = {
        "name": "John Doe",
        "email": "invalid-email-format"  # Invalid email
    }
    
    response = test_client.post("/students", json=payload)  # Assuming the endpoint is /students
    assert response.status_code == 400, "Expected 400 Bad Request status code"
    
    # Check if the error message is clear and actionable
    assert "error" in response.json(), "Response should contain an error key"
    assert response.json()["error"]["code"] == "E002", "Expected error code for invalid email format"
    assert "Invalid email format" in response.json()["error"]["message"], "Expected specific message for invalid email format"

def test_update_student_with_invalid_email_format(test_client):
    """Test that updating a student's email with an invalid format returns a 400 error."""
    # Sample payload attempting to update with an invalid email format
    student_id = 1  # Example student ID assuming it already exists
    payload = {
        "email": "invalid-email-format"  # Invalid email
    }
    
    response = test_client.put(f"/students/{student_id}/email", json=payload)  # Assuming the endpoint is structured this way
    assert response.status_code == 400, "Expected 400 Bad Request status code"
    
    # Check if the error message is clear and actionable
    assert "error" in response.json(), "Response should contain an error key"
    assert response.json()["error"]["code"] == "E002", "Expected error code for invalid email format"
    assert "Invalid email format" in response.json()["error"]["message"], "Expected specific message for invalid email format"
```