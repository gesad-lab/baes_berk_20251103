```python
import pytest
from fastapi.testclient import TestClient
from myapp.main import app
from myapp.database import create_database_schema
from myapp.models import Course  # Import the Course model to interact with it

# Create a TestClient for making requests to the FastAPI app
client = TestClient(app)

@pytest.fixture(scope="module", autouse=True)
def setup_database():
    """Fixture to set up the database schema on startup."""
    create_database_schema()  # Ensure the database schema is set up for testing
    yield  # This is where the testing will occur
    # Clean up the database or perform any necessary teardown after tests 

def test_create_course_succeeds():
    """Test creating a course with valid input."""
    response = client.post("/courses", json={"name": "Mathematics", "level": "Beginner"})
    
    assert response.status_code == 201  # Expecting a 201 Created response
    data = response.json()
    assert data["name"] == "Mathematics"  # Validate response data
    assert data["level"] == "Beginner"

def test_get_course_succeeds():
    """Test retrieving a course by ID."""
    # First, create a course to retrieve
    create_response = client.post("/courses", json={"name": "Science", "level": "Intermediate"})
    course_id = create_response.json()["id"]  # Get the ID of the created course

    response = client.get(f"/courses/{course_id}")
    
    assert response.status_code == 200  # Expecting a 200 OK response
    data = response.json()
    assert data["id"] == course_id  # Validate that we get the correct course back
    assert data["name"] == "Science"
    assert data["level"] == "Intermediate"

def test_create_course_validation_error():
    """Test creating a course with missing fields results in validation error."""
    response = client.post("/courses", json={"name": "", "level": "Intermediate"})
    
    assert response.status_code == 400  # Expecting a 400 Bad Request response
    assert "validation" in response.json()["error"]["message"]  # Check for validation error message

def test_get_non_existent_course():
    """Test retrieving a course that does not exist returns a 404 error."""
    response = client.get("/courses/99999")  # Assuming this ID does not exist
    
    assert response.status_code == 404  # Expecting a 404 Not Found response
    assert response.json()["error"]["code"] == "E404"  # Ensure correct error code/message is returned

```