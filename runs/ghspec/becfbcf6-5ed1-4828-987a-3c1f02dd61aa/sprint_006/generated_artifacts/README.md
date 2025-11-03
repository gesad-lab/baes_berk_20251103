```
# File: README.md

# Updated API Endpoints

## Course Management

### Assigning a Teacher to a Course

- **Endpoint**: `/courses/{course_id}/assign-teacher`
- **Method**: PATCH
- **Body**:
  ```json
  {
      "teacher_id": integer  // ID of the teacher to assign
  }
  ```
- **Response**:
  ```json
  {
      "message": "Teacher assigned successfully",
      "course": {
          "id": integer,
          "name": "Course Name",
          "teacher_id": integer
      }
  }
  ```
- **Notes**: Ensure that the `teacher_id` exists before assignment.

### Retrieving Course Details

- **Endpoint**: `/courses/{course_id}`
- **Method**: GET
- **Response**:
  ```json
  {
      "id": integer,
      "name": "Course Name",
      "teacher": {
          "id": integer,
          "name": "Teacher Name",
          "email": "teacher@example.com"
      }
  }
  ```
- **Notes**: If no teacher is assigned, the response will exclude the `teacher` field.

### Test Scenarios

1. **Assigning a Teacher to a Course**:
   - An administrator assigns a teacher to an existing course.
   - Verify that the course record updates correctly to reflect the assigned teacher, and this information is retrievable.

2. **Validating Teacher Assignment**:
   - An administrator attempts to assign a non-existent teacher to a course.
   - Verify that the system returns an appropriate error message indicating that the specified teacher does not exist.

3. **Retrieving Course with Teacher Information**:
   - A user retrieves information about a specific course along with the assigned teacher.
   - Verify that the retrieved course data includes accurate details of the assigned teacher.

4. **Retrieving Course without a Teacher Assigned**:
   - A user retrieves a course that does not have any teacher assigned.
   - Verify that the response omits teacher details.

### Example Test for Retrieving a Course without a Teacher Assigned

```python
import pytest
from app import app, db, Course

@pytest.fixture
def client():
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    with app.test_client() as client:
        with app.app_context():
            db.create_all()  # Create the database schema for testing

            # Creating a sample course for tests
            course = Course(name="Algebra 101")
            db.session.add(course)
            db.session.commit()

            yield client  # Provide the test client for the tests

def test_retrieve_course_without_teacher(client):
    """Test retrieving a course that has no teacher assigned."""
    course_id = 1  # Assuming the ID of the course created above

    response = client.get(f'/courses/{course_id}')
    assert response.status_code == 200
    assert 'teacher' not in response.get_json()  # Ensure teacher field is omitted
    assert response.get_json()['id'] == course_id
```

### Additional Notes

- The above test verifies that when a course is retrieved without an assigned teacher, the response appropriately excludes the `teacher` field from the JSON response.
```