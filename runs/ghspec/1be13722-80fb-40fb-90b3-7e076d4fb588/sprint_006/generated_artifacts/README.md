# README.md

# Course and Teacher Integration Testing

## Overview

This document outlines the tests implemented for the new feature that establishes a relationship between the Course entity and the Teacher entity within the system. This integration enhances the functionality, allowing users to retrieve comprehensive course details that include information about the associated teacher.

## User Scenarios & Testing

### 1. Assign a Teacher to a Course
- **Scenario**: As an administrator, I want to assign a teacher to a course so that the course is associated with the correct instructor.
- **Test**: 
  - **Description**: Submit a request to update an existing course with a teacher ID, verifying that the course record is updated successfully with the teacher relationship.
  - **Implementation**:
```python
def test_assign_teacher_to_course():
    response = client.put(f"/courses/{course_id}", json={"teacher_id": valid_teacher_id})
    assert response.status_code == 200
    assert response.json()["teacher_id"] == valid_teacher_id
```

### 2. Retrieve Course with Teacher Information
- **Scenario**: As a user, I want to retrieve a course's details, including the associated teacher, to understand the course structure better.
- **Test**:
  - **Description**: Query the course entity by ID and check that it returns the correct course details, including the assigned teacher's name.
  - **Implementation**:
```python
def test_retrieve_course_with_teacher():
    response = client.get(f"/courses/{course_id}")
    assert response.status_code == 200
    assert response.json()["teacher"]["name"] == expected_teacher_name
```

### 3. Handle Errors for Invalid Teacher Assignment
- **Scenario**: As an administrator, I want to receive error messages when I attempt to assign a non-existent teacher to a course.
- **Test**:
  - **Description**: Attempt to update a course with an invalid teacher ID and validate that appropriate error messages are returned.
  - **Implementation**:
```python
def test_invalid_teacher_assignment():
    response = client.put(f"/courses/{course_id}", json={"teacher_id": invalid_teacher_id})
    assert response.status_code == 400
    assert response.json() == {"error": {"code": "E002", "message": "Invalid teacher ID"}}
```

## Testing Summary

These tests ensure that the integration between courses and teachers is functional and that the system handles invalid scenarios gracefully. 

### Running the Tests
To execute the tests, ensure that the development environment is correctly set up. Then, run the test suite using:
```bash
pytest tests/api/test_course.py
```

### Conclusion
The implementation of associative functionality between courses and teachers has been effectively tested, ensuring a more structured and informative experience for users.