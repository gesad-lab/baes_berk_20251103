```python
# tests/test_course.py
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_create_course_valid():
    """Test creating a course with a valid name and level."""
    response = client.post("/courses", json={"name": "Math 101", "level": "beginner"})
    assert response.status_code == 200
    assert response.json() == {"message": "Course created successfully", "course": {"name": "Math 101", "level": "beginner"}}

def test_create_course_empty_fields():
    """Test creating a course with empty fields."""
    response = client.post("/courses", json={"name": "", "level": ""})
    assert response.status_code == 400
    assert response.json() == {"error": {"code": "E001", "message": "Both name and level are required"}}

def test_get_courses():
    """Test retrieving all courses after creation."""
    response = client.get("/courses")
    assert response.status_code == 200
    assert "courses" in response.json()
```
