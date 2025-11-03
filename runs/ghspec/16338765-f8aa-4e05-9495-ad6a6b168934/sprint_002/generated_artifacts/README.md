# README.md

# API Documentation for Student Management

## Overview

This API is designed to manage student records efficiently and effectively. It provides functionality for creating, retrieving, updating, and deleting student entries.

## Features

- **Create Student**: Adds a new student record with name and email.
- **Retrieve Students**: Fetches all student records including their email addresses.
- **Update Student**: Modifies the information of an existing student, including their email.

## Setup Instructions

Before running the application, ensure you have the necessary dependencies installed. You can set up your environment using the following steps:

```bash
# Clone the repository
git clone <repository-url>

# Navigate into the project directory
cd <project-directory>

# Install required packages
pip install -r requirements.txt

# Set up the environment variables (if needed)
cp .env.example .env

# Apply database migrations
# Ensure your database schema is updated to include email field
alembic upgrade head

# Run the application
uvicorn main:app --reload
```

## Endpoints

### 1. Create a Student

- **POST** `/students`
- **Request Body**:
  ```json
  {
      "name": "string",       // Name of the student
      "email": "string"      // Email of the student
  }
  ```
- **Response**:
  - **200 OK**: Student created successfully
  - **400 Bad Request**: Invalid input
  ```json
  {
      "id": "integer",        // Student ID
      "name": "string",       // Name of the student
      "email": "string"       // Email of the student
  }
  ```

### 2. Retrieve All Students

- **GET** `/students`
- **Response**:
  - **200 OK**: List of students including their emails
  ```json
  [
      {
          "id": "integer",
          "name": "string",
          "email": "string"
      },
      ...
  ]
  ```

### 3. Update a Student

- **PATCH** `/students/{id}`
- **Request Body**:
  ```json
  {
      "email": "string"      // Updated email of the student (optional)
  }
  ```
- **Response**:
  - **200 OK**: Student updated successfully
  - **404 Not Found**: Student not found
  ```json
  {
      "id": "integer",        // Student ID
      "name": "string",       // Name of the student
      "email": "string"       // Updated email of the student
  }
  ```

## Testing Strategy

To ensure the functionality of the API, implement the following tests:

1. **Unit Tests**:
   - Test the creation of a student to ensure it works as expected, returning both the name and email.
   - Verify unit tests for new functionality that includes the added email field.

2. **Integration Tests**:
   - Validate endpoint functionality by ensuring that correctly formatted requests for creating, retrieving, and updating student records can be processed without issues.

### Success Criteria

- Verify that creating a student with valid data responds correctly with both fields.
- Ensure that retrieving students returns the updated records with email addresses.
- Confirm that updating a student's email changes the record appropriately and reflects accurately in subsequent retrievals.

## Deployment Considerations

- Ensure that the necessary database migrations are applied before deploying the application.
- Validate that the application starts successfully with the new email field included, requiring no manual intervention.

By following this guide, developers and testers can efficiently work with the Student Management API and ensure all functionalities operate as specified.