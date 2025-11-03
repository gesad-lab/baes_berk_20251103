# Updated README.md

# Project Title

## Overview

This project is designed to manage students and courses using a FastAPI-based backend. The application provides endpoints to manage the many-to-many relationship between students and courses.

## API Endpoints

### Associate a Course to a Student

- **POST /students/{student_id}/courses**
  - **Description**: Associate a course to a student using their IDs.
  - **Request Body**: JSON object with the following structure:
    ```json
    {
      "course_id": "string"  // The ID of the course to associate
    }
    ```
  - **Responses**:
    - **201 Created**: Course associated successfully.
    - **400 Bad Request**: Invalid input, such as student or course not found, or the course is already associated.

### Retrieve All Courses for a Student

- **GET /students/{student_id}/courses**
  - **Description**: Retrieve all courses associated with a specific student.
  - **Responses**:
    - **200 OK**: Returns a JSON array of courses associated with the student.
    - **404 Not Found**: Student not found.

### Remove a Course Association from a Student

- **DELETE /students/{student_id}/courses/{course_id}**
  - **Description**: Remove a specific course association from a student.
  - **Responses**:
    - **204 No Content**: Course successfully removed.
    - **404 Not Found**: Student or course not found, or the course is not associated with the student.

## Error Handling

The application provides clear error messages for invalid associations:
- **E001**: Student not found.
- **E002**: Course not found.
- **E003**: Attempt to associate a course that is already linked to the student.

All error responses are returned in a consistent JSON format:
```json
{
  "error": {
    "code": "E001",
    "message": "Student not found.",
    "details": {}  // Additional error details if needed
  }
}
```

## Database Management

The database schema includes a many-to-many relationship between Students and Courses. An intermediary table named `student_courses` has been created with the following structure:

- **student_id**: Foreign key reference to the Student entity.
- **course_id**: Foreign key reference to the Course entity.

## Setup Instructions

1. Clone the repository.
2. Install dependencies using:
   ```
   pip install -r requirements.txt
   ```
3. Set up the database:
   - Configure your database connection in the `.env` file.
   - Run migrations using Alembic:
     ```
     alembic upgrade head
     ```
4. Start the development server:
   ```
   uvicorn main:app --reload
   ```

## Project Structure

- `src/`: Application source code  
  - `main.py`: Entry point of the FastAPI application  
  - `models/`: Database models (including Student and Course models)  
  - `schemas/`: Pydantic models for request/response validation  
  - `routes/`: API endpoints for handling HTTP requests  
  - `database/`: Database connection and setup
- `tests/`: Test files for the application  
- `README.md`: This documentation file  

## Usage Instructions

Refer to the API endpoints section for details on how to use the API. Each endpoint is designed to follow RESTful principles and returns JSON-formatted responses.

For auto-generated API documentation, navigate to `/docs` after starting the FastAPI server.