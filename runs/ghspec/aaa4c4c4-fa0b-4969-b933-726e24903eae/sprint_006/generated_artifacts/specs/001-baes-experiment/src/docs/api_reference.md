---
# API Reference Documentation

## Course and Teacher Integration

This section outlines the new functionalities introduced for managing courses and their associated teachers in the API.

### API Endpoints

#### 1. Assign Teacher to Course

**POST** `/api/v1/courses/{course_id}/assign_teacher`

Assign a teacher to a specific course.

**Request Parameters:**
- `course_id` (path, required): The unique identifier of the course.
  
**Request Body:**
```json
{
  "teacher_id": "string"  // The unique identifier of the teacher to be assigned.
}
```

**Response:**
- **201 Created** if the teacher is successfully assigned to the course.
- **400 Bad Request** if the `teacher_id` is invalid or if the course does not exist.
- **404 Not Found** if the course or teacher cannot be found.

**Example Request:**
```bash
curl -X POST "http://localhost:8000/api/v1/courses/1/assign_teacher" \
-H "Content-Type: application/json" \
-d '{"teacher_id": "abc123"}'
```

**Example Response:**
```json
{
  "message": "Teacher assigned successfully."
}
```

---

#### 2. Retrieve Courses with Teacher Information

**GET** `/api/v1/courses`

Retrieve a list of all courses along with their associated teacher details.

**Response:**
- **200 OK** if the request is successful.
  
**Response Body:**
```json
{
  "courses": [
    {
      "id": "string",            // The course ID.
      "title": "string",         // Course title.
      "description": "string",   // Brief description of the course.
      "teacher": {
        "id": "string",          // The teacher's unique identifier.
        "name": "string"         // The name of the teacher.
      }
    },
    ...
  ]
}
```

**Example Response:**
```json
{
  "courses": [
    {
      "id": "1",
      "title": "Introduction to APIs",
      "description": "Learn about RESTful APIs and their architecture.",
      "teacher": {
        "id": "abc123",
        "name": "John Doe"
      }
    }
  ]
}
```

---

### Notes
- Make sure to adhere to the updated API structure as we phase in teacher assignments within the Course model.
- This documentation will evolve as new functionalities are developed and integrated. Always refer back to the latest updates to ensure compliance with the API's structural and functional changes.

Adaptations will be communicated via the `README.md` and through version control updates. 

For further details or if you have any questions about the integration, please reach out to the development team.

---