# File: docs/api_documentation.md

# API Documentation

## Overview
This document outlines the API endpoints for managing students and courses within the application. It includes endpoints for assigning, retrieving, and deleting course enrollments for students.

## Course Management API Endpoints

### Assign Courses to a Student
- **Endpoint**: `POST /students/{id}/courses`
- **Description**: Assign one or more courses to a specific student identified by their student ID.
- **Request Body**:
  ```json
  {
    "course_ids": [1, 2, 3]  // List of course IDs to associate with the student
  }
  ```
- **Responses**:
  - **201 Created**: Successfully assigned courses.
    ```json
    {
      "message": "Courses assigned successfully."
    }
    ```
  - **404 Not Found**: If the student ID does not exist.
    ```json
    {
      "error": {
        "code": "E001",
        "message": "Student not found."
      }
    }
    ```
  - **400 Bad Request**: If invalid course IDs are provided.
    ```json
    {
      "error": {
        "code": "E002",
        "message": "Invalid course IDs provided."
      }
    }
    ```

### Retrieve Courses for a Student
- **Endpoint**: `GET /students/{id}/courses`
- **Description**: Retrieve all courses associated with a specific student.
- **Responses**:
  - **200 OK**: Returns a list of courses for the student.
    ```json
    {
      "courses": [
        {
          "id": 1,
          "name": "Course 1",
          "level": "Beginner"
        },
        {
          "id": 2,
          "name": "Course 2",
          "level": "Intermediate"
        }
      ]
    }
    ```
  - **404 Not Found**: If the student ID does not exist.
    ```json
    {
      "error": {
        "code": "E001",
        "message": "Student not found."
      }
    }
    ```

### Remove a Course from a Student's Enrollment
- **Endpoint**: `DELETE /students/{id}/courses/{course_id}`
- **Description**: Remove a specific course from a student's enrollment.
- **Responses**:
  - **204 No Content**: Successfully removed the course from the student's enrollment.
  - **404 Not Found**: If either the student ID or course ID does not exist.
    ```json
    {
      "error": {
        "code": "E001",
        "message": "Student not found."
      }
    }
    ```
    or
    ```json
    {
      "error": {
        "code": "E003",
        "message": "Course not found for this student."
      }
    }
    ```

## Conclusion
This API enables management of course assignments to students in a seamless manner, allowing for flexibility and maintaining data integrity for both `Student` and `Course` entities.