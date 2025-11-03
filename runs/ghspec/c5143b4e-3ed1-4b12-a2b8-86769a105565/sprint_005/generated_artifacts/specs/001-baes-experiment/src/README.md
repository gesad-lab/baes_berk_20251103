# Updated README.md

# Teacher Management API

## Overview & Purpose
The purpose of this feature is to create a new Teacher entity within the existing system that allows easy management and storage of teacher-related information. By introducing this entity with essential fields such as name and email, we aim to enhance the application’s ability to track and manage educators, which is crucial for effective educational administration. This addition will lay the groundwork for potential future functionality, such as linking teachers to courses or students.

## API Endpoints

### Creating Teacher Entity
- **POST** `/teachers`
  - **Description**: Create a new Teacher record.
  - **Request Body**:
    ```json
    {
      "name": "string",    // Required: The name of the teacher
      "email": "string"    // Required: The email of the teacher
    }
    ```
  - **Responses**:
    - **201 Created**: Returns the newly created Teacher object.
      ```json
      {
        "id": "string",      // Unique identifier for the Teacher
        "name": "string",    // Name of the teacher
        "email": "string",    // Email of the teacher
        "created_at": "timestamp", // Timestamp for when the record was created
        "updated_at": "timestamp"  // Timestamp for when the record was last updated
      }
      ```
    - **400 Bad Request**: If either `name` or `email` is missing or if the email is incorrectly formatted.
      ```json
      {
        "error": {
          "code": "E001",  // Validation error code
          "message": "Invalid input",
          "details": {
            "name": "Name is required",
            "email": "Email format is invalid" // Specific validation messages
          }
        }
      }
      ```

## User Scenarios & Testing
1. **Create a Teacher**:
   - As an admin user, I want to create a Teacher record by providing the name and email, ensuring that the teacher's information is accurately captured.
   - **Test**: Ensure that a POST request to the `/teachers` endpoint with valid name and email fields creates a new Teacher record and returns the created Teacher object in JSON format.
   - **Edge Cases**: Test cases should ensure appropriate validation error messages are returned for missing or invalid fields.

## Environment Setup
- Ensure Python packages such as `FastAPI`, `SQLAlchemy`, and `Alembic` are installed and functional.

---

This update provides complete details about the new Teacher entity management, ensuring clarity on usage and requirements for the API endpoint.