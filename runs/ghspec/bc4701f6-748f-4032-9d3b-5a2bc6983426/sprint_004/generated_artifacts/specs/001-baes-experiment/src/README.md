# Updated README.md

# Project Title

## Overview & Purpose
The purpose of this feature is to establish a relationship between the Student and Course entities within the existing application. This enhancement will allow each Student to enroll in multiple Courses, thereby enriching the data model and improving educational management capabilities. Enabling this relationship aligns with the application's goals of providing comprehensive educational resources and facilitating better academic tracking for users.

## New API Endpoints

### 1. Enrolling a Student in a Course
- **Method**: POST
- **URL**: `/enrollments`
- **Request Body**:
    ```json
    {
        "student_id": <integer>,  // required
        "course_id": <integer>     // required
    }
    ```
- **Response**:
    - **201 Created** on success with the updated student’s details, including their courses:
    ```json
    {
        "student_id": <integer>,
        "courses": [
            {
                "course_id": <integer>,
                "course_name": "<string>",
                "level": "<string>"
            },
            ...
        ]
    }
    ```

### 2. Retrieving a Student's Courses
- **Method**: GET
- **URL**: `/students/{student_id}/courses`
- **Response**:
    - Returns a list of courses associated with the student in JSON format:
    ```json
    {
        "student_id": <integer>,
        "courses": [
            {
                "course_id": <integer>,
                "course_name": "<string>",
                "level": "<string>"
            },
            ...
        ]
    }
    ```

### Error Handling
- **Non-existent Course or Student**:
    - A user sends a POST request with a student ID or course ID that does not exist.
    - The application responds with an appropriate error message:
    ```json
    {
        "error": {
            "code": "E001",
            "message": "Course or student not found."
        }
    }
    ```

## Database Schema Update
Upon application startup, the database schema will be updated to include a join or mapping table that preserves existing Student and Course data while establishing their relationship.

## User Scenarios & Testing
1. **Enrolling a Student in a Course**: Users can send a POST request to enroll a student in a course, expecting a success message with updated student details.
2. **Retrieving a Student's Courses**: Users can retrieve all courses a student is enrolled in by their unique student ID through a GET request.
3. **Error Handling - Non-existent Course or Student**: Users are informed with clear error messages when invalid IDs are supplied.

## Functional Requirements
- Detailed endpoints for enrolling students in courses and retrieving their courses are documented above, with HTTP methods and required request/response formats outlined.

[Rest of the README contents would remain unchanged]