# README.md

# Student Management API

This is a simple API for managing student records. It allows users to create new student entries and retrieve all existing students. The API is built with FastAPI and uses SQLite for data storage.

## Table of Contents
- [Getting Started](#getting-started)
- [API Endpoints](#api-endpoints)
  - [Create a Student](#create-a-student)
  - [Retrieve All Students](#retrieve-all-students)
  - [Health Check](#health-check)
- [Error Handling](#error-handling)
- [Database Schema](#database-schema)
- [Running the Application](#running-the-application)
- [License](#license)

## Getting Started

To get started, clone the repository and install the required dependencies.

```bash
git clone https://github.com/yourusername/student-management-api.git
cd student-management-api
pip install -r requirements.txt
```

## API Endpoints

### Create a Student
- **Endpoint**: `POST /students`
- **Request Body**:
  - `name`: string (required)
  
**Response**:
- **Success (200 OK)**: 
  ```json
  {
    "id": 1,
    "name": "John Doe"
  }
  ```
- **Error (400 Bad Request)** (if `name` is missing):
  ```json
  {
    "error": {
      "code": "E001",
      "message": "Name is a required field."
    }
  }
  ```

### Retrieve All Students
- **Endpoint**: `GET /students`

**Response**:
- **Success (200 OK)**:
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

### Health Check
- **Endpoint**: `GET /health`

**Response**:
- **Success (200 OK)**: 
  ```json
  {
    "status": "healthy"
  }
  ```

## Error Handling

The API provides error messages for invalid requests. If the user submits a request without a required field, the API will return a 400 Bad Request with a corresponding error message.

Example Error Response:
```json
{
  "error": {
    "code": "E001",
    "message": "Name is a required field."
  }
}
```

## Database Schema

Upon application startup, the SQLite database schema is automatically created if it does not already exist. The schema includes a table for Students with the following structure:

- **Table**: Students
  - `id`: (auto-incrementing primary key)
  - `name`: (string, required)

## Running the Application

To run the application, execute the following command from the project root:

```bash
uvicorn app.main:app --reload
```

This will start the FastAPI server on `http://127.0.0.1:8000`.

## License

This project is licensed under the MIT License - see the LICENSE file for details.