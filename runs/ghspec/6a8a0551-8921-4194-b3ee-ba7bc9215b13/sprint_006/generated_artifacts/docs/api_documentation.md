# File: docs/api_documentation.md

# API Documentation

## Overview
This document provides an overview of the new API endpoints added to the student management system for managing the relationship between Courses and Teachers. The application integrates new functionality that allows for the assignment of a teacher to a course.

### Base URL
`http://<your-api-domain>/api/v1`

---

## Endpoints

### Assign Teacher to Course

#### `POST /courses/{id}/assign-teacher`
Assign a teacher to a specific course.

- **Parameters**
    - `id` (path): The unique identifier of the course to which the teacher will be assigned.
  
- **Request Body**
    ```json
    {
        "teacher_id": "string"  // The unique identifier of the teacher to be assigned
    }
    ```

- **Responses**
    - **200 OK**
      - Description: Teacher successfully assigned to course.
      - Response Body:
      ```json
      {
          "message": "Teacher assigned successfully."
      }
      ```

    - **400 Bad Request**
      - Description: Invalid input or the provided teacher does not exist.
      - Response Body:
      ```json
      {
          "error": {
              "code": "E400",
              "message": "Invalid teacher ID provided.",
              "details": {}
          }
      }
      ```

    - **404 Not Found**
      - Description: Course not found for the provided ID.
      - Response Body:
      ```json
      {
          "error": {
              "code": "E404",
              "message": "Course not found.",
              "details": {}
          }
      }
      ```

---

### Retrieve Course Details

#### `GET /courses/{id}`
Retrieve details of a specific course, including the assigned teacher.

- **Parameters**
    - `id` (path): The unique identifier of the course.

- **Responses**
    - **200 OK**
      - Description: Course retrieved successfully with teacher details.
      - Response Body:
      ```json
      {
          "id": "string",
          "name": "string",
          "description": "string",
          "teacher_id": "string",  // ID of the assigned teacher
          "teacher_name": "string"  // Name of the assigned teacher
      }
      ```

    - **404 Not Found**
      - Description: Course not found for the provided ID.
      - Response Body:
      ```json
      {
          "error": {
              "code": "E404",
              "message": "Course not found.",
              "details": {}
          }
      }
      ```

--- 

## Assumptions
- When making assignments, users will know the existing Course and Teacher IDs.
- Data integrity will be maintained throughout the relational data integration.
- Robust system testing will ensure proper functionality of the new relationships within existing workflows. 

## Conclusion
This documentation outlines the new API endpoints for assigning teachers to courses and retrieving course details. It serves as a guide for developers and consumers of the API to understand the functionality and expected input/output formats. Please refer to the relevant implementation files for further details regarding the backend logic and validation.