# API Documentation

This document outlines the available API endpoints for the Student Module of our Flask application.

## Base URL
The base URL for all endpoints is:
```
http://localhost:5000
```

## Endpoints

### 1. Create a New Student
- **Method**: `POST`
- **Endpoint**: `/students`
- **Description**: This endpoint creates a new student with the provided input data.
- **Request Body**:
  ```json
  {
    "name": "string",
    "age": "integer",
    "email": "string"
  }
  ```
  - `name`: The name of the student (required).
  - `age`: The age of the student (required).
  - `email`: The email address of the student (required, must be a valid email format).
  
- **Response**:
  - **201 Created**: If the student is successfully created.
    ```json
    {
      "id": "string",
      "name": "string",
      "age": "integer",
      "email": "string"
    }
    ```
  - **400 Bad Request**: If the input data is invalid.
    ```json
    {
      "error": {
        "code": "E001",
        "message": "Invalid input data"
      }
    }
    ```
  
### 2. Retrieve Student Information by ID
- **Method**: `GET`
- **Endpoint**: `/students/{id}`
- **Description**: This endpoint retrieves information about a student by their unique ID.
- **Path Parameters**:
  - `id`: The unique identifier for the student (required).
  
- **Response**:
  - **200 OK**: If the student is found.
    ```json
    {
      "id": "string",
      "name": "string",
      "age": "integer",
      "email": "string"
    }
    ```
  - **404 Not Found**: If no student is found with the provided ID.
    ```json
    {
      "error": {
        "code": "E002",
        "message": "Student not found"
      }
    }
    ```

## Local Deployment Instructions
To run the application locally:
1. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Create a `.env` file based on the `.env.example` file, filling in the necessary environment variables.
3. Run the application:
   ```bash
   flask run
   ```
4. Access the API at `http://localhost:5000`.

## Conclusion
This documentation provides the necessary details for the current API endpoints related to student management. For further information or updates, please refer to the project resources or contact the development team.