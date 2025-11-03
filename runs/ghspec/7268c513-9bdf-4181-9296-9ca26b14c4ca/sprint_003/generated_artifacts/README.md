# README.md

# Project Documentation

## API Endpoints

### Create Course
- **Endpoint**: `POST /courses`
- **Description**: Creates a new course with the specified name and level.
- **Request Body**: 
    ```json
    {
        "name": "string",
        "level": "string"
    }
    ```
    - `name` (string, required): The name of the course.
    - `level` (string, required): The difficulty level of the course.
- **Response**:
    - **201 Created**: Returns the details of the created course.
    - **400 Bad Request**: Returned if the `name` or `level` is missing, with the following error structure:
    ```json
    {
        "error": {
            "code": "E001",
            "message": "Name is required."
        }
    }
    ```

### Get All Courses
- **Endpoint**: `GET /courses`
- **Description**: Retrieves a list of all courses in the system.
- **Response**:
    - **200 OK**: Returns a JSON array of course records, with each record containing:
    ```json
    {
        "name": "string",
        "level": "string"
    }
    ```

## Error Handling
- Any request to the above endpoints with missing required fields will return a structured error message in JSON format, indicating the specific issue encountered.

## Database Migration
- The application includes a migration step to create a new `courses` table, which will have columns for `name` and `level`, while ensuring that existing data within the `students` table is preserved. 

## Setup Instructions
- Follow the setup instructions in the repository to configure and migrate your database before using the above endpoints.