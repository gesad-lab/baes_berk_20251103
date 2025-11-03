# README.md

# Student Management API

This is a simple API for managing students. It provides endpoints to create, retrieve, and list students.

## Table of Contents

- [Installation](#installation)
- [API Endpoints](#api-endpoints)
  - [Create Student](#create-student)
  - [Retrieve Student](#retrieve-student)
  - [List all Students](#list-all-students)
- [Testing](#testing)
- [Error Handling](#error-handling)

## Installation

To set up the project locally, follow these steps:

1. Clone the repository:
   ```
   git clone <repository-url>
   cd <repository-directory>
   ```

2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Run the application:
   ```
   python app.py
   ```

## API Endpoints

### Create Student

- **Endpoint**: `POST /students`
- **Request Body**:
  ```json
  {
    "name": "Student Name"
  }
  ```
- **Response**:
  - **Success**: 
    - **Status**: `201 Created`
  - **Error**:
    - **Status**: `400 Bad Request` 
    - **Message**: If name is missing

### Retrieve Student

- **Endpoint**: `GET /students/{id}`
- **Response**:
  - **Success**: 
    - **Status**: `200 OK`
    ```json
    {
      "id": 1,
      "name": "Student Name"
    }
    ```
  - **Error**:
    - **Status**: `404 Not Found` 
    - **Message**: If student does not exist

### List all Students

- **Endpoint**: `GET /students`
- **Response**:
  - **Success**: 
    - **Status**: `200 OK`
    ```json
    [
      {"id": 1, "name": "Student Name"},
      {"id": 2, "name": "Another Student"}
    ]
    ```

## Testing

To ensure the API functions correctly, the following test cases are implemented:

1. **Create Student**: Test endpoint with valid and invalid payloads.
2. **Retrieve Student**: Validate responses for both existing and non-existing students.
3. **List Students**: Ensure all student names are returned correctly in response.
4. **Error Handling**: Test error conditions for missing required fields.

## Error Handling

The application will respond with appropriate error messages when user input does not meet API requirements. These include:
- **400 Bad Request**: For requests with missing fields.
- **404 Not Found**: When a requested student does not exist.