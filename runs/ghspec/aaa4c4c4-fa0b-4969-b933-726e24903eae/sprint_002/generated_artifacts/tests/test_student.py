```python
import pytest
from fastapi.testclient import TestClient
from main import app  # Assuming the FastAPI app is created in main.py

client = TestClient(app)

@pytest.fixture(scope="module")
def setup_database():
    # This fixture would typically configure and initialize the database.
    # Implementation depends on your specific setup and testing requirements
    pass

def test_create_student_missing_email(setup_database):
    """Test creating a student without an email should return an error."""
    response = client.post("/students", json={"name": "Jane Doe"})
    
    # Assert that the status code is 400 Bad Request
    assert response.status_code == 400
    
    # Assert that the response body contains the appropriate error message
    assert response.json() == {"detail": "Email is required."}
    
def test_create_student_empty_email(setup_database):
    """Test creating a student with an empty email should return an error."""
    response = client.post("/students", json={"name": "John Doe", "email": ""})
    
    # Assert that the status code is 400 Bad Request
    assert response.status_code == 400
    
    # Assert that the response body contains the appropriate error message
    assert response.json() == {"detail": "Email is required."}
```