# README.md

# Project Title

## Overview
This project is a RESTful API for managing students and courses using FastAPI and SQLite. The application allows for the creation, retrieval, and validation of student information including their name and email, as well as course information related to the academic offerings.

## Functional Requirements

### Student Management

1. **Create Student**:
   - **Endpoint**: `POST /students`
   - **Request Body**: 
     ```json
     {
       "name": "string",  // required
       "email": "string"  // required
     }
     ```
   - **Response**: 
     ```json
     {
       "id": "integer",
       "name": "string",
       "email": "string"
     }
     ```

### Course Management

1. **Create Course**:
   - **Endpoint**: `POST /courses`
   - **Request Body**: 
     ```json
     {
       "name": "string",  // required
       "level": "string"  // required
     }
     ```
   - **Response**: 
     ```json
     {
       "id": "integer",
       "name": "string",
       "level": "string"
     }
     ```
   - **Testing**: Verify that a POST request to the `/courses` endpoint with the name and level in the request body successfully creates a new course and returns a success message along with the course's ID.

2. **Retrieve Course Information**:
   - **Endpoint**: `GET /courses/{id}`
   - **Response**: 
     ```json
     {
       "id": "integer",
       "name": "string",
       "level": "string"
     }
     ```
   - **Testing**: Verify that a GET request to the `/courses/{id}` endpoint returns the expected course details, including its name and level.

3. **Error Handling for Missing Course Fields**:
   - **Endpoint**: `POST /courses`
   - **Testing**: Verify that a POST request to the `/courses` endpoint without either the name or level results in a 400 Bad Request status and an error message indicating which field is required.

## User Scenarios & Testing

1. **User Story 1: Create a Course**
   - As an admin, I want to add a new course by providing its name and level, so that I can organize the courses available to students.

2. **User Story 2: Retrieve Course Information**
   - As an admin, I want to view the details of a specific course, including its name and level, so that I can ensure accurate course records are maintained. 

3. **User Story 3: Error Handling for Missing Course Fields**
   - As a user, I want to receive informative error messages when I attempt to create a course without providing a name or level, as both fields are required. 

## Development Phases
1. **Setup Project Environment**:
   - Initialize a new Git repository.
   - Use Poetry to manage dependencies and add required libraries.

2. **Implement Database Updates**:
   - Create the `Course` model with name and level fields.
   - Implement database migration to create the `courses` table.

3. **Modify API Layer**:
   - Define new POST and GET endpoints in the FastAPI application.
   - Incorporate input validation for creating courses.

4. **Service Layer Development**:
   - Implement service functions to create and retrieve courses.
   - Ensure error handling for validation scenarios.

5. **Testing**:
   - Use Pytest to add unit and integration tests for the course functionalities.
   - Ensure test coverage meets the target of 70% for business logic.

6. **Documentation**:
   - Update this README with the new API endpoint details.
   - Ensure all code is adequately documented with comments and docstrings.