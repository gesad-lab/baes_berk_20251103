# docs/api_documentation.md

# API Documentation

This documentation serves as a guide for the new API endpoints introduced for managing Courses and Students within our system.

## Course Endpoints

### 1. Create a Course

**Endpoint**: `/courses`  
**Method**: `POST`  
**Description**: This endpoint allows for the creation of a new course record.

#### Request Body
```json
{
    "name": "Introduction to Programming",
    "level": "Beginner"
}
```

#### Fields
- `name`: (string, required) The name of the course.
- `level`: (string, required) The level of the course (e.g., Beginner, Intermediate, Advanced).

#### Responses
- **201 Created**: Course created successfully.
  ```json
  {
      "id": 1,
      "name": "Introduction to Programming",
      "level": "Beginner"
  }
  ```
- **400 Bad Request**: Validation errors (e.g., missing name or level).
  ```json
  {
      "error": {
          "code": "E001",
          "message": "Name and level are required."
      }
  }
  ```

### 2. Retrieve a Course

**Endpoint**: `/courses/{id}`  
**Method**: `GET`  
**Description**: This endpoint retrieves a specific course by its ID.

#### URL Parameters
- `id`: (integer, required) The ID of the course.

#### Responses
- **200 OK**: Course retrieved successfully.
  ```json
  {
      "id": 1,
      "name": "Introduction to Programming",
      "level": "Beginner"
  }
  ```
- **404 Not Found**: Course with the specified ID does not exist.
  ```json
  {
      "error": {
          "code": "E002",
          "message": "Course not found."
      }
  }
  ```

## Student Endpoints

### 3. Create a Student

**Endpoint**: `/students`  
**Method**: `POST`  
**Description**: This endpoint allows for the creation of a new student record.

#### Request Body
```json
{
    "name": "John Doe",
    "email": "john.doe@example.com"
}
```

#### Fields
- `name`: (string, required) The name of the student.
- `email`: (string, optional) The email of the student. Must be a valid email format.

#### Responses
- **201 Created**: Student created successfully.
  ```json
  {
      "id": 1,
      "name": "John Doe",
      "email": "john.doe@example.com"
  }
  ```
- **400 Bad Request**: Validation errors (e.g., invalid email format).
  ```json
  {
      "error": {
          "code": "E001",
          "message": "Invalid email format."
      }
  }
  ```

### 4. Health Check

**Endpoint**: `/health`  
**Method**: `GET`  
**Description**: Endpoint to check the API's health status.

#### Responses
- **200 OK**: API is operational.
  ```json
  {
      "status": "ok"
  }
  ```

## Note

All endpoints return responses in JSON format. Ensure to handle errors appropriately in your applications by reading the response body for error codes and messages.