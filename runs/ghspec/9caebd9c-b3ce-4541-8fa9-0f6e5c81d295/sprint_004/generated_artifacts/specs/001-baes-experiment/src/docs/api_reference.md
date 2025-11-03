# File: docs/api_reference.md

# API Reference Documentation

## Endpoints

### 1. Enroll a Student in a Course
- **Endpoint**: `POST /students/{student_id}/enroll`
- **Request Body**:
  ```json
  {
    "course_id": "Course ID"
  }
  ```
- **Description**: Allows a user to enroll an existing student into an existing course by providing the student ID and course ID. 
- **Response**:
  - **Success (201 Created)**:
    ```json
    {
      "message": "Successfully enrolled student in the course."
    }
    ```
  - **Error (400 Bad Request)**: If student ID or course ID is invalid.
    ```json
    {
      "error": {
        "code": "E001",
        "message": "Invalid student ID or course ID."
      }
    }
    ```

### 2. Retrieve Student Courses
- **Endpoint**: `GET /students/{student_id}/courses`
- **Description**: Fetches the list of courses that a specific student is enrolled in.
- **Response**:
  - **Success (200 OK)**:
    ```json
    [
      {
        "course_id": "Course ID",
        "course_name": "Course Name",
        "level": "Course Level"
      },
      ...
    ]
    ```
  - **Error (404 Not Found)**: If the student ID is not found.
    ```json
    {
      "error": {
        "code": "E002",
        "message": "Student not found."
      }
    }
    ```

### 3. Error Handling for Enrollment
- **Scenario**: A user attempts to enroll a student in a course with an invalid student ID or course ID.
- **Expected Behavior**: The API ensures that invalid IDs return appropriate error messages along with corresponding status codes.

## Database Schema Update
- **New Table**: `student_courses`
  - **Fields**:
    - `student_id` (foreign key, references the Student entity)
    - `course_id` (foreign key, references the Course entity)

**Note**: Ensure that existing student and course data remain intact before and after the migration process. 

---

This documentation has been updated to reflect the new endpoints for enrolling students and retrieving their courses. Please refer to the respective sections for detailed specifications and expected behaviors.