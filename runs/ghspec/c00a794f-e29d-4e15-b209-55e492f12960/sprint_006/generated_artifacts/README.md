# README.md

# Teacher Entity Management

## Overview
This application allows for the management of teachers, including the creation and retrieval of teacher records. Teachers have essential attributes such as name and email.

## API Endpoints

### Create a New Teacher

- **Endpoint:** `/api/v1/teachers`
- **Method:** `POST`
- **Request Body:**
  ```json
  {
    "name": "John Doe",
    "email": "johndoe@example.com"
  }
  ```
- **Response:**
  - **Status Code:** `201 Created`
  - **Body:**
    ```json
    {
        "message": "Teacher created successfully.",
        "teacher": {
            "id": 1,
            "name": "John Doe",
            "email": "johndoe@example.com"
        }
    }
    ```

### Assign Teacher to Course

- **Endpoint:** `/api/v1/courses/{course_id}/assign_teacher`
- **Method:** `POST`
- **Request Body:**
  ```json
  {
    "teacher_id": 1
  }
  ```
- **Response:**
  - **Status Code:** `200 OK` (on success)
  - **Body:**
    ```json
    {
        "message": "Teacher assigned to course successfully."
    }
    ```
  - **Error Response (if teacher_id is not provided):**
    - **Status Code:** `400 Bad Request`
    - **Body:**
    ```json
    {
        "error": {
            "code": "E001",
            "message": "A teacher must be specified."
        }
    }
    ```

### Retrieve Course Information with Teacher Details

- **Endpoint:** `/api/v1/courses/{course_id}`
- **Method:** `GET`
- **Response:**
  - **Status Code:** `200 OK`
  - **Body:**
  ```json
  {
      "course_id": 1,
      "course_name": "Math 101",
      "teacher": {
          "name": "John Doe",
          "email": "johndoe@example.com"
      }
  }
  ```

## Success Criteria
1. Admins can successfully assign a teacher to a course and save this change without errors.
2. The application returns the correct course details, including teacher information, in JSON format when queried.
3. The application properly handles attempts to assign teachers without specifying a teacher, providing actionable error messages.
4. The database migration successfully alters the Course table to include the teacher_id column and retains all existing Course data without data loss.
5. The application operates without errors and maintains backward compatibility with previous versions.