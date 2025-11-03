# docs/api_documentation.md

# API Documentation

## Version 1.0

This document serves as a guide for using the API endpoints related to courses.

---

## Endpoints

### 1. Create a Course
- **Route**: `POST /api/v1/courses`
- **Request Body**:
  ```json
  {
    "name": "Introduction to Programming",
    "level": "Beginner"
  }
  ```
- **Response**:
  - **201 Created**
  ```json
  {
    "id": 1,
    "name": "Introduction to Programming",
    "level": "Beginner"
  }
  ```
  - **400 Bad Request** for validation errors.
  ```json
  {
    "error": {
      "code": "E001",
      "message": "Name and level are required."
    }
  }
  ```

### 2. Retrieve a Course
- **Route**: `GET /api/v1/courses/{id}`
- **Response**:
  - **200 OK**
  ```json
  {
    "id": 1,
    "name": "Introduction to Programming",
    "level": "Beginner"
  }
  ```
  - **404 Not Found** if Course does not exist.

### 3. Update a Course
- **Route**: `PUT /api/v1/courses/{id}`
- **Request Body**:
  ```json
  {
    "name": "Advanced Programming",
    "level": "Intermediate"
  }
  ```
- **Response**:
  - **200 OK**
  ```json
  {
    "id": 1,
    "name": "Advanced Programming",
    "level": "Intermediate"
  }
  ```
  - **400 Bad Request** for validation errors (e.g., missing fields).

---

Ensure that all necessary headers (e.g., Content-Type: application/json) are included in your requests. For further assistance, please refer to the specific endpoint documentation above.