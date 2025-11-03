# README.md

# Project Title

## Overview
This project provides a system for managing student enrollments in courses. It includes various API endpoints for enrolling students in courses, retrieving their enrollments, and managing those enrollments.

## API Endpoints

### Health Check
- **Endpoint**: `GET /health`
- **Description**: Confirms that the API is operational and that the enrollment functionality is working correctly post-deployment.
- **Response**:
    - **200 OK**: API is operational
    - **500 Internal Server Error**: Issues with the database or enrollment functionality

### Student Enrollment in Course
- **Endpoint**: `POST /students/{student_id}/enroll`
- **Description**: Enroll a student in a specified course.
- **Request Body**:
    ```json
    {
        "course_id": 1
    }
    ```
- **Response**:
    - **200 OK**: Enrollment confirmed.
    - **404 Not Found**: If either the student or the course does not exist.

### Retrieve Student Courses
- **Endpoint**: `GET /students/{student_id}/courses`
- **Description**: Retrieve a list of courses a student is enrolled in.
- **Response**:
    - **200 OK**: A JSON array containing course details.
    - **404 Not Found**: If the student does not exist.

### Remove Student from Course
- **Endpoint**: `DELETE /students/{student_id}/courses/{course_id}`
- **Description**: Remove a student from a specified course.
- **Response**:
    - **200 OK**: Removal confirmed.
    - **404 Not Found**: If either the student or the course does not exist.

## Database Management
- An associative entity named `Enrollment` has been introduced to connect `Student` and `Course`. This ensures existing data remains intact and maintains referential integrity between students and courses.

## Change Log
- Added student enrollment functionality with corresponding API endpoints.
- Updated health check endpoint to verify the operational status of the enrollment features.