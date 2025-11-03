# README.md

# Project Title

## Overview

This project is a web application for managing student enrollments in courses, allowing users to enroll students, retrieve courses they are enrolled in, and handle validation of enrollment requests.

## API Endpoints

### 1. Enroll a Student in a Course
- **Endpoint**: `POST /students/{student_id}/enroll`
- **Description**: This endpoint allows a user to enroll a specific student in a given course.
- **Request Body**:
  - `course_id: integer` (required) - The ID of the course to enroll the student in.
- **Response**:
  - **Success**: Returns HTTP status 201 Created with a JSON body confirming the enrollment, including the enrolled `student_id` and `course_id`.
  - **Failure**: Returns HTTP status 400 Bad Request with error details if the enrollment fails, such as when the specified course does not exist.

### 2. Retrieve a Student's Enrolled Courses
- **Endpoint**: `GET /students/{student_id}/courses`
- **Description**: This endpoint retrieves a list of courses a particular student is enrolled in.
- **Response**:
  - **Success**: Returns HTTP status 200 OK with a JSON array of course details including course IDs, names, and levels.
  - **Failure**: Returns HTTP status 404 Not Found if the student does not exist.

## User Scenarios & Testing

### Scenario: Enrolling a Student in a Course
- **Test**: Verify that the student is successfully enrolled and that the response confirms the enrollment with the correct student ID and course ID.

### Scenario: Retrieving Student's Enrolled Courses
- **Test**: Verify that the response returns a JSON array with the course details for each course linked to the student.

### Scenario: Validation Error on Invalid Enrollment
- **Test**: Verify that the API returns a validation error indicating that the specified course is not found.

### Scenario: Ensuring Data Integrity After Enrollment
- **Test**: Ensure that the student's data reflects the updated list of enrolled courses after the enrollment operation.

## Database Migration
- An existing database schema must be updated to add a foreign key reference in the Student table that links to the Course table. Ensure the integrity of existing data is maintained through the migration process.

## Modules Overview
### Routing Module
- Handles incoming HTTP requests and maps endpoints for student enrollment to the appropriate controller functions.

### Controller Module
- Contains functions that process enrollment requests, validate input, and return responses.

### Model Module
- Extends the existing `Student` model to incorporate a list of `enrolled_courses`.

### Validation Module
- Contains logic for validating enrollment data.

## Testing Guidelines
- Create unit tests for the new functionalities with sufficient coverage.
- Ensure that new tests validate both successful scenarios and edge cases like validation errors. 

## Conclusion
These updates to the API enhance the management of student enrollments and ensure that users have the necessary functionalities to enroll students and retrieve enrollment data efficiently.