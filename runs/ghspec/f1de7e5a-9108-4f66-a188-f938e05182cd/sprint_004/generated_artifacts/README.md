# README.md

# Application API Documentation

## Introduction
This application provides an API for managing students and courses. The API allows for student enrollment in courses and retrieving the courses associated with a student. 

## API Endpoints

### 1. Enroll a Student in a Course
- **Endpoint**: `/students/{student_id}/enroll`
- **Method**: `POST`
- **Request Body**:
  ```json
  {
      "course_id": "<integer>"
  }
  ```
- **Response**:
  - **201 Created**: Indicates the student has been successfully enrolled in the course.
  - **400 Bad Request**: Returned if the `course_id` does not reference a valid course.

### 2. Retrieve Courses for a Student
- **Endpoint**: `/students/{student_id}/courses`
- **Method**: `GET`
- **Response**:
  - **200 OK**: Returns a JSON array of course objects that the student is enrolled in.

## Database Schema

### Student Courses Junction Table
The following table has been added to support the many-to-many relationship between `Student` and `Course` entities:

- **Table Name**: `student_courses`
- **Fields**:
  - `student_id`: Integer (foreign key referencing `Student`)
  - `course_id`: Integer (foreign key referencing `Course`)
  - **Primary Key**: Composite key on both `student_id` and `course_id`

## Migration Guide
A database migration script has been created to establish the `student_courses` junction table while preserving existing `Student` and `Course` data. Please ensure to run this migration after setting up the application.

## Running Tests
To run the unit and integration tests for the API:
1. Ensure that you have the necessary testing framework installed.
2. Run the tests using the following command:
   ```bash
   pytest tests/
   ```

## Conclusion
This documentation outlines the setup and usage of the new API endpoints related to student enrollment in courses. Please refer to the integration tests for examples of how to interact with the API.