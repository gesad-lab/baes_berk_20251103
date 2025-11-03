# File: docs/api_specification.md

# API Documentation

## Overview
This document provides specifications for the API endpoints of the application, built using Python and Flask. It outlines the endpoints available for managing teachers and courses, including information regarding request and response formats, as well as any associated error codes.

## Endpoints

### Teacher Endpoints

#### POST /teachers
- **Description**: Creates a new Teacher record.
- **Request Body**:
    - `name` (string): The name of the teacher.
    - `email` (string): The email address of the teacher.
- **Responses**:
    - `201 Created`: Returns a confirmation message upon successful creation.
    - `400 Bad Request`: Returns descriptive error messages for validation failures.

### Course Endpoints

#### POST /courses
- **Description**: Creates a new Course record associated with a Teacher.
- **Request Body**:
    - `title` (string): The title of the course.
    - `description` (string): A brief description of the course.
    - `teacher_id` (integer): A reference to the Teacher's ID for course ownership.
- **Responses**:
    - `201 Created`: Returns a confirmation message upon successful creation of the course.
    - `400 Bad Request`: Returns error messages if the `teacher_id` is missing or does not correspond to an existing Teacher.

#### GET /courses/{id}
- **Description**: Retrieves details of a specific Course by its ID.
- **Path Parameters**:
    - `id` (integer): The ID of the course to retrieve.
- **Responses**:
    - `200 OK`: Returns course details along with associated Teacher information when found.
    - `404 Not Found`: Returns an error message if the course with the specified ID does not exist.

## Error Codes
- **E001**: Invalid teacher_id format.
- **E002**: Teacher_id does not exist in the teacher records.
- **E003**: Missing required fields in the request body.

## Additional Notes
- Ensure that the application’s database migration scripts are applied to update the existing schema to support course management.
- Implement automated tests for the new Course endpoints to ensure functionality and error validation.

## Version
- This documentation reflects the API specification as of version 1.0.0.