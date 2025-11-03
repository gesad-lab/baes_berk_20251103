# README.md

# Student Management API

This API allows the management of student records in a simple, RESTful manner. You can create, retrieve, update, and delete student records.

## API Endpoints

### 1. Create Student
- **Endpoint**: `POST /students`
- **Request Body**:
  ```json
  {
    "name": "string"
  }
  ```
- **Responses**:
  - **201 Created**: 
    ```json
    {
      "id": integer,
      "name": "string"
    }
    ```
  - **400 Bad Request**: If `name` is missing.

### 2. Retrieve Student
- **Endpoint**: `GET /students/{student_id}`
- **Responses**:
  - **200 OK**: 
    ```json
    {
      "id": integer,
      "name": "string"
    }
    ```
  - **404 Not Found**: If the `student_id` does not exist.

### 3. Update Student
- **Endpoint**: `PUT /students/{student_id}`
- **Request Body**:
  ```json
  {
    "name": "string"
  }
  ```
- **Responses**:
  - **200 OK**: 
    ```json
    {
      "id": integer,
      "name": "string"
    }
    ```
  - **404 Not Found**: If the `student_id` does not exist.
  - **400 Bad Request**: If `name` is missing.

### 4. Delete Student
- **Endpoint**: `DELETE /students/{student_id}`
- **Responses**:
  - **204 No Content**: On successful deletion.
  - **404 Not Found**: If the `student_id` does not exist.

## Database Schema
The application will automatically create the necessary schema for the Student entity upon the startup of the application.