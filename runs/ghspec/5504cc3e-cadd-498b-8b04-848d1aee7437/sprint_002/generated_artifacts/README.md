# Updated README.md

# Student Registration System

## Overview & Purpose

This project provides a simple API for managing student registrations. Users can register students, update their information, and retrieve a list of all registered students.

## New Features

In this update, we have introduced functionality to include an email field in the student registration system. This enables better contact information management for students.

## User Scenarios & Testing

1. **Student Registration with Email**:
   - As a user, you can now register a student by providing a name and an email address.
   - **Test**: Verify that a valid name and email can be successfully submitted and stored.

2. **Retrieve Student Information with Email**:
   - Users can retrieve a list of all registered students, including their email addresses.
   - **Test**: Verify that the API returns all students with their names and email addresses in JSON format.

3. **Update Student Email**:
   - You can update a student's email address to ensure their contact information is current.
   - **Test**: Verify that updating a student's email successfully changes the stored information.

4. **Email Format Validation**:
   - Users will receive meaningful error messages when trying to register or update a student with an invalid email format.
   - **Test**: Verify that appropriate error messages are returned for invalid email submissions.

5. **Data Preservation During Migration**:
   - Ensure that existing student data is preserved after updating the database schema to include the email field.
   - **Test**: Verify that all previously stored student records remain intact after the migration.

## Functional Requirements

- The Student entity has been updated to include an email field, defined as a required string.
- The application now supports creating a new student entity via an API endpoint that includes the email field.
- Users can retrieve a list of all student entities, returning the name and email addresses via a GET request.
- An API endpoint allows users to update an existing student's email address based on their unique identifier.
- The database schema has been updated to include the email field while ensuring data migration does not disrupt existing records.

## API Endpoints

### Create Student

- **POST /api/students**
- **Request Body**:
    ```json
    {
        "name": "John Doe",
        "email": "john.doe@example.com"
    }
    ```
- **Response**:
    - 201 Created on successful registration.
    - 400 Bad Request for invalid input (e.g., email format).

### Retrieve Students

- **GET /api/students**
- **Response**:
    ```json
    [
        {
            "name": "John Doe",
            "email": "john.doe@example.com"
        },
        ...
    ]
    ```

### Update Student Email

- **PUT /api/students/{id}**
- **Request Body**:
    ```json
    {
        "email": "new.email@example.com"
    }
    ```
- **Response**:
    - 200 OK on successful update.
    - 400 Bad Request for invalid email format.

## Testing

- Ensure to execute the defined tests to verify the integrity of the new functionalities.
- Tests will cover registration, retrieval, updating email addresses, and handling various error scenarios.

This document should aid in navigating the features added to the Student Registration System along with usage instructions for effective interaction with the API.