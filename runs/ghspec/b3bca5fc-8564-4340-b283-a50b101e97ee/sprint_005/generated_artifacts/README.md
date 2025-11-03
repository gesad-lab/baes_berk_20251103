# README.md

# Teacher API Documentation

## Overview

This README file provides details regarding the new Teacher API endpoints, their functionalities, and examples of the JSON request and response structures.

## API Endpoints

### 1. Create a New Teacher

- **Endpoint**: `POST /api/v1/teachers`
- **Description**: Creates a new teacher in the system.

#### Request

- **Content-Type**: application/json
- **Body**:
```json
{
  "name": "John Doe",
  "subject": "Mathematics"
}
```

#### Response

- **Status**: 201 Created
- **Body**:
```json
{
  "id": 1,
  "name": "John Doe",
  "subject": "Mathematics"
}
```

### 2. Get All Teachers

- **Endpoint**: `GET /api/v1/teachers`
- **Description**: Retrieves a list of all teachers.

#### Response

- **Status**: 200 OK
- **Body**:
```json
[
  {
    "id": 1,
    "name": "John Doe",
    "subject": "Mathematics"
  },
  {
    "id": 2,
    "name": "Jane Smith",
    "subject": "Science"
  }
]
```

### 3. Get Teacher by ID

- **Endpoint**: `GET /api/v1/teachers/{id}`
- **Description**: Retrieves details of a specific teacher by their ID.

#### Request

- **Path Variable**: 
  - `id`: The ID of the teacher to retrieve.

#### Response

- **Status**: 200 OK
- **Body**:
```json
{
  "id": 1,
  "name": "John Doe",
  "subject": "Mathematics"
}
```

- **Status**: 404 Not Found (if the teacher does not exist)
- **Body**:
```json
{
  "error": {
    "code": "E404",
    "message": "Teacher not found."
  }
}
```

### 4. Update Teacher

- **Endpoint**: `PUT /api/v1/teachers/{id}`
- **Description**: Updates the details of an existing teacher.

#### Request

- **Path Variable**: 
  - `id`: The ID of the teacher to update.
- **Content-Type**: application/json
- **Body**:
```json
{
  "name": "John Doe",
  "subject": "Physics"
}
```

#### Response

- **Status**: 200 OK
- **Body**:
```json
{
  "id": 1,
  "name": "John Doe",
  "subject": "Physics"
}
```

### 5. Delete Teacher

- **Endpoint**: `DELETE /api/v1/teachers/{id}`
- **Description**: Deletes a teacher from the system.

#### Request

- **Path Variable**: 
  - `id`: The ID of the teacher to delete.

#### Response

- **Status**: 204 No Content (if successful)
- **Body**: (empty)

## Conclusion

This documentation provides a comprehensive overview of the new Teacher API endpoints. Each section includes the HTTP method, request/response structures, and important status codes. Please ensure to handle errors appropriately based on the examples provided. 

For any questions or further assistance, please refer to the support section.