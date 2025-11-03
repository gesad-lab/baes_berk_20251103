# src/docs/api_documentation.md

# API Documentation

## Endpoints

### Create Student
- **Endpoint**: `POST /students`
- **Request Body**: 
  ```
  {
    "name": "<student_name>",
    "email": "<student_email>"
  }
  ```
  - Both `name` and `email` fields are required.
  
- **Success Response**:
  - **Status Code**: `201 Created`
  - **Response Body**: 
  ```
  {
    "id": "<student_id>",
    "name": "<student_name>",
    "email": "<student_email>"
  }
  ```

### Get All Students
- **Endpoint**: `GET /students`
  
- **Success Response**:
  - **Status Code**: `200 OK`
  - **Response Body**:
  ```
  [
    {
      "id": "<student_id>",
      "name": "<student_name>",
      "email": "<student_email>"
    },
    ...
  ]
  ```

## Error Responses
- **Missing Email**
  - **Condition**: If the request to create a student lacks the `email` field.
  - **Response**:
    - **Status Code**: `400 Bad Request`
    - **Response Body**:
    ```
    {
      "error": {
        "code": "E001",
        "message": "Email field is required.",
        "details": {}
      }
    }
    ```

## Migration Notes
- Ensure that the database schema includes the new `email` column in the `students` table. You must set up a migration step using Alembic to add this column without affecting current data.

## Testing Scenarios
1. **Creating a Student Record with Email**:
   - Submit a `POST` request with student details including an email and verify the success response contains the email.

2. **Retrieving Student Records with Email**:
   - Send a `GET` request and check that the returned JSON array includes the email field.

3. **Handling Errors for Missing Email**:
   - Attempt to create a student record with no email and validate that the correct error message is returned.

### Additional Notes
Make sure to integrate additional tests to cover the new functionality introduced by the email field, following the principles of unit, integration, and API response verification as discussed in the specifications.