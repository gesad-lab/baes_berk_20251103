# src/api/docs/student_api.md

# Student API Documentation

This document provides an overview of the Student API, which allows the management of student entities in the system. The API supports the creation and retrieval of students along with their associated email addresses.

## API Endpoints

### POST /students

- **Description**: Create a new student entry.
- **Request Body**:
  ```json
  {
      "name": "string",
      "email": "string"
  }
  ```
- **Parameters**:
  - `name`: The name of the student (required)
  - `email`: The email address of the student (required, must be a valid email format)

- **Responses**:
  - **201 Created**: Successfully created a student.
    ```json
    {
        "id": "integer",
        "name": "string",
        "email": "string"
    }
    ```
  - **400 Bad Request**: Missing or invalid email in the request body.
    ```json
    {
        "error": {
            "code": "E001",
            "message": "Invalid email format"
        }
    }
    ```

### GET /students

- **Description**: Retrieve a list of all students.
- **Responses**:
  - **200 OK**: A list of all students.
    ```json
    [
        {
            "id": "integer",
            "name": "string",
            "email": "string"
        },
        {
            "id": "integer",
            "name": "string",
            "email": "string"
        }
    ]
    ```
  
## Database Schema Changes

As part of the updates, the Student table in the database is modified to include the email address field as follows:

- `email`: string, required (to store the student's email address)

## Validation

- Ensure that the email field is validated to follow standard email format rules.
- If the email field is missing or invalid, return a `400 Bad Request` response indicating the error.

## Summary

The enhancement of the Student entity by adding an email field aims to improve communication and management capabilities. The API now allows for comprehensive data handling of students, ensuring their information is complete and useful for future operations.