# README.md

# Project Title

## Introduction
This documentation outlines how to set up and utilize the API for managing educational entities, specifically focusing on creating Teacher entities.

## API Endpoints

### Create a Teacher
- **Endpoint**: `/teachers`
- **Method**: `POST`
- **Description**: Creates a new Teacher entity.
- **Request Payload**:
  - `name` (string, required): The full name of the Teacher.
  - `email` (string, required): The email address of the Teacher.
  
- **Success Response**:
  - **Code**: `201 Created`
  - **Content**: A JSON object containing the created Teacher's details.
    ```json
    {
      "id": 1,
      "name": "John Doe",
      "email": "john.doe@example.com"
    }
    ```
  
- **Error Responses**:
  - **Code**: `400 Bad Request`
    - **Condition**: If the name or email is missing.
    - **Content**: A JSON object with error details.
      ```json
      {
        "error": {
          "code": "E001",
          "message": "Both name and email fields are required."
        }
      }
      ```

## Logging
All API actions related to Teacher creation are logged for traceability. Logs provide insight into the creation process, including successful operations and validation errors.

### Example Log Messages
- When a Teacher is successfully created:
  ```
  INFO: Teacher created successfully: {"id": 1, "name": "John Doe", "email": "john.doe@example.com"}
  ```
- When a creation attempt fails due to missing fields:
  ```
  WARNING: Teacher creation failed due to missing fields: {"name": "", "email": ""}
  ```

## Database Schema
A new `Teacher` table has been added to the database with the following columns:
- **id** (integer, primary key)
- **name** (string, required)
- **email** (string, required)

## Migration Steps
Ensure that migrations are executed to create the Teacher table without affecting existing Student and Course data.

## Testing
To verify the functionality, please reference the scenarios described in the User Scenarios & Testing section. Automated tests ensure that all edge cases are handled correctly.

## Conclusion
This README serves as a guide for developers and users interacting with the Teacher API. For further inquiries, please contact the development team.

---
