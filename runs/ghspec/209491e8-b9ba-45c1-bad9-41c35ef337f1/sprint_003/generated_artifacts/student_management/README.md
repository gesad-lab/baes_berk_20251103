# student_management/README.md

# Student Management API

## Overview

This project provides an API for managing students and courses in an educational setting using FastAPI and SQLite.

## API Endpoints

### Student Management Endpoints

- **Create Student**
  - `POST /students`
  - **Request Body**: JSON object with student details
  - **Response**: Created student details
  
- **Retrieve Students**
  - `GET /students`
  - **Response**: JSON array of student records

### Course Management Endpoints

#### Create a New Course
- **Endpoint**: `POST /courses`
- **Description**: Create a new course with details.
- **Request Body**: 
  ```json
  {
    "name": "Introduction to Programming",
    "level": "Beginner"
  }
  ```
- **Response**: 
  - **201 Created**: JSON object with created course details:
    ```json
    {
      "id": 1,
      "name": "Introduction to Programming",
      "level": "Beginner"
    }
    ```
- **Error Responses**:
  - **400 Bad Request**: If `name` or `level` is missing or invalid.
    - Example Error:
    ```json
    {
      "error": {
        "code": "E001",
        "message": "Missing required fields: name, level",
        "details": {}
      }
    }
    ```

#### Retrieve All Courses
- **Endpoint**: `GET /courses`
- **Description**: Retrieve a list of all courses.
- **Response**: 
  - **200 OK**: JSON array of course records:
    ```json
    [
      {
        "id": 1,
        "name": "Introduction to Programming",
        "level": "Beginner"
      },
      {
        "id": 2,
        "name": "Advanced Algorithms",
        "level": "Advanced"
      }
    ]
    ```

### Error Handling
All API responses are returned in JSON format. If input validation fails, appropriate error messages are returned indicating what went wrong and how to correct it.

## Testing
- Perform API tests to ensure endpoints handle the creation and retrieval of courses effectively.
- Validate that appropriate error messages are returned for missing or invalid inputs.

## Database Migration
Ensure that the database schema includes a `courses` table with fields for `name` and `level`, and that these migrations do not disrupt existing student data. 

## Development Setup
Follow the instructions in `README.md` for setting up the project environment, including installing necessary dependencies listed in `requirements.txt`.

## Contribution
Ensure all new features are documented and include corresponding tests in the `tests` directory.