# README.md

# Project Title

## Overview & Purpose

The purpose of this feature is to enhance the existing Student entity by adding an email address attribute. This update aims to provide better student management, allowing educators and administrators to communicate effectively with students. The inclusion of the email field will also facilitate potential future integrations, such as notifications and announcements through email, thus improving overall communication within the educational setting.

## Functional Requirements

1. **Update Student Entity**:
   - The Student entity must include a new field: `email` (string, required).

2. **Create Student Entity with Email**:
   - Users must be able to submit a POST request to create a new Student with both `name` and `email`.
   - The email must be a valid format and not empty.
   - **Example Request**:
     ```http
     POST /api/v1/students
     Content-Type: application/json

     {
       "name": "John Doe",
       "email": "john.doe@example.com"
     }
     ```
   - **Example Response**:
     ```json
     {
       "id": 1,
       "name": "John Doe",
       "email": "john.doe@example.com"
     }
     ```

3. **Retrieve Student Including Email**:
   - Users must be able to submit a GET request to retrieve a student by their ID.
   - The response should include the student's ID, name, and email, or an error message if the student does not exist.
   - **Example Request**:
     ```http
     GET /api/v1/students/1
     ```
   - **Example Response**:
     ```json
     {
       "id": 1,
       "name": "John Doe",
       "email": "john.doe@example.com"
     }
     ```
   - **Example Error Response**:
     ```json
     {
       "error": {
         "code": "E001",
         "message": "Student not found."
       }
     }
     ```

4. **Database Schema Update**:
   - Update the database schema to include the `email` field for the Student entity.
   - The database migration process must ensure that existing Student data is preserved.

5. **JSON Responses**:
   - All API responses must be in JSON format, including both success responses and error messages.

## Example JSON Structure

- **Create Student Response**: 
```json
{
  "id": 1,
  "name": "John Doe",
  "email": "john.doe@example.com"
}
```
- **Error Response**: 
```json
{
  "error": {
    "code": "E002",
    "message": "Invalid email format."
  }
}
```

## Testing

Unit tests and integration tests must be written to ensure that the new email functionality works correctly and integrates seamlessly with the existing student management system. Additionally, tests should verify that responses adhere to the updated JSON structure.

## Deployment Considerations

Ensure the migration processes are smooth by confirming the email addition does not disrupt existing operations. Health check endpoints may be included for monitoring after deployment.