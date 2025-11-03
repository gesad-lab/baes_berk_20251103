# README.md

# Student Management API

This is the documentation for the Student Management API, a service to manage student records, including creation, retrieval, and updating of students.

## Functional Requirements

### 1. Create Student
- **Endpoint**: `POST /students/`
- **Description**: This endpoint creates a new student.
- **Request Body**:
  ```json
  {
    "name": "string",
    "email": "string"
  }
  ```
- **Response**: 
  - **201 Created**: Returns the created student's details:
    ```json
    {
      "id": "integer",
      "name": "string",
      "email": "string"
    }
    ```

### 2. Retrieve Student
- **Endpoint**: `GET /students/{id}`
- **Description**: Retrieves student details by ID.
- **Response**: 
  - **200 OK**: Returns the student data including the email field:
    ```json
    {
      "id": "integer",
      "name": "string",
      "email": "string"
    }
    ```
  - **404 Not Found**: If the student is not found.

### 3. Update Student's Email
- **Endpoint**: `PUT /students/{id}/email`
- **Description**: Updates a student's email by ID.
- **Request Body**:
  ```json
  {
    "email": "string"
  }
  ```
- **Response**:
  - **200 OK**: Returns the updated student data:
    ```json
    {
      "id": "integer",
      "name": "string",
      "email": "string"
    }
    ```
  - **404 Not Found**: If the student does not exist.

### 4. Delete Student
- **Endpoint**: `DELETE /students/{id}`
- **Description**: Deletes a student by ID.
- **Response**:
  - **200 OK**: Returns a confirmation message.
  - **404 Not Found**: If the student is not found.

## Database Schema
- The Student entity now includes a new column:
  - `email`: String, Required.

## Database Migration
- The migration process ensures that existing student data is preserved while introducing the new "email" field.

## JSON Response Format
- All API responses continue to be in JSON format with appropriate HTTP status codes.