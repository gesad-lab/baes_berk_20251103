# README.md

# Project Overview

This project is a tool to manage educational entities like students and courses. It allows for the creation, validation, and management of student and course data through a RESTful API.

## Course Entity

The Course entity represents an educational course that students can enroll in. Below are details regarding the usage, expected request structure, and validation rules for the Course entity.

### Usage

To work with the Course entity, you can use the following endpoints:

- `POST /api/v1/courses`: Create a new course.
- `GET /api/v1/courses`: Retrieve a list of all courses.
- `GET /api/v1/courses/{id}`: Get details about a specific course.
- `PUT /api/v1/courses/{id}`: Update an existing course.
- `DELETE /api/v1/courses/{id}`: Remove a course.

### Expected Request Structure

When creating or updating a course, the request body should be in JSON format and follow the structure below:

```json
{
    "title": "Introduction to Python",
    "description": "A comprehensive introduction to Python programming.",
    "credits": 3,
    "instructor": "John Doe"
}
```

### Validation Rules

Validation is critical to ensure the integrity of course data. The following validation rules apply:

- **title**: Must be a non-empty string. This field is required.
- **description**: Must be a string. Length should not exceed 2000 characters.
- **credits**: Must be an integer greater than 0 (e.g., 1, 2, 3).
- **instructor**: Must be a non-empty string. This field is required.

### Error Handling

If the validation fails when creating or updating a course, the API will return a 400 Bad Request status along with detailed error messages in the following format:

```json
{
    "error": {
        "code": "E001",
        "message": "Validation failed on course data",
        "details": {
            "title": "Title is required",
            "credits": "Credits must be a positive integer"
        }
    }
}
```

## Getting Started

1. Clone the repository.
2. Install required dependencies.
3. Set up your environment variables before running the application.
4. Follow the API documentation for details on requests and usage.