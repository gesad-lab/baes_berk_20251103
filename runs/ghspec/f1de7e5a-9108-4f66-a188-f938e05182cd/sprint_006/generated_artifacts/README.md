# README.md

# Project Title

This project is an educational management application that allows for the management of students, courses, and teachers.

## API Documentation

### Assign Teacher to Course

- **Endpoint**: `/courses/{courseId}/assign-teacher`
- **Method**: `POST`
- **Request Body**:
    ```json
    {
        "teacherId": "<integer>"
    }
    ```
- **Response**:
    - **Status Code**: 200 (OK)
        - Confirmation message indicating the teacher has been successfully assigned to the course.
    - **Error Handling**:
        - If the `teacherId` does not exist, a **404 Not Found** status will be returned with an error message: `{"error": {"code": "E001", "message": "Teacher not found"}}`.

### Get Course Details

- **Endpoint**: `/courses/{courseId}`
- **Method**: `GET`
- **Response**:
    - **Status Code**: 200 (OK)
        - JSON object containing course details, including:
        ```json
        {
            "id": "<integer>",
            "name": "<string>",
            "level": "<string>",
            "teacher": {
                "id": "<integer>",
                "name": "<string>"
            }
        }
        ```

## Database Schema Update

The SQLite database schema has been updated to include a foreign key relationship in the `courses` table referencing the `teachers` table.

- **Table Name**: `courses`
- **Updated Fields**:
    - `teacher_id`: Integer (Foreign Key referencing `teachers.id`, nullable)

## Database Migration

A migration has been created to add the `teacher_id` column to the `courses` table while preserving existing data for `Students`, `Courses`, and `Teachers`.

## Testing

### Running Tests

To run unit and integration tests, ensure you have the necessary test framework (e.g., pytest) installed, and then execute the following command:
```bash
pytest
```
This will execute all tests located in the `tests` directory.

### Test Cases

In the `tests/test_api.py`, new test cases will be added for the teacher assignment functionality. Ensure to verify that the tests cover both success and failure scenarios.

In the `tests/test_integration.py`, integration tests will confirm that the new endpoints work as expected and that the database layer functions correctly with the new schema changes. 

### Note

Make sure your local environment is set up according to the configuration in `.env.example` file, ensuring database connectivity and any required environment variables are correctly configured before running the application or the tests.