# Integration Tests for Student Management API

This document outlines integration tests for the Student Management API endpoints `POST /students` and `GET /students/{id}`.

```markdown
# Student Management API Tests

## Integration Tests Overview

This section describes the integration tests for verifying the functionality of the `POST /students` and `GET /students/{id}` endpoints.

## Pre-requisites

- Ensure the API server is running and the SQLite database is set up properly.
- Install required testing libraries if not already installed.

## Required Libraries

To run the tests, you may need to install the following libraries if you're using Python's `pytest`:

```bash
pip install pytest requests
```

## Test Cases

### 1. Creating a Student

- **Endpoint**: `POST /students`
- **Description**: This test verifies that a student can be created with valid input.
- **Request**:
    - **Method**: POST
    - **Body**: 
      ```json
      {
          "name": "John Doe"
      }
      ```
- **Expected Response**:
    - Status: 201 Created
    - Body:
      ```json
      {
          "message": "Student created successfully",
          "student": {
              "id": 1,
              "name": "John Doe"
          }
      }
      ```

### 2. Retrieving a Student

- **Endpoint**: `GET /students/{id}`
- **Description**: This test checks that student details can be retrieved by their unique ID.
- **Request**:
    - **Method**: GET
    - **Path**: `/students/1`
- **Expected Response**:
    - Status: 200 OK
    - Body:
      ```json
      {
          "id": 1,
          "name": "John Doe"
      }
      ```

### 3. Handling Invalid Input

- **Endpoint**: `POST /students`
- **Description**: This test validates that the API returns an error when trying to create a student without a name.
- **Request**:
    - **Method**: POST
    - **Body**:
      ```json
      {}
      ```
- **Expected Response**:
    - Status: 400 Bad Request
    - Body:
      ```json
      {
          "error": {
              "code": "E001",
              "message": "Name is required"
          }
      }
      ```

## Running the Tests

To run the tests, you can use the following command:

```bash
pytest tests/test_routes.py
```

Ensure the database is reset before each test if needed to start with a clean slate.

## Conclusion

The above integration tests ensure that the `POST /students` and `GET /students/{id}` endpoints work correctly for both valid and invalid inputs, complying with the specifications set out in the functional requirements.

```