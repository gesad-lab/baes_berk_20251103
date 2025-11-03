# README.md

# Course API Documentation

## Overview

The Course API allows the management of educational courses within the system. It introduces a new Course entity that enhances our classification of various educational offerings. Each course is categorized by a name and a level, allowing for better organization and querying of course-related data.

## Functional Requirements

### Course Entity

Each course entity has the following structure:

- **Course**
  - **name**: (String) - required
  - **level**: (String) - required

## New Features

### Associate Student with Courses

- **Endpoint**: `POST /students/{student_id}/courses`
  - **Description**: Allows an admin to associate multiple courses with a given student.
  - **Request Body**:
    ```json
    {
      "course_ids": [1, 2, 3]
    }
    ```
  - **Response**:
    - Status `200 OK`: Student successfully updated with associated courses.
    - Status `404 Not Found`: If the student or any provided course IDs do not exist.

---

### Retrieve Student with Courses

- **Endpoint**: `GET /students/{student_id}`
  - **Description**: Retrieves a student's details along with a list of their associated courses.
  - **Response**:
    - Status `200 OK`: Returns student information, including associated courses.
    ```json
    {
      "student": {
        "id": 1,
        "name": "John Doe",
        "courses": [
          {"id": 1, "name": "Mathematics"},
          {"id": 2, "name": "Science"}
        ]
      }
    }
    ```

---

### Handle Non-Existent Course Association

- **Endpoint**: `POST /students/{student_id}/courses`
  - **Description**: Attempts to associate a non-existent course with a student.
  - **Response**:
    - Status `404 Not Found`: Returns an error response indicating the course does not exist.
    ```json
    {
      "error": {
        "code": "E001",
        "message": "Course does not exist."
      }
    }
    ```

---

## Database Migration

- **Migration Process**: When introduced, the `student_courses` table should be created with the following structure:
  - **student_courses**
    - `student_id` (Integer, Foreign Key to Student.id)
    - `course_id` (Integer, Foreign Key to Course.id)

- **Validation**: After the migration, verify that existing Student and Course data is preserved and that the relationship between Students and Courses is successfully established.

---

## Conclusion

The Course API now includes the ability to associate students with multiple courses, providing enhanced flexibility in managing educational offerings within the application.