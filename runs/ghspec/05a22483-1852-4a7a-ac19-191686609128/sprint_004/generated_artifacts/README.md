# README.md

# Project Title

## Overview

This application provides a system for managing students and courses, allowing for seamless enrollment and retrieval of academic commitments.

## Enrollment Functionality

### Enrolling a Student in a Course

To enroll a student in a course, send a `POST` request to the `/api/enrollments` endpoint. The request body should include:

```json
{
  "student_id": <STUDENT_ID>,
  "course_id": <COURSE_ID>
}
```

- **Success Response**: A successful enrollment will return a 201 status code along with a confirmation message in JSON format:

```json
{
  "message": "Enrollment successful",
  "student_id": <STUDENT_ID>,
  "course_id": <COURSE_ID>
}
```

- **Error Handling**: If the enrollment attempt is made with an invalid student or course ID, the response will include a 400 status code with error details:

```json
{
  "error": {
    "code": "E001",
    "message": "Invalid course ID provided."
  }
}
```

### Retrieving Student Course Enrollment

To retrieve the list of courses a specific student is enrolled in, send a `GET` request to the `/api/enrollments/<STUDENT_ID>` endpoint. The response will include a list of enrolled courses:

- **Success Response**: A successful retrieval will return a 200 status code with the list of courses:

```json
{
  "student_id": <STUDENT_ID>,
  "enrolled_courses": [
    {
      "course_id": <COURSE_ID>,
      "course_name": "Introduction to Programming"
    },
    {
      "course_id": <COURSE_ID>,
      "course_name": "Advanced Python Programming"
    }
  ]
}
```

### Error Handling for Invalid Enrollment

When attempting to enroll a student in a course that does not exist, the application will return an informative error message, ensuring users are aware of what went wrong:

- **Error Response**: If the course ID is invalid:

```json
{
  "error": {
    "code": "E002",
    "message": "Attempted to enroll in a non-existent course."
  }
}
```

## Database Schema

The application's database has been updated to include a new `Enrollment` table which serves as a join table between the `Student` and `Course` entities. This ensures that academic data is accurately mapped while maintaining the integrity of existing records.

## API Endpoints Summary

1. **Enroll a Student in a Course**
   - `POST /api/enrollments` - Enrolls a student in a course.

2. **Retrieve Courses for a Student**
   - `GET /api/enrollments/<STUDENT_ID>` - Gets a list of courses for a specific student.

## Testing

We have implemented extensive tests for the enrollment functionality, including scenarios for successful enrollments, retrieval of courses, and various error conditions. Please refer to the testing directory for the test cases related to these features.

## Installation & Setup

1. Clone the repository.
2. Install the dependencies using `pip install -r requirements.txt`.
3. Set up your database (follow the database setup instructions).
4. Run the application.

For further details on contributions, please refer to the CONTRIBUTING.md file.