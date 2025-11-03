# Updated API Documentation

# API Endpoints

## Courses

### Create a Course

**POST** `/courses`

**Request Body**:
```json
{
  "name": "Course Name",
  "level": "Course Level"
}
```

- **Parameters**:
  - `name` (string, required): The name of the course.
  - `level` (string, required): The level of the course (e.g., Beginner, Intermediate, Advanced).

**Response**:
- **201 Created**

```json
{
  "id": 1,
  "name": "Course Name",
  "level": "Course Level"
}
```

---

### Get All Courses

**GET** `/courses`

**Response**:
- **200 OK**

```json
[
  {
    "id": 1,
    "name": "Course Name 1",
    "level": "Beginner"
  },
  {
    "id": 2,
    "name": "Course Name 2",
    "level": "Intermediate"
  }
]
```

## Error Responses

In case of error, the response will be structured as follows:

```json
{
  "error": {
    "code": "E001",
    "message": "Error message describing what went wrong",
    "details": {}
  }
}
```

### Example Error Responses:

- **400 Bad Request**
  - **Reason**: Missing required fields.
  
```json
{
  "error": {
    "code": "E002",
    "message": "Missing required fields: name, level",
    "details": {}
  }
}
```

- **500 Internal Server Error**
  - **Reason**: Something went wrong on the server.

```json
{
  "error": {
    "code": "E500",
    "message": "An unexpected error occurred.",
    "details": {}
  }
}
```

## Notes
- Ensure to provide valid `name` and `level` when creating courses.
- All responses will be in JSON format.