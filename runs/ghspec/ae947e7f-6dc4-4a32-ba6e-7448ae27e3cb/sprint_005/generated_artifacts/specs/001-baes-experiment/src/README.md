# README.md

# API Documentation

## Overview

This document outlines the API endpoints associated with the Teacher entity in the student management system. The purpose of introducing the Teacher entity is to enhance the tracking and management of educators.

## Teacher Entity

The Teacher entity consists of the following properties:

- **name**: String (required)
- **email**: String (required)

Both fields are mandatory when creating a Teacher to ensure data integrity within the system.

## API Endpoints

### 1. Create a New Teacher

**POST /teachers**

- **Description**: This endpoint is used to create a new teacher in the system.
- **Request Body**:
    ```json
    {
        "name": "John Doe",
        "email": "john.doe@example.com"
    }
    ```
- **Responses**:
    - **201 Created**: If the teacher is successfully created.
        ```json
        {
            "message": "Teacher created successfully."
        }
        ```
    - **400 Bad Request**: If required fields are missing.
        ```json
        {
            "error": {
                "code": "E001",
                "message": "Name and email are required fields."
            }
        }
        ```

### 2. Retrieve Teacher Information

**GET /teachers/{id}**

- **Description**: This endpoint retrieves the details of an existing teacher using their unique identifier.
- **Path Parameters**:
    - `id` (integer): The unique identifier of the teacher.
- **Responses**:
    - **200 OK**: If the teacher is found.
        ```json
        {
            "id": 1,
            "name": "John Doe",
            "email": "john.doe@example.com"
        }
        ```
    - **404 Not Found**: If no teacher matches the specified ID.
        ```json
        {
            "error": {
                "code": "E002",
                "message": "Teacher not found."
            }
        }
        ```

## User Scenarios & Testing

1. **Scenario 1: Create a New Teacher**
   - As an admin user, I want to create a new teacher with a specified name and email to ensure that each educator is represented within the system.
   - **Test Case**:
     - Input: Teacher's name, Teacher's email
     - Expected Output: Success message confirming the creation of the new teacher entity.

2. **Scenario 2: Validate Teacher Entity with Missing Fields**
   - As an admin user, I want to ensure that I cannot create a teacher without providing required fields to maintain data integrity.
   - **Test Case**:
     - Input: Empty name, Empty email
     - Expected Output: Error message indicating the required fields are missing.

3. **Scenario 3: Retrieve Teacher Information**
   - As an admin user, I want to retrieve information about a specific teacher using their ID.
   - **Test Case**:
     - Input: Valid teacher ID
     - Expected Output: Teacher details in JSON format.