# README.md

# Project Title

This project manages entities related to students, courses, and teachers. It utilizes FastAPI for the backend, SQLite for the database, SQLAlchemy for ORM, and pytest for testing.

## API Documentation

This application follows OpenAPI standards for API documentation. The API includes endpoints for managing students, courses, and newly added teachers.

### Teacher API Endpoints

#### Create Teacher

- **Endpoint**: `POST /api/v1/teachers`
- **Request Body**: 
    ```json
    {
        "name": "string",
        "subject": "string",
        "email": "string"
    }
    ```
- **Responses**:
    - `201 Created`: Teacher created successfully.
    - `400 Bad Request`: Invalid input data.

#### Get All Teachers

- **Endpoint**: `GET /api/v1/teachers`
- **Responses**:
    - `200 OK`: Returns a list of teachers.
    - `404 Not Found`: No teachers found.

#### Get Teacher by ID

- **Endpoint**: `GET /api/v1/teachers/{teacher_id}`
- **Responses**:
    - `200 OK`: Returns the teacher details.
    - `404 Not Found`: Teacher not found.

#### Update Teacher

- **Endpoint**: `PUT /api/v1/teachers/{teacher_id}`
- **Request Body**: 
    ```json
    {
        "name": "string",
        "subject": "string",
        "email": "string"
    }
    ```
- **Responses**:
    - `200 OK`: Teacher details updated successfully.
    - `404 Not Found`: Teacher not found.
    - `400 Bad Request`: Invalid input data.

#### Delete Teacher

- **Endpoint**: `DELETE /api/v1/teachers/{teacher_id}`
- **Responses**:
    - `204 No Content`: Teacher deleted successfully.
    - `404 Not Found`: Teacher not found.

### Usage Instructions

To interact with the API, you can use tools like Postman or curl. Ensure your FastAPI server is running before sending requests.

#### Example Usage with curl

1. **Create a Teacher**
    ```bash
    curl -X POST "http://localhost:8000/api/v1/teachers" -H "Content-Type: application/json" -d '{"name": "Jane Doe", "subject": "Mathematics", "email": "jane.doe@example.com"}'
    ```

2. **Get All Teachers**
    ```bash
    curl -X GET "http://localhost:8000/api/v1/teachers"
    ```

3. **Get Teacher by ID**
    ```bash
    curl -X GET "http://localhost:8000/api/v1/teachers/{teacher_id}"
    ```

4. **Update Teacher**
    ```bash
    curl -X PUT "http://localhost:8000/api/v1/teachers/{teacher_id}" -H "Content-Type: application/json" -d '{"name": "Jane Smith", "subject": "Mathematics", "email": "jane.smith@example.com"}'
    ```

5. **Delete Teacher**
    ```bash
    curl -X DELETE "http://localhost:8000/api/v1/teachers/{teacher_id}"
    ```

### Conclusion

This project aims to provide a robust API for managing educational entities. The newly added teacher endpoints support full CRUD operations to efficiently manage teacher data.