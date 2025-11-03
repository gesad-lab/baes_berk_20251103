```python
import requests

BASE_URL_COURSES = "http://localhost:8000/courses"  # Base URL for Course API
BASE_URL_TEACHERS = "http://localhost:8000/teachers"  # Base URL for Teacher API

def test_assign_teacher_to_course():
    """Test assigning a teacher to a specific course."""
    # Setup: Create a teacher to assign
    teacher_response = requests.post(BASE_URL_TEACHERS, json={"name": "John Doe", "email": "john.doe@example.com"})
    assert teacher_response.status_code == 201  # Confirm creation status
    teacher = teacher_response.json()
    teacher_id = teacher["id"]
    
    # Test: Assign the created teacher to a course
    response = requests.patch(f"{BASE_URL_COURSES}/1/assign-teacher", json={"teacher_id": teacher_id})
    assert response.status_code == 200  # Confirm successful assignment
    assert response.json()["teacher_id"] == teacher_id  # Ensure the teacher is assigned correctly

def test_assign_teacher_with_invalid_id():
    """Test assigning a teacher with an invalid teacher_id to a course."""
    invalid_teacher_id = 99999  # Assuming this ID does not exist
    response = requests.patch(f"{BASE_URL_COURSES}/1/assign-teacher", json={"teacher_id": invalid_teacher_id})
    
    assert response.status_code == 400  # Confirm bad request for invalid ID
    assert response.json()["error"]["code"] == "E001"  # Expect a specific error code
    assert "valid teacher ID" in response.json()["error"]["message"]  # Expect informative error message

def test_get_course_details_with_teacher():
    """Test retrieving course details including teacher assignment."""
    # Assuming the teacher has already been assigned in the previous test
    response = requests.get(f"{BASE_URL_COURSES}/1")

    assert response.status_code == 200  # Confirm successful fetch
    course_details = response.json()
    assert "teacher_id" in course_details  # Ensure teacher_id is present in the response
    assert course_details["teacher_id"] > 0  # Ensure it is a valid ID

def test_get_course_details_invalid_course():
    """Test fetching details of a non-existing course."""
    response = requests.get(f"{BASE_URL_COURSES}/99999")  # Assuming this course ID does not exist
    assert response.status_code == 404  # Confirm not found status
    assert response.json()["error"]["code"] == "E002"  # Expect a specific error code
    assert "Course not found" in response.json()["error"]["message"]  # Expect informative error message
```