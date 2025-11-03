# Updated API Documentation
## API Endpoints

### Enrollment Endpoints

#### POST /students/{studentId}/enroll

**Description**: This endpoint allows an authenticated user to enroll a student in a specified course.

- **Path Parameters**:
  - `studentId` (int): The unique identifier of the student who will be enrolled.

- **Request Body**:
  ```json
  {
    "course_id": 1  // The ID of the course to enroll the student in.
  }
  ```

- **Responses**:
  - **200 OK**: Successfully enrolled the student.
  ```json
  {
    "message": "Student successfully enrolled in course."
  }
  ```
  - **404 Not Found**: Returned if the student ID or course ID does not exist.
  ```json
  {
    "error": {
      "code": "E404",
      "message": "Student or course not found."
    }
  }
  ```

#### GET /students/{studentId}/courses

**Description**: Retrieves a list of courses that a specific student is enrolled in.

- **Path Parameters**:
  - `studentId` (int): The unique identifier of the student whose courses are to be retrieved.

- **Responses**:
  - **200 OK**: Successfully retrieved the list of courses the student is enrolled in.
  ```json
  {
    "courses": [
      {
        "course_id": 1,
        "course_name": "Mathematics"
      },
      {
        "course_id": 2,
        "course_name": "Science"
      }
    ]
  }
  ```
  - **404 Not Found**: Returned if the student ID does not exist.
  ```json
  {
    "error": {
      "code": "E404",
      "message": "Student not found."
    }
  }
  ```

### Additional Information

- Ensure proper handling for HTTP status codes and error responses as mentioned.
- The implementation of `EnrollmentService` includes methods `enroll_student` and `get_courses_for_student` which encapsulate the core business logic for student enrollment and course retrieval.
- Extend the current test suite with cases for validating successful enrollments, retrieval of courses, and appropriate error handling for missing resources.

This documentation aims to provide clarity on the newly added API endpoints to ensure seamless integration and usage in client applications.