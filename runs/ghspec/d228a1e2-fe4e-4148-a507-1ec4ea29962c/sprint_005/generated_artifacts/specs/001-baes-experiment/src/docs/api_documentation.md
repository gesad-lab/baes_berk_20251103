---
# API Documentation for Teacher Management

## 1. Create Teacher API Endpoint
- **Method**: POST
- **URL**: `/teachers`
- **Request Body**: 
  - A JSON object containing the following required fields:
    - `name`: (string) The name of the teacher.
    - `email`: (string) The email of the teacher.
- **Response**:
  - On success (HTTP Status 201):
    ```json
    {
      "success": true,
      "message": "Teacher created successfully."
    }
    ```
  - On failure (HTTP Status 400):
    ```json
    {
      "success": false,
      "error": {
        "code": "E001",
        "message": "Invalid input."
      }
    }
    ```

## 2. List Teachers API Endpoint
- **Method**: GET
- **URL**: `/teachers`
- **Response**:
  - A JSON array containing objects for each teacher:
    ```json
    [
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
    ```

## 3. Get Teacher Details API Endpoint
- **Method**: GET
- **URL**: `/teachers/{teacher_id}`
- **Response**:
  - A JSON object containing the details of the requested teacher:
    ```json
    {
      "id": 1,
      "name": "John Doe",
      "email": "john.doe@example.com"
    }
    ```
  - On failure (HTTP Status 404):
    ```json
    {
      "success": false,
      "error": {
        "code": "E002",
        "message": "Teacher not found."
      }
    }
    ```

## 4. Database Migration
- Update the database schema to introduce a `teacher` table with the following fields:
  - `id`: Integer (primary key)
  - `name`: String (required)
  - `email`: String (required, should be unique)
- Ensure that the migration script preserves all existing `Student` and `Course` data during this structural change.

## 5. Out of Scope
- User authentication, authorization, and role management are not included in this phase.
- UI or front-end components for interacting with the Teacher API are not part of this specification.
- Advanced features such as teacher assignments to specific courses or students, and performance tracking, are outside the current requirement.
- Updates or deletions of existing teachers beyond creation and retrieval are not included in this initial scope. 

## 6. Future Considerations
Future phases may involve:
- Implementing user roles to manage teacher assignments.
- Enhancing features for tracking teacher assignments, performances, and courses managed by each teacher.
- Adding the ability to update and delete teachers beyond the initial create and retrieve functionalities.

---