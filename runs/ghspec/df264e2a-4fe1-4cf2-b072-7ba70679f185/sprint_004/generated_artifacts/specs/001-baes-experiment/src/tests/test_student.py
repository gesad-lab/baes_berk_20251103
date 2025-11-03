```python
import pytest

def test_associate_student_with_course(client):
    response = client.post("/students/1/courses", json={"course_id": 1})
    assert response.status_code == 200
    assert response.json() == {"message": "Course assigned successfully."}

def test_invalid_course_assignment(client):
    # Test case for assigning a course with an invalid course ID
    response = client.post("/students/1/courses", json={"course_id": 999})
    assert response.status_code == 404
    assert response.json() == {
        "error": {
            "code": "E001",
            "message": "Invalid course ID."
        }
    }

def test_retrieve_student_with_courses(client):
    response = client.get("/students/1")
    assert response.status_code == 200
    assert response.json() == {
        "id": 1,
        "name": "John Doe",
        "email": "john@example.com",
        "courses": []  # adjust based on available courses for the student
    }
```