# Updated README.md

# Student Management System

This application allows for the creation, retrieval, and management of student records. Each student record includes both a name and an email address, facilitating communication and data management.

## API Endpoints

### 1. Create a Student
**Endpoint**: `POST /students`

**Request Body**:
```json
{
    "name": "John Doe",
    "email": "john.doe@example.com"
}
```

**Response**:
- Success (201 Created):
```json
{
    "message": "Student created successfully.",
    "student": {
        "name": "John Doe",
        "email": "john.doe@example.com"
    }
}
```
- Error (400 Bad Request):
```json
{
    "error": {
        "code": "E001",
        "message": "Name is required."
    }
}
```
```json
{
    "error": {
        "code": "E002",
        "message": "Invalid email format."
    }
}
```

### 2. Retrieve All Students
**Endpoint**: `GET /students`

**Response**:
- Success (200 OK):
```json
[
    {
        "name": "John Doe",
        "email": "john.doe@example.com"
    },
    {
        "name": "Jane Smith",
        "email": "jane.smith@example.com"
    }
]
```

## Validation
The application performs validation when creating a student:
- Name and email must be provided.
- Email must meet standard formatting requirements (e.g., must include "@" and a domain).

## Database Schema Update
The database schema for students has been updated to include an email field. A migration has been successfully performed to ensure the schema includes this new field without any data loss.

## Error Handling
The application returns clear and actionable error messages for missing or invalid name or email inputs, ensuring a smooth user experience.

## Concurrency
The application is designed to handle concurrent requests effectively while maintaining performance within reasonable limits.

## Setup Instructions
1. Set up your virtual environment and install the necessary packages listed in `requirements.txt`.
2. Configure your environment variables based on the `.env.example` file.

---

By following the above API usage details, you can now interact with the student management system to create and retrieve student records efficiently.