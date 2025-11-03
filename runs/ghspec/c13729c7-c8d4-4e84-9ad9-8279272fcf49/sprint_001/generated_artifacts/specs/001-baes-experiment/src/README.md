# README.md

# Student Management API

## Overview

The Student Management API is a simple web application designed to manage student entities. Each student has a single required field for their name. The API provides endpoints to create and retrieve student data in a clean JSON format.

## Purpose

This application leverages modern web practices for the efficient management and retrieval of student data, ensuring seamless integrations and interactions via a RESTful API.

## Functional Requirements
1. **Create a New Student**
   - **Endpoint**: `POST /students`
   - **Required Field**: Name (cannot be empty)
   - **Response**: JSON object containing the created student's ID and name, or an error if the name field is missing.

2. **Retrieve a Student**
   - **Endpoint**: `GET /students/{id}`
   - **Response**: JSON object containing the student's ID and name, or a 404 error if the student does not exist.

3. **Automatic Database Schema Creation**
   - On application startup, the database schema will be automatically created, ensuring the necessary student table exists.

## Setup Instructions

### 1. Set Up Environment
- **Create a Virtual Environment**: 
  ```bash
  python -m venv venv
  ```
- **Activate the Virtual Environment**: 
  - On Windows:
    ```bash
    venv\Scripts\activate
    ```
  - On macOS/Linux:
    ```bash
    source venv/bin/activate
    ```

### 2. Install Dependencies
- **Install FastAPI and SQLite Dependencies**:
  ```bash
  pip install fastapi[all] sqlalchemy
  ```

### 3. Configure Environment Variables
- **Create a `.env.example` File**:
```plaintext
# Example environment variables
# DB_URL=sqlite:///./students.db
```

### 4. Run the Application
- **Start the Application**:
```bash
uvicorn src.api.students:app --reload
```
- The application will be accessible at `http://127.0.0.1:8000`.

## API Usage

### Creating a New Student
To create a new student, send a `POST` request to `/students` with a JSON body:
```json
{
  "name": "John Doe"
}
```

#### Error Handling
If the `name` field is missing, the system will return the following error response:
```json
{
  "error": {
    "code": "E001",
    "message": "Name is required."
  }
}
```

### Retrieving a Student
To retrieve a specific student by ID, send a `GET` request to `/students/{id}`.

### Example Successful Response
```json
{
  "id": 1,
  "name": "John Doe"
}
```

### Example Error Response
If the student does not exist:
```json
{
  "error": {
    "code": "E002",
    "message": "Student not found."
  }
}
```

## Project Structure
```
/src
  /api
    __init__.py
    students.py
  /models
    __init__.py
    student.py
  /database
    __init__.py
    session.py
    migrations.py
  /tests
    __init__.py
    test_students.py
```

## Conclusion
This API provides a straightforward interface for managing student data with essential error handling and validations. Future enhancements may include additional features, more robust logging, and refined error management. For any questions or contributions, please refer to the project's repository.