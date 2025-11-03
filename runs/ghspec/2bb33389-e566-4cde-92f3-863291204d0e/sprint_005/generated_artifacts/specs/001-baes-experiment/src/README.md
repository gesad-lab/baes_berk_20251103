# README.md

# Project Title

## Introduction
This project serves as a RESTful API for managing educational entities, particularly focusing on teachers, courses, and students.

## New Functionality
### Teacher Management
With this latest update, the API now supports the creation of teachers. This includes validation for the required fields and error handling for invalid input.

### Endpoints
#### Create a Teacher
- **Endpoint**: `/api/v1/teachers`
- **Method**: `POST`
- **Request Body**: 
    ```json
    {
        "name": "John Doe",
        "email": "john.doe@example.com"
    }
    ```

- **Success Response**:
    - **Code**: 201
    - **Response Body**:
    ```json
    {
        "message": "Teacher created successfully",
        "teacher": {
            "id": 1,
            "name": "John Doe",
            "email": "john.doe@example.com"
        }
    }
    ```

- **Error Responses**:
  - **Missing Name**:
    - **Code**: 400
    - **Response Body**:
    ```json
    {
        "error": {
            "code": "E001",
            "message": "Name is required"
        }
    }
    ```
  
  - **Missing Email**:
    - **Code**: 400
    - **Response Body**:
    ```json
    {
        "error": {
            "code": "E002",
            "message": "Email is required"
        }
    }
    ```

  - **Invalid Email Format**:
    - **Code**: 400
    - **Response Body**:
    ```json
    {
        "error": {
            "code": "E003",
            "message": "Invalid email format"
        }
    }
    ```

## Usage Examples
### Example 1: Successful Teacher Creation
```bash
curl -X POST "http://localhost:8000/api/v1/teachers" -H "Content-Type: application/json" -d '{"name": "Jane Doe", "email": "jane.doe@example.com"}'
```

### Example 2: Teacher Creation Without Name
```bash
curl -X POST "http://localhost:8000/api/v1/teachers" -H "Content-Type: application/json" -d '{"email": "missing.name@example.com"}'
```

### Example 3: Teacher Creation With Invalid Email
```bash
curl -X POST "http://localhost:8000/api/v1/teachers" -H "Content-Type: application/json" -d '{"name": "Invalid Email", "email": "invalid.email"}'
```

## Database Migration
On application startup, the system checks for the existence of the new `Teacher` table in the SQLite database schema. This migration ensures that existing data in the `Students` and `Courses` tables remains intact.

## Conclusion
This update significantly enhances the API's functionality, thereby supporting educational management with the addition of teacher data handling. Users are encouraged to test the new implementation and report any issues through the project's issue tracker.