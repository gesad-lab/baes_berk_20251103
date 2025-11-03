# README.md

# Course Management Application

## Overview

This application allows for the management of student enrollments in courses, enabling admins to enroll students and users to view their associated courses.

## Features

- **Enroll Student in Course**: Admins can enroll a student in a specific course, allowing for the management of the student's course participation.
- **Retrieve Student Courses**: Users can view all courses that they are enrolled in, to better understand their academic commitments.
- **Validation for Enrollments**: The application provides clear feedback when enrollment requests fail due to invalid student or course IDs.

## API Endpoints

### 1. Enroll Student in Course

- **Endpoint**: `POST /students/{student_id}/courses`
- **Description**: Enroll a specific student in a course.
- **Input**: 
  - JSON object containing:
    - `course_id` (UUID, required)
- **Output**: 
  - JSON object confirming successful enrollment, including:
    - `student_id`
    - `course_id`
- **Example Request**:
  ```json
  POST /students/123e4567-e89b-12d3-a456-426614174000/courses
  {
      "course_id": "123e4567-e89b-12d3-a456-426614174001"
  }
  ```

### 2. Retrieve Student Courses

- **Endpoint**: `GET /students/{student_id}/courses`
- **Description**: Retrieve a list of all courses linked to a specific student.
- **Output**: 
  - JSON array of enrolled courses, each containing:
    - `id`
    - `name`
    - `level`
- **Example Request**:
  ```json
  GET /students/123e4567-e89b-12d3-a456-426614174000/courses
  ```

## Validation for Enrollments

- The application ensures that enrollment requests fail and provide actionable feedback if:
  - A student does not exist.
  - A course is invalid.
- **Example Error Responses**:
  ```json
  {
      "error": {
          "code": "E001",
          "message": "Invalid student ID.",
          "details": {}
      }
  }
  ```

## Database Schema Update

- The `Student` table has been updated to include a relationship with the `Course` table through a new junction table called `StudentCourses`, which holds references to both `student_id` and `course_id`. 
- A migration script has been implemented to create this new table while ensuring existing data in both the `Student` and `Course` tables is preserved.

## Testing

- Comprehensive tests have been included to validate the new functionality.
- Tests cover:
  - Successful enrollment of students in courses.
  - Successful retrieval of a student's courses.
  - Validation checks for invalid student or course IDs and appropriate error messages.

## Manual Testing

For manual testing, use tools like Postman to interact with the API endpoints and validate their functionality against the expected behavior as outlined above.

## Contributing

For contributions and improvements, please refer to the contributing guidelines in this repository.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.