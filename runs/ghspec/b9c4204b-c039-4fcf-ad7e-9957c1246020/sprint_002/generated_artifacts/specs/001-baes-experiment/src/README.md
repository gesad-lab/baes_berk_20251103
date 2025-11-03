# README.md

---
# Project Overview

This project allows users to manage student entities, including creating and retrieving student information using RESTful API endpoints. Below are the functional requirements and response structure for these endpoints.

## Functional Requirements

1. **Create Student Entity with Email**
   - The application provides an endpoint for creating a new student that accepts a JSON payload with required fields: `name` (string) and `email` (string).
   - Upon successful creation, it returns a JSON response containing the created student data, including both name and email.

   ### Create Student Endpoint
   - **Request**: `POST /students`
     ```json
     {
       "name": "John Doe",
       "email": "john.doe@example.com"
     }
     ```
   - **Response (Success)**: `201 Created`
     ```json
     {
       "id": 1,
       "name": "John Doe",
       "email": "john.doe@example.com"
     }
     ```
   - **Response (Error)**: `400 Bad Request`
     ```json
     {
       "error": {
         "code": "E001",
         "message": "The email field is required."
       }
     }
     ```

2. **List Students with Email**
   - The application provides an endpoint for retrieving a list of all students.
   - The endpoint returns a JSON array of student entities that include their names and emails.

   ### Retrieve Students Endpoint
   - **Request**: `GET /students`
   - **Response (Success)**: `200 OK`
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

1. **Scenario: Create a new student with email**
   - **Given** a user sends a request to add a new student with valid name and email,
   - **When** the request is processed,
   - **Then** a new student entity is created in the database with both name and email, and a successful confirmation response with the student data is returned.

2. **Scenario: Retrieve student list including email**
   - **Given** a user sends a request to retrieve all students,
   - **When** the request is processed,
   - **Then** a list of all student entities including their names and emails in JSON format is returned.

3. **Scenario: Handle missing email when creating a student**
   - **Given** a user sends a request to add a new student with a valid name but without an email,
   - **When** the request is processed,
   - **Then** an error response indicating that the email field is required is returned.

4. **Scenario: Update existing student**
   - **Given** a user sends a request to update an existing student’s email,
   - **When** the request is processed,
   - **Then** the student's email is updated in the database, and a successful confirmation response with the updated student data is returned.

## JSON Response Structure Validation

It is crucial to validate the structure of JSON responses across all endpoints. The validation checks will ensure that the following criteria are met:

- Successful responses must include the necessary fields as specified in the functional requirements (e.g., `id`, `name`, `email` for students).
- Error responses must include an `error` object with `code` and `message` fields for consistency and clarity.
- All responses must adhere to the expected JSON format defined in the functional requirements.

This validation will help ensure API consistency and provide users with clear and actionable information regarding their requests.