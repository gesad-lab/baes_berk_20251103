```python
import pytest
from fastapi.testclient import TestClient
from src.main import app
from pydantic import BaseModel

@pytest.fixture(scope="module")
def test_client():
    """Create a test client for the FastAPI application."""
    client = TestClient(app)
    yield client

# Pydantic models for Course creation and response
class CourseCreate(BaseModel):
    name: str  # The name of the course
    level: str  # The level of the course, required field

class CourseResponse(BaseModel):
    id: int  # The unique identifier of the course
    name: str  # The name of the course
    level: str  # The level of the course

def test_create_student_with_invalid_email_format(test_client):
    """Test that creating a student with an invalid email format returns a 400 error."""
    # Sample payload with an invalid email format
    payload = {
        "name": "John Doe",
        "email": "invalid_email_format"
    }
    response = test_client.post("/students", json=payload)
    assert response.status_code == 400
    assert "error" in response.json()
```