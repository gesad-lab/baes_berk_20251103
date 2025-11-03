# README.md

# Student Registration API

## Overview

This project is an API for managing student registrations and course assignments. It utilizes Flask for handling API requests and SQLAlchemy for database operations.

## API Endpoints

### Students

#### Create a Student
- **Endpoint**: `POST /students`
- **Description**: Creates a new student in the database.
- **Request Body**:
  ```json
  {
    "name": "string",         // Name of the student
    "email": "string"        // Email address of the student
  }
  ```
- **Response**:
  - **201 Created**: Returns the created student object.
  - **400 Bad Request**: If the input data is invalid.

#### Retrieve a Student
- **Endpoint**: `GET /students/<student_id>`
- **Description**: Retrieves information about a specific student by their ID.
- **Response**:
  - **200 OK**: Returns the student object.
  - **404 Not Found**: If the student does not exist.

### Courses

#### Create a Course
- **Endpoint**: `POST /courses`
- **Description**: Creates a new course in the database.
- **Request Body**:
  ```json
  {
    "title": "string",       // Title of the course
    "description": "string"  // Description of the course
  }
  ```
- **Response**:
  - **201 Created**: Returns the created course object.
  - **400 Bad Request**: If the input data is invalid.

#### Retrieve a Course
- **Endpoint**: `GET /courses/<course_id>`
- **Description**: Retrieves information about a specific course by its ID.
- **Response**:
  - **200 OK**: Returns the course object.
  - **404 Not Found**: If the course does not exist.

## Running Migrations

Before running the application, ensure that the database is initialized with the latest schema. You can run the migration script as follows:

1. Ensure you have the necessary database configuration set in your environment.
2. Execute the migration script with the following command:
   ```bash
   flask db upgrade
   ```

## Configuration

- Ensure the following environment variables are set for the application to run correctly:
  - `DATABASE_URL`: The URL of your database.
  - `SECRET_KEY`: A secret key for session management.

## Conclusion

This API serves as a foundation for managing student registrations and courses. You can extend its functionality further as needed by adding more endpoints and features.