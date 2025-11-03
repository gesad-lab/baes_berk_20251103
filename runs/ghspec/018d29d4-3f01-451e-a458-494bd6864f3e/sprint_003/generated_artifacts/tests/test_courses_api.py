```python
import pytest
from fastapi.testclient import TestClient
from main import app  # Assume the FastAPI app is instantiated in a file named main.py

client = TestClient(app)

@pytest.fixture(autouse=True)
def setup_database():
    # Setup the database: create tables as necessary before tests
    # This would normally include dropping any existing tables and re-creating them
    pass  # Replace with actual setup code

def test_create_course_with_valid_data():
    """Test creating a course with valid name and level."""
    response = client.post("/courses", json={"name": "Mathematics", "level": "Advanced"})
    assert response.status_code == 201
    assert response.json() == {"id": 1, "name": "Mathematics", "level": "Advanced"}  # Adjust based on actual response

def test_create_course_missing_fields():
    """Test creating a course with missing required fields."""
    response = client.post("/courses", json={"name": "Mathematics"})
    assert response.status_code == 400
    assert response.json() == {"error": {"code": "E001", "message": "Level is required."}}  # Adjust based on actual error response

def test_create_course_with_invalid_level():
    """Test creating a course with an invalid level (if applicable)."""
    response = client.post("/courses", json={"name": "Mathematics", "level": "NonexistentLevel"})
    assert response.status_code == 400
    assert response.json() == {"error": {"code": "E002", "message": "Invalid level specified."}}  # Adjust based on actual error response
```