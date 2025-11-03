# README.md

# Project Title

## Overview
This project provides an application for managing student records, enhancing interaction with students by now including their email addresses.

## API Endpoints

### 1. Create a Student
- **Endpoint**: `POST /students`
- **Request Body**:
  ```json
  {
    "name": "string",
    "email": "string"
  }
  ```
- **Success Response**:
  - **Code**: 201 CREATED
  - **Content**:
  ```json
  {
    "message": "Student created",
    "student": {
      "id": integer,
      "name": "string",
      "email": "string"
    }
  }
  ```
  
- **Error Response**:
  - **Code**: 400 BAD REQUEST
  - **Content**:
  ```json
  {
    "error": {
      "code": "E001",
      "message": "Email is required"
    }
  }
  ```

### 2. Retrieve a Student
- **Endpoint**: `GET /students/{id}`
- **Success Response**:
  - **Code**: 200 OK
  - **Content**:
  ```json
  {
    "id": integer,
    "name": "string",
    "email": "string"
  }
  ```
  
- **Error Response**:
  - **Code**: 404 NOT FOUND
  - **Content**:
  ```json
  {
    "error": {
      "code": "E002",
      "message": "Student not found"
    }
  }
  ```

## Error Handling
1. If a user submits a request to create a student without an email, the server will respond with an appropriate error message indicating that the email is required.

## Database Migration
- Upon starting the application after this feature implementation, the database schema will be automatically updated to include the `email` field in the Student entity while preserving existing data.

## Future Considerations
- Future improvements may include managing notifications for students based on their email and implementing user authentication and authorization for enhanced user management. 

## Testing
Ensure to write unit tests for the functionalities, particularly focusing on the creation and retrieval of student records, including handling error cases.

Feel free to reach out for clarification or further information regarding the implementation and usage of the API endpoints.