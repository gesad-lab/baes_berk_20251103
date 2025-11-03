# File: /docs/api.md

# API Documentation

## Enroll a Student in a Course

- **Endpoint**: `/api/v1/enroll`
- **Method**: POST
- **Request Body**:
  ```json
  {
    "student_id": int, // ID of the student
    "course_id": int   // ID of the course
  }
  ```
- **Response**:
  - **201 Created**: Successfully enrolled a student in a course.
    ```json
    {
      "message": "Student enrolled successfully.",
      "student_id": int,
      "course_id": int
    }
    ```
  - **400 Bad Request**: Missing parameters or non-existent entities.
    ```json
    {
      "error": {
        "code": "E001",
        "message": "Invalid request. Both student_id and course_id must be provided and valid."
      }
    }
    ```
- **Validation**: Check that both `student_id` and `course_id` exist in the database. Prevent duplicate enrollments.

---

## Get Courses for a Student

- **Endpoint**: `/api/v1/students/<int:student_id>/courses`
- **Method**: GET
- **Path Parameters**:
  - `student_id`: ID of the student whose courses are to be retrieved.
- **Response**:
  - **200 OK**: Successfully retrieved a list of courses for the student.
    ```json
    {
      "student_id": int,
      "courses": [
        {
          "course_id": int,
          "course_name": string // Name of the course
        },
        ...
      ]
    }
    ```
  - **404 Not Found**: Student not found or no courses found for the student.
    ```json
    {
      "error": {
        "code": "E002",
        "message": "Student not found or no courses enrolled."
      }
    }
    ```

---

## Unenroll a Student from a Course

- **Endpoint**: `/api/v1/unenroll`
- **Method**: DELETE
- **Request Body**:
  ```json
  {
    "student_id": int, // ID of the student
    "course_id": int   // ID of the course
  }
  ```
- **Response**:
  - **200 OK**: Successfully unenrolled the student from the course.
    ```json
    {
      "message": "Student unenrolled successfully.",
      "student_id": int,
      "course_id": int
    }
    ```
  - **404 Not Found**: Relationship does not exist or invalid IDs.
    ```json
    {
      "error": {
        "code": "E003",
        "message": "Enrollment relationship not found."
      }
    }
    ```

---

## Database Migration

- Create a new relationship mapping table `StudentCourses` that facilitates the many-to-many relationship between `Student` and `Course`.
- Ensure that during the migration process, existing `Student` and `Course` data is preserved.

This API structure provides a clear pathway for managing student enrollments in courses while adhering to RESTful principles. Further enhancements may include additional validation and detailed error responses for improved client-server communication.