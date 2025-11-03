# README.md

# Teacher Management API Documentation

## Overview

This API allows you to manage teachers in the Teacher Management application. It provides endpoints to create and retrieve teacher entities.

## API Endpoints

### Create Teacher

- **Endpoint**: `POST /api/v1/teachers`
- **Description**: Creates a new teacher in the system.
- **Request Body**:
    ```json
    {
        "name": "Jane Doe",
        "email": "jane.doe@example.com"
    }
    ```
- **Responses**:
    - **201 Created**: Successfully created a teacher:
        ```json
        {
            "id": 1,
            "name": "Jane Doe",
            "email": "jane.doe@example.com"
        }
        ```
    - **400 Bad Request**: Email already exists or required fields are missing:
        ```json
        {
            "error": {
                "code": "E001",
                "message": "Email already exists."
            }
        }
        ```
        
### Get Teacher by ID

- **Endpoint**: `GET /api/v1/teachers/{id}`
- **Description**: Retrieves a teacher by their ID.
- **Path Parameters**:
    - `id`: The ID of the teacher to retrieve.
- **Responses**:
    - **200 OK**: Successfully retrieved the teacher:
        ```json
        {
            "id": 1,
            "name": "Jane Doe",
            "email": "jane.doe@example.com"
        }
        ```
    - **404 Not Found**: Teacher not found:
        ```json
        {
            "error": {
                "code": "E002",
                "message": "Teacher not found."
            }
        }
        ```

## Success Criteria

- The application successfully creates Teacher entities with complete accuracy, verified by test cases achieving at least 95% success.
- The API must return the correct JSON response when creating and retrieving Teacher entities.
- Errors for duplicate emails and missing required fields are handled correctly, returning appropriate messages.
- The existing Student and Course data remains unchanged and intact after the database migration.

## Testing

The functionality of the API endpoints can be tested using the test cases found in the `tests/test_teacher.py` file. The following tests are included:

- **Create Teacher**: Tests the creation of a new teacher.
- **Create Teacher with Duplicate Email**: Tests error handling when attempting to create a teacher with an existing email.
- **Get Teacher by ID**: Tests the retrieval of a teacher by their ID.

## Conclusion

This documentation provides an overview of the Teacher Management API, detailing the available endpoints, expected request/response formats, and the criteria for success. Please refer to the test cases for examples of how to utilize the API and for ensuring accuracy in functionality.