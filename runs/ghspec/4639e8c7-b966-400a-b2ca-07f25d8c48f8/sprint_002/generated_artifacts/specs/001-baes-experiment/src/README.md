# Updated README.md file to include new API specifications

# README.md

## Project Title

Student Management System

## Introduction

This project is a Student Management System built using Flask. The system allows administrators to manage student records, including creating, updating, retrieving, and validating student information.

## API Specifications

### 1. Create a New Student Record

- **Endpoint**: `POST /students`
- **Request Body**:
  ```json
  {
    "name": "John Doe",
    "email": "john.doe@example.com"
  }
  ```
- **Response**:
  - **201 Created**: Returns the created student record.
  - **400 Bad Request**: Returns an error if the email is missing or invalid.

### 2. Retrieve All Student Records

- **Endpoint**: `GET /students`
- **Response**:
  - **200 OK**: Returns a list of all students in JSON format, including the email field.
  ```json
  [
    {
      "id": 1,
      "name": "John Doe",
      "email": "john.doe@example.com"
    },
    ...
  ]
  ```

### 3. Error Handling for Invalid Email

- **Endpoints**: Applies to `POST /students`
- **Error Response**:
  - **400 Bad Request**: When an invalid email is provided (e.g., empty string or incorrectly formatted).
  ```json
  {
    "error": {
      "code": "E001",
      "message": "Invalid email format.",
      "details": {
        "email": "This field cannot be empty or must be a valid email."
      }
    }
  }
  ```

### 4. Update an Existing Student Record

- **Endpoint**: `PUT /students/<id>`
- **Request Body**:
  ```json
  {
    "name": "John Doe",
    "email": "john.doe@example.com"
  }
  ```
- **Response**:
  - **200 OK**: Returns the updated student record.
  - **400 Bad Request**: Returns an error if the email is invalid.

## User Scenarios & Testing

1. **As an Admin User**, I want to create a new student record with an email address so that I can store complete student information.
   - Test: Verify that I can submit a name and email address and successfully create a student record.

2. **As an Admin User**, I want to retrieve a list of all student records, including their email addresses, so that I can view complete existing data.
   - Test: Ensure that all student records returned in a JSON format now include the email field.

3. **As an Admin User**, I want to handle cases where I input invalid email data to ensure the application responds appropriately.
   - Test: Submit an empty email field or incorrectly formatted email and confirm that an error message is returned.

4. **As an Admin User**, I want to update an existing student record to add or change an email address so that I can maintain accurate student information.
   - Test: Verify that I can successfully update the email address for an existing student record.

## Database Schema Update

- The Student entity must now include an email field, which is required and must be a string type.
- A proper database migration must be implemented to ensure the schema updates without affecting existing student records.

## Installation

- Clone the repository and navigate to the project folder.
- Install the required dependencies with:
  ```bash
  pip install -r requirements.txt
  ```
- Run the application with:
  ```bash
  python src/app.py
  ```

## License

- This project is licensed under the MIT License. See the LICENSE file for details.