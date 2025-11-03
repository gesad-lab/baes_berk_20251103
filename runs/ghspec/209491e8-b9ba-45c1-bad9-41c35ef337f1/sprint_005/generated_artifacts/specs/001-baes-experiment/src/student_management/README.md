# student_management/README.md

# Student Management API

This API provides endpoints for managing students, teachers, and courses related to a student management system.

## Teacher Management API

### 1. Create a Teacher

- **Endpoint**: `POST /teachers`
- **Description**: Create a new teacher in the system.
  
#### Request Body
- `name` (string, required): The full name of the teacher.
- `email` (string, required): The email address of the teacher.

#### Example Request
```json
{
  "name": "John Doe",
  "email": "john.doe@example.com"
}
```

#### Response
- **Status**: `201 Created`
- **Body**:
```json
{
  "message": "Teacher created successfully.",
  "teacher": {
    "id": 1,
    "name": "John Doe",
    "email": "john.doe@example.com"
  }
}
```

### 2. Retrieve Teacher Information

- **Endpoint**: `GET /teachers/{teacher_id}`
- **Description**: Retrieve information for a specific teacher using their unique identifier.

#### Example Request
```
GET /teachers/1
```

#### Response
- **Status**: `200 OK`
- **Body**:
```json
{
  "id": 1,
  "name": "John Doe",
  "email": "john.doe@example.com"
}
```

### 3. Validation Errors

- **Status**: `400 Bad Request`
  
If required fields are missing, the response will include a detailed error message. 

#### Example Response for Missing Fields
```json
{
  "error": {
    "code": "E001",
    "message": "Validation failed. Name and email are required."
  }
}
```

## Database Schema Changes

A new table for teachers will be implemented in the database with the following attributes:

- `id`: Automatically generated integer (Primary Key)
- `name`: String (Required)
- `email`: String (Required)

This schema change will not affect existing tables for students and courses, ensuring data integrity and consistency across the application.

## Testing

- Ensure the `POST /teachers` endpoint correctly accepts valid input and returns a success message.
- Validate that appropriate error messages are returned for invalid input (missing name or email).

## Contact

For questions or feedback regarding the API, please contact the development team.