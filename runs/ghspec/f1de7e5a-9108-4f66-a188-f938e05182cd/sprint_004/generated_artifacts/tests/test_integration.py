```python
import pytest
from fastapi.testclient import TestClient
from main import app  # Assuming your main app is in a file called main.py
from models import Course, Student, StudentCourses  # Ensure you import relevant models

client = TestClient(app)

# Test case for enrolling a student in a course
def test_enroll_student_in_course():
    # First, create a test student
    student_response = client.post("/students", json={"name": "John Doe", "email": "john@example.com"})
    assert student_response.status_code == 201
    student_id = student_response.json()["id"]

    # Then, create a test course
    course_response = client.post("/courses", json={"name": "Mathematics", "level": "Beginner"})
    assert course_response.status_code == 201
    course_id = course_response.json()["id"]

    # Enroll the student in the course
    enroll_response = client.post(f"/students/{student_id}/enroll", json={"course_id": course_id})
    assert enroll_response.status_code == 200
    assert enroll_response.json()["message"] == "Student enrolled successfully"

    # Retrieve the courses for the student
    courses_response = client.get(f"/students/{student_id}/courses")
    assert courses_response.status_code == 200
    assert len(courses_response.json()) == 1
    assert courses_response.json()[0]["id"] == course_id
    assert courses_response.json()[0]["name"] == "Mathematics"
    assert courses_response.json()[0]["level"] == "Beginner"

# Test case for retrieving courses when no courses are enrolled
def test_get_courses_for_student_with_no_enrollments():
    # Create a test student
    student_response = client.post("/students", json={"name": "Jane Doe", "email": "jane@example.com"})
    assert student_response.status_code == 201
    student_id = student_response.json()["id"]

    # Attempt to retrieve courses for the new student
    courses_response = client.get(f"/students/{student_id}/courses")
    assert courses_response.status_code == 200
    assert courses_response.json() == []  # Expecting an empty list

# Test case for enrolling a student in an invalid course
def test_enroll_student_in_invalid_course():
    # Create a test student
    student_response = client.post("/students", json={"name": "Jack Smith", "email": "jack@example.com"})
    assert student_response.status_code == 201
    student_id = student_response.json()["id"]

    # Attempt to enroll the student in an invalid course
    enroll_response = client.post(f"/students/{student_id}/enroll", json={"course_id": 999})  # Invalid course ID
    assert enroll_response.status_code == 400
    assert enroll_response.json()["error"]["code"] == "E001"
    assert enroll_response.json()["error"]["message"] == "Invalid course ID"
```
