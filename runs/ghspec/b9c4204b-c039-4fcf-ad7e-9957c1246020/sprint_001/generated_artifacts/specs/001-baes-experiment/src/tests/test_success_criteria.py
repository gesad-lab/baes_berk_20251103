import pytest
from fastapi.testclient import TestClient
from src.main import app  # Adjust based on your file structure
import time

client = TestClient(app)

@pytest.mark.parametrize("student_data,expected_status,expected_response", [
    ({"name": "John Doe"}, 201, {"name": "John Doe"}),
    ({"name": ""}, 400, {"detail": "Field 'name' is required"})
])
def test_create_student(student_data, expected_status, expected_response):
    """Test creation of a new student."""
    # Measure the time taken for the request to complete
    start_time = time.time()
    response = client.post("/students/", json=student_data)
    end_time = time.time()

    # Validate the response code and content
    assert response.status_code == expected_status
    assert response.json() == expected_response
    # Validate that response is returned within 2 seconds
    assert (end_time - start_time) < 2


def test_retrieve_student_list():
    """Test retrieval of the student list."""
    # Ensure there are at least 2 students in the database
    # Create students first if necessary
    client.post("/students/", json={"name": "Alice Smith"})
    client.post("/students/", json={"name": "Bob Jones"})

    start_time = time.time()
    response = client.get("/students/")
    end_time = time.time()

    # Validate the response code
    assert response.status_code == 200
    # Validate response is a list with at least 2 students
    assert isinstance(response.json(), list)
    assert len(response.json()) >= 2
    # Validate that response is returned within 2 seconds
    assert (end_time - start_time) < 2

