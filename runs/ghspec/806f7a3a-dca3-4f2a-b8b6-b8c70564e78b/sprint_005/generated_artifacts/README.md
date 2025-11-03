# README.md

# Project Title

## Introduction
This project is designed to manage educational entities such as Teachers, Students, and Courses. The system allows for CRUD operations on these entities while ensuring data integrity and validation.

## User Scenarios & Testing

### Creating a Teacher
An administrator inputs the name and email of a new teacher. The system successfully creates a corresponding Teacher record in the database.
- **Test**: Input valid name and email to create a Teacher and verify the record exists in the database.

### Retrieving a Teacher's Details
A user requests to view details of a specific teacher by their ID. The system should return the teacher’s name and email.
- **Test**: Query a Teacher by ID and ensure the returned data matches the details entered during creation.

### Validating Teacher Creation
When creating a Teacher, the application validates that both the name and email are provided and that the email format is correct.
- **Test**: Attempt to create a Teacher with missing fields or incorrect email format and confirm appropriate error messages are displayed.

### Preservation of Existing Data
Upon creating the Teacher entity, existing data in Student and Course should remain unaltered.
- **Test**: Verify that the data for Student and Course entities remains intact after migration.

## API Endpoints
The following API endpoints are available for teacher-related operations:

### Create Teacher
- **Endpoint**: `POST /api/v1/teachers`
- **Request Body**: 
    ```json
    {
        "name": "string",
        "email": "string"
    }
    ```
- **Response**:
    - **201 Created**: Teacher successfully created.
    - **400 Bad Request**: Missing fields or invalid email format.

### Retrieve Teacher
- **Endpoint**: `GET /api/v1/teachers/{id}`
- **Response**:
    - **200 OK**: Returns the teacher's details.
    - **404 Not Found**: Teacher with specified ID does not exist.

## Setup and Installation
1. Clone the repository.
2. Install dependencies.
3. Set up the database and run migrations.

For a full list of endpoints and detailed API usage, refer to `/docs/api.md`.