```python
import requests

BASE_URL = "http://localhost:8000/courses"  # Base URL for Course API

def test_assign_teacher_to_course():
    """Test assigning a teacher to a specific course."""
    response = requests.patch(f"{BASE_URL}/1/assign-teacher", json={"teacher_id": 1})
    
    assert response.status_code == 200  # Confirm successful assignment
    response_data = response.json()
    assert response_data["message"] == "Teacher assigned successfully."

def test_assign_teacher_to_course_invalid_teacher():
    """Test assigning an invalid teacher to a course returns an appropriate error."""
    response = requests.patch(f"{BASE_URL}/1/assign-teacher", json={"teacher_id": 999})
    
    assert response.status_code == 400  # Bad request due to invalid teacher_id
    response_data = response.json()
    assert response_data["error"]["code"] == "E002"  # Assuming a specific error code for invalid teacher
    assert response_data["error"]["message"] == "Invalid teacher_id provided."

def test_get_course_details_with_teacher():
    """Test retrieving course details including the assigned teacher."""
    response = requests.get(f"{BASE_URL}/1")
    
    assert response.status_code == 200  # Confirm retrieval success
    course_data = response.json()
    assert course_data["id"] == 1
    assert "teacher_id" in course_data  # Check that teacher_id is present
    assert course_data["teacher_id"] == 1  # Assuming teacher_id 1 is assigned to course 1

def test_get_course_details_no_teacher():
    """Test retrieving course details for a course without an assigned teacher."""
    response = requests.get(f"{BASE_URL}/2")  # Assuming course 2 has no teacher assigned
    
    assert response.status_code == 200  # Confirm retrieval success
    course_data = response.json()
    assert course_data["id"] == 2
    assert course_data["teacher_id"] is None  # teacher_id should be None for unassigned teacher
```