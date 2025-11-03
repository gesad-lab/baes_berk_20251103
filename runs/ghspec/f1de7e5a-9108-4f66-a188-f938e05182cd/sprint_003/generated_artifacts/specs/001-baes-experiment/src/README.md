```python
import pytest
from fastapi.testclient import TestClient
from main import app  # Assuming your main app is in a file called main.py

client = TestClient(app)

# Test case for creating a new course
def test_create_course():
    response = client.post("/courses", json={"name": "Introduction to Programming", "level": "Beginner"})
    assert response.status_code == 201
    assert response.json() == {"name": "Introduction to Programming", "level": "Beginner"}

# Test case for retrieving courses
def test_retrieve_courses():
    response = client.get("/courses")
    assert response.status_code == 200
    assert isinstance(response.json(), list)  # Ensure the response is a list
    assert "name" in response.json()[0]  # Check that the first course has a name
    assert "level" in response.json()[0]  # Check that the first course has a level

# Test case for creating a course with missing name
def test_create_course_without_name():
    response = client.post("/courses", json={"level": "Beginner"})
    assert response.status_code == 400  # Expect Bad Request
    assert response.json()["error"]["code"] == "E001"  # Replace with appropriate error code
    assert "name" in response.json()["error"]["message"]

# Test case for creating a course with missing level
def test_create_course_without_level():
    response = client.post("/courses", json={"name": "Data Structures"})
    assert response.status_code == 400  # Expect Bad Request
    assert response.json()["error"]["code"] == "E002"  # Replace with appropriate error code
    assert "level" in response.json()["error"]["message"]

# Test case for creating a course with missing both fields
def test_create_course_without_fields():
    response = client.post("/courses", json={})
    assert response.status_code == 400  # Expect Bad Request
    assert response.json()["error"]["code"] == "E003"  # Replace with appropriate error code
    assert "name" in response.json()["error"]["message"]
    assert "level" in response.json()["error"]["message"]
```