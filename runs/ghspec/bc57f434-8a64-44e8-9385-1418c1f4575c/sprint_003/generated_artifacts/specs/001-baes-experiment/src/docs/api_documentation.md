# File: docs/api_documentation.md

# API Documentation

## Overview
This document outlines the API endpoints available for managing courses in the application. The newly implemented endpoints allow users to create and retrieve course details.

## API Endpoints

### 1. Create Course
- **Endpoint**: `POST /courses`
- **Description**: Creates a new course with the specified name and level.
- **Request Body**:
    ```json
    {
        "name": "Introduction to Programming",
        "level": "Beginner"
    }
    ```
- **Response**:
    - **Status Code**: `201 Created`
    - **Body**:
    ```json
    {
        "id": 1,
        "name": "Introduction to Programming",
        "level": "Beginner"
    }
    ```

- **Error Responses**:
  - **Status Code**: `400 Bad Request`
    - **Body**:
    ```json
    {
        "error": {
            "code": "E001",
            "message": "Name and level are required fields."
        }
    }
    ```

### 2. Retrieve Course Details
- **Endpoint**: `GET /courses/{id}`
- **Description**: Retrieves the details of a specific course by its ID.
- **Path Parameters**:
    - `id` (integer): The ID of the course to retrieve.

- **Response**:
    - **Status Code**: `200 OK`
    - **Body**:
    ```json
    {
        "id": 1,
        "name": "Introduction to Programming",
        "level": "Beginner"
    }
    ```

- **Error Responses**:
  - **Status Code**: `404 Not Found`
    - **Body**:
    ```json
    {
        "error": {
            "code": "E002",
            "message": "Course not found."
        }
    }
    ```

## Database Changes
A new table, `Course`, has been created in the database schema with the following fields:
- `id`: Integer (Primary Key, Auto-increment)
- `name`: String (Required)
- `level`: String (Required)

## Validation
The following validations are applied to the request for creating a course:
- `name`: Must be a non-empty string.
- `level`: Must be a non-empty string.

## Conclusion
This API now provides the ability to manage course entities seamlessly, enhancing the application's functionality to handle educational course data. Ensure proper error handling and validations are in place as outlined.