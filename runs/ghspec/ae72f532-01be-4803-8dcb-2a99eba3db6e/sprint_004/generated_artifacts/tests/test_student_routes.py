```python
import pytest
from fastapi.testclient import TestClient
from src.app import app

client = TestClient(app)

# Function to create a student for testing purposes
def create_student(name: str):
    response = client.post("/students/", json={"name": name})
    return response.json()

# Function to create a course for testing purposes
def create_course(name: str, level: str):
    response = client.post("/courses/", json={"name": name, "level": level})
    return response.json()

# Test to enroll a student in a course
def test_enroll_student_in_course():
    # Create a student and a course
    student = create_student("John Doe")
    course = create_course("Mathematics", "Beginner")
    
    # Enroll the student in the course
    response = client.put(f"/students/{student['id']}/enroll", json={"course_ids": [course['id']]})
    
    # Check that the response is successful
    assert response.status_code == 200
    assert response.json()['course_ids'] == [course['id']]
    
    # Verify enrollment by retrieving the student
    response = client.get(f"/students/{student['id']}")
    assert response.status_code == 200
    assert course['id'] in response.json()['course_ids']

# Test for failure when course ID is invalid
def test_enroll_student_with_invalid_course_id():
    student = create_student("John Doe")
    
    # Attempt to enroll the student in a non-existent course
    response = client.put(f"/students/{student['id']}/enroll", json={"course_ids": [999]})
    
    # Check that the status code indicates an error
    assert response.status_code == 400
    assert response.json() == {"error": {"code": "E002", "message": "Invalid course ID"}}

# Test to verify response format when retrieving students
def test_get_student_with_courses():
    student = create_student("Jane Doe")
    course_1 = create_course("History", "Intermediate")
    course_2 = create_course("Science", "Advanced")
    
    client.put(f"/students/{student['id']}/enroll", json={"course_ids": [course_1['id'], course_2['id']]})
    
    # Retrieve the student details
    response = client.get(f"/students/{student['id']}")
    
    # Check that the response format is as expected
    assert response.status_code == 200
    assert response.json() == {
        "id": student['id'],
        "name": "Jane Doe",
        "course_ids": [course_1['id'], course_2['id']]
    }

# Ensure the test client and the tests are functioning correctly
if __name__ == "__main__":
    pytest.main()
```