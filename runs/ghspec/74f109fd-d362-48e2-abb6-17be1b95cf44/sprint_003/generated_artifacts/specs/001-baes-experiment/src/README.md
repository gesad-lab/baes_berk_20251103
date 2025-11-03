# README.md

## Overview & Purpose
The purpose of this feature is to introduce a new Course entity into the educational management system. This entity will enable users to manage courses effectively, supporting better tracking of educational offerings. The new Course entity will include a name and a level, which are essential for categorizing courses and understanding their complexity. This feature aligns with our goal to enhance the educational experience by providing structured data about available courses.

## API Endpoints for Course Management

### 1. Create Course
- **Endpoint**: `POST /api/v1/courses`
- **Description**: Users must be able to submit a POST request to create a new Course with both `name` and `level`.
- **Request Body**:
  ```json
  {
      "name": "Course Name",
      "level": "Course Level"
  }
  ```
- **Response**:
  - **Success (201 Created)**:
    ```json
    {
        "id": 1,
        "name": "Course Name",
        "level": "Course Level"
    }
    ```
  - **Error (400 Bad Request)**: If fields are missing or invalid.
    ```json
    {
        "error": {
            "code": "E001",
            "message": "Both name and level are required."
        }
    }
    ```

### 2. Retrieve Course by ID
- **Endpoint**: `GET /api/v1/courses/{id}`
- **Description**: Users must be able to submit a GET request to retrieve a course by its ID.
- **Response**:
  - **Success (200 OK)**:
    ```json
    {
        "id": 1,
        "name": "Course Name",
        "level": "Course Level"
    }
    ```
  - **Error (404 Not Found)**: If the course does not exist.
    ```json
    {
        "error": {
            "code": "E002",
            "message": "Course not found."
        }
    }
    ```

## Database Schema Update
- A new Course table will be created with the following fields:
  - **`name`** (string, required)
  - **`level`** (string, required)

The database migration process must ensure that existing Student data is preserved and unaffected by this change.

## JSON Responses
All API responses must be in JSON format, including both success responses and error messages.

---

This README update reflects the new structure and functionalities of the API, providing users with the necessary information to utilize the enhanced educational management system effectively.