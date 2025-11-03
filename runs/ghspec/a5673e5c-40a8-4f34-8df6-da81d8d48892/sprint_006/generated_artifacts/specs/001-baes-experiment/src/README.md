# Updating README.md to include tests for Course-Teacher association

# README.md

# Project Title

## Overview

This project involves managing educational entities such as Courses and Teachers, allowing association between them through API endpoints.

## Usage

...

## Testing the API

### Test Cases for Teacher Association with Course

#### User Scenario 3: Update Course Teacher
- **Given** a Course is associated with a Teacher,
- **When** the user updates the Teacher for that Course,
- **Then** the Course record should reflect the new Teacher association.

#### Functional Requirements
1. A relationship must be established from the Course entity to the Teacher entity.
2. The Course entity should have a new field indicating the associated Teacher's identifier (e.g., Teacher ID).
3. The application must provide an API endpoint to associate a Teacher with an existing Course.
4. The application must provide an API endpoint to retrieve Course details, including the associated Teacher information.
5. A database migration must be created to update the Course table, introducing the Teacher relationship while preserving existing Student, Course, and Teacher data.

#### Success Criteria
- The system should allow users to successfully associate a Teacher with a Course with an accuracy rate of at least 90% on user interactions.
- The API must accurately return Course details, including Teacher information in valid JSON format for all requests.
- Any modifications to Course teacher associations must be accurately reflected in the system.
- The database migration must execute without data loss or integrity issues for existing Students, Courses, and Teachers.

### How to Test

1. Run the application.
2. Execute the following tests to ensure that the Course-Teacher association functionality works as intended:

```bash
pytest tests/test_courses.py
```

This command will run all tests related to Course-Teacher functionalities, provided that the setup for the database is properly configured. 

### Test Setup

Refer to the `tests/test_courses.py` for the specific test cases implemented, including creating, updating, and retrieving Course records with associated Teacher information.

- Ensure you have existing tests for Teacher CRUD operations in place as setup fixtures for consistent state across tests.
- Validate that responses return the correct status codes and payloads.

### Test Examples

```python
def test_update_course_teacher():
    # Setup: Create a course and associate it to a teacher
    response = client.post("/courses", json={"name": "Math 101", "teacher_id": "12345"})
    assert response.status_code == 201

    # Action: Update teacher for the existing course
    response = client.patch("/courses/1", json={"teacher_id": "54321"})
    assert response.status_code == 200

    # Verification: Check the updated course details
    response = client.get("/courses/1")
    assert response.json()["teacher_id"] == "54321"
```

You should follow the structure defined in the `tests/test_courses.py` to maintain consistency with the existing code style.

### Conclusion

The tests ensure the functionality related to Course and Teacher associations operates as expected, thus contributing to the stability and reliability of the application. Please refer to the relevant test files for detailed implementation.