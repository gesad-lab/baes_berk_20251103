# Student API Documentation

## Overview

The Student API allows users to manage student data through a simple RESTful interface. You can create new students, retrieve a list of all students, and handle validation for input errors. This API is built using FastAPI and SQLAlchemy, with SQLite as the database.

## Table of Contents

- [Environment Setup](#environment-setup)
- [Project Structure](#project-structure)
- [Endpoints](#endpoints)
  - [Create Student](#create-student)
  - [Retrieve Student List](#retrieve-student-list)
- [Error Handling](#error-handling)
- [Testing](#testing)

## Environment Setup

To set up the environment for the Student API, follow these steps:

1. **Python Installation**: Ensure you have Python 3.11+ installed.
2. **Create Virtual Environment**: 
   ```bash
   python -m venv venv
   ```
3. **Activate Virtual Environment**:
   - On Windows:
   ```bash
   venv\Scripts\activate
   ```
   - On macOS/Linux:
   ```bash
   source venv/bin/activate
   ```
4. **Install Dependencies**: Install the required packages.
   ```bash
   pip install -r requirements.txt
   ```

## Project Structure

The project follows the structure below for better organization:

```
student_api/
├── src/
│   ├── main.py              # Entry point for the application
│   ├── models.py            # Data models
│   ├── crud.py              # CRUD operations
│   ├── schemas.py           # Pydantic schemas for validation
│   ├── database.py          # Database setup and session management
├── tests/
│   ├── test_main.py         # Test cases for API endpoints
├── .env.example              # Example of environment variables
├── requirements.txt          # Project dependencies
└── README.md                 # Project documentation
```

## Endpoints

### Create Student

- **Endpoint**: `POST /students`
- **Request Body**: 
    ```json
    {
        "name": "John Doe"
    }
    ```
- **Success Response**: 
    - **Status**: 201 Created
    - **Body**:
    ```json
    {
        "id": 1,
        "name": "John Doe"
    }
    ```

### Retrieve Student List

- **Endpoint**: `GET /students`
- **Success Response**: 
    - **Status**: 200 OK
    - **Body**:
    ```json
    [
        {
            "id": 1,
            "name": "John Doe"
        },
        {
            "id": 2,
            "name": "Jane Smith"
        }
    ]
    ```

## Error Handling

- When creating a student without a name, the API will return a validation error.
- **Error Response**: 
    - **Status**: 400 Bad Request
    - **Body**:
    ```json
    {
        "error": {
            "code": "E001",
            "message": "Name is required.",
            "details": {}
        }
    }
    ```

## Testing

To test the API endpoints, run the unit tests provided in `tests/test_main.py`. Ensure you have at least 70% code coverage for the business logic, especially for critical paths such as creating and retrieving students. 

You can use pytest to run the tests:
```bash
pytest tests/
``` 

This README provides a comprehensive overview of the Student API, its setup, and usage instructions for developers and users alike.