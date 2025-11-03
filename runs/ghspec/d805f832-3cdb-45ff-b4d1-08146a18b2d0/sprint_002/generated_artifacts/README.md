# Updated README.md

# Student Management API

## Overview

This web application provides an API to manage student records, allowing the creation and retrieval of student information. The recent updates enhance the functionality by requiring an email address for each student, which will improve communication and data collection within the system.

## API Endpoints

### 1. Create a Student

- **Endpoint**: `POST /students`
- **Description**: Creates a new Student with the required fields.
- **Input**: 
  - JSON object with the following properties:
    - `name` (string, required)
    - `email` (string, required, validated for correct format)
- **Output**: 
  - JSON object containing the following:
    - `id`: Unique identifier of the created student
    - `name`: The name of the student
    - `email`: The email of the student
- **Error Handling**:
  - Returns an error response if the `email` field is missing or does not meet the correct format.

### 2. Retrieve a Student

- **Endpoint**: `GET /students/{id}`
- **Description**: Retrieves the details of a student by their unique ID.
- **Output**: 
  - JSON object containing the following:
    - `id`: Unique identifier of the student
    - `name`: The name of the student
    - `email`: The email of the student

## Database Schema

- The `students` table has been updated to include an `email` field, which is required for every student record. 
- Existing student data has been preserved during this schema update.

## User Scenarios & Testing

1. **Creating a Student with Email**: 
   - A user sends a request to create a Student with valid `name` and `email` fields.
   - Expected Outcome: The API returns a success response with the newly created student's data.

2. **Retrieving a Student with Email**: 
   - A user retrieves the details of an existing Student by ID.
   - Expected Outcome: The API returns the student's details in JSON format.

3. **Creating a Student without Email**: 
   - A user attempts to create a Student with a valid name but missing the email.
   - Expected Outcome: The API returns an error response indicating the missing email.

## Implementation Approach

1. **Environment Setup**:
   - Ensure Python 3.11+ is installed.
   - Create a virtual environment.
   - Install dependencies: 
     ```bash
     pip install fastapi[all] sqlalchemy
     ```

2. **Database Migration**:
   - Update the `students` table to include the `email` field. Use Alembic for migrations or SQLAlchemy commands to add the new column without losing existing data.

3. **Request Validation**:
   - Implement request validation using Pydantic models to ensure that all fields, including `email`, are correctly formatted.

## Code Documentation

- Each module, class, and function will have docstrings explaining their purpose and usage to aid developers in understanding the code structure and flow.

This document outlines how to use the API effectively, what each endpoint does, and the requirements for creating and managing students in the system.