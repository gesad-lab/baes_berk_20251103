# README.md

# Course Management API

## Overview

The Course Management API allows for the management of courses, including creating, retrieving, and updating course details. This document serves to describe how to utilize the API endpoints as well as details of the underlying features.

## New Feature: Teacher-Course Assignment

### Description

A new feature has been implemented to enable assigning a teacher to a course. This allows for better management of educational resources by organizing courses with specific educators.

### API Endpoints

#### 1. Assign Teacher to Course

- **Endpoint**: `/courses/{course_id}/assign-teacher`
- **Method**: `POST`
- **Request Body**:
    ```json
    {
      "teacher_id": <teacher_id>
    }
    ```
- **Response**:
    - **Success** (200):
        ```json
        {
          "message": "Teacher assigned successfully."
        }
        ```
    - **Error** (400):
        ```json
        {
          "error": {
            "message": "Invalid course ID."
          }
        }
        ```

#### 2. Retrieve Course Details

- **Endpoint**: `/courses/{course_id}`
- **Method**: `GET`
- **Response**:
    - **Success** (200):
        ```json
        {
          "course": {
            "id": <course_id>,
            "name": "Mathematics",
            "level": "Beginner",
            "teacher": {
              "id": <teacher_id>,
              "name": "John Doe"
            }
          }
        }
        ```

### Setup Instructions

1. Install required packages and dependencies.
2. Run database migrations to update the schema accordingly.
   ```bash
   flask db upgrade
   ```

### Running Tests

To ensure that the new features are functioning correctly, you can run the tests. The following tests have been added for the teacher assignment feature:

- Test assigning a teacher to a course.
- Test assigning a teacher to a non-existent course.
- Test retrieving course details including assigned teacher.

Run the following command to execute tests:
```bash
pytest tests/test_routes.py
```

Make sure to have the testing environment set up appropriately to run these tests.

---

This update provides a clear summary of the new feature related to teacher-course assignments, including detailed API information and setup instructions.