# Content of README.md

# Project Documentation

## Purpose

This project involves the management of courses and teachers within an educational framework, allowing for effective assignment and retrieval of courses based on teacher assignments.

## Features

- Assign teachers to courses
- Retrieve courses by teacher
- Handling of invalid teacher assignments

## API Endpoints

### Assign a Teacher to a Course

- **POST** `/courses/{course_id}/assign_teacher`
  - Assigns a teacher to the specified course.
  - **Request Body**: 
    - `teacher_id`: The ID of the teacher to be assigned (must exist in the database).
  - **Success Response**:
    - Status Code: `200 OK`
    - Body: `{"message": "Teacher assigned successfully."}`
  - **Error Responses**:
    - **404 Not Found**: If the `teacher_id` does not exist.
      - Body: `{"error": {"code": "E404", "message": "Teacher not found."}}`

### Retrieve Courses for a Specific Teacher

- **GET** `/teachers/{teacher_id}/courses`
  - Retrieves a list of all courses taught by the specified teacher.
  - **Success Response**:
    - Status Code: `200 OK`
    - Body: A list of courses associated with the teacher.

## User Scenarios & Testing

1. **Scenario: Associate a Teacher with an Existing Course**
   - **Description**: Ensure admin can assign a teacher to a course.
   - **Test Steps**:
     1. Send a POST request to `/courses/{course_id}/assign_teacher` with a valid teacher ID.
     2. Assert that the response status is `200 OK`.
     3. Validate that the course now references the specified teacher in the database.

2. **Scenario: Retrieve Courses for a Specific Teacher**
   - **Description**: Ensure users can view all courses taught by a specific teacher.
   - **Test Steps**:
     1. Send a GET request to `/teachers/{teacher_id}/courses`.
     2. Assert that the response status is `200 OK`.
     3. Validate that the response contains a list of courses for the specified teacher.

3. **Scenario: Validate Teacher Assignment with Invalid Data**
   - **Description**: Ensure assignment fails with invalid teacher ID.
   - **Test Steps**:
     1. Send a POST request to `/courses/{course_id}/assign_teacher` with a non-existent teacher ID.
     2. Assert that the response status is `404 Not Found`.
     3. Validate that the response body contains the error message indicating the teacher was not found.

## Database Migration

- Migration script must successfully update the `Course` table to include the new `teacher_id` foreign key without losing any existing records in related tables. Ensure to include the migration script in the `/db/migrations/` directory.

## Contribution

Please follow the contribution guidelines to maintain project integrity, including code styles, documentation updates, and testing practices.