# README.md

Updated to include error handling scenarios for teacher assignment to courses.

```
# Project Title

## Overview
This project is an API for managing courses, teachers, and student assignments. It allows admins to assign teachers to courses, view course details, and retrieve lists of courses with their associated teachers.

## API Endpoints
1. **Assign a Teacher to a Course**
   - Endpoint: `PATCH /courses/{course_id}`
   - Description: Update a Course record by sending a PATCH request with a valid teacher ID.
   - **Test**: Confirm the response includes the updated course information reflecting the assignment of the teacher.
  
2. **Viewing Course with Assigned Teacher**
   - Endpoint: `GET /courses/{course_id}`
   - Description: Retrieve details of a course, including the assigned teacher.
   - **Test**: Expect a response containing the course details, teacher's name, and email.

3. **Error Handling for Invalid Teacher Assignment**
   - Endpoint: `PATCH /courses/{course_id}`
   - Description: Attempt to assign a non-existent teacher to a course.
   - **Test**: Expect an error response indicating that the teacher does not exist (e.g., `{"error": {"code": "E001", "message": "Teacher does not exist"}}`).

4. **Retrieving All Courses Including Teachers**
   - Endpoint: `GET /courses`
   - Description: List all courses along with their assigned teachers.
   - **Test**: Expect a list of courses, each including details of the assigned teacher.

## Error Handling
- The API now includes robust error handling when trying to assign a teacher to a course. Invalid `teacher_id` values will trigger appropriate responses:
  - If the `teacher_id` does not exist, a structured error message is returned indicating the problem.
  - Ensure to validate and handle edge cases effectively to maintain data integrity.

## Testing
- Additional tests have been written to cover error handling scenarios:
  - Testing assignment of a non-existent teacher.
  - Ensuring proper error messages are returned for invalid requests.
  
## Development Steps
1. Update the database model to include `teacher_id`.
2. Create request/response schemas for updates.
3. Develop API routes and implement error handling.
4. Write and run tests to validate functionality, including error cases.

## Setup
- Follow the standard setup procedures to run the application.

## Usage
Refer to the detailed endpoint specifications for API usage examples.

```