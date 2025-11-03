# README.md

# Student Management API

This API allows managing student records, including creating, retrieving, and listing students.

## New Features

### Email Field Addition

The API has been updated to include an additional `email` field for student records. Below are the features related to this field:

1. **Create Student with Email**:
   - The API now supports creating a student record with a mandatory `email` field.
   - The email must be a valid string and is required for all new student records.

   #### Example Request
   ```http
   POST /api/v1/students
   Content-Type: application/json

   {
       "name": "John Doe",
       "email": "john@example.com"
   }
   ```

   #### Example Response
   ```http
   HTTP/1.1 201 Created
   Content-Type: application/json

   {
       "id": 1,
       "name": "John Doe",
       "email": "john@example.com"
   }
   ```

2. **Get Student by ID**:
   - The response for retrieving a student by their ID now includes the `email` field alongside the student's name and ID.

   #### Example Request
   ```http
   GET /api/v1/students/1
   ```

   #### Example Response
   ```http
   HTTP/1.1 200 OK
   Content-Type: application/json

   {
       "id": 1,
       "name": "John Doe",
       "email": "john@example.com"
   }
   ```

3. **List All Students**:
   - When listing all student records, the response will now include the `email` field for each student in the JSON array.

   #### Example Request
   ```http
   GET /api/v1/students
   ```

   #### Example Response
   ```http
   HTTP/1.1 200 OK
   Content-Type: application/json

   [
       {
           "id": 1,
           "name": "John Doe",
           "email": "john@example.com"
       },
       {
           "id": 2,
           "name": "Jane Smith",
           "email": "jane@example.com"
       }
   ]
   ```

### Database Schema Update
- The student records in the database now include an `email` column. A migration script has been implemented to add this new column while preserving existing data.

### Validation
- Input validation for the `email` field ensures that the format is correct. Invalid email submissions will return appropriate error responses.

## API Documentation
For further details on how to interact with the API, refer to the [API Documentation](#).

## Installation
1. Clone the repository.
2. Install the required dependencies from `requirements.txt`.
3. Run the application on your local server.

This README file will continue to be updated as new features are added or existing functionality is changed.