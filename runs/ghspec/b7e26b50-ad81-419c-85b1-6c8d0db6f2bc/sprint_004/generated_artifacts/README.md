# README.md

# Project Title

## Introduction

This project aims to manage student and course enrollments within an educational framework. It provides APIs for associating students with courses and retrieving details about associated courses.

---

## API Documentation

### Endpoints

#### Associate Student with Courses
- **`PATCH /students/{id}/courses`**

  Associates a student with one or more courses.

  **Parameters:**
  - `id` (path parameter): The unique identifier of the student.
  - `course_ids` (body parameter): A list of course IDs to associate with the student.

  **Request Example:**
  ```json
  {
    "course_ids": [1, 2, 3]
  }
  ```

  **Responses:**
  - **200 OK**: Successfully associated courses with the student.
    ```json
    {
      "message": "Successfully associated courses."
    }
    ```
  - **400 Bad Request**: If one or more course IDs are invalid or non-existent.
    ```json
    {
      "error": {
        "code": "E001",
        "message": "One or more course IDs are invalid."
      }
    }
    ```

#### Fetch Associated Courses for a Student
- **`GET /students/{id}/courses`**

  Retrieves the list of courses associated with a specific student.

  **Parameters:**
  - `id` (path parameter): The unique identifier of the student.

  **Responses:**
  - **200 OK**: Returns a list of associated courses.
    ```json
    {
      "courses": [
        {
          "id": 1,
          "name": "Mathematics",
          "credits": 4
        },
        {
          "id": 2,
          "name": "Physics",
          "credits": 3
        }
      ]
    }
    ```
  - **404 Not Found**: If the student ID does not exist.
    ```json
    {
      "error": {
        "code": "E002",
        "message": "Student not found."
      }
    }
    ```

### Error Codes

- **E001**: Invalid course ID provided during association.
- **E002**: Student not found for the requested operation.

### Additional Notes

- Ensure that the `student_courses` table is created in your database to support these functionalities.

---

## Setup Instructions

To get started with this project, follow the setup instructions documented in this README. Ensure you have the required dependencies installed and the database migrated with the correct schema.

---

## Running Tests

Run the tests using the command:

```bash
pytest tests/
```

Ensure that the test coverage meets the required targets for business logic.