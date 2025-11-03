# README.md

# Student Management System

This is a simple student management system built using FastAPI and SQLAlchemy. The application allows users to create and retrieve student records from a database.

## Requirements

- Python 3.8 or higher
- FastAPI
- SQLAlchemy
- Uvicorn

## Installation

1. Create a new virtual environment:
   ```bash
   python -m venv venv
   ```

2. Activate the virtual environment:
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

3. Install the required dependencies:
   ```bash
   pip install fastapi sqlalchemy uvicorn
   ```

## Database Setup

The application uses SQLAlchemy for ORM. Ensure that the necessary database configurations are set in an environment file or directly in the code.

## API Endpoints

### Create a Student

- **Endpoint**: `POST /students`
- **Request Body**:
  ```json
  {
    "name": "John Doe"
  }
  ```
- **Success Response**:
  - **Code**: 201 Created
  - **Content**:
    ```json
    {
      "id": 1,
      "name": "John Doe"
    }
    ```

### Retrieve a Student

- **Endpoint**: `GET /students/{id}`
- **Success Response**:
  - **Code**: 200 OK
  - **Content**:
    ```json
    {
      "id": 1,
      "name": "John Doe"
    }
    ```

### Validation of Student Creation

- **Endpoint**: `POST /students`
- **Request Body**:
  ```json
  {
    "name": ""
  }
  ```
- **Error Response**:
  - **Code**: 400 Bad Request
  - **Content**:
    ```json
    {
      "error": {
        "code": "E001",
        "message": "Name must not be empty."
      }
    }
    ```

## Testing

To ensure code quality and reliability, write unit tests that cover at least 70% of the codebase. Focus on the following scenarios:

1. **Creating a Student**:
   - Verify that submitting a valid name creates a new student record and returns the record in JSON format.

2. **Retrieving a Student**:
   - Verify that querying with a valid student ID returns the correct student details in JSON format.

3. **Validation of Student Creation**:
   - Verify that an error message is returned when trying to create a student without the name field.

## Running the Application

To start the application, use the following command:
```bash
uvicorn main:app --reload
```

## Logging

The application uses Python's built-in logging module to log application events. Ensure that logging configuration is set up according to your preference.

## Graceful Shutdown

The application is designed to handle shutdown signals gracefully, finishing any in-flight requests before shutting down.

---

This README provides a basic overview and usage of the Student Management System, as well as important instructions for installation, configuration, and testing.