# README.md

# Student Management Web Application

## Overview

This application provides a robust interface for managing student records, including the ability to create, retrieve, and manage student information.

## Features

- Create new student records
- Retrieve student records by ID
- Validate student email formats

## API Endpoints

### Create Student

**POST /api/v1/students**

**Request Body**:
```json
{
  "name": "John Doe",
  "email": "john.doe@example.com"
}
```

**Response**:
- **201 Created**: Student created successfully
- **400 Bad Request**: Invalid email format

### Retrieve Student

**GET /api/v1/students/{id}**

**Response**:
- **200 OK**: Returns the student record
- **404 Not Found**: Student with the specified ID does not exist

## Testing

### Unit Tests

To ensure the functionality of the application, unit tests have been implemented for the following scenarios:

1. Creating and retrieving students, ensuring the email addresses are correctly handled.
2. Validating error handling for invalid email formats.

**Test Cases Include**:
- Successful creation of a student with valid email.
- Attempt to create a student with an invalid email format, expecting a 400 error response.
- Successful retrieval of an existing student record.

### Running Tests

To run the unit tests, use the following command:
```bash
pytest tests/
```

Make sure that all dependencies are installed and the application is set up in the environment.

### Coverage

The test coverage for business logic is targeted at a minimum of 70%, with critical paths (creation and retrieval of students) aimed at achieving 90%+ coverage. 

## Schema Details

The `Student` entity now includes the following fields:

- `id`: Unique identifier for each student (automatically generated)
- `name`: The student's full name
- `email`: The student's email address (must be a valid format)

## API Usage Example

### Creating a Student
To create a new student, send a POST request to `/api/v1/students` with a JSON body containing the student's name and email.

### Retrieving a Student
To retrieve a student, send a GET request to `/api/v1/students/{id}` where `{id}` is the unique identifier of the student.

## License

This project is licensed under the MIT License - see the LICENSE file for details.