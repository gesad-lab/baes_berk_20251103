# Updated README.md

# Course Management API

This document outlines the API for managing courses within the Student Management application.

## API Endpoints

### Create a New Course

- **Endpoint**: `/api/v1/courses`
- **Method**: `POST`
- **Request Body**:
    ```json
    {
        "name": "Course Name",
        "level": "Course Level"
    }
    ```
- **Success Response**:
    - **Code**: 201 Created
    - **Content**:
    ```json
    {
        "id": 1,
        "name": "Course Name",
        "level": "Course Level"
    }
    ```

- **Error Responses**:
    - **Code**: 400 Bad Request
    - **Content**:
    ```json
    {
        "error": {
            "code": "E001",
            "message": "Invalid input: name and level are required."
        }
    }
    ```
  
### Retrieve All Courses

- **Endpoint**: `/api/v1/courses`
- **Method**: `GET`
- **Success Response**:
    - **Code**: 200 OK
    - **Content**:
    ```json
    [
        {
            "id": 1,
            "name": "Course Name",
            "level": "Course Level"
        }
    ]
    ```

### Update a Course

- **Endpoint**: `/api/v1/courses/<id>`
- **Method**: `PUT`
- **Request Body**:
    ```json
    {
        "level": "New Course Level"
    }
    ```
- **Success Response**:
    - **Code**: 200 OK
    - **Content**:
    ```json
    {
        "message": "Course updated successfully."
    }
    ```

- **Error Responses**:
    - **Code**: 400 Bad Request
    - **Content**:
    ```json
    {
        "error": {
            "code": "E002",
            "message": "Invalid input: level must be provided."
        }
    }
    ```

## Security Measures

- All inputs are sanitized to prevent SQL injection and other vulnerabilities.

## Migration Steps

Ensure the following migrations are applied before running the service:
1. Create the Course table with appropriate fields.
2. Ensure data integrity by maintaining foreign key constraints with existing Student records.

## Logging

Logging practices are in place to ensure that sensitive data is not exposed, while providing sufficient context for debugging errors.

---

## Setup Instructions

To run the application:
1. Ensure you have the required environment set up.
2. Run database migrations.
3. Start the Flask application.

For detailed contribution and usage, refer to the installation and deployment sections.

--- 

This update to the `README.md` file reflects new API endpoints and emphasizes the importance of input sanitization to prevent SQL injection and other attacks within the Course service.