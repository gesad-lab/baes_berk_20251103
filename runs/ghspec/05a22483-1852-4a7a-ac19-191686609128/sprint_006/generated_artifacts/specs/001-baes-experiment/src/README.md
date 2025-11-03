# README.md

# Course and Teacher API

## Overview
This document provides an overview of the API endpoints related to course-teacher assignments, detailing how you can interact with the new features implemented in our application.

## API Endpoints

### 1. Courses

#### 1.1 Create a Course
**POST** `/api/v1/courses`

**Request Body:**
```json
{
    "title": "Introduction to Programming",
    "description": "Learn the basics of programming.",
    "teacher_id": 1  // ID of the teacher assigned to the course
}
```

**Response:**
- **201 Created**: Returns the created course object.
- **400 Bad Request**: If the input data is invalid.

#### 1.2 Get All Courses
**GET** `/api/v1/courses`

**Response:**
- **200 OK**: Returns a list of courses.

#### 1.3 Get Specific Course
**GET** `/api/v1/courses/{course_id}`

**Response:**
- **200 OK**: Returns the course object.
- **404 Not Found**: If the course does not exist.

#### 1.4 Update a Course
**PUT** `/api/v1/courses/{course_id}`

**Request Body:**
```json
{
    "title": "Introduction to Programming - Updated",
    "description": "Learn the basics of programming with updates.",
    "teacher_id": 2  // New teacher ID if reassignment is necessary
}
```

**Response:**
- **200 OK**: Returns the updated course object.
- **404 Not Found**: If the course does not exist.
- **400 Bad Request**: If the input data is invalid.

#### 1.5 Delete a Course
**DELETE** `/api/v1/courses/{course_id}`

**Response:**
- **204 No Content**: Successfully deleted the course.
- **404 Not Found**: If the course does not exist.

### 2. Teachers

#### 2.1 Create a Teacher
**POST** `/api/v1/teachers`

**Request Body:**
```json
{
    "name": "John Doe",
    "email": "john@example.com"
}
```

**Response:**
- **201 Created**: Returns the created teacher object.
- **400 Bad Request**: If the input data is invalid.

#### 2.2 Get All Teachers
**GET** `/api/v1/teachers`

**Response:**
- **200 OK**: Returns a list of teachers.

#### 2.3 Get Specific Teacher
**GET** `/api/v1/teachers/{teacher_id}`

**Response:**
- **200 OK**: Returns the teacher object.
- **404 Not Found**: If the teacher does not exist.

#### 2.4 Update a Teacher
**PUT** `/api/v1/teachers/{teacher_id}`

**Request Body:**
```json
{
    "name": "Jane Doe",
    "email": "jane@example.com"
}
```

**Response:**
- **200 OK**: Returns the updated teacher object.
- **404 Not Found**: If the teacher does not exist.
- **400 Bad Request**: If the input data is invalid.

#### 2.5 Delete a Teacher
**DELETE** `/api/v1/teachers/{teacher_id}`

**Response:**
- **204 No Content**: Successfully deleted the teacher.
- **404 Not Found**: If the teacher does not exist.

## Note
- Ensure to replace the `{course_id}` and `{teacher_id}` placeholders with actual IDs when making requests.
- For successful operations, the API will return appropriate HTTP status codes along with the resulting data or an error message.

## Conclusion
This additional functionality allows for better management of course-teacher assignments, facilitating the assignment of teachers to courses effectively within the system. Please refer to the endpoints above to integrate with the API accordingly.