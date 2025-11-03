# README.md

# Project Overview

This project is focused on managing educational entities, specifically students, courses, and teachers. The goal is to enhance the educational database structure for effective management and association of these entities.

## API Endpoints

### Teachers Management

#### 1. Create a Teacher
- **Endpoint**: `POST /teachers`
- **Request Body**: 
  ```json
  {
    "name": "string (required)",
    "email": "string (required)"
  }
  ```
- **Response**: 
  - **Status**: `201 Created`
  - **Body**: The created teacher object with an additional `id` field:
    ```json
    {
      "id": 1,
      "name": "John Doe",
      "email": "john@example.com"
    }
    ```

#### 2. Retrieve Teacher Information
- **Endpoint**: `GET /teachers/{id}`
- **Response**:
  - **Status**: `200 OK` or `404 Not Found`
  - **Body for 200 OK**: The requested teacher object, including `name` and `email` attributes:
    ```json
    {
      "id": 1,
      "name": "John Doe",
      "email": "john@example.com"
    }
    ```

#### 3. List All Teachers
- **Endpoint**: `GET /teachers`
- **Response**:
  - **Status**: `200 OK`
  - **Body**: An array of teacher objects, each including their `id`, `name`, and `email`:
    ```json
    [
      {
        "id": 1,
        "name": "John Doe",
        "email": "john@example.com"
      },
      {
        "id": 2,
        "name": "Jane Smith",
        "email": "jane@example.com"
      }
    ]
    ```

#### 4. Validation
- Input validation is performed to ensure that both `name` and `email` fields are provided when creating a teacher.
- The email format is validated to ensure it adheres to standard email formats. If validation fails, an appropriate error response is returned.

## Testing

Integration tests are implemented to validate that the `/teachers` endpoints work as expected through the following scenarios:

- **Test Case 1**: Verify that a new teacher can be created successfully with valid name and email fields. 
  - Expected: Returns a 201 Created status and the created teacher object.

- **Test Case 2**: Confirm that retrieving a teacher by ID returns the correct information. 
  - Expected: Returns the teacher object for the valid ID or 404 Not Found for an invalid ID.

- **Test Case 3**: Validate that listing all teachers displays a complete set of teacher records. 
  - Expected: Returns a 200 OK status and an array of teacher objects.

- **Test Case 4**: Ensure appropriate error messages are returned for invalid teacher creation attempts (e.g., missing name or email).
  - Expected: Returns 400 Bad Request with a clear error message when creating a teacher with invalid input.

These tests help guarantee the reliability and correctness of the teacher management feature within the application, allowing for effective additions and further integrations in the future.