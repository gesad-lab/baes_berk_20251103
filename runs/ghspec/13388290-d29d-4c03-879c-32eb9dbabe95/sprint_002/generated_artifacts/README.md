# README.md

# Project Title

## Overview & Purpose

The purpose of this feature update is to enhance the existing Student entity by adding an email field. Incorporating an email attribute will allow for improved contact management and communication with students. This feature maintains the current functionality while expanding the data structure, thereby delivering added value to users needing to manage student records effectively.

## Setup

To set up the project, you need to follow the established environment configuration, including setting up the database. Please ensure you have the following requirements:

1. **Required Environment Variables**: 
   - DATABASE_URL: URL for the database used by the application.
   - Other environment-specific configurations as necessary.

2. **Database Migration**: 
   - Ensure that the `students` table includes the newly required `email` field. The updated schema should reflect:
     - **Table**: students
       - **Columns**:
         - `id`: INTEGER PRIMARY KEY AUTOINCREMENT
         - `name`: TEXT NOT NULL
         - `email`: TEXT NOT NULL

3. **Email Field Requirement**:
   - The email field is now a required field for creating a Student entity. When using the API to create a student, you must include a valid email in the request payload.
   - A user trying to create a student without an email will receive an error indicating this is a required field.

## API Endpoints

The following endpoints are available for student management:

- **POST /students**: Create a new student record with name and email.
- **GET /students/{id}**: Retrieve a student record by ID, including email.

## Success Criteria

- The database schema includes the email field after the migration and starts without errors.
- A user can successfully create a student record with a valid name and email.
- Attempting to create a student without an email results in a clear error response indicating the requirement.
- A user can retrieve an existing student record and confirm the accuracy of both the name and email data returned.
- The migration process successfully preserves all existing student records during the update.

## Running Tests

To ensure everything is functioning as expected, run the test suite:

```bash
pytest tests/
```

This will execute all tests, including those to validate the new email field functionality.

## Conclusion

With this update, students can be managed more effectively through the application with the addition of the email field, thereby enhancing communication capabilities.