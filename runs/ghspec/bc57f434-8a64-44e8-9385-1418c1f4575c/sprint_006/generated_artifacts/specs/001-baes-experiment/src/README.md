# README.md

# Project Title

## Overview

This project provides a RESTful API for managing courses and teachers using FastAPI and SQLite. 

## Database Changes

The following modification has been made to the database schema:

- **Course Table Update**: 
  - Added a new optional foreign key field `teacher_id` to the `Course` table.
  - `teacher_id` references the `id` field of the `Teacher` table.

**Migration**: A migration script has been executed to ensure that this new field has been added while preserving existing data in the `Student`, `Course`, and `Teacher` tables.

## API Endpoints

The following endpoints have been introduced for managing courses and their associations with teachers:

### Update Course

- **PUT /courses/{id}**
  
  Updates an existing course to include an optional `teacher_id`.

  **Request Body**:
  ```json
  {
    "teacher_id": 1
  }
  ```

  **Response**:
  - **200 OK**: Successfully updated course.
  - **400 Bad Request**: When an invalid teacher ID is provided.
  - Error response example:
    ```json
    {
      "error": {
        "code": "E001",
        "message": "Invalid teacher ID provided.",
        "details": {}
      }
    }
    ```

### Get Course

- **GET /courses/{id}**
  
  Retrieves the details of a course, including the associated teacher's information.

  **Response**:
  - **200 OK**: Successfully retrieved course details along with teacher information.
  - **404 Not Found**: If the course does not exist.
  
  Example response for successful retrieval:
  ```json
  {
    "id": 1,
    "name": "Introduction to Programming",
    "teacher": {
      "id": 1,
      "name": "John Doe",
      "email": "john.doe@example.com"
    }
  }
  ```

## Success Criteria

1. Courses can be updated to include a teacher without disrupting existing data or relationships.
2. Retrieved course details will accurately reflect the associated teacher’s information.
3. The migration will be executed without data integrity issues.
4. Appropriate error messages will be returned for invalid teacher assignments.
5. All API responses will adhere to the specified JSON format.
6. API responses are expected to meet performance standards, responding within acceptable time limits (e.g., under 200ms).

## Assumptions

- The application is configured to support the new relationship without impacting performance.
- Administrators have the necessary permissions to modify course data.
- Validation of teacher IDs will ensure they exist before any updates or assignments.

## Testing

Ensure to run the following tests to validate the new functionality:

- `tests/test_api_courses.py`: Test for API endpoint functionality related to courses.
- `tests/test_integration_courses.py`: Integration tests for course and teacher entity interactions.