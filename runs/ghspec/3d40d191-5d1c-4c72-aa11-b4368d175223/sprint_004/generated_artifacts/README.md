# README.md

# Project Title

## Overview & Purpose
The purpose of this feature is to establish a relationship between the Student and Course entities within the existing application. With this enhancement, a Student can be linked to multiple Courses, allowing the application to manage student enrollments effectively and facilitate future functionalities such as tracking student progress in various courses. This integration will provide greater flexibility in managing educational pathways and course assignments for students.

## API Endpoints

### Enroll Student in Course

- **Endpoint**: `POST /students/{student_id}/courses`
- **Description**: Enroll a student in a specific course.
- **Request Body**:
  ```json
  {
    "course_id": 1
  }
  ```
- **Response**:
  - **Success**: 
    - Status Code: `201 Created`
    - Body:
      ```json
      {
        "message": "Enrollment successful",
        "enrollment": {
          "student_id": 1,
          "course_id": 1
        }
      }
      ```
  - **Error**: 
    - Status Code: `400 Bad Request`
    - Body:
      ```json
      {
        "error": {
          "code": "E001",
          "message": "Missing course_id"
        }
      }
      ```

### Retrieve Student Courses

- **Endpoint**: `GET /students/{student_id}/courses`
- **Description**: Retrieve all courses that a specific student is enrolled in.
- **Response**:
  - **Success**:
    - Status Code: `200 OK`
    - Body:
      ```json
      [
        {
          "id": 1,
          "name": "Mathematics",
          "level": "Beginner"
        },
        {
          "id": 2,
          "name": "Science",
          "level": "Intermediate"
        }
      ]
      ```
  - **Error**:
    - Status Code: `404 Not Found`
    - Body:
      ```json
      {
        "error": {
          "code": "E002",
          "message": "Student not found"
        }
      }
      ```

## User Scenarios & Testing
- **Enroll Student in Course**: A user wants to enroll a student in a specific course. They send a request with the identifiers of the student and the course, and the application responds with confirmation of the enrollment, including the student and course details.
- **Retrieve Student Courses**: A user wants to view all courses that a specific student is enrolled in. They send a request containing the student’s identifier, and the application responds with a list of enrolled courses.
- **Error Handling Missing Student/Course**: A user attempts to enroll a student in a course without providing either the student or course identifiers. The application should respond with a clear error message indicating which identifier is missing.

## Functional Requirements
- See API Endpoints section above for details on the functionalities related to student enrollment and course retrieval.

## Architecture
The architecture follows the Model-View-Controller (MVC) pattern, with the following components impacted by this implementation:
- **API Layer**: New endpoints for enrolling students in courses and retrieving student course details.
- **Service Layer**: Logic for handling student enrollments and fetching course information.
- **Data Access Layer (DAL)**: Updates to the data models to accommodate the many-to-many relationship.
- **Database**: The SQLite database schema will be updated to establish a join table for the Student-Course relationship.

## Existing Code Files Modifications
- **api.py** will have new endpoints for enrolling students in courses and retrieving course information.
- **models.py** will need modification to add the `StudentCourse` join table.
- **services.py** will be updated with new services for course enrollment and retrieval.
- A new file `schemas.py` will be created to manage validation schemas.
- **tests/test_student_courses.py** will be newly created for comprehensive course-related tests.

## Getting Started

Provide information about:
- Prerequisites
- How to run the application
- Configuration options

## Contributing

Instructions for how others can contribute to this project.