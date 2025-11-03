# README.md

# Project Title

A brief description of your project and its purpose.

## Development Phases

### 1. Setup Project Environment
- Initialize a new Git repository and branch.
- Use Poetry for dependencies, including specific packages for FastAPI, SQLAlchemy, Alembic, and testing tools.

### 2. Implement Database Updates
- Create the `StudentCourses` model with the required fields.
- Define relationships between the models (`Student` and `Course`).

### 3. Modify API Layer
- Define new POST and GET endpoints in the FastAPI application for enrolling students and retrieving courses respectively.
- Ensure proper validation for request bodies and parameters.

### 4. Service Layer Development
- Implement service methods for enrolling students and retrieving courses from the `StudentCourses` intermediary table.
- Ensure thorough error handling for invalid cases.

### 5. Database Migration
- Utilize Alembic to generate a migration file that creates the `student_courses` table.
- Confirm that migrations do not interfere with existing data.

### 6. Testing
- Use Pytest to develop unit and integration tests to ensure functionality for the new enrollment and course retrieval features.
- Aim for a minimum of 70% coverage on business logic touching on enrollments and relationships.

### 7. Documentation
- Update `README.md` to reflect new API endpoints, request/response formats, and usage instructions.
- Ensure all code is adequately documented with comments and docstrings.

## API Endpoints

### Enroll Student in Course
- **Endpoint**: `/api/v1/enroll`
- **Method**: POST
- **Request Body**:
    ```json
    {
        "student_id": "string",
        "course_id": "string"
    }
    ```
- **Response**:
    - **200 OK**: Successful enrollment
    - **400 Bad Request**: Invalid data or parameters

### Retrieve Courses for a Student
- **Endpoint**: `/api/v1/courses`
- **Method**: GET
- **Query Parameters**:
    - `student_id` (required): The ID of the student for whom courses are being retrieved.
- **Response**:
    - **200 OK**: Returns a list of courses the student is enrolled in.
    - **404 Not Found**: Student not found.

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```
2. Install dependencies using Poetry:
   ```bash
   poetry install
   ```

## Usage

To run the FastAPI application:
```bash
poetry run uvicorn your_app:app --reload
```

## Tests

To run tests using Pytest:
```bash
poetry run pytest
```

Ensure that you have set up your database properly and that the migrations are applied before running tests.

--- 

This README now reflects the recent updates to the API endpoints and provides a clear structure for setup, usage, and testing, in line with the development phases outlined in the project specifications.