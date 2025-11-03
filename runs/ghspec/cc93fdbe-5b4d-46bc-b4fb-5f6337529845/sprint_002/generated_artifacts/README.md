# README.md

# Student Management Web Application

This application provides a simple interface for managing student records.

## API Endpoints

### POST /students
Create a new student record.

**Request Body**:
```json
{
  "name": "string",
  "email": "string" // new parameter: the email address of the student
}
```

**Response**:
- **201 Created**: When the student is successfully created.
- **400 Bad Request**: If the mandatory fields are missing or invalid.

### GET /students/{id}
Retrieve a student record by ID.

**Path Parameters**:
- `id`: The unique identifier of the student.

**Response**:
- **200 OK**: Returns the student record.
  ```json
  {
    "id": "string",
    "name": "string",
    "email": "string" // new field: the student's email address
  }
  ```
- **404 Not Found**: If the student with the given ID does not exist.

## Migration Guide

To facilitate the addition of the `email` parameter for students, the following schema updates have been made in the database:

1. The `students` table has been modified to include a new column:
   - `email`: STRING, must be a valid email format.

Ensure your application and database are updated accordingly. Migration scripts have been provided to handle these changes seamlessly.

For further assistance, please refer to the detailed migration documentation included in the project. 

Thank you for using the Student Management Web Application!