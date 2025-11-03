# docs/api_documentation.md

## API Documentation

### Create Student
- **Endpoint**: `POST /students`
- **Request Body**:
  ```json
  {
    "name": "string, required",
    "email": "string, required, format: valid_email@example.com"
  }
  ```
  - **Details**:
    - **name**: The student's name (string, required).
    - **email**: The student's email (string, required and must be unique). It should follow the standard email format (e.g., `user@example.com`).
      - **Validation**: The email field should be validated to ensure that it meets format requirements. If the format is incorrect, an error response should be returned.
- **Response**:
  ```json
  {
    "id": "integer",
    "name": "string",
    "email": "string"
  }
  ```
  - **Example**:
    ```json
    {
      "id": 1,
      "name": "John Doe",
      "email": "john.doe@example.com"
    }
    ```
  
### Retrieve Student
- **Endpoint**: `GET /students/{id}`
- **Response**:
  ```json
  {
    "id": "integer",
    "name": "string",
    "email": "string"
  }
  ```
  - **Example**:
    ```json
    {
      "id": 1,
      "name": "John Doe",
      "email": "john.doe@example.com"
    }
    ```
  - If the student is not found, an error message will be returned:
    ```json
    {
      "error": {
        "code": "E404",
        "message": "Student not found"
      }
    }
    ```

### Database Schema
- The `Student` table schema has been updated to include:
  - `email`: TEXT NOT NULL UNIQUE (new field).

### Database Migration
- A migration script must be created to add the email field to the `Student` table without affecting existing data:
  - Ensure that existing records are not impacted and that new records must include a valid email format as outlined above.

### Notes
- Ensure proper error handling scenarios are managed effectively to provide clear and actionable responses to the user regarding the email field validation.