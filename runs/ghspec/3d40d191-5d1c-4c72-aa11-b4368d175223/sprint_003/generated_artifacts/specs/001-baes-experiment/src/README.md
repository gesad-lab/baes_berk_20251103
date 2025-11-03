# README.md

# Project Title

## Overview

This project is a FastAPI-based application designed to manage educational entities, such as students and courses.

## API Documentation

### Students

- **Create Student**
  - **Endpoint**: `POST /students`
  - **Request Body**: JSON object containing "name" (string, required).
  - **Response**: Returns the created Student object with a success message and a 201 Created status.

### Courses

- **Create Course**
  - **Endpoint**: `POST /courses`
  - **Request Body**: JSON object containing:
    - `name`: string (required)
    - `level`: string (required)
  - **Response**: Returns the created Course object with a success message and a 201 Created status.
  
  - **Error Handling**:
    - If the request is made without a "name" or "level" field, it returns a 400 Bad Request status with an error message indicating the missing required field(s). The error message provides clear guidance on the correction needed.

- **Retrieve Courses**
  - **Endpoint**: `GET /courses`
  - **Response**: Returns an array of Course objects in JSON format with the following properties:
    - `id`: integer
    - `name`: string
    - `level`: string
  - **Response Status**: 200 OK

## Database Management

- The database schema has been updated to include a new Course table with the following fields:
  - `id`: integer (auto-generated primary key)
  - `name`: string (required)
  - `level`: string (required)
  
- A database migration has been created that adds the Course table without affecting the existing Student data.

## Success Criteria

- The API endpoint for creating Courses is functional and correctly handles requests that include both name and level.
- Error messages for requests missing either name or level fields are clear and informative.
- The API endpoint for retrieving all Courses is functional and returns the expected details.
- The database schema is updated seamlessly, allowing existing Student records to remain intact and functional.

## Out of Scope

- Additional fields or functionalities for the Course entity beyond name and level fields will not be included in this feature.
- User interface changes related to displaying Course information or managing Courses in any frontend components will not be part of this specification, focusing solely on backend API updates and database schema changes.

## Additional Notes

This README will be updated as more features are added to the application. Please refer to the appropriate documentation sections for the most current information regarding endpoints and operational details.