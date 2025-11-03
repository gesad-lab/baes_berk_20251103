# README.md

# Project Title

## Overview

This application serves as a management system for students and courses, allowing tracking of enrollment and academic progress.

## API Documentation

### Enrollment Endpoints

1. **Enroll Student in Courses**
   - **Endpoint**: `POST /api/v1/enroll`
   - **Description**: Enroll a student in one or more courses.
   - **Request Body**:
     ```json
     {
       "student_id": "123",
       "course_ids": ["456", "789"]
     }
     ```
   - **Response**:
     - **Status 201 Created**: Enrollment successful.
     - **Status 400 Bad Request**: Invalid student or course ID.
   - **Example**:
     ```http
     POST /api/v1/enroll HTTP/1.1
     Content-Type: application/json
     
     {
       "student_id": "123",
       "course_ids": ["456", "789"]
     }
     ```

2. **Retrieve Student Courses**
   - **Endpoint**: `GET /api/v1/students/<student_id>/courses`
   - **Description**: Retrieve a list of courses associated with a specific student.
   - **Response**:
     - **Status 200 OK**: Returns a list of courses.
     - **Status 404 Not Found**: Student ID does not exist.
   - **Example**:
     ```http
     GET /api/v1/students/123/courses HTTP/1.1
     ```

3. **Remove Student from Course**
   - **Endpoint**: `DELETE /api/v1/un-enroll`
   - **Description**: Remove a student from a specific course.
   - **Request Body**:
     ```json
     {
       "student_id": "123",
       "course_id": "456"
     }
     ```
   - **Response**:
     - **Status 204 No Content**: Removal successful.
     - **Status 400 Bad Request**: Invalid student or course ID.
   - **Example**:
     ```http
     DELETE /api/v1/un-enroll HTTP/1.1
     Content-Type: application/json
     
     {
       "student_id": "123",
       "course_id": "456"
     }
     ```

### Data Model Changes

A new relationship has been established between the `Student` and `Course` entities, allowing many-to-many associations. 

- **Junction Table**: `student_course`
  - **student_id**: Reference to Student entity (required)
  - **course_id**: Reference to Course entity (required)

This change facilitates the tracking of student enrollments in multiple courses and vice versa.

## Testing

The new API functionalities are tested to ensure proper integration and validation. Ensure that the following scenarios are covered in tests:

- Enroll a student successfully.
- Retrieve all courses for a student.
- Remove a student from a specific course.
- Validate that data is preserved during migrations.

## Contribution

To contribute to this project, please fork the repository and submit a pull request detailing your changes. Ensure that you include tests for any new functionality added.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.