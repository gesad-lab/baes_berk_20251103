# README.md

# Project Title

## Overview

This project is an educational platform that allows efficient management of teaching staff, courses, and student enrollments. The following document provides setup instructions, project structure, and usage examples for the API endpoints, with a focus on the new Teacher entity.

## Setup Instructions

1. **Clone the Repository**: 
   ```bash
   git clone https://github.com/yourusername/project-name.git
   cd project-name
   ```

2. **Install Dependencies**: 
   Make sure you have Python and pip installed, then run:
   ```bash
   pip install -r requirements.txt
   ```

3. **Setup Database**:
   Configure your `.env` for database connection and run migrations:
   ```bash
   alembic upgrade head
   ```

4. **Run Application**:
   Start the FastAPI application:
   ```bash
   uvicorn main:app --reload
   ```

5. **Access API Documentation**:
   Visit [http://localhost:8000/docs](http://localhost:8000/docs) to see the auto-generated API documentation.

## Project Structure

```
src/
│
├── main.py          # Entry point of the FastAPI application
├── models/          # Database models (including Student, Course, and Teacher)
├── schemas/         # Pydantic models for request/response validation
├── routes/          # API endpoints handling HTTP requests
└── database/        # Database connection and setup
tests/
└── test_course_routes.py  # Tests for Course routes
README.md
```

## API Specifications for Teacher Entity

### 1. API Endpoints

#### 1.1 Create a New Teacher
- **Endpoint**: `POST /teachers`
- **Request Body**:
    ```json
    {
      "name": "string",  // Required
      "email": "string"  // Required, must be unique
    }
    ```
- **Response (201 Created)**:
    ```json
    {
      "id": "integer",
      "name": "string",
      "email": "string"
    }
    ```

- **Error Responses**:
    - **400 Bad Request**: If missing required fields or duplicate email
      ```json
      {
        "error": {
          "code": "E001",
          "message": "Missing required field: name",
          "details": {}
        }
      }
      ```

#### 1.2 Retrieve Teacher Details
- **Endpoint**: `GET /teachers/{teacher_id}`
- **Response (200 OK)**:
    ```json
    {
      "id": "integer",
      "name": "string",
      "email": "string"
    }
    ```

- **Error Responses**:
    - **404 Not Found**: If the teacher does not exist
      ```json
      {
        "error": {
          "code": "E002",
          "message": "Teacher not found",
          "details": {}
        }
      }
      ```

#### 1.3 List All Teachers
- **Endpoint**: `GET /teachers`
- **Response (200 OK)**:
    ```json
    [
      {
        "id": "integer",
        "name": "string",
        "email": "string"
      },
      ...
    ]
    ```

### 2. User Scenarios

#### 2.1 Creating a New Teacher
As an admin, I want to create a new Teacher entry in the system.

- **How To**:
  Send a POST request to `/teachers` with a valid name and email.

- **Expected Result**:
  You should receive a success response containing the details of the created Teacher.

#### 2.2 Viewing Teacher Details
As a user, I want to view the details of a specific Teacher.

- **How To**:
  Send a GET request to `/teachers/{teacher_id}`.

- **Expected Result**:
  You should receive the details of the requested Teacher.

## Conclusion

This document serves as a guide for developers to set up the environment and utilize the Teacher API endpoints effectively within the educational platform application. For further inquiries, please refer to the API documentation or raise an issue in the repository.