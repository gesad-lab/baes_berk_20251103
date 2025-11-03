# Updated API Documentation

## API Documentation

### Base URL
The base URL for all API endpoints is `/api/v1`.

### Endpoints

#### 1. Get Student Details
**GET** `/students/{id}`

This endpoint retrieves a student's information along with the courses they are associated with.

**Parameters:**
- `id` (path parameter, integer): The unique identifier for the student.

**Response:**
- **200 OK**: Returns a JSON object containing student details and their associated courses.
  
```json
{
    "id": 1,
    "name": "John Doe",
    "courses": [
        {
            "id": 101,
            "name": "Mathematics"
        },
        {
            "id": 102,
            "name": "Science"
        }
    ]
}
```

**Error Responses:**
- **404 Not Found**: Student with the provided ID does not exist.

---

#### 2. Associate Courses with Student
**PUT** `/students/{id}/courses`

This endpoint allows associating multiple courses with a student.

**Parameters:**
- `id` (path parameter, integer): The unique identifier for the student.

**Body:**
- `course_ids` (array of integers): An array of course IDs to associate with the student.

**Request Example:**
```json
{
    "course_ids": [101, 102, 103]
}
```

**Response:**
- **200 OK**: Successfully associates courses and returns the updated student details.

```json
{
    "id": 1,
    "name": "John Doe",
    "courses": [
        {
            "id": 101,
            "name": "Mathematics"
        },
        {
            "id": 102,
            "name": "Science"
        },
        {
            "id": 103,
            "name": "History"
        }
    ]
}
```

**Error Responses:**
- **400 Bad Request**: 
  - If `course_ids` is empty.
  - If any of the provided course IDs do not exist.

---

### Notes
- Ensure that the database is seeded with Student and Course data for the endpoints to work correctly.
- Implement necessary input validation to handle errors gracefully.
- Use appropriate status codes in all responses to indicate the outcome of the request.