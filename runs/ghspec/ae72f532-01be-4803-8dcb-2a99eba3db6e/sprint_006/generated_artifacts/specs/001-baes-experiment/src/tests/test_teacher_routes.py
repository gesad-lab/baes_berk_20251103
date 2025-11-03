```python
import pytest
from fastapi.testclient import TestClient
from src.app import app

client = TestClient(app)

# Helper function to create a course for testing purposes
def create_course(course_name: str):
    response = client.post("/courses/", json={"name": course_name})
    return response.json(), response.status_code

# Helper function to retrieve course details
def retrieve_course_details(course_id: int):
    response = client.get(f"/courses/{course_id}")
    return response.json(), response.status_code

# Test case for retrieving course details with a valid ID
def test_retrieve_course_details_valid_id():
    # Create a course to retrieve
    course_data, _ = create_course("Mathematics 101")
    course_id = course_data["id"]

    # Retrieve the details of the newly created course
    retrieved_data, status_code = retrieve_course_details(course_id)

    assert status_code == 200
    assert retrieved_data["id"] == course_id
    assert retrieved_data["name"] == "Mathematics 101"

# Test case for retrieving course details with an invalid ID
def test_retrieve_course_details_invalid_id():
    # Attempt to retrieve a course that does not exist
    retrieved_data, status_code = retrieve_course_details(999999)

    assert status_code == 404
    assert "error" in retrieved_data
    assert retrieved_data["error"]["code"] == "E001"
    assert retrieved_data["error"]["message"] == "Course not found"

# Test case for retrieving course details without providing a course ID
def test_retrieve_course_details_no_id():
    # Attempt to retrieve course details with an invalid request (missing ID)
    retrieved_data, status_code = client.get("/courses/")

    assert status_code == 422  # Unprocessable Entity for invalid request
    assert "detail" in retrieved_data  # Check for validation error details
```