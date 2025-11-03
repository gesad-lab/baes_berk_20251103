# README.md

## API Documentation

### Teachers API

#### Create a Teacher

- **Endpoint**: `/teachers` (POST)
- **Request Body**:
    ```json
    {
        "name": "<string>",
        "email": "<string>"
    }
    ```
- **Response**:
    - **Status Code**: `201 Created`
    - **Response Body**: Confirmation message that the teacher has been successfully created.

#### Retrieve All Teachers

- **Endpoint**: `/teachers` (GET)
- **Response**:
    - **Status Code**: `200 OK`
    - **Response Body**: An array of teacher objects, where each object contains:
        - `name`: The name of the teacher.
        - `email`: The email of the teacher.

### Teacher Model Specification

The `Teacher` model includes the following attributes:
- `id`: Integer (Primary Key, Auto-increment)
- `name`: String (required)
- `email`: String (required, unique)

### Input Validation

- Both `name` and `email` fields must be provided when creating a teacher.
- The application will return a status code `400 Bad Request` if either field is missing, along with a detailed error message indicating what went wrong.

### Database Schema

The application has been updated to include a new `teachers` table with the following schema:
- **Table Name**: `teachers`
- **Fields**:
  - `id`: Integer (Primary Key, Auto-increment)
  - `name`: String (required)
  - `email`: String (required, unique)

### Migrations

A database migration script has been created to add the `teachers` table while preserving existing `Student` and `Course` data.

### Testing Guidelines

- Ensure that unit tests and integration tests are updated to cover the new API functionalities for teachers.
- Use the testing framework set up in the previous sprints to execute the tests.

### Running Tests

To run tests, execute the following command in the terminal:
```bash
pytest tests/
```

### Deployment Notes

- Ensure that the FastAPI application is set up to include the new teacher-related endpoints.
- Run the database migration script to reflect the schema changes after updating the application.

## Out of Scope

- UI changes necessary for administrators to manage teachers (creating, updating, or viewing) are not included in this feature.
- Functionality for handling teacher assignments to courses or students is not covered in this iteration.
- Notifications or alerts related to teacher creation or status updates are not included in the current scope.