# README.md

# Student Management System

## Overview

The Student Management System allows for easy management of courses and teachers. This README provides information on the API endpoints available for interaction with the application.

## API Endpoints

### Courses

#### Assign Teacher to Course

- **Endpoint**: `/api/v1/courses/<int:course_id>/assign_teacher`
- **Method**: `POST`
- **Request Body**: 
  ```json
  {
      "teacher_id": "integer"
  }
  ```
- **Description**: Assign a teacher to a specific course using the course ID. The `teacher_id` must be a valid ID of an existing teacher.
  
- **Response**:
  - **200 OK**: Teacher assigned successfully
    ```json
    {
        "message": "Teacher assigned successfully to course."
    }
    ```
  - **400 Bad Request**: If `teacher_id` is missing or invalid
    ```json
    {
        "error": {
            "code": "E001",
            "message": "Valid teacher ID must be provided."
        }
    }
    ```
  - **404 Not Found**: If the course does not exist
    ```json
    {
        "error": {
            "code": "E002",
            "message": "Course not found."
        }
    }
    ```

#### Get Course Details

- **Endpoint**: `/api/v1/courses/<int:course_id>`
- **Method**: `GET`
- **Description**: Retrieve details for a specific course using the course ID.

- **Response**:
  - **200 OK**: Successfully retrieved course details
    ```json
    {
        "id": "integer",
        "title": "string",
        "teacher": {
            "name": "string",
            "email": "string"
        }
    }
    ```
  - **404 Not Found**: If the course does not exist
    ```json
    {
        "error": {
            "code": "E002",
            "message": "Course not found."
        }
    }
    ```

## Database Migration

Ensure to run the following command to apply the latest migrations to your database:

```bash
alembic upgrade head
```

This will update the existing course schema to accommodate the new course functionality, specifically adding the `teacher_id` field to the `Course` model. 

## Application Structure

To accommodate new course management features, the application structure has been updated as follows:

```
/student_management
├── src/
│   ├── app.py
│   ├── models.py  # Modified Course model to add teacher_id
│   ├── routes.py  # New routes for course management implemented
│   ├── tests/
│   │   ├── test_routes.py  # Tests for new course functionality added
├── config.py
├── requirements.txt
├── README.md
```

## Testing

Testing for the new functionalities can be found in the `tests/test_routes.py` file. Ensure to run tests after adding new features to confirm everything works as expected.