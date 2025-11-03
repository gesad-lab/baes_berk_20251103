# README.md

# Teacher Entity Management

## Overview
This application allows for the management of teachers, including the creation and retrieval of teacher records. Teachers have essential attributes such as name and email.

## API Endpoints

### Create a New Teacher

- **Endpoint:** `/api/v1/teachers`
- **Method:** `POST`
- **Request Body:**
  ```json
  {
    "name": "John Doe",
    "email": "johndoe@example.com"
  }
  ```
- **Response:**
  - **Status Code:** `201 Created`
  - **Body:**
    ```json
    {
      "id": 1,
      "name": "John Doe",
      "email": "johndoe@example.com"
    }
    ```

### Retrieve Teacher Information

- **Endpoint:** `/api/v1/teachers/{id}`
- **Method:** `GET`
- **Response:**
  - **Status Code:** `200 OK`
  - **Body:**
    ```json
    {
      "id": 1,
      "name": "John Doe",
      "email": "johndoe@example.com"
    }
    ```
- **Error Response:**
  - **Status Code:** `404 Not Found`
  - **Body:**
    ```json
    {
      "error": {
        "code": "E404",
        "message": "Teacher not found"
      }
    }
    ```

## Validation

When creating a teacher, the following validations are performed:
- **Name is required:** If the name is not provided, the response will indicate a validation error:
  - **Status Code:** `400 Bad Request`
  - **Body:**
  ```json
  {
    "error": {
      "code": "E400",
      "message": "Name is required."
    }
  }
  ```

## Database Migration

A new table called `Teacher` has been added to the database schema. The structure of the `teacher` table is as follows:
- **teacher table**
  - `id`: Integer (Primary Key, Auto-increment)
  - `name`: String (Required)
  - `email`: String (Required)

This ensures that all existing `Student` and `Course` data in the database remain unaffected during the migration process.

## Success Criteria

1. Admins can successfully create new teacher records with valid names and emails.
2. The application responds with the correct teacher details in JSON format when queried.
3. The application properly handles attempts to create teachers with missing information, providing actionable error messages.
4. The database migration successfully creates the Teacher table and retains all existing Student and Course data without data loss.
5. The application operates without errors and maintains backward compatibility with previous versions.

