# README.md

# Student Management API

This API allows users to manage student records, including creating new students and retrieving existing student information.

## API Documentation

### Creating a Student with Email

- **Endpoint**: `POST /students`
- **Request Body**: 
  ```json
  {
    "name": "John Doe",
    "email": "john.doe@example.com"
  }
  ```
- **Expected Result**: 
  A new student entity is created in the database with both name and email.
  
- **Response**:
  ```json
  {
    "message": "Student created successfully",
    "student": {
      "name": "John Doe",
      "email": "john.doe@example.com"
    }
  }
  ```

### Retrieving all Students with Emails

- **Endpoint**: `GET /students`
- **Expected Result**: 
  A JSON response containing a list of all student entities, including their names and emails.
  
- **Response**:
  ```json
  [
    {
      "name": "John Doe",
      "email": "john.doe@example.com"
    },
    {
      "name": "Jane Smith",
      "email": "jane.smith@example.com"
    }
  ]
  ```

### Handling Invalid Email Input

- **Endpoint**: `POST /students`
- **Request Body**: 
  ```json
  {
    "name": "John Doe",
    "email": "invalid-email-format"
  }
  ```
- **Expected Result**: 
  An error message is returned indicating that the email field must be a valid email address.
  
- **Response**:
  ```json
  {
    "error": {
      "code": "E001",
      "message": "The email field must be a valid email address."
    }
  }
  ```

### Handling Missing Email

- **Endpoint**: `POST /students`
- **Request Body**: 
  ```json
  {
    "name": "John Doe"
  }
  ```
- **Expected Result**: 
  An error message is returned indicating that the email field is required.
  
- **Response**:
  ```json
  {
    "error": {
      "code": "E002",
      "message": "The email field is required."
    }
  }
  ```

## Database Schema

The application uses an SQLite database to store student records. Each student record includes:

- `name`: string (required)
- `email`: string (required)

## Running the Application

To run the application, ensure you have the necessary dependencies installed. Please refer to the `requirements.txt` for the list of dependencies.

1. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

2. Start the application:
   ```bash
   python main.py
   ```

Ensure the SQLite database is set up correctly and migrations are applied to handle the new `email` field.