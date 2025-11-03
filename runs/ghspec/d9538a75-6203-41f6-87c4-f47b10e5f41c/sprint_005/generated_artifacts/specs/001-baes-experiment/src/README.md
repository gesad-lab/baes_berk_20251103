# README.md

# Teacher Management API Documentation

## Overview
This documentation outlines the newly added API endpoints for managing teachers within the system. The introduction of the `Teacher` entity enhances the management of educational staff.

## Teacher Entity

### Fields
- `name`: A required string that represents the teacher’s name.
- `email`: A required string that represents the teacher’s email. Must be unique.

### Database Schema
A new `Teacher` table has been created with the following attributes:
- `id`: An auto-incrementing integer that serves as the primary key.
- `name`: A string that is required.
- `email`: A string that is required and must be unique.

## API Endpoints

### Create Teacher
- **Endpoint**: `POST /api/v1/teachers`
- **Description**: Creates a new teacher in the system.
- **Request Body**:
    ```json
    {
        "name": "John Doe",
        "email": "john.doe@example.com"
    }
    ```
- **Response**:
    - **201 Created** on successful creation:
    ```json
    {
        "id": 1,
        "name": "John Doe",
        "email": "john.doe@example.com"
    }
    ```
    - **400 Bad Request** if validation fails (e.g., missing fields, duplicate email):
    ```json
    {
        "error": {
            "code": "E001",
            "message": "Validation error",
            "details": {
                "name": "Field is required",
                "email": "Email must be unique"
            }
        }
    }
    ```

### Retrieve Teacher
- **Endpoint**: `GET /api/v1/teachers/<int:teacher_id>`
- **Description**: Retrieves the details of a specific teacher.
- **Response**:
    - **200 OK** on successful retrieval:
    ```json
    {
        "id": 1,
        "name": "John Doe",
        "email": "john.doe@example.com"
    }
    ```
    - **404 Not Found** if the teacher does not exist:
    ```json
    {
        "error": {
            "code": "E002",
            "message": "Teacher not found"
        }
    }
    ```

## Migrations
Make sure to run the required migration scripts to add the `Teacher` table to the existing database without affecting the existing `Student` and `Course` tables.

## Out of Scope
- Integration of teachers with courses and students.
- Advanced functionalities like teacher performance tracking or analytics.
- Front-end user interface modifications for teacher management.
- The removal or modification of existing entities, such as students or courses.

## Testing
Unit tests for the new API endpoints have been added to ensure functionality and validation checks. Minimum coverage is expected to meet the project's quality standards.

For any further questions, please refer to the technical documentation or contact the development team.