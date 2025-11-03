---
# src/api/docs/student_api.md

# Student API Documentation

## Overview
This document outlines the API endpoints available for managing Student entities within the system, including functionality for creating and retrieving students.

## Entity Management

### Student Entity
The Student entity has been updated to include a required `email` field. The following validations are applied:
- The `email` field cannot be empty.
- The `email` field must follow a valid email format.

## API Endpoints

### Create Student
- **Endpoint**: `POST /students`
- **Description**: Create a new student.
- **Request Body**:
  ```json
  {
    "name": "student_name",
    "email": "student_email@example.com"
  }
  ```
- **Response**:
  - **Success (201 Created)**:
    ```json
    {
      "message": "Student created successfully.",
      "student": {
        "id": student_id,
        "name": "student_name",
        "email": "student_email@example.com"
      }
    }
    ```
  - **Error (400 Bad Request)**: Invalid email format or missing fields
    ```json
    {
      "error": {
        "code": "E001",
        "message": "Invalid email format.",
        "details": {}
      }
    }
    ```

### Get Student
- **Endpoint**: `GET /students/{id}`
- **Description**: Retrieve a specific student's details.
- **Response**:
  - **Success (200 OK)**:
    ```json
    {
      "id": student_id,
      "name": "student_name",
      "email": "student_email@example.com"
    }
    ```
  - **Error (404 Not Found)**: Student does not exist
    ```json
    {
      "error": {
        "code": "E002",
        "message": "Student not found.",
        "details": {}
      }
    }
    ```

## Database Management

### Database Schema Update
The SQLite database schema has been updated to include the `email` field in the `students` table. Existing student data has been preserved during this migration process.

## JSON Response Format
All API responses consistently return data in JSON format, including the newly added `email` field where applicable.

## Success Criteria
1. Students can be created successfully with valid names and email inputs.
2. Accurate student information is returned upon request, including the email.
3. User-friendly error messages for invalid email data inputs.
4. Database migration preserves existing student data.
5. All API responses utilize JSON format consistently, as specified.

---
