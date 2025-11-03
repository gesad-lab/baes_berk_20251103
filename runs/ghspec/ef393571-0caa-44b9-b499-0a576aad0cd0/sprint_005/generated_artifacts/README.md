# Updated README.md with Teacher API Documentation

# README.md

## Overview & Purpose
The purpose of this feature is to create a new Teacher entity within the existing educational management system. This will support the need for managing information related to teachers, which is essential for handling course assignments, teaching responsibilities, and facilitating communication with students. By integrating the Teacher entity, we will enhance the overall capabilities of the system, paving the way for future features involving teacher-student interactions and course management.

## Teacher API Endpoints

### Create a Teacher
- **Endpoint**: `POST /teachers`
- **Description**: This endpoint creates a new Teacher entity in the system.
- **Request Body**:
  ```json
  {
      "name": "string",
      "email": "string"
  }
  ```
  - `name`: The name of the teacher (Required)
  - `email`: The email address of the teacher (Required)

- **Responses**:
  - **201 Created**: Successful creation of a Teacher entity.
    ```json
    {
        "message": "Teacher created successfully.",
        "teacher_id": 1
    }
    ```
  - **400 Bad Request**: Invalid input data.
    ```json
    {
        "error": {
            "code": "E001",
            "message": "Invalid input data.",
            "details": {
                "name": "must not be empty",
                "email": "must be a valid email"
            }
        }
    }
    ```

### List Teachers
- **Endpoint**: `GET /teachers`
- **Description**: This endpoint retrieves a list of all teachers in the system.
- **Responses**:
  - **200 OK**: Returns a list of Teacher entities.
    ```json
    {
        "teachers": [
            {
                "id": 1,
                "name": "John Doe",
                "email": "john.doe@example.com"
            },
            {
                "id": 2,
                "name": "Jane Smith",
                "email": "jane.smith@example.com"
            }
        ]
    }
    ```

## Database Migration
The database migration will ensure that existing Student and Course data is preserved while integrating the new Teacher table.

## Success Criteria
1. The application starts successfully and updates the existing database schema to include the Teacher table.
2. A Teacher can be created with valid inputs, confirmed by a successful API response.
3. Teachers can be listed, and the application provides the correct data for all Teacher entities.
4. The application properly handles creation attempts with invalid input data, returning appropriate error messages and status codes.

## Additional Sections
(Existing sections below remain unchanged)

## Setup
(Setup instructions and other existing content remains as is)

---

*This update includes the newly defined API endpoints for managing Teacher entities, allowing for enhanced educational management capabilities within the system.*