# README.md

---

# Project Title

## API Documentation

### Assigning Teachers to Courses

#### Post a Teacher to a Course
To assign a teacher to a course, you can use the following endpoint:

**POST** `/courses/{course_id}/teachers`

**Request Body:**
```json
{
    "teacher_id": "123456"
}
```

**Response:**
- **201 Created**
```json
{
    "message": "Teacher assigned successfully."
}
```

- **400 Bad Request**
```json
{
    "error": {
        "code": "E001",
        "message": "Invalid teacher ID."
    }
}
```

### Retrieving Course Details

To retrieve the details of a specific course, including the assigned teachers, use:

**GET** `/courses/{course_id}`

**Response:**
- **200 OK**
```json
{
    "course_id": "math101",
    "course_name": "Mathematics 101",
    "teachers": [
        {
            "teacher_id": "123456",
            "name": "Jane Doe",
            "email": "jane@example.com"
        }
    ]
}
```

- **404 Not Found**
```json
{
    "error": {
        "code": "E002",
        "message": "Course not found."
    }
}
```

## Getting Started

### Installation
- Instructions for installing the project.

### Running the Application
- Instructions for running the application.

### Tests
- Instructions for running tests.

### Contributing
- Guidelines for contributing to the project.

### License
- Information about the project's license.

--- 

This document provides a high-level overview of the new API endpoints added for assigning teachers to courses and retrieving course details, complete with sample requests and responses.