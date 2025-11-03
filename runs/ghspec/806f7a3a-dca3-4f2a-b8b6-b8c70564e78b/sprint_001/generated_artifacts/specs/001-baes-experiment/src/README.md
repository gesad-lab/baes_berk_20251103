# API Documentation for Student Management System

This API allows for the management of student records, including creation, retrieval, updating, and deletion of students.

## Endpoints

### 1. Create Student
- **Endpoint**: `POST /api/v1/students`
- **Description**: Creates a new student record with the provided name.

- **Request Body**:
```json
{
  "name": "John Doe"
}
```

- **Responses**:
  - **201 Created**
    - Example Response Body:
    ```json
    {
      "id": 1,
      "name": "John Doe"
    }
    ```
  - **400 Bad Request** 
    - Example Response Body:
    ```json
    {
      "error": {
        "code": "E001",
        "message": "Name field is required and must be a non-empty string."
      }
    }
    ```

### 2. Retrieve Student by ID
- **Endpoint**: `GET /api/v1/students/<id>`
- **Description**: Retrieves a student record by its unique ID.

- **Responses**:
  - **200 OK**
    - Example Response Body:
    ```json
    {
      "id": 1,
      "name": "John Doe"
    }
    ```
  - **404 Not Found**
    - Example Response Body:
    ```json
    {
      "error": {
        "code": "E002",
        "message": "Student with the given ID not found."
      }
    }
    ```

### 3. Update Student
- **Endpoint**: `PUT /api/v1/students/<id>`
- **Description**: Updates an existing student record with a new name.

- **Request Body**:
```json
{
  "name": "Jane Doe"
}
```

- **Responses**:
  - **200 OK**
    - Example Response Body:
    ```json
    {
      "id": 1,
      "name": "Jane Doe"
    }
    ```
  - **400 Bad Request** 
    - Example Response Body:
    ```json
    {
      "error": {
        "code": "E001",
        "message": "Name field is required and must be a non-empty string."
      }
    }
    ```
  - **404 Not Found**
    - Example Response Body:
    ```json
    {
      "error": {
        "code": "E002",
        "message": "Student with the given ID not found."
      }
    }
    ```

### 4. Delete Student
- **Endpoint**: `DELETE /api/v1/students/<id>`
- **Description**: Deletes an existing student record.

- **Responses**:
  - **204 No Content** (No response body)
  - **404 Not Found**
    - Example Response Body:
    ```json
    {
      "error": {
        "code": "E002",
        "message": "Student with the given ID not found."
      }
    }
    ```

## Error Codes
- **E001**: Invalid input for the name field (required and should be a non-empty string).
- **E002**: Student not found for the given ID.

## Additional Notes
- The application automatically generates the SQLite database schema on startup if it doesn't already exist.
- Ensure that all requests are made to the correct API version specified in the endpoint.