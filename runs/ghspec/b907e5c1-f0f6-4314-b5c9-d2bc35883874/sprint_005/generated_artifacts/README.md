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
  "course_id": "string"
}
```

#### Response
- **Success (201 Created)**: Course successfully associated with the student.
- **Error (400 Bad Request)**: Invalid input or student not found.

### 2. Teacher Management

#### Create a Teacher

**POST** `/teachers`

#### Description
Creates a new teacher in the system.

#### Request Body
```json
{
  "name": "string",
  "email": "string"
}
```

#### Response
- **Success (201 Created)**: Teacher successfully created.
- **Error (400 Bad Request)**: Invalid input or email format is incorrect.

#### Retrieve a Teacher

**GET** `/teachers/{teacher_id}`

#### Description
Retrieves the details of a specific teacher by their ID.

#### Response
- **Success (200 OK)**: Returns the teacher's details.
- **Error (404 Not Found)**: Teacher not found.

#### List Teachers

**GET** `/teachers`

#### Description
Lists all teachers in the system.

#### Response
- **Success (200 OK)**: Returns a list of teachers.
- **Error (500 Internal Error)**: Unexpected error occurred. 

## Additional Information

For more detail on error responses and other related information, please refer to the error handling documentation in the system.