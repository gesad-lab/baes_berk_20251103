# docs/api.md

# API Documentation

## Overview

This API provides endpoints for managing student and course associations within the application, leveraging Flask for the backend and SQLAlchemy for ORM with SQLite as the database.

## Endpoints

### Associate Student with Course

- **Endpoint**: `/api/v1/students/<int:student_id>/courses/<int:course_id>`
- **Method**: POST
- **Description**: Associates a student with a specific course.
- **Request Parameters**:
  - `student_id` (int): The ID of the student.
  - `course_id` (int): The ID of the course.
- **Request Body**: None
- **Response**:
  - **201 Created**: Successfully associated student with the course.
    ```json
    {
      "message": "Student successfully associated with the course."
    }
    ```
  - **400 Bad Request**: If the provided IDs are invalid.
    ```json
    {
      "error": {
        "code": "E001",
        "message": "Invalid student ID or course ID."
      }
    }
    ```
  - **404 Not Found**: If the student or course cannot be found.
    ```json
    {
      "error": {
        "code": "E002",
        "message": "Student or course not found."
      }
    }
    ```

### Retrieve Student's Courses

- **Endpoint**: `/api/v1/students/<int:student_id>/courses`
- **Method**: GET
- **Description**: Retrieves a list of courses associated with a specific student.
- **Request Parameters**:
  - `student_id` (int): The ID of the student whose courses are being requested.
- **Response**:
  - **200 OK**: A list of courses associated with the student.
    ```json
    {
      "student_id": 1,
      "courses": [
        {
          "course_id": 101,
          "course_name": "Mathematics"
        },
        {
          "course_id": 102,
          "course_name": "Science"
        }
      ]
    }
    ```
  - **404 Not Found**: If the student cannot be found.
    ```json
    {
      "error": {
        "code": "E002",
        "message": "Student not found."
      }
    }
    ```

## Assumptions

- Users will provide valid inputs for student ID and course IDs when making associations.
- The application will run in an environment with access to the current database holding student and course data.
- Users have a basic understanding of web applications and APIs.

## Error Handling

The API follows a strict error handling policy where all error messages are returned in a standardized format, including error codes to facilitate debugging.

---

This documentation serves as a overview of the new capabilities regarding student-course associations and how they can be utilized through the provided API endpoints.