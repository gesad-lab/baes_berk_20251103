# File: docs/api_overview.md

# API Overview

## Introduction

This document provides an overview of the API endpoints available for interaction with the system. It contains details on the request formats, response structures, and any necessary authentication methods.

## Endpoints

### Students

#### Create Student
- **URL**: `/students`
- **Method**: `POST`
- **Request**:
  ```json
  {
      "name": "John Doe",
      "email": "john.doe@example.com"
  }
  ```
- **Response**:
  - **201 Created**: Returns the created student object.
  - **400 Bad Request**: If the input data is invalid.

### Courses

#### Create Course
- **URL**: `/courses`
- **Method**: `POST`
- **Request**:
  ```json
  {
      "title": "Introduction to API Development",
      "description": "A comprehensive course on building APIs using FastAPI.",
      "credits": 3
  }
  ```
- **Response**:
  - **201 Created**: Returns the created course object.
  - **400 Bad Request**: If the input data is invalid.

#### Get All Courses
- **URL**: `/courses`
- **Method**: `GET`
- **Response**:
  - **200 OK**: Returns a list of all courses.
    ```json
    [
        {
            "id": 1,
            "title": "Introduction to API Development",
            "description": "A comprehensive course on building APIs using FastAPI.",
            "credits": 3
        },
        ...
    ]
    ```

#### Get Course by ID
- **URL**: `/courses/{id}`
- **Method**: `GET`
- **Response**:
  - **200 OK**: Returns the course object for the given ID.
  - **404 Not Found**: If the course does not exist.

### Error Handling

All endpoints return consistent error responses structured as follows:
```json
{
    "error": {
        "code": "E001",
        "message": "Invalid input data.",
        "details": {}
    }
}
```

## Database Schema Changes

The following changes have been made to the database schema as part of the introduction of the `/courses` endpoint:

- A new table `courses` has been added with the following structure:
  - `id`: Integer primary key
  - `title`: String, not null
  - `description`: Text, nullable
  - `credits`: Integer, not null
  - `created_at`: Timestamp, default to current time
  - `updated_at`: Timestamp, default to current time, updated on modification

These changes aid in the migration understanding and should be incorporated when updating the database schema.