# Updated README.md content

# Student Management Web Application

## Overview

The Student Management Web Application is designed to manage student records efficiently. This document outlines the API endpoints available for creating and retrieving student data.

## API Endpoints

### Create Student

- **Endpoint**: `POST /students`
- **Request Body**:
  - `name` (string, required): The name of the student.
  - `email` (string, required): The email address of the student.
  
- **Response**: 
  - `200 OK`: Returns a JSON object containing created student details.
  - Error Message: If the `name` or `email` is missing, an appropriate error message is returned.

  #### Example Request
  ```json
  {
    "name": "John Doe",
    "email": "john.doe@example.com"
  }
  ```

  #### Example Response
  ```json
  {
    "id": 1,
    "name": "John Doe",
    "email": "john.doe@example.com"
  }
  ```

### Retrieve All Students

- **Endpoint**: `GET /students`
- **Response**: 
  - `200 OK`: Returns a JSON array of all student objects, including their emails.

  #### Example Response
  ```json
  [
    {
      "id": 1,
      "name": "John Doe",
      "email": "john.doe@example.com"
    },
    {
      "id": 2,
      "name": "Jane Smith",
      "email": "jane.smith@example.com"
    }
  ]
  ```

## Database Migration

The SQLite database schema is automatically updated upon migration to include the new `email` field in the `Students` table. This table includes the following columns:
- `id` (auto-incrementing primary key)
- `name` (string, required)
- `email` (string, required)

## User Scenarios & Testing

1. **Create a Student with Email**:
   - **Scenario**: A user submits a name and an email to create a new student record.
   - **Test**: Verify that the API returns a success response and the student record, including the email, is created in the database.

2. **Retrieve All Students with Emails**:
   - **Scenario**: A user requests a list of all student records.
   - **Test**: Ensure that the API returns a JSON response containing all student records, including their emails.

3. **Error Handling for Missing Email**:
   - **Scenario**: A user attempts to create a student without providing an email.
   - **Test**: Confirm that the API returns an appropriate error message indicating that the email field is required.

## Conclusion

This document provides a concise overview of the new functionality added to the Student Management Web Application. The inclusion of an email field enhances data management capabilities and allows better communication with students, meeting modern educational needs.