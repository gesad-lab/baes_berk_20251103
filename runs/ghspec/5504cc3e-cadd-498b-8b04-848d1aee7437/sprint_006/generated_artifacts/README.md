```markdown
# README.md

## API Endpoints

### Assign Teacher to Course
- **POST** `/api/courses/{course_id}/assign_teacher`
- **Description**: Assign a teacher to a specified course by providing the teacher's ID.
- **Request Payload**:
    ```json
    {
        "teacher_id": "<TEACHER_ID>"
    }
    ```
- **Response**:
    - **200 OK**: Teacher assigned successfully. Returns course details including the assigned teacher's name.
    - **400 Bad Request**: Invalid course or teacher ID supplied.
    - **404 Not Found**: Course or teacher not found.

### View Course with Teacher Information
- **GET** `/api/courses/{course_id}`
- **Description**: Retrieve detailed information about a specific course, including its assigned teacher.
- **Response**:
    - **200 OK**: Returns course details including the assigned teacher's name.
    - **404 Not Found**: Course not found.

## Testing

### Testing Course Details Retrieval API Endpoint
- **Tests**:
    - Ensure that the API returns correct course details including teacher information on successful request.
    - Confirm that invalid course IDs result in a 404 response.
    - Validate the error response format for clarity and consistency.
  
### Example of Integration Test for Course Details Retrieval:
```python
import pytest
from flask import json
from app import create_app, db
from src.models.course import Course
from src.models.teacher import Teacher

@pytest.fixture
def client():
    """Setup testing client for the application."""
    app = create_app('testing')  # Create app in testing mode
    with app.test_client() as client:
        with app.app_context():
            db.create_all()  # Setup database schema for testing
            # Create sample data for testing
            teacher = Teacher(name="John Doe")
            course = Course(title="Math 101", teacher=teacher)
            db.session.add(teacher)
            db.session.add(course)
            db.session.commit()
        yield client  # Provide the test client

def test_view_course_with_teacher(client):
    """Test retrieval of course details including assigned teacher information."""
    response = client.get('/api/courses/1')  # Assuming course ID 1 exists
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data['title'] == "Math 101"
    assert data['teacher']['name'] == "John Doe"

def test_view_course_with_invalid_id(client):
    """Test retrieval attempt with an invalid course ID."""
    response = client.get('/api/courses/999')  # Assuming ID 999 does not exist
    assert response.status_code == 404
    error_data = json.loads(response.data)
    assert error_data['error']['code'] == "E404"
```
```