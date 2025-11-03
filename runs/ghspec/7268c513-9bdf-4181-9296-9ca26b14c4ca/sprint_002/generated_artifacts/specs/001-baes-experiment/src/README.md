# Updated README.md

# Student Management System

## Overview
This application is a simple student management system that allows users to create and retrieve student records. In this update, we have added support for an email field for each student.

## API Endpoints

### 1. Create a New Student
- **Endpoint**: `POST /students`
- **Request Body**: 
  ```json
  {
    "name": "string",
    "email": "string"
  }
  ```
  - **Fields**:
    - `name`: (required) The name of the student.
    - `email`: (required) The email address of the student.

- **Responses**:
  - `201 Created`:
    ```json
    {
      "name": "string",
      "email": "string"
    }
    ```
    - The response will include the details of the created student.
  
  - `400 Bad Request`:
    ```json
    {
      "error": {
        "code": "E001",
        "message": "Email is required."
      }
    }
    ```
    - This response occurs if either the `name` or `email` field is missing from the request.

### 2. Get All Students
- **Endpoint**: `GET /students`
- **Responses**:
  - `200 OK`:
    ```json
    [
      {
        "name": "string",
        "email": "string"
      },
      ...
    ]
    ```
    - A JSON array of student records, where each record contains both the `name` and `email` fields.

## Error Handling
Any request with missing required fields will return an error message in the structured JSON format mentioned above.

## Database Migration
The application includes a migration step that updates the existing `students` table to add the new `email` column while preserving existing data.

## Setup Instructions
Follow the instructions below to set up your development environment:

1. Clone the repository:
   ```
   git clone <repository-url>
   cd <repository-directory>
   ```

2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Run database migrations:
   ```
   flask db upgrade
   ```

4. Start the application:
   ```
   flask run
   ```

## User Scenarios & Testing
- **User Story 1**: As an admin, I want to create a new student entry with a name and an email so that a record is accurately stored.
- **User Story 2**: As an admin, I want to retrieve student data to verify the email addresses were stored correctly.
- **User Story 3**: As an admin, I want to receive an error message when I attempt to create a student with an empty email.

This update aims to enhance the student management capabilities of the application by incorporating email addresses for communication and tracking purposes.