# File: docs/api_reference.md

## API Reference Documentation

### Students API

The Students API allows you to manage student records, including creation, retrieval, and update functionalities.

#### Create Student

- **Endpoint**: `/students`
- **Method**: `POST`
- **Description**: Creates a new student record.

##### Request Body
The request must include the following fields:

| Field      | Type   | Required | Description                |
|------------|--------|----------|----------------------------|
| `name`     | string | Yes      | The name of the student.   |
| `email`    | string | Yes      | The email of the student.  |

##### Response
- **Status Code**: 
  - `201 Created` - When the student is successfully created.
  - `400 Bad Request` - When one or more required fields are missing.

##### Example Request
```json
{
  "name": "John Doe",
  "email": "john.doe@example.com"
}
```

##### Example Response
**Success (201 Created)**:
```json
{
  "message": "Student created successfully.",
  "student_id": 1
}
```

**Error (400 Bad Request)**:
```json
{
  "error": {
    "code": "E001",
    "message": "Email field is required.",
    "details": {}
  }
}
```

### Notes
- Ensure the `email` field is unique across the database to avoid duplication.
- Proper error handling is implemented for cases where required fields are missing in the request to ensure a robust API. 

### Additional Endpoints
Details of other endpoints can be included here as they are developed.