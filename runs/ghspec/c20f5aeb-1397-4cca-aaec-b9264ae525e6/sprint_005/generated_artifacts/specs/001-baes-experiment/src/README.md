# README.md

# Student Management System

## Overview

This project is designed to manage student, course, and teacher data efficiently. The primary objective is to improve the overall organization and management within an educational environment.

## API Endpoints

### Teacher Management

#### 1. Create Teacher
- **Endpoint**: `POST /teachers`
- **Request Body**:
    ```json
    {
        "name": "John Doe",
        "email": "john.doe@example.com"
    }
    ```
- **Response**: 
    - Status: `201 Created`
    - Body:
    ```json
    {
        "id": 1,
        "name": "John Doe",
        "email": "john.doe@example.com"
    }
    ```
- **Description**: Creates a new Teacher with the specified `name` and `email`. Both fields are required.

#### 2. Retrieve Teacher Details
- **Endpoint**: `GET /teachers/{teacher_id}`
- **Response**: 
    - Status: `200 OK`
    - Body:
    ```json
    {
        "id": 1,
        "name": "John Doe",
        "email": "john.doe@example.com"
    }
    ```
- **Description**: Retrieves the details of the specified Teacher. 

### Database Schema

- **Teacher Table**:
  - `id`: Integer (auto-incremented primary key)
  - `name`: String (required)
  - `email`: String (required)
  
This schema update ensures that existing data related to Students and Courses remains intact and unaffected.

### Data Validation

When creating a Teacher, the following fields are required:
- `name`: Must be a valid string.
- `email`: Must be a valid string in email format.

If either field is missing or invalid, a validation error will be returned.

## Testing

Make sure to run the tests related to the new Teacher functionality:

- Tests for API endpoints are available in `tests/test_routes.py`.
- Tests for model validations can be found in `tests/test_models.py`.

## Deployment

Ensure that the migration scripts are included in the deployment process to set up the new Teacher table. Thorough integration testing is recommended post-deployment to verify the new endpoints.

---

For further information about the project and its structure, please refer to the accompanying documentation in the README.md file.