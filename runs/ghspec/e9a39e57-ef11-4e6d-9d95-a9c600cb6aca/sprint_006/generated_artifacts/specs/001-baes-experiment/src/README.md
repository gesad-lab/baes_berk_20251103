# README.md

# Project Title

## Overview

This is the API documentation for the project. It covers the available endpoints, their request and response formats, and additional details relevant to using the API.

## API Endpoints

### 1. Assign Teacher to Course

- **Endpoint**: `POST /courses/{course_id}/assign_teacher`
- **Description**: This endpoint assigns a teacher to a specific course.

#### Request Format

- **Method**: `POST`
- **Content-Type**: `application/json`

**Example Request Body**:
```json
{
  "teacher_id": 1
}
```

#### Response Format

- **Success Response**:
  - **Status**: 200 OK
  - **Body**:
    ```json
    {
      "message": "Teacher assigned successfully.",
      "course": {
        "id": 1,
        "name": "Math 101",
        "level": "Beginner",
        "teacher_id": 1,
        "teacher": {
          "name": "John Doe",
          "email": "john.doe@example.com"
        }
      }
    }
    ```

- **Error Response**:
  - **Status**: 400 Bad Request
  - **Body**:
    ```json
    {
      "error": {
        "code": "E002",
        "message": "Invalid teacher assignment."
      }
    }
    ```

### 2. Retrieve Course Information

- **Endpoint**: `GET /courses/{course_id}`
- **Description**: This endpoint retrieves detailed information about a specific course, including associated teacher details.

#### Request Format

- **Method**: `GET`
- **Content-Type**: `application/json`

**Example Request**:
```http
GET /courses/1 HTTP/1.1
Host: example.com
Content-Type: application/json
```

#### Response Format

- **Success Response**:
  - **Status**: 200 OK
  - **Body**:
    ```json
    {
      "id": 1,
      "name": "Math 101",
      "level": "Beginner",
      "teacher_id": 1,
      "teacher": {
        "name": "John Doe",
        "email": "john.doe@example.com"
      }
    }
    ```

- **Error Response**:
  - **Status**: 404 Not Found
  - **Body**:
    ```json
    {
      "error": {
        "code": "E001",
        "message": "Course not found"
      }
    }
    ```

## Database Migration

- The database schema has been updated to include `teacher_id` in the `Course` table, establishing a foreign key reference to the `Teacher` entity. 

## Conclusion

This documentation provides an overview of the new endpoints for assigning teachers to courses and retrieving course information. Follow the formats outlined for requests and responses to effectively interact with the API.