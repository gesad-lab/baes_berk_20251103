# Updated README.md

# Project Title

## Overview

This project is aimed at managing student records efficiently. It allows users to create, retrieve, and manage students, including their emails for accurate records.

## API Endpoints

### Student Management

- **Create a Student**
  - `POST /students`
  - Request Body:
    ```json
    {
      "name": "John Doe",
      "email": "john.doe@example.com"
    }
    ```
  - Response (201 Created):
    ```json
    {
      "id": 1,
      "name": "John Doe",
      "email": "john.doe@example.com"
    }
    ```

- **Retrieve a Student by ID**
  - `GET /students/{id}`
  - Response (200 OK):
    ```json
    {
      "id": 1,
      "name": "John Doe",
      "email": "john.doe@example.com"
    }
    ```

- **Retrieve All Students**
  - `GET /students`
  - Response (200 OK):
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

## User Scenarios & Testing

1. **Scenario: Create a Student with Email**
   - As a user, I want to create a new student by providing their name and email so that I can maintain accurate records in the system.
   - **Test Steps**:
     1. Send a POST request to `/students` with the student name and email in the request body.
     2. Assert that the response status is 201 Created.
     3. Validate that the response body contains the created student's ID, name, and email.

2. **Scenario: Retrieve a Student with Email**
   - As a user, I want to view the details of a student by their ID, including their email.
   - **Test Steps**:
     1. Send a GET request to `/students/{id}`.
     2. Assert that the response status is 200 OK.
     3. Validate that the response body contains the student's ID, name, and email.

3. **Scenario: Retrieve All Students with Email**
   - As a user, I want to see a list of all students along with their emails to effectively manage student records.
   - **Test Steps**:
     1. Send a GET request to `/students`.
     2. Assert that the response status is 200 OK.
     3. Validate that the response is an array of students, each containing an ID, name, and email.

## Functional Requirements

1. The Student entity shall be updated to include an `email` field:
   - `email`: a required string field.
2. The database schema shall be updated to accommodate the new email field in the existing Student table.
3. A database migration must be implemented to add the email field while preserving existing student data.
4. The following API endpoints shall be updated:
   - `POST /students`: to create a new student, must now accept the email field in the request body.
   - `GET /students/{id}`: to retrieve a student, must now include the email in the response.
   - `GET /students`: to retrieve all students, must now include emails in the response.

## Testing

Ensure to update your unit tests in `test_student.py` to validate the functionality around the email handling in the student management endpoints as described in the scenarios above.