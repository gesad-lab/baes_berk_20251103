# README.md

---

# Project: Educational Management System

## Overview
This project facilitates the management of educational data, focusing on entities such as teachers and students. It includes the ability to create and retrieve teacher information through a RESTful API.

## Feature: Create Teacher Entity

### Overview & Purpose
The purpose of this feature is to create a new Teacher entity within the educational management system, enabling the system to store information about teachers, including their names and email addresses. This new entity will facilitate better management of instructors, enhance the educational data model, and support future features related to teacher assignments, class management, and communication.

### User Scenarios & Testing
1. **Creating a Teacher**:
   - User submits a request to create a new teacher by providing a name and an email.
   - The system should respond with a confirmation that the teacher has been successfully created, returning the teacher ID as well as the provided details.

2. **Retrieving Teacher Information**:
   - User sends a request to retrieve the details of a specific teacher by their ID.
   - The system should respond with the teacher's name and email, or an error message if the teacher does not exist.

   **Test Scenario**:
   - Verify that retrieving a teacher by a valid ID returns the correct name and email.
   - Verify that retrieving a teacher by an invalid ID returns an error message indicating the teacher does not exist.

3. **Creating a Teacher with Missing Fields**:
   - User attempts to create a teacher without providing a name or email.
   - The system should respond with an error indicating that both fields are required for teacher creation.

4. **Error Handling for Invalid Email Format**:
   - User submits a request to create a teacher with an invalid email format.
   - The system should respond with an appropriate error message indicating the email must be valid.

### API Endpoints
- `POST /api/teachers`: Create a new teacher.
- `GET /api/teachers/{id}`: Retrieve teacher information by ID.

### Database Schema
```sql
CREATE TABLE teachers (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT NOT NULL
);
```

### Testing the Retrieval of a Teacher by ID
To test the retrieval functionality, the following test cases should be implemented:

- **Valid ID Retrieval**: Input a valid teacher ID, expect a successful response with the teacher's details.
- **Invalid ID Retrieval**: Input a non-existent teacher ID, expect an error response indicating the teacher was not found.

Use these tests to validate the implementation of the retrieve functionality in the API as follows:

```python
import pytest
from src.services.teacher_service import TeacherService
from src.models.teacher import Teacher
from sqlalchemy.exc import IntegrityError

@pytest.fixture
def teacher_service():
    """Fixture for initializing the TeacherService for tests."""
    return TeacherService()

def test_retrieve_teacher_by_valid_id(teacher_service):
    """Test retrieval of a teacher by a valid ID."""
    # Assuming there's a teacher created already with ID 1
    teacher = teacher_service.get_teacher(1)
    assert teacher is not None
    assert teacher.name == "John Doe"
    assert teacher.email == "john.doe@example.com"

def test_retrieve_teacher_by_invalid_id(teacher_service):
    """Test retrieval of a teacher by an invalid ID."""
    teacher = teacher_service.get_teacher(-1)  # Assuming -1 does not exist
    assert teacher is None
```

---

### Additional Notes
Ensure to create corresponding tests for all mentioned scenarios for comprehensive coverage.