# Updated README.md

# Project Title

## Overview

The purpose of this feature is to establish a relationship between the Student and Course entities in the existing application. This addition will allow a Student to enroll in multiple courses, enhancing the user experience by enabling effective course management and tracking of student enrollment. Thus, it will facilitate better understanding and organization of educational data.

## API Documentation

### Enrollment and Course Retrieval Endpoints

#### 1. Enroll Student in Course

- **Endpoint**: `POST /students/{id}/enroll`
- **Description**: Enroll a student in a specific course by specifying the student's ID and course ID.
- **Request Body** (JSON):
  ```json
  {
    "course_id": <course_id>
  }
  ```
- **Responses**:
  - **200 OK**: Successfully enrolled the student in the course.
    ```json
    {
      "message": "Successfully enrolled in the course."
    }
    ```
  - **400 Bad Request**: Missing or invalid student ID or course ID.
    ```json
    {
      "error": {
        "code": "E001",
        "message": "Invalid input. Student ID and Course ID are required."
      }
    }
    ```
  - **404 Not Found**: Student ID or course ID does not exist.
    ```json
    {
      "error": {
        "code": "E002",
        "message": "Student or Course not found."
      }
    }
    ```

#### 2. Get Student Courses

- **Endpoint**: `GET /students/{id}/courses`
- **Description**: Retrieve a list of courses that a specific student is enrolled in.
- **Responses**:
  - **200 OK**: A list of enrolled courses for the student.
    ```json
    {
      "courses": [
        {
          "id": <course_id>,
          "name": "<course_name>"
        },
        ...
      ]
    }
    ```
  - **404 Not Found**: Student ID does not exist.
    ```json
    {
      "error": {
        "code": "E002",
        "message": "Student not found."
      }
    }
    ```

### User Scenarios & Testing

1. **Enroll Student in Course**:
   - As a user, I want to enroll a student in a specific course by specifying the student’s ID and course ID.
   - **Test**: Send a POST request to enroll a student in a course and verify that the enrollment is successful.

2. **Get Student Courses**:
   - As a user, I want to retrieve a list of courses that a specific student is enrolled in.
   - **Test**: Send a GET request for a student’s ID and verify that the correct list of courses is returned.

3. **Validation for Enrollment**:
   - If I attempt to enroll a student without a valid student ID or course ID, I want to receive a clear error message indicating the required fields.
   - **Test**: Send the POST request without required IDs and verify that a validation error is returned.

4. **Error Handling for Invalid IDs**:
   - If I provide non-existent student or course IDs, I want to receive an appropriate error message.
   - **Test**: Send a POST request with invalid IDs and verify that the appropriate error messages are returned.

## Functional Requirements

1. **API Endpoints**:
   - **POST /students/{id}/enroll**: Enroll a student in a course by specifying the course ID.
   - **GET /students/{id}/courses**: Retrieve a list of courses a student is enrolled in.

2. **Database Changes**:
   - Create a new table `StudentCourse` to manage the many-to-many relationship between students and courses with the following fields:
     - `student_id`: Integer (Foreign Key referencing Student)
     - `course_id`: Integer (Foreign Key referencing Course)

## Contribution

For contributions, please create a pull request, ensuring that the tests are updated alongside any code changes, and adhere to the established coding standards.