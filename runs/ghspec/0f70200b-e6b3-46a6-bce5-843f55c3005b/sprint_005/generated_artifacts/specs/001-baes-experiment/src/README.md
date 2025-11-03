```python
import pytest
from fastapi.testclient import TestClient
from src.app import app
from src.models import Teacher

client = TestClient(app)

@pytest.fixture(scope="module")
def test_teachers():
    """Setup test teachers in the database before any tests run."""
    # Assume a setup function exists to clear and populate the database
    clear_and_seed_database_with_teachers()
    yield
    # Tear down test database cleanup
    clear_test_database()

def test_get_teacher_success(test_teachers):
    """Test if fetching a teacher by ID returns the correct data."""
    # Assuming we have a teacher with ID 1 for testing
    response = client.get("/teachers/1")
    
    assert response.status_code == 200, "Expected status code 200"
    assert "name" in response.json(), "Response should contain teacher name"
    assert "email" in response.json(), "Response should contain teacher email"
    assert response.json()["id"] == 1, "Expected teacher ID to be 1"

def test_get_non_existent_teacher(test_teachers):
    """Test if fetching a non-existent teacher returns a 404 error."""
    response = client.get("/teachers/9999")  # Assuming 9999 does not exist
    
    assert response.status_code == 404, "Expected status code 404"
    assert response.json() == {"error": {"code": "E404", "message": "Teacher not found", "details": {}}}, "Expected not found error response"
```