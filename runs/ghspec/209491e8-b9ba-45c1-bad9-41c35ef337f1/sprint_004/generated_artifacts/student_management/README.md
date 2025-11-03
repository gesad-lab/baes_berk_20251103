# student_management/README.md

# Student Management API

## Overview

This API allows users to manage students and courses effectively. It includes functionalities for enrolling students in courses, retrieving course details, and setting up a many-to-many relationship between students and courses.

## API Endpoints

### 1. Enroll a Student in a Course

- **Endpoint**: `POST /students/{student_id}/courses`
- **Description**: Enroll a student in a course.
- **Request Body**:
    ```json
    {
        "course_id": "string"
    }
    ```
- **Path Parameters**:
    - `student_id` (string): The ID of the student to enroll.
- **Response**:
    - **Success (201 Created)**:
        ```json
        {
            "message": "Successfully enrolled in the course."
        }
        ```
    - **Error (400 Bad Request)**:
        ```json
        {
            "error": {
                "code": "E001",
                "message": "Invalid course ID."
            }
        }
        ```
    - **Error (404 Not Found)**:
        ```json
        {
            "error": {
                "code": "E002",
                "message": "Student not found."
            }
        }
        ```

### 2. Retrieve Courses for a Student

- **Endpoint**: `GET /students/{student_id}/courses`
- **Description**: Retrieve a list of courses a student is enrolled in.
- **Path Parameters**:
    - `student_id` (string): The ID of the student whose courses are to be retrieved.
- **Response**:
    - **Success (200 OK)**:
        ```json
        [
            {
                "course_id": "string",
                "course_name": "string"
            }
        ]
        ```
    - **Error (404 Not Found)**:
        ```json
        {
            "error": {
                "code": "E002",
                "message": "Student not found."
            }
        }
        ```

## Database Schema

- A many-to-many relationship is established between the `Student` and `Course` entities through the `student_courses` join table.
- The schema is designed to retain all existing data in both the `Student` and `Course` tables while supporting concurrent requests and maintaining data integrity.

## Testing

Make sure to validate the functionality of the new endpoints by performing API tests to ensure they support the enrollment process accurately and return appropriate error messages for invalid requests.