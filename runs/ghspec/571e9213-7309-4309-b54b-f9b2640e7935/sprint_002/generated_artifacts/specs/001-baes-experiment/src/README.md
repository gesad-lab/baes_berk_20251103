# README.md

# Project Title

This project is an API for managing a student database with functionality to create and retrieve students along with their relevant information, including email addresses.

## Overview

The API allows administrators to create and manage student records. The student information includes fields such as name and email, ensuring comprehensive record-keeping and data integrity.

## API Endpoints

### 1. Creating a Student
- **POST /students**
  - **Description**: Adds a new student record.
  - **Request Body**: 
    ```json
    {
      "name": "string", // Required: The name of the student
      "email": "string" // Required: The email of the student (must be a valid email format)
    }
    ```
  - **Response**: 
    - **Status 201**: Success
      ```json
      {
        "id": "integer",   // The unique identifier for the created student
        "name": "string",  // Name of the student
        "email": "string"  // Email of the student
      }
      ```
  - **Error Responses**:
    - **400 Bad Request**: If the email field is missing or not properly formatted.
      ```json
      {
        "error": {
          "code": "E001",
          "message": "The email field is required and must be properly formatted."
        }
      }
      ```

### 2. Retrieving a Student
- **GET /students/{id}**
  - **Description**: Retrieves details for a specific student by their unique ID.
  - **Response**:
    - **Status 200**: Success
      ```json
      {
        "id": "integer",   // The unique identifier of the student
        "name": "string",  // Name of the student
        "email": "string"  // Email of the student
      }
      ``` 

### Email Field Validation
To ensure data integrity when creating a student, the email field must:
- Be provided.
- Follow a valid email format.

If these conditions are not met, an appropriate error message will be returned. 

## User Scenarios & Testing
1. **Creating a Student with Email**:
   - Test the endpoint by sending a POST request with valid name and email to the `/students` endpoint. Expect a success response that includes the student data (ID, name, email).

2. **Retrieving a Student with Email**:
   - Test the endpoint by sending a GET request to the `/students/{id}` endpoint for an existing student and expect a valid student record in response that includes the email field.

3. **Validation of Email Format**:
   - Attempt to create a student without a valid email format. Expect an error response indicating the email field is required and must be properly formatted.

4. **Validation of Missing Email**:
   - Attempt to create a student without an email. Expect an error response stating that the email field is required.

## Setup Instructions
- Clone the repository.
- Install the required dependencies.
- Set up the database using the provided migration scripts.
- Run the application with FastAPI for local testing.

## Project Structure
- `src/`: Application source code  
  - `main.py`: Entry point of the FastAPI application  
  - `models/`: Database models (including updated student model)  
  - `schemas/`: Pydantic models for request/response validation  
  - `routes/`: API endpoints for handling HTTP requests  
  - `database/`: Database connection and setup  
- `tests/`: Test files  
- `README.md`: Setup and documentation  