# README.md

# Course Management API

This API is designed for managing courses within an educational system. It provides functionality for creating and retrieving courses, along with proper validation and error handling.

## User Scenarios & Testing

1. **Create a Course**: An administrator creates a course by providing a name and level. The system should confirm the successful creation of the course.
   - **Test**: Submit valid details for the course, and verify that a new course record is created with both fields populated, returning a success message in JSON format.
     - Implemented in `tests/test_course.py`.

2. **Retrieve Course Information**: An administrator requests to view all registered courses. The system responds with a list of courses including their names and levels.
   - **Test**: Send a request to retrieve courses and verify that the JSON response includes all course records, displaying the name and level.
     - Implemented in `tests/test_course.py`.

3. **Error Handling on Missing Fields**: An administrator attempts to create a course without providing the required fields. The system should return an appropriate error message.
   - **Test**: Submit a blank name and blank level for a course creation request, ensuring that the response includes clear error messages in JSON format.
     - Implemented in `tests/test_course.py`.

4. **Error Handling on Invalid Field Submission**: An administrator tries to create a course with empty name or level inputs. The system should return clear error messages.
   - **Test**: Submit a name but no level, and submit a level but no name, while verifying that the appropriate error messages are returned.
     - Implemented in `tests/test_course.py`.

## Test Structure

### Tests

The testing framework uses FastAPI's TestClient for endpoint testing. The following test cases have been implemented for course management:

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

## Additional Notes

- The API will create the `Course` table on startup as part of schema migration, ensuring seamless integration within the database without losing existing data related to students or other entities. The addition of the `Course` entity does not interfere with existing data integrity.