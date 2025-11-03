# Content of docs/api_reference.md

# API Reference Documentation

## Overview

This document serves as a reference for the API endpoints available in our application. Each endpoint is described with its method, URL, parameters, request body, and response format.

## Authentication

All API endpoints require authentication. Make sure to include a valid token in the `Authorization` header for each request.

## Endpoints

### 1. Student Enrollment

#### POST /api/v1/enrollments

Enroll a student in a course.

**Request Body:**
```json
{
  "student_id": "string",  // ID of the student to enroll
  "course_id": "string"    // ID of the course in which to enroll the student
}
```

**Response:**
- **201 Created**
  ```json
  {
    "message": "Enrollment successful",
    "enrollment_id": "string"  // ID of the newly created enrollment
  }
  ```
- **400 Bad Request**
  ```json
  {
    "error": {
      "code": "E001",
      "message": "Invalid student ID or course ID",
      "details": {}
    }
  }
  ```
- **401 Unauthorized**
  ```json
  {
    "error": {
      "code": "E002",
      "message": "Authentication failed. Please login."
    }
  }
  ```

### 2. List Courses

#### GET /api/v1/courses

Retrieve a list of available courses.

**Response:**
- **200 OK**
  ```json
  [
    {
      "id": "string",          // Unique identifier for the course
      "name": "string",        // Name of the course
      "level": "string"        // Course level (e.g., beginner, intermediate, advanced)
    }
  ]
  ```

### 3. Course Details

#### GET /api/v1/courses/{id}

Retrieve details of a specific course by ID.

**Parameters:**
- `id` (path): The unique identifier of the course.

**Response:**
- **200 OK**
  ```json
  {
    "id": "string",
    "name": "string",
    "level": "string",
    "description": "string"  // Description of the course
  }
  ```
- **404 Not Found**
  ```json
  {
    "error": {
      "code": "E003",
      "message": "Course not found"
    }
  }
  ```

## Conclusion

This API allows for managing student enrollments and querying course details. Ensure that you handle errors gracefully and provide meaningful feedback in your applications in response to API interactions.