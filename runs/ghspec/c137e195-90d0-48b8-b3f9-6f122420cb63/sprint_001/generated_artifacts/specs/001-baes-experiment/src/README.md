# README.md

# Student Entity Management Web Application

## Overview & Purpose
The goal of this feature is to create a web application that allows for the management of a Student entity. Each Student will have a required name field. This application will serve as a foundational system for storing, retrieving, and managing student data, providing a simple and efficient user experience. The web application will be built using best practices for structuring a Python web application and will utilize a SQLite database for data persistence.

## API Endpoints

### Students API
- `POST /api/students`: Create a new student.
  - **Request Body**: 
    ```json
    {
      "name": "string"
    }
    ```
  - **Responses**:
    - `201 Created`: Student successfully created.
    - `400 Bad Request`: Missing required fields or invalid data.

- `GET /api/students`: Retrieve all students.
  - **Responses**:
    - `200 OK`: Array of students in JSON format.

## Testing Strategy
- **Unit Tests** using pytest to verify individual components.
- **Integration Tests** to ensure correct interactions between components, especially for API endpoints.
- Testing the following scenarios:
    - Creating a student with valid/invalid data.
    - Retrieving all students and verifying the output format.
    - Error handling for missing name fields.

## Project Structure
```
src/
    ├── api/
    │   └── students.py           # Contains endpoints for student management
    ├── models/
    │   └── student.py            # Defines the Student model
    ├── database/
    │   └── db.py                 # Database connection and initialization
    ├── error_handlers/
    │   └── error_responses.py     # Centralized error handling
    └── main.py                   # Application entry point
tests/
    ├── test_students.py           # Tests for student API endpoints
```

## Installation
1. Clone the repository.
2. Install required packages using `pip install -r requirements.txt`.
3. Set up the database with the initial schema.

## Run the Application
- Use the command `python src/main.py` to start the application.

## Running Tests
- Execute tests with `pytest` command in the root of the project directory. 
- Ensure that test coverage is at least 70%.