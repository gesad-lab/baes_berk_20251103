# README.md

# Project Title

## Overview

This project is designed to manage courses and their assignments to teachers using FastAPI, SQLAlchemy, and Alembic for database migrations. Below is a concise guide to set up the environment, implement necessary functionality, and understand the API endpoints available.

## Setup Project Environment

1. **Initialize the Repository**:
   - Clone this repository or create a new branch if necessary.

2. **Use Poetry for Dependency Management**:
   - Install Poetry if not already installed:
     ```
     pip install poetry
     ```
   - Install project dependencies:
     ```
     poetry install
     ```

## Database Model Updates

- The `Course` model has been updated to include a `teacher_id` field, establishing a relationship with the `Teacher` model. This enables tracking which teacher is assigned to which course.

## API Layer

### Endpoints

1. **Assign Teacher to Course** (PATCH `/courses/{courseId}/assign`)
   - Description: Assigns a teacher to a specified course.
   - Request Body:
     ```json
     {
       "teacherId": "string" // The ID of the teacher to assign
     }
     ```
   - Response:
     - 200 OK: If the assignment is successful.
     - 400 Bad Request: If the provided IDs are invalid.

2. **Retrieve Course Details** (GET `/courses/{courseId}`)
   - Description: Retrieves details of a specified course, including the assigned teacher.
   - Response:
     ```json
     {
       "courseId": "string",
       "courseName": "string",
       "teacher": {
         "teacherId": "string",
         "teacherName": "string"
       }
     }
     ```
   - Status Codes:
     - 200 OK: If the course is found.
     - 404 Not Found: If the course does not exist.

## Service Layer Development

- Implemented service methods for assigning teachers to courses and retrieving course details.
- Error handling is robust, ensuring that invalid inputs are managed gracefully.

## Database Migration

- Alembic is used to manage database migrations. The migration scripts will add the `teacher_id` to the existing `courses` table without data loss, ensuring foreign key constraints are properly enforced.

## Testing

- Unit and integration tests have been created using Pytest to validate the functionality for assigning teachers and retrieving courses. 
- Aim for a minimum of 70% coverage for business logic.

## Conclusion

This README serves as a comprehensive guide to using the project, from initial setup to understanding the available API endpoints and expected behaviors. For further assistance, refer to the documentation or raise an issue in the repository.