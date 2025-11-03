# File: docs/api_documentation.md

# API Documentation

## Overview
This document provides an overview of the API endpoints available for managing courses and their associated teachers in the application.

## Base URL
```
http://<your-server-domain>/api/v1
```

## Endpoints

### 1. Courses

#### 1.1 Get Course Details
- **Endpoint**: `/courses/{courseId}`
- **Method**: `GET`
- **Description**: Retrieves the details of a specific course, including its associated teacher if present.
- **Path Parameters**:
  - `courseId` (integer): The unique identifier for the course.
- **Responses**:
  - `200 OK`: Returns a JSON object with course details.
    ```json
    {
      "id": 1,
      "title": "Introduction to Programming",
      "description": "Learn the basics of programming.",
      "teacher": {
        "id": 1,
        "name": "John Doe"
      }
    }
    ```
  - `404 Not Found`: Course not found.

#### 1.2 Assign Teacher to Course
- **Endpoint**: `/courses/{courseId}/assign-teacher`
- **Method**: `PUT`
- **Description**: Assigns a teacher to a specific course.
- **Path Parameters**:
  - `courseId` (integer): The unique identifier for the course.
- **Request Body**:
  ```json
  {
    "teacher_id": 1
  }
  ```
- **Responses**:
  - `200 OK`: Successfully assigned the teacher.
  - `400 Bad Request`: Invalid teacher ID specified.
  - `404 Not Found`: Course or teacher not found.

## Error Responses
All error responses will follow the format:
```json
{
  "error": {
    "code": "E001",
    "message": "Detailed error message here",
    "details": {}
  }
}
```

## Conclusion
This documentation will be updated as new features and enhancements are added to the API. For any inquiries or issues, please contact the API support team.