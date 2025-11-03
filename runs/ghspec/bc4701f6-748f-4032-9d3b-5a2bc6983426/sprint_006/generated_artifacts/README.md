# README.md

# Project Title

## Introduction
This is a brief description of the project and its purpose.

## API Endpoints

### Assign a Teacher to a Course
- **Method**: `PATCH`
- **URL**: `/courses/{course_id}`
- **Request Body**:
  ```json
  {
      "teacher_id": "string"
  }
  ```
- **Description**: This endpoint allows a user to assign a teacher to a specific course by providing the course ID and the teacher's unique ID in the request body.

- **Response**:
  - **Success (200 OK)**: The course record is updated successfully. The response will include the updated course details.
    ```json
    {
        "course_id": "string",
        "course_name": "string",
        "teacher": {
            "name": "string",
            "email": "string"
        }
    }
    ```
  - **Error (404 Not Found)**: If the teacher ID does not exist, a 404 error will be returned.
    ```json
    {
        "error": {
            "code": "E404",
            "message": "Teacher not found"
        }
    }
    ```

### Retrieve Course Details including Teacher Information
- **Method**: `GET`
- **URL**: `/courses/{course_id}`
- **Description**: This endpoint retrieves details of a specific course, including information about the assigned teacher if any.

- **Response**:
  - **Success (200 OK)**: Returns course details with teacher information if associated.
    ```json
    {
        "course_id": "string",
        "course_name": "string",
        "teacher": {
            "name": "string",
            "email": "string"
        }
    }
    ```
  - **Error (404 Not Found)**: If the course ID does not exist, a 404 error will be returned.
    ```json
    {
        "error": {
            "code": "E404",
            "message": "Course not found"
        }
    }
    ```

## Database Schema Changes
- The database schema has been updated to establish a foreign key relationship from the `courses` table to the `teachers` table. This allows for the association between courses and their assigned teachers while preserving existing data for Students and Courses.

## Error Handling
- The application identifies invalid requests or non-existent resources and responds with clear, actionable error messages formatted in JSON.

## Usage
Instructions for setting up and using the application.

## Conclusion
A summary of the project and any additional notes.