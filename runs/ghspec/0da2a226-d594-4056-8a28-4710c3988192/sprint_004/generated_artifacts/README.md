# README.md

# Project Title

## Overview

This is an application for managing student enrollments in courses. Users can enroll students in courses, retrieve enrolled courses, and see error messages for invalid enrollments.

## API Endpoints

### Enroll a Student in a Course

- **POST** `/students/{student_id}/courses`
  
  Enrolls a student in a specified course.

  **Request Body**:
  ```json
  {
    "course_id": 1
  }
  ```

  **Responses**:
  - 200 OK: Student successfully enrolled.
  - 400 Bad Request: Invalid course ID or student's already enrolled in the course.
  - 404 Not Found: Student not found.

### Retrieve Student Enrolled Courses

- **GET** `/students/{student_id}/courses`
  
  Retrieves a list of courses that the specified student is enrolled in.

  **Responses**:
  - 200 OK: Returns a list of courses in JSON format.
    ```json
    [
      {
        "course_id": 1,
        "name": "Mathematics",
        "level": "Advanced"
      },
      {
        "course_id": 2,
        "name": "Physics",
        "level": "Intermediate"
      }
    ]
    ```
  - 404 Not Found: Student not found.

### Attempt to Enroll a Student in an Invalid Course

- **POST** `/students/{student_id}/courses`
  
  Enrolls a student in a specified course but handles error for invalid course ID.

  **Request Body**:
  ```json
  {
    "course_id": -1
  }
  ```

  **Responses**:
  - 400 Bad Request: Invalid course ID.

### Handle Enrollment of Existing Course

- **POST** `/students/{student_id}/courses`
  
  Attempts to enroll the same student in a course they are already enrolled in.

  **Request Body**:
  ```json
  {
    "course_id": 1
  }
  ```

  **Responses**:
  - 409 Conflict: Student is already enrolled in this course.

## User Scenarios & Testing

1. **Scenario: Enroll a Student in a Course**
   - Given a user has access to the application,
   - When the user selects a student and a course and submits the enrollment,
   - Then the student should now be associated with that course in the database.

2. **Scenario: Retrieve Student Enrolled Courses**
   - Given a user knows an existing student ID,
   - When the user requests the courses associated with that student,
   - Then the application should return a list of courses the student is enrolled in.

3. **Scenario: Attempt to Enroll a Student in an Invalid Course**
   - Given a user has access to the application,
   - When the user selects a student and attempts to enroll them in a course that does not exist,
   - Then the application should return an error message indicating that the course is invalid.

4. **Scenario: Handle Enrollment of Existing Course**
   - Given a student is already enrolled in a course,
   - When the user attempts to enroll the same student in that course again,
   - Then the application should return a message indicating that the student is already enrolled in this course.

## Functional Requirements

1. The application must allow users to enroll a student in an existing course by updating the Student record to include a list of associated courses.

2. The application must return all courses associated with a student in JSON format when requested, including information such as course name and level.

3. The application must validate course IDs provided during enrollment, responding with an error if the course does not exist.

## Technical Requirements

- Ensure you have the necessary Python packages installed.
- Run the migrations to ensure the database schema is up to date.
- API responses must be in JSON format.

## Testing

Make sure to run the tests to verify that all functionalities are working as expected before deploying any changes.