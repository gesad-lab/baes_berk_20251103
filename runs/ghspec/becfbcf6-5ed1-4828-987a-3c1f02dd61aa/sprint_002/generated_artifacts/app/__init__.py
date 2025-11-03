# README.md

# Student Management Application API

This document provides an overview of the API for the Student Management application, including endpoint specifications, usage details, and error handling.

## API Endpoints

### Create a Student

- **Method**: POST
- **Endpoint**: `/students`
- **Request Body**:
  ```json
  {
    "name": "string (required)",
    "email": "string (required, valid email format)"
  }
  ```
- **Response**:
  - **Status Code**: 201 Created
  - **Body**:
    ```json
    {
      "id": "integer",
      "name": "string",
      "email": "string"
    }
    ```

#### Error Responses
- **Missing Name**:
  - **Status Code**: 400 Bad Request
  - **Body**:
    ```json
    {
      "error": {
        "code": "E001",
        "message": "The name field is required."
      }
    }
    ```
- **Missing Email**:
  - **Status Code**: 400 Bad Request
  - **Body**:
    ```json
    {
      "error": {
        "code": "E002",
        "message": "The email field is required and must be a valid format."
      }
    }
    ```

### Retrieve All Students

- **Method**: GET
- **Endpoint**: `/students`
- **Response**:
  - **Status Code**: 200 OK
  - **Body**:
    ```json
    [
      {
        "id": "integer",
        "name": "string",
        "email": "string"
      }
    ]
    ```

## Database Migration

To support the new email field for the Student entity, the application includes a database migration that adds the email column to the existing Student schema. This migration will run on application startup, ensuring that all existing data is preserved.

## JSON Response Format

All responses from the API are formatted in valid JSON syntax regardless of the success or failure of the operation.

## Testing the API

Ensure that the API responds correctly according to the specifications above. Consider the following scenarios:

1. **Creating a Student with Email**: Verify that the API correctly creates a student with valid data, returning the appropriate ID and email.
2. **Error on Invalid Student Creation (Missing Email)**: Attempt to create a student without an email and check for the correct error response.

## Conclusion

This document should provide a comprehensive overview of the updated API for creating and retrieving students. Ensure that all integration tests cover these new functionalities to maintain the application's robustness.