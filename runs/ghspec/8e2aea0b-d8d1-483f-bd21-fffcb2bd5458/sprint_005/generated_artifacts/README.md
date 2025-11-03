# Updated README.md

# Project Overview

This project is a simple student registration system that allows administrators to manage teachers and courses with an emphasis on clean architecture and maintainability.

## User Scenarios & Testing

1. **Create a New Teacher**: 
   - As an administrator, I want to add a new teacher with their name and email address to the system so that they can be associated with courses.
   - **Test**: Submit a request to create a new teacher and verify that the teacher is successfully added to the database.

    ```bash
    curl -X POST http://localhost:5000/teachers \
    -H "Content-Type: application/json" \
    -d '{"name": "John Doe", "email": "john.doe@example.com"}'
    ```

    Expected Response:
    ```json
    {
      "message": "Teacher successfully created.",
      "teacher_id": 1,
      "name": "John Doe",
      "email": "john.doe@example.com"
    }
    ```
   
2. **View Teacher Information**: 
   - As a user, I want to retrieve information about a specific teacher so that I can check their name and email address.
   - **Test**: Request the details of a teacher and confirm that the correct name and email are displayed.

    ```bash
    curl -X GET http://localhost:5000/teachers/1
    ```

    Expected Response:
    ```json
    {
      "teacher_id": 1,
      "name": "John Doe",
      "email": "john.doe@example.com"
    }
    ```

3. **Error Handling for Invalid Teacher Creation**: 
   - As an administrator, I want to receive feedback when I attempt to create a teacher without providing a name or email, ensuring data integrity.
   - **Test**: Attempt to create a teacher with missing required fields and verify that appropriate error messages are returned.

    Example Error Request:
    ```bash
    curl -X POST http://localhost:5000/teachers \
    -H "Content-Type: application/json" \
    -d '{"name": "", "email": ""}'
    ```

    Expected Response:
    ```json
    {
      "error": {
        "code": "E001",
        "message": "Name and email are required.",
        "details": {}
      }
    }
    ```

4. **Ensure Unique Email Addresses**: 
   - As an administrator, I want to ensure that each teacher's email address is unique in the database.
   - **Test**: Submit a request to create a teacher with an email that already exists and verify that the appropriate error message is returned.

    Example Error Request:
    ```bash
    curl -X POST http://localhost:5000/teachers \
    -H "Content-Type: application/json" \
    -d '{"name": "Jane Smith", "email": "john.doe@example.com"}'
    ```

    Expected Response:
    ```json
    {
      "error": {
        "code": "E002",
        "message": "Email address must be unique.",
        "details": {}
      }
    }
    ```

## Functional Requirements

1. The application shall create a new Teacher entity with the following fields:
   - `name`: string, required
   - `email`: string, required and must be unique.

2. The application shall provide an endpoint to create a new teacher.
   - Endpoint: `POST /teachers`
   - Request Body: 
     ```json
     {
       "name": "string",
       "email": "string"
     }
     ```
   - Response: 
     - Status Code: `201 Created`
     - Response Body: 
     ```json
     {
       "message": "Teacher successfully created.",
       "teacher_id": "integer",
       "name": "string",
       "email": "string"
     }
     ```

3. The application shall provide an endpoint to retrieve a specific teacher's information.
   - Endpoint: `GET /teachers/{teacher_id}`
   - Response:
     - Status Code: `200 OK`
     - Response Body: 
     ```json
     {
       "teacher_id": "integer",
       "name": "string",
       "email": "string"
     }
     ```

4. The database schema shall be updated to include a new Teacher table with the specified fields, ensuring that the migration process pre...

## Input Validation

- Create a Marshmallow schema for Teacher that validates the `name` and `email` fields to ensure their presence and uniqueness.

## Test Coverage

- Create unit tests for the teacher creation functionality and retrieval of teacher data, ensuring that edge cases are covered and appropriate error messages are returned. 

- Ensure tests also cover the uniqueness of email addresses.