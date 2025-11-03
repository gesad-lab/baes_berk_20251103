# README.md

# Student Management System

## API Documentation

### Creating a Student

- **Endpoint**: `POST /students`
- **Description**: Create a new Student by providing a name and an email address.
- **Request Body**:
  ```json
  {
      "name": "John Doe",
      "email": "john.doe@example.com"
  }
  ```
- **Successful Response**:
  - **Status Code**: 201 Created
  - **Response Body**:
  ```json
  {
      "message": "Student created successfully.",
      "student": {
          "id": 1,
          "name": "John Doe",
          "email": "john.doe@example.com"
      }
  }
  ```
- **Error Responses**:
  - **400 Bad Request**: If the email field is missing or improperly formatted.
    - **Response**:
    ```json
    {
        "error": {
            "code": "E001",
            "message": "Email is required."
        }
    }
    ```
    ```json
    {
        "error": {
            "code": "E002",
            "message": "Invalid email format."
        }
    }
    ```

### Retrieving a Student

- **Endpoint**: `GET /students/{id}`
- **Description**: Retrieve details of a Student using their unique identifier.
- **Successful Response**:
  - **Status Code**: 200 OK
  - **Response Body**:
  ```json
  {
      "id": 1,
      "name": "John Doe",
      "email": "john.doe@example.com"
  }
  ```

### Handling Invalid Email Input

- **Scenario**: If a user attempts to create a Student without providing an email.
- **Expected Response**:
  ```json
  {
      "error": {
          "code": "E001",
          "message": "Email is required."
      }
  }
  ```

- **Scenario**: If the user provides an improperly formatted email address.
- **Expected Response**:
  ```json
  {
      "error": {
          "code": "E002",
          "message": "Invalid email format."
      }
  }
  ```

## Success Criteria

1. The application can successfully create a Student when provided with a valid name and a valid email.
2. The application returns the created Student’s details in JSON format, including the email.
3. The application can correctly fetch a Student’s details, including the email, when queried by ID.
4. The application handles invalid email input by returning clear error messages indicating validation failures.

## Assumptions

- The system will validate email address formats correctly before accepting them.
- The existing Student entity can be extended without performance impact.
- The schema migration will be tested against a sample of existing student data to ensure data integrity.

## Development Notes

- Ensure to run the necessary database migrations to reflect the changes in the data model.
- Update tests to include cases for the new email functionality to ensure comprehensive test coverage.