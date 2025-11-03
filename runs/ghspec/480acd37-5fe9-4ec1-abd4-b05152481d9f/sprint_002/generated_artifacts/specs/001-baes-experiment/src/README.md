# README.md

# Student Management API

## Overview
This project provides a simple API for managing student records. It allows users to create, retrieve, and update student information, including their names and email addresses.

## API Endpoints

### 1. Create a Student Record
- **POST /students**
- **Request Body**:
  ```json
  {
    "name": "string",
    "email": "string"
  }
  ```
- **Response**:
  - **201 Created**: Returns the created student object:
    ```json
    {
      "id": "integer",
      "name": "string",
      "email": "string"
    }
    ```
- **User Scenario**:
  A user can submit a request to create a new student record by providing both a name and an email address. The system will respond with the created student data, including an ID.

### 2. Retrieve All Student Records
- **GET /students**
- **Response**:
  - **200 OK**: Returns a JSON array of all student records:
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
- **User Scenario**:
  A user can request a list of all student records, which includes the email addresses.

### 3. Update a Student Record
- **PUT /students/{id}**
- **Request Body**:
  ```json
  {
    "name": "string",
    "email": "string"
  }
  ```
- **Response**:
  - **200 OK**: Returns the updated student object:
    ```json
    {
      "id": "integer",
      "name": "string",
      "email": "string"
    }
    ```
- **User Scenario**:
  A user can update an existing student’s email address by providing the student ID and a new email.

### 4. Field Validation for Email
- **Validation**: The system validates email fields to ensure they follow the standard email format. 
- **Test**: Ensure that submitting an invalid email format results in an appropriate error response:
  - **400 Bad Request**: Returns an error message if the email is invalid:
    ```json
    {
      "error": {
          "code": "E001",
          "message": "Invalid email format"
      }
    }
    ```

## Functional Requirements
1. **Database Changes**:
   - The Student table now includes the `email` field (required).

2. **API Endpoints Adjustment**:
   - The API endpoints have been adjusted to include the email field for student records, as detailed above.