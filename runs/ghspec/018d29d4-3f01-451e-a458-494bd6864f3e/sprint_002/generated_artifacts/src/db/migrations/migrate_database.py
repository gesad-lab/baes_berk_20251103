# Update the README with instructions for the email requirements and example requests.

# README.md

# Student Management Web Application

## Overview & Purpose
The purpose of adding an email field to the existing Student entity is to improve the management capabilities of student records within the Student Management Web Application. By including a required email attribute, we enable better communication and notification options for students, enhancing the overall functionality of the application. This feature is crucial for maintaining updated and contactable student records.

## Functional Requirements
1. The system shall allow the user to create a student entity with the following attributes:
   - **name** (string, required)
   - **email** (string, required, must follow valid email format)

2. The system shall return responses in JSON format for all API requests.

3. The system shall automatically initialize the database schema on startup, ensuring the student table includes the email field.

4. A database migration must preserve existing student data when the email field is added to the Student entity.

5. The system shall handle input validation for the email field and provide meaningful error messages when required fields are not provided or are incorrectly formatted.

## API Endpoints

### Create Student
- **POST** `/students`
- **Request Body**:
  ```json
  {
    "name": "John Doe",
    "email": "john.doe@example.com"
  }
  ```
- **Response**:
  - **201 Created**: If the student is created successfully.
  - **400 Bad Request**: If the email format is invalid or if fields are missing.

### Example Requests

1. **Create Student Record with Email**:
   ```bash
   curl -X POST "http://localhost:8000/students" -H "Content-Type: application/json" -d '{"name": "Test Student", "email": "test@example.com"}'
   ```

2. **Create Student Record Without Email**:
   ```bash
   curl -X POST "http://localhost:8000/students" -H "Content-Type: application/json" -d '{"name": "Test Student"}'
   ```
   - **Expected Response**:
   ```json
   {
     "error": {
       "code": "E001",
       "message": "Email field is required."
     }
   }
   ```

3. **Create Student Record with Invalid Email Format**:
   ```bash
   curl -X POST "http://localhost:8000/students" -H "Content-Type: application/json" -d '{"name": "Test Student", "email": "invalid-email"}'
   ```
   - **Expected Response**:
   ```json
   {
     "error": {
       "code": "E002",
       "message": "Email format is invalid."
     }
   }
   ```

## User Scenarios & Testing
1. **Create Student Record with Email**: A user should be able to send a request to create a new student and include an email address.
   - Given a valid name and email, when the user submits the creation request, a new student record should be created successfully.

2. **Retrieve Student Record with Email**: A user should be able to fetch a student record and see the email address associated with the student.
   - Given an existing student ID, when the user requests the student, the relevant details, including name and email, should be returned.

3. **Invalid Student Record Creation Without Email**: A user attempts to create a student record without providing an email address.
   - The system should return a clear error message indicating the email field is required.

4. **Invalid Student Record Creation with Invalid Email Format**: A user attempts to create a student record providing an email in an invalid format.
   - The system should return a clear error message stating the email format is invalid.

## Database Initialization
The application will ensure the student table is updated on startup using SQLAlchemy migrations to include the new email field without losing existing data.