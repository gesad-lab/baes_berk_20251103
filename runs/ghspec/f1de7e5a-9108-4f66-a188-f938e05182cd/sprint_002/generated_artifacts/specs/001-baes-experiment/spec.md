# Feature: Add Email Field to Student Entity

## Overview & Purpose
The purpose of this feature is to extend the existing `Student` entity by adding an email field to it. This addition allows for the collection of email addresses for each student, enabling future communication or notifications. It is essential for enhancing the functionality of the Student Management Web Application while ensuring data integrity and continuity of existing student records.

## User Scenarios & Testing
1. **Create a Student with Email**:
   - As a user, I want to create a new student entry by providing a name and an email so that I can store their contact information.
   - Test: Validate that a POST request to the API successfully creates a student with a valid name and email.

2. **Retrieve Students with Email**:
   - As a user, I want to retrieve a list of all students, including their emails, to view existing entries along with contact information.
   - Test: Validate that a GET request returns a list of students in JSON format, including their email addresses.

3. **Email Validation**:
   - As a user, I want to be informed if I provide an invalid email address (e.g., incorrectly formatted) while creating a student.
   - Test: Validate that the application returns a clear error message when attempting to create a student with an invalid email format.

## Functional Requirements
1. The application must provide an updated API endpoint to create a student:
   - **Endpoint**: `/students` (POST)
   - **Request Body**:
     ```json
     {
         "name": "<string>",
         "email": "<string>"
     }
     ```
   - **Response**:
     - Status code 201 (Created) with the created student object, including both name and email attributes.

2. The application must provide an updated API endpoint to retrieve all students:
   - **Endpoint**: `/students` (GET)
   - **Response**:
     - Status code 200 (OK) with a JSON array of student objects, including their email addresses.

3. The application must validate the input data:
   - The `name` field must be a non-empty string.
   - The `email` field must be a valid email format. The application must return a status code 400 (Bad Request) if the validation fails for either field, along with an error message.

4. The SQLite database schema must be updated to include the email field:
   - **Table Name**: `students`
   - **New Field**:
     - `email` (text, unique, not NULL)

5. A database migration must be created to add the email field while preserving existing Student data.

## Success Criteria
1. Users can create a new student entry with both a name and an email address, receiving a 201 status code along with the student data in the response.
2. Users can retrieve all student entries, and the response includes a valid JSON array of student objects, with email addresses included.
3. Input validation works correctly, returning a 400 status code with a descriptive error message when invalid input (empty name or invalid email) is provided.
4. The application starts without errors, and the SQLite database is correctly updated with the new schema, maintaining existing data integrity.

## Key Entities
- **Student**:
  - Attributes:
    - `id`: Integer (auto-increment, primary key)
    - `name`: String (required, cannot be null)
    - `email`: String (required, must be a valid email format)

## Assumptions
- The web application will continue to be deployed in an environment that supports Python 3.11+ in line with the previous sprint.
- SQLite will still function as a suitable database for this application due to its lightweight nature and ease of handling migrations.

## Out of Scope
- User authentication or authorization will not be addressed in this iteration.
- Changes to the frontend user interface are outside the scope; this feature focuses solely on the backend API functionality and the associated `Student` entity enhancements.
- More complex business logic related to email communications or processing beyond basic email storage will not be included.