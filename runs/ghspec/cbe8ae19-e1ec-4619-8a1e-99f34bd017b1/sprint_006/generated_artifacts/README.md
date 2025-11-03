# README.md

# Project Name

## Introduction
This project is focused on managing courses and teachers, allowing users to assign teachers to courses and retrieve detailed information regarding courses along with their assigned teachers.

## API Endpoints

### Assign Teacher to Course
- **Endpoint**: `POST /api/courses/{course_id}/assign_teacher`
- **Description**: Assign a teacher to an existing course.
- **Parameters**:
  - `course_id` (path parameter): The ID of the course.
  - Request Body:
    - `teacher_id` (integer): ID of the teacher to be assigned to the course.
- **Success Response**:
  - **Code**: 200 OK
  - **Content**: `{"message": "Teacher assigned successfully."}`
- **Error Responses**:
  - **Code**: 400 Bad Request
    - **Content**: `{"error": {"code": "E001", "message": "Invalid course ID."}}`
  - **Code**: 404 Not Found
    - **Content**: `{"error": {"code": "E002", "message": "Teacher not found."}}`

### Retrieve Course with Teacher Details
- **Endpoint**: `GET /api/courses/{course_id}`
- **Description**: Retrieve detailed information about a specific course, including the name of the assigned teacher.
- **Parameters**:
  - `course_id` (path parameter): The ID of the course.
- **Success Response**:
  - **Code**: 200 OK
  - **Content**: 
    ```json
    {
      "course_id": 1,
      "course_name": "Mathematics",
      "teacher": {
        "teacher_id": 2,
        "teacher_name": "John Doe"
      }
    }
    ```
- **Error Responses**:
  - **Code**: 404 Not Found
    - **Content**: `{"error": {"code": "E003", "message": "Course not found."}}`

## Database Schema Update
The existing Course table has been updated to include a new field:
- `teacher_id`: Integer (Foreign Key referencing the Teacher entity).

## Database Migration
A migration script has been created to add the `teacher_id` field to the existing Course table, ensuring that existing Course and Teacher data is preserved.

## Testing
Unit tests for course-teacher assignment and retrieval have been implemented, located in the `tests` directory. Ensure to run the tests to verify the functionality.

## Setup
1. Clone the repository.
2. Install the required dependencies with:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the database migration to update the schema.

## Usage
Refer to the API endpoints section to understand how to interact with the system effectively. Be sure to validate inputs when making requests to the API.