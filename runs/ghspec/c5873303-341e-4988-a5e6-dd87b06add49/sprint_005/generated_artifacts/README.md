# README.md

# Educational Management System

## Overview

This project is designed to manage educational institutions, including functionality for managing students, courses, and now teachers. The application provides a RESTful API for convenient access to various resources.

## API Endpoints

### Teacher Endpoints

#### 1. Create Teacher

- **Endpoint**: `POST /teachers`
- **Request Body**:
  ```json
  {
      "name": "John Doe",
      "email": "john.doe@example.com"
  }
  ```
  - `name`: (string, required) The name of the teacher.
  - `email`: (string, required) The email of the teacher.

- **Expected Response**:
  ```json
  {
      "message": "Teacher created successfully",
      "teacher": {
          "id": 1,
          "name": "John Doe",
          "email": "john.doe@example.com"
      }
  }
  ```
  
#### 2. Retrieve Teachers

- **Endpoint**: `GET /teachers`
  
- **Expected Response**:
  ```json
  [
      {
          "name": "John Doe",
          "email": "john.doe@example.com"
      },
      {
          "name": "Jane Doe",
          "email": "jane.doe@example.com"
      }
  ]
  ```

## Database Schema

### Teachers Table

- A new table named `teachers` has been created with the following structure:
  - `id`: Unique identifier for the teacher (auto-generated).
  - `name`: Teacher's name (string, required).
  - `email`: Teacher's email (string, required, unique).

## Migration

A migration script has been implemented to introduce the `teachers` table while preserving existing records of Student and Course entities.

## User Scenarios & Testing

### Scenario 1: Create a New Teacher
- **Test**: When an admin submits valid teacher information, verify that the teacher is successfully created in the database.

### Scenario 2: Retrieve Teacher Information
- **Test**: Ensure that querying the list of teachers returns a response containing the correct names and emails of all teachers.

### Scenario 3: Handle Invalid Teacher Creation
- **Test**: Ensure appropriate error messages are returned when required fields are missing during teacher creation.

## How to Run the Application

1. Install the required dependencies from `requirements.txt`.
2. Run the application using your preferred method (e.g., uvicorn).
3. Access the documentation at `/docs` for further details on available endpoints.

## Conclusion

This README provides an overview of the new teacher functionality within the Educational Management System, enabling effective management of educators alongside students and courses.