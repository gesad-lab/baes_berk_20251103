# README.md

# Project Title

## Overview
This project is a RESTful API for managing students using FastAPI and SQLite. The application allows for the creation, retrieval, and validation of student information including their name and email.

## Functional Requirements

1. **Create Student**:
   - **Endpoint**: `POST /students`
   - **Request Body**: 
     ```json
     {
       "name": "string",  // required
       "email": "string"  // required
     }
     ```
   - **Response**: 
     ```json
     {
       "id": "integer",
       "name": "string",
       "email": "string"
     }
     ```

2. **Retrieve Student**:
   - **Endpoint**: `GET /students/{id}`
   - **Response**: 
     ```json
     {
       "id": "integer",
       "name": "string",
       "email": "string"
     }
     ```
   - **Error Response for non-existing ID**:
     ```json
     {
       "error": {
         "code": "E404",
         "message": "Student not found."
       }
     }
     ```

3. **Validation**:
   - The `email` field is required and must be a valid string format.
   - Returns a 400 Bad Request status with a clear message if the validation for the email fails.
   - Duplicate email addresses are not allowed and will trigger validation errors.

4. **Database Initialization**:
   - The existing Students table schema has been updated to include the email field as follows:
     - `email`: string (not null)

5. **Database Migration**:
   - A database migration strategy has been implemented to add the email field while preserving existing student data.

## Success Criteria
- The application must allow creating a student with both a name and email, returning the student's ID, name, and email successfully.
- The application must allow retrieving a student's information by ID, returning the correct information including email.
- The application must return appropriate error messages for missing or invalid input for both the name and email fields.
- The database schema must be updated to include the email field without data loss or corruption of existing student records.

## Assumptions
- Users of the application have the necessary permissions to create and view students’ names and emails.
- The collected email addresses will be sufficiently validated to ensure correctness.

## Technical Stack
- **Programming Language**: Python 3.11+
- **Framework**: FastAPI (for building the RESTful API)
- **Database**: SQLite (for local data storage)
- **ORM**: SQLAlchemy (for database interactions)
- **Testing**: Pytest (for tests)
- **Environment Management**: Poetry (for dependency management)

## Running the Application

1. Install dependencies:
   ```bash
   poetry install
   ```

2. Run the application:
   ```bash
   uvicorn main:app --reload
   ```

3. Access the API documentation at `http://127.0.0.1:8000/docs`.

## Contributing
Contributions to the project are welcomed. Please open an issue or submit a pull request for review.