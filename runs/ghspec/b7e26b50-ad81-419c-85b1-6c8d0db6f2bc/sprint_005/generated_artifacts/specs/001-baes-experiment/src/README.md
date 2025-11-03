---
# README.md

## Teacher Creation Feature

### Overview & Purpose
The purpose of this feature is to create a new Teacher entity within the application. This will allow for the management of teacher information, including their names and email addresses. By establishing the Teacher entity, we enhance the system's ability to track educators, facilitating better management of course assignments and communication within the educational environment.

### API Specifications

#### Create Teacher Endpoint
- **Endpoint**: `POST /teachers`
- **Request Body**:
  - `name`: string (required)
  - `email`: string (required, must be unique)
  
- **Response**:
  - **201 Created**: 
    ```json
    {
      "id": <teacher_id>,
      "name": "<teacher_name>",
      "email": "<teacher_email>"
    }
    ```
  - **400 Bad Request**: If the request body is missing the `name` or `email`:
    ```json
    {
      "error": {
        "code": "E400",
        "message": "Missing required field",
        "details": {"field": "name or email"}
      }
    }
    ```
  - **409 Conflict**: If the email already exists in the system:
    ```json
    {
      "error": {
        "code": "E409",
        "message": "Email must be unique"
      }
    }
    ```

### Database Schema Update
- **New Table**: `Teacher`
  - `id`: integer, primary key, auto-increment
  - `name`: string, required
  - `email`: string, required, unique

### Migration
A database migration will be created to add the new `Teacher` table while preserving existing data in the `Student` and `Course` tables. It is critical that existing data within these tables remains intact during this process.

### Success Criteria
- The application can successfully create a teacher record through the specified endpoint and return appropriate success messages in JSON format.
- The application correctly handles error cases, providing clear messages for missing or duplicate information.
- Coverage for the teacher creation functionality is at least 70% with automated tests.
- Verify that the database migration script correctly establishes the `teachers` table and preserves existing records in the `Student` and `Course` tables.

## Testing & Validation
- Unit tests must be written in `tests/test_api.py` to ensure functionality for creating teachers, achieving at least 70% coverage on associated business logic.

### Deployment
Ensure that the Docker configuration remains intact and tested with the new functionality.

---