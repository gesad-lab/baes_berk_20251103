# student_api/README.md

# Student API

This is the documentation for the Student API, a RESTful service for managing student entities. 

## Endpoints

### Create Student

- **POST** `/students`
- **Request Body**:
  ```json
  {
    "name": "string",  // Required: The name of the student
    "email": "string"  // Required: The email of the student
  }
  ```
- **Response**:
  - **201 Created**: Returns the created Student object.
    ```json
    {
      "id": "integer",
      "name": "string",
      "email": "string"
    }
    ```
- **Error Responses**:
  - **400 Bad Request**: If the `email` is missing or invalid.
    ```json
    {
      "error": {
        "code": "E001",
        "message": "Email field is required."
      }
    }
    ```

### Retrieve Students

- **GET** `/students`
- **Response**:
  - **200 OK**: Returns a list of all Student objects.
    ```json
    [
      {
        "id": "integer",
        "name": "string",
        "email": "string"
      }
    ]
    ```

## Database Migration

Upon the addition of the `email` field to the Student entity, the existing SQLite database schema will be updated. The migration process will ensure that all existing student data is preserved.

## Email Validation

The API now includes validation for the `email` field during student creation. A valid email format is required, and appropriate error messages will be returned for any missing or invalid entries.

## Overview & Purpose

This API allows for the management of student entities, including adding email contact details for each student, thereby enhancing data management capabilities and user interaction.

## Environment Setup

Make sure to install or update the necessary packages, including FastAPI, SQLAlchemy, and Alembic for handling migrations.

## Usage

Refer to the endpoint details above to interact with the Student API. Ensure that appropriate data is provided for successful operations.