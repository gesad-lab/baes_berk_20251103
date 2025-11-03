# README.md

# API Documentation

## Overview
This document provides details about the API endpoints available for managing the Teacher-Course relationship within the application.

## API Endpoints

### 1. Assign Teacher to Course

- **Endpoint**: `POST /api/v1/courses/{course_id}/assign_teacher`
- **Description**: Assign a teacher to a specified course.
- **Request Body**:
  ```json
  {
      "teacher_id": "string"  // The ID of the teacher to be assigned
  }
  ```
- **Response**:
  - **Success (200 OK)**:
    ```json
    {
        "message": "Teacher assigned successfully",
        "course_id": "string",
        "teacher_id": "string"
    }
    ```
  - **Error (400 Bad Request)**:
    ```json
    {
        "error": {
            "code": "E001",
            "message": "Invalid course or teacher ID"
        }
    }
    ```

### 2. Retrieve Course Details

- **Endpoint**: `GET /api/v1/courses/{course_id}`
- **Description**: Retrieve details of a specific course including the assigned teacher.
- **Response**:
  - **Success (200 OK)**:
    ```json
    {
        "course_id": "string",
        "course_name": "string",
        "teacher": {
            "teacher_id": "string",
            "teacher_name": "string"
        }
    }
    ```
  - **Error (404 Not Found)**:
    ```json
    {
        "error": {
            "code": "E002",
            "message": "Course not found"
        }
    }
    ```

### Notes
- All endpoints are versioned and follow RESTful principles.
- Error responses will include a code for easier debugging.

## Modules

- **Routing Module**: Responsible for handling incoming HTTP requests and mapping endpoints for Course-Teacher relationship.
- **Controller Module**: Contains functions that process requests to assign/update a Teacher to a Course and retrieve Course details.
- **Model Module**: Defines the `Course` model with a relationship to `Teacher`, and interacts with the database.
- **Validation Module**: Contains logic for validating Teacher assignment requests.

## Usage
To use the API, ensure your application is running and use an API client (like Postman or cURL) to send requests to the defined endpoints.

Make sure to replace `{course_id}` with the actual ID of the course you want to manage.