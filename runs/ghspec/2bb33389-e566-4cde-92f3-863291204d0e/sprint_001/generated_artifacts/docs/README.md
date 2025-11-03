# README.md

# Student Management API

This document provides an overview of the Student Management API, including usage instructions, API endpoints, and test cases related to error scenarios for validation.

## API Endpoints

### 1. Create a New Student
- **Endpoint**: `POST /students`
- **Request Body**:
  ```json
  {
      "name": "string"  // Required
  }
  ```
- **Responses**:
  - **201 Created**: Successfully created a student.
  - **400 Bad Request**: If the name field is missing.

### 2. Retrieve Student Information
- **Endpoint**: `GET /students`
- **Responses**:
  - **200 OK**: Returns a list of all students.

## Test Cases for Error Scenarios

### Scenario 1: Create Student with Missing Name
- **Test Case**: Attempt to create a new student without providing a name.
- **Expected Response**:
  - **Status Code**: 400 Bad Request
  - **Response Body**:
    ```json
    {
        "error": {
            "code": "E001",
            "message": "Name field is required."
        }
    }
    ```

### Scenario 2: Other Potential Validation Errors
- You can expand on this section for other validation errors that may arise, ensuring they are covered with appropriate tests.

## Functional Requirements
- Ensure that all error scenarios are covered with automated tests, including the missing name when creating a new student. Each error case should have a corresponding test that validates the expected JSON response format and status code.

## Success Criteria
- All error scenarios must produce the expected responses and status codes as outlined above, providing clear feedback to the user on what went wrong to facilitate corrective action.