# Updated README.md with New API Documentation

# Project Title

This project is an educational management system.

## Overview

The application is designed to facilitate the management of educational resources such as students, courses, and teachers.

## API Documentation

### Create a Teacher

- **Endpoint**: `POST /api/v1/teachers`
- **Request Body**:
  ```json
  {
    "name": "string (required)",
    "email": "string (required)"
  }
  ```
- **Response (Success)**:
  ```json
  {
    "id": "integer",
    "name": "string",
    "email": "string"
  }
  ```
- **Response (Error)**:
  - 400 Bad Request: If `name` or `email` fields are missing or invalid.
  ```json
  {
    "error": {
      "code": "E001",
      "message": "Invalid input: name and email are required."
    }
  }
  ```

### Get Teacher Details

- **Endpoint**: `GET /api/v1/teachers/{id}`
- **Response (Success)**:
  ```json
  {
    "id": "integer",
    "name": "string",
    "email": "string"
  }
  ```
- **Response (Error)**:
  - 404 Not Found: If the teacher with the specified ID does not exist.
  ```json
  {
    "error": {
      "code": "E002",
      "message": "Teacher not found."
    }
  }
  ```

## Database Schema

- **Table Name**: `teachers`
- **Columns**:
  - `id`: Integer, primary key, auto-increment.
  - `name`: String, required.
  - `email`: String, required.

### Database Migration

A migration will be executed to create the `teachers` table, ensuring that existing `Student` or `Course` data remains unaffected.

## Testing

Ensure that the following test scenarios are covered:

1. **Creating a Teacher**:
   - Verify that creating a teacher with valid name and email fields successfully saves the record in the database and returns the created teacher’s details in JSON format.

2. **Retrieving a Teacher's Details**:
   - Verify the retrieval of a teacher’s details using a valid ID, ensuring the correct JSON response format.

## Setup

To set up the project, follow these steps:

1. Clone the repository.
2. Install dependencies listed in `requirements.txt`.
3. Configure the database connection in the environment variables.
4. Run migrations to set up the database structure.
5. Start the FastAPI application.

## Health Check

Implement a health check endpoint to verify the status of the application and new features.

---

Keep this section updated with any subsequent changes to the API or database schema for consistency across the documentation.