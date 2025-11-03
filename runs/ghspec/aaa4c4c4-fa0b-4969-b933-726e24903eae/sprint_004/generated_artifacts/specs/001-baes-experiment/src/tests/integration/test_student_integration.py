```python
import pytest
from fastapi.testclient import TestClient
from main import app  # Assuming your FastAPI app is instantiated in main.py

# Initialize the test client
client = TestClient(app)

@pytest.fixture(scope="module")
def create_student():
    """Fixture to create a student for testing purposes."""
    response = client.post("/students", json={"name": "John Doe", "email": "john.doe@example.com"})
    assert response.status_code == 201
    return response.json()  # Return the created student data

@pytest.fixture(scope="module")
def create_course():
    """Fixture to create a course for testing purposes."""
    response = client.post("/courses", json={"name": "Mathematics", "level": "Beginner"})
    assert response.status_code == 201
    return response.json()  # Return the created course data

@pytest.fixture(scope="module")
def enroll_student(create_student, create_course):
    """Fixture to enroll a student into a course."""
    response = client.post(f"/students/{create_student['id']}/enroll", json={"course_id": create_course['id']})
    assert response.status_code == 200  # Assuming a successful enrollment returns HTTP 200
    return response.json()  # Return the enrollment data

def test_get_student_with_courses(enroll_student, create_student):
    """Test retrieving a student along with their enrolled courses."""
    response = client.get(f"/students/{create_student['id']}/courses")
    assert response.status_code == 200
    data = response.json()
    
    # Verify the structure of the response
    assert isinstance(data, list)  # Response should be a list of courses
    assert len(data) > 0  # There should be at least one course
    
    # Assert that the enrollment details are correct
    assert 'id' in data[0]
    assert 'name' in data[0]
    assert data[0]['name'] == "Mathematics"  # Verify the course name

def test_course_enrollment_response_structure(enroll_student):
    """Test the response structure when enrolling a student in a course."""
    response = enroll_student  # Use the response from the enroll_student fixture
    
    # Assert the structure of the enrollment response
    assert 'student_id' in response
    assert 'course_id' in response
    assert response['course_id'] not in (None, "")  # Ensure course_id is valid
```