# README.md

# Project Title

## Overview

This application allows the management of students with the ability to create, retrieve, and validate student records in a database.

## API Endpoints

### Create Student

- **Endpoint**: `/students`
- **Method**: `POST`
- **Description**: Create a new student with valid name and email.

#### Request Body
```json
{
    "name": "string",
    "email": "string"
}
```

- **name**: The name of the student. (Required)
- **email**: The email of the student. (Required, must be a valid email format)

#### Successful Response
- **Status Code**: `201 Created`
- **Response Body**:
```json
{
    "id": "integer",
    "name": "string",
    "email": "string"
}
```

### Get Student by ID

- **Endpoint**: `/students/{id}`
- **Method**: `GET`
- **Description**: Retrieve an existing student’s details by their ID.

#### Path Parameters
- **id**: The unique identifier of the student. (Required)

#### Successful Response
- **Status Code**: `200 OK`
- **Response Body**:
```json
{
    "id": "integer",
    "name": "string",
    "email": "string"
}
```

### Error Handling

The application gracefully handles invalid requests. For example:

- **Invalid Request Body**: If the email field is missing, a response with the following format will be returned:
    - **Status Code**: `400 Bad Request`
    - **Response Body**:
    ```json
    {
        "error": {
            "code": "E001",
            "message": "Email field is required."
        }
    }
    ```

## Database Migration

A migration has been applied to add an email column to the existing student records while preserving the current data.

## Important Notes

- Ensure you have the latest database structure after running migrations before testing or using the API.
- The application maintains existing student records, allowing for search and retrieval post-migration.

## Testing

Automated tests are included to verify the functionality:
- Creating a student with an email.
- Error handling when the email is missing.
- Ensuring existing students retain their information following the migration. 

---

By providing detailed specifications of the new API endpoints and expected behaviors, this documentation update ensures clarity and completeness in the project’s API usage.