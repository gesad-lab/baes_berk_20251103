# File: docs/api/student_course_api.md

# Student Course API Documentation

## 1. Overview
This document provides information about the API endpoints available for managing the student-course relationships in the application.

## 2. Functional Requirements

### 2.1 Enroll Student in Course API Endpoint
- **Method**: POST
- **URL**: `/students/{student_id}/courses`
- **Request Body**: 
  ```json
  {
    "course_id": integer
  }
  ```
- **Response**: 
  - **Success**: 
  ```json
  {
    "message": "Student enrolled in course successfully."
  }
  ```
  - **Failure**: 
  ```json
  {
    "error": {
      "code": "E400",
      "message": "Invalid course_id or student_id.",
      "details": {}
    }
  }
  ```
- **HTTP Status Codes**:
  - 201 Created (when student is successfully enrolled)
  - 400 Bad Request (if validation fails)
  - 404 Not Found (if the student or course does not exist)

### 2.2 List Student Courses API Endpoint
- **Method**: GET
- **URL**: `/students/{student_id}/courses`
- **Response**: 
  - **Success**:
  ```json
  [
    {
      "course_id": integer,
      "name": "Course Name",
      "level": "Course Level"
    }
  ]
  ```
  - **Failure**: 
  ```json
  {
    "error": {
      "code": "E404",
      "message": "Student not found.",
      "details": {}
    }
  }
  ```
- **HTTP Status Codes**:
  - 200 OK (when courses are successfully retrieved)
  - 404 Not Found (if the student does not exist)

### 2.3 Remove Student from Course API Endpoint
- **Method**: DELETE
- **URL**: `/students/{student_id}/courses/{course_id}`
- **Response**:
  - **Success**: 
  ```json
  {
    "message": "Student removed from course successfully."
  }
  ```
  - **Failure**: 
  ```json
  {
    "error": {
      "code": "E404",
      "message": "Enrollment not found for the specified course.",
      "details": {}
    }
  }
  ```
- **HTTP Status Codes**:
  - 200 OK (when student is successfully removed)
  - 404 Not Found (if the enrollment record or student/course does not exist)

## 3. Database Migration
To introduce a many-to-many relationship between Student and Course entities, a new junction table called `student_courses` will be created. This migration script will ensure that all existing Student and Course data is preserved during this structural change.

## 4. Success Criteria
- The application correctly handles enrollment, listing, and removal of students from courses via above API endpoints.
- The API returns appropriate HTTP status codes depending on the operation's success or failure.
- Error messages are meaningful and help users understand what went wrong and how to address any issues.
- Automated tests have been implemented to ensure at least 70% coverage of the business logic regarding course enrollments, listings, and removals.

## 5. Assumptions
- User authentication and authorization features will not be implemented at this stage.
- All API responses are formatted in JSON.
- All ID parameters (`student_id` and `course_id`) are assumed to be valid integers that correspond to existing records.