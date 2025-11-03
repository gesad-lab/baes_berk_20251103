# Update the OpenAPI documentation in the specified file

# File: docs/api_specification.md

# Current file content:
```markdown
# API Specification

## Overview
This document serves as the API specification for the application.

## Endpoints

### 1. User Management
- **POST /users**: Create a new user
- **GET /users/{user_id}**: Get user details

### 2. Course Management
- **POST /courses**: Create a new course
- **GET /courses/{course_id}**: Get course details
```

# Updated file content:
```markdown
# API Specification

## Overview
This document serves as the API specification for the application.

## Endpoints

### 1. User Management
- **POST /users**: Create a new user
- **GET /users/{user_id}**: Get user details

### 2. Course Management
- **POST /courses**: Create a new course
- **GET /courses/{course_id}**: Get course details

### 3. Student-Course Enrollment Management
- **POST /enrollments**: Enroll a student in a course
  - **Request Body**:
    ```json
    {
      "student_id": "string",  // The ID of the student to enroll
      "course_id": "string"     // The ID of the course to enroll in
    }
    ```
  - **Responses**:
    - **201 Created**: Enrollment successful
      ```json
      {
        "message": "Enrollment successful",
        "enrollment_id": "string"  // The ID of the newly created enrollment
      }
      ```
    - **400 Bad Request**: Invalid input parameters
      ```json
      {
        "error": {
          "code": "E001",
          "message": "Student ID and Course ID must be valid."
        }
      }
      ```

- **GET /enrollments/{enrollment_id}**: Get enrollment details
  - **Responses**:
    - **200 OK**: Enrollment found
      ```json
      {
        "student_id": "string",
        "course_id": "string",
        "status": "string" // Enrollment status
      }
      ```
    - **404 Not Found**: Enrollment not found
      ```json
      {
        "error": {
          "code": "E002",
          "message": "Enrollment not found."
        }
      }
      ```
```
