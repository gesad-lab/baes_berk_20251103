```python
import json
import pytest
from fastapi.testclient import TestClient
from src.main import app  # Main FastAPI application
from src.models import TeacherCreate  # Assuming there is a TeacherCreate model

client = TestClient(app)

# Performance tests for the teacher API endpoints
@pytest.mark.performance
def test_create_teacher_response_time():
    """Test that creating a teacher responds within 2 seconds."""
    start_time = time.time()
    response = client.post("/teachers", json={"name": "John Doe", "email": "john.doe@example.com"})
    duration = time.time() - start_time
    assert response.status_code == 201  # Ensure teacher is created successfully
    assert duration < 2.0  # Check response time is under 2 seconds

@pytest.mark.performance
def test_list_teachers_response_time():
    """Test that retrieving the list of teachers responds within 2 seconds."""
    start_time = time.time()
    response = client.get("/teachers")
    duration = time.time() - start_time
    assert response.status_code == 200  # Ensure teachers are retrieved successfully
    assert duration < 2.0  # Check response time is under 2 seconds
```