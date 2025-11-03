```markdown
# API Documentation for Course Management

## Course Management Overview

The Course Management feature allows users to create, retrieve, update, and delete course records within the Student Entity Management Web Application. This documentation outlines the API endpoints related to course management and specifies the expected behavior for each operation.

## User Scenarios & Testing

1. **Scenario 1**: A user wants to create a new course record with a name and level.
   - Test: Verify that when valid name and level are provided, a new course record is created successfully in the database.

2. **Scenario 2**: A user attempts to create a new course record with missing name or level.
   - Test: Ensure that the application returns an appropriate error message indicating that both fields are required.

3. **Scenario 3**: A user retrieves a list of all course records and checks if the name and level fields are included.
   - Test: Confirm that both fields are present in the response for each course record.

4. **Scenario 4**: A user wants to update an existing course’s name or level.
   - Test: Verify that updating the course’s details works as expected and reflects the changes in the database.

5. **Scenario 5**: A user wants to delete a course record and check that the record is removed.
   - Test: Ensure that the specified course record is deleted from the database successfully.

## API Endpoints

### Delete Course

- **Endpoint**: `DELETE /api/courses/{course_id}`
- **Description**: Deletes a specified course record from the database.
- **Parameters**:
  - `course_id` (path parameter): The unique identifier of the course to delete.
- **Responses**:
  - `204 No Content`: The course was successfully deleted.
  - `404 Not Found`: The course with the specified ID does not exist.
  - `400 Bad Request`: Invalid input or format provided.

### Test Case for Deleting a Course

Here's a test case that should be added to `tests/api/test_course_api.py` to ensure the delete functionality works as intended:

```python
import pytest
from fastapi.testclient import TestClient
from src.main import app
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from src.models import Course

# Test configuration
SQLALCHEMY_DATABASE_URL = "sqlite:///./test_db.sqlite3"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

@pytest.fixture(scope="module")
def test_client():
    # Override dependency to use test database
    app.dependency_overrides[get_db] = lambda: TestingSessionLocal()
    yield TestClient(app)

def test_delete_course(test_client):
    # Create a new course to ensure we can delete it later
    course_data = {"name": "Math 101", "level": "Beginner"}
    response = test_client.post("/api/courses", json=course_data)
    assert response.status_code == 201  # Ensure course creation was successful
    course_id = response.json()["id"]  # Extract the new course ID

    # Delete the created course
    response = test_client.delete(f"/api/courses/{course_id}")
    assert response.status_code == 204  # Ensure delete was successful

    # Verify that the course does not exist anymore
    response = test_client.get(f"/api/courses/{course_id}")
    assert response.status_code == 404  # Course should no longer exist
```

This test ensures that when a course is deleted, it is indeed removed from the database, confirming the expected behavior outlined in the specifications. Please ensure to run this test alongside other existing tests for a comprehensive validation of course management functionality.
```