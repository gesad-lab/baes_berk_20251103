# Feature: Add Email Field to Student Entity

## Overview & Purpose
The purpose of this feature is to extend the existing "Student" entity by adding an email field, allowing for better communication and record-keeping of student-related information. This enhancement will allow the web application to store and manage student email addresses alongside their names. With this new functionality, the application aims to improve the usability and effectiveness of student record management.

## User Scenarios & Testing
1. **Creating a Student with Email**:
   - As a user, I want to add a new student by submitting a name and an email address, so that I can keep track of student records along with their contact information.
   - **Test Case**: Submit valid name and email, then verify the response contains the created student's details, including the email.

2. **Retrieving Student Information with Email**:
   - As a user, I want to retrieve a list of all students, ensuring the email field is included in the response.
   - **Test Case**: Request the list of students and verify that the returned data contains `id`, `name`, and `email` for each student.

3. **Handling Invalid Email Inputs**:
   - As a user, I want to receive clear error messages when submitting an invalid email address, so that I understand the corrective action required.
   - **Test Case**: Submit a request with valid name but an invalid email and verify an appropriate error message is returned.

## Functional Requirements
1. **Create Student**:
   - Endpoint: `POST /students`
   - Request Body: 
     - `name`: required string (minimum length of 1 character)
     - `email`: required string (must fit valid email format)
   - Response: 
     - On Success (201 Created): Return a JSON object containing the created student's `id`, `name`, and `email`.
     - On Error (400 Bad Request): Return an error message if name or email is missing or invalid.

2. **Retrieve Students**:
   - Endpoint: `GET /students`
   - Response:
     - On Success (200 OK): Return a JSON array of student objects containing `id`, `name`, and `email`.

3. **Database Schema Update**:
   - Update the existing database schema to include the new `email` field in the "Student" entity while preserving existing student records.
   - Ensure that the database migration is designed to handle the addition of the email field without data loss.

## Success Criteria
- Adding a student record requires valid name and email, and returns a 201 status with the correct data.
- Retrieval of students correctly returns a 200 status with a complete list of students, including their emails.
- Submitting invalid email results in a clear 400 error with a descriptive message.
- Database schema is updated successfully to include the `email` field without losing existing data during migration.

## Key Entities
- **Student**:
  - `id`: unique identifier (integer, primary key, auto-incremented)
  - `name`: required field (string)
  - `email`: required field (string, must fit valid email format)

## Assumptions
- The existing SQLite database has the necessary structure to accommodate the new `email` field without conflicts.
- Users will provide correctly formatted email addresses for consistency in data entry.
- The application will continue to maintain separation of concerns and utilize standard practices from the previous sprint.

## Out of Scope
- User authentication or authorization related to email usage.
- Features for sending emails or notifications based on the email field.
- Changes to frontend interfaces; this feature solely focuses on backend updates.