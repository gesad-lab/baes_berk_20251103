# README.md

# Student Management System

## Overview
The Student Management System is designed to facilitate the management of students, courses, and teachers within an educational framework. This system allows the handling of essential data with efficient APIs to create and retrieve information about students, courses, and teachers.

## New Teacher Endpoint Functionalities

### Teacher Entity
The `Teacher` entity has been introduced to help manage teacher information. Each teacher record must contain the following attributes:
- **name**: (String, required) The full name of the teacher.
- **email**: (String, required) The email address for communication.

### API Endpoints

#### 1. Create a Teacher
- **Endpoint**: `POST /teachers`
- **Description**: This endpoint allows users to create a new teacher record.
- **Request Body**:
    ```json
    {
        "name": "John Doe",
        "email": "john.doe@example.com"
    }
    ```
- **Response**: On success, returns the created teacher's details including status:
    ```json
    {
        "status": "success",
        "teacher": {
            "id": 1,
            "name": "John Doe",
            "email": "john.doe@example.com"
        }
    }
    ```
- **Error Responses**:
    - Missing Fields: If required fields are not provided, the application will respond with an error message indicating which fields are missing.
        ```json
        {
            "error": {
                "code": "E001",
                "message": "Missing required field: name"
            }
        }
        ```
    - Invalid Email Format: If the email does not meet the correct format, the following error will be returned:
        ```json
        {
            "error": {
                "code": "E002",
                "message": "Invalid email format"
            }
        }
        ```

#### 2. Retrieve Teacher Details
- **Endpoint**: `GET /teachers/{id}`
- **Description**: Fetch details of a specific teacher using their ID.
- **Response**: Returns the teacher's details:
    ```json
    {
        "id": 1,
        "name": "John Doe",
        "email": "john.doe@example.com"
    }
    ```

### Database Schema
The system has been updated to include a new `Teacher` table in the database. This ensures that the addition does not compromise the existing `Student` or `Course` data. At the same time, all necessary validations have been set up to ensure the correctness of data associated with the `Teacher` entity.

### Migration
A migration script has been created to add the `teachers` table without affecting existing records. This includes setting up the required fields and relationships.

## Conclusion
The introduction of the `Teacher` entity enhances the functionalities of the Student Management System and sets the groundwork for future developments including course assignments and performance tracking.

## Getting Started
For detailed setup and usage instructions, refer to the `README.md` in the root directory.

## License
This project is licensed under the MIT License. See the LICENSE file for details.