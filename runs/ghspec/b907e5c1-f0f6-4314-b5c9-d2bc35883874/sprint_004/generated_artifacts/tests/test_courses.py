# README.md

# Educational Management System API

## Overview

This document provides an overview of the API endpoints for the Educational Management System. This system manages students and courses, allowing for effective tracking of student enrollments and course engagements.

## API Endpoints

### 1. Associate a Course with a Student

**POST** `/students/{student_id}/courses`

#### Description
Associates a specified course with a student. The course ID is provided in the JSON payload.

#### Request Body
```json
{
    "course_id": "<course_id>"
}
```

#### Response
- **Status Code**: 
  - `201 Created`: Successfully associated the course with the student.
  - `400 Bad Request`: If the provided course ID is invalid.
  - `404 Not Found`: If the student ID does not exist.

#### Example
```bash
curl -X POST http://localhost:5000/students/1/courses \
-H "Content-Type: application/json" \
-d '{"course_id": "101"}'
```

#### Successful Response Example
```json
{
    "message": "Course associated successfully."
}
```

### 2. Retrieve Courses for a Student

**GET** `/students/{student_id}/courses`

#### Description
Retrieves a list of courses associated with a specified student.

#### Response
- **Status Code**: 
  - `200 OK`: Successfully retrieved a list of courses.
  - `404 Not Found`: If the student ID does not exist.

#### Example
```bash
curl -X GET http://localhost:5000/students/1/courses
```

#### Successful Response Example
```json
{
    "courses": [
        {
            "id": "101",
            "name": "Mathematics 101"
        },
        {
            "id": "102",
            "name": "Physics 101"
        }
    ]
}
```

## Error Handling

All endpoints return structured error responses when applicable. Error responses will include the error code and message to assist with troubleshooting.

```json
{
    "error": {
        "code": "E001",
        "message": "Invalid course ID."
    }
}
```
### Required Migration

A database migration will be created to establish a many-to-many relationship between the Student and Course entities through a junction table. This ensures that the existing Student and Course data remains intact while enabling new associations.

## Conclusion

The enhancements to the Educational Management System will improve the tracking of student enrollments across multiple courses, providing a better experience both for students and administrators.

---

This document will be kept up-to-date as new features and changes are implemented within the API. Please refer to it for the latest endpoint information and usage guidelines.