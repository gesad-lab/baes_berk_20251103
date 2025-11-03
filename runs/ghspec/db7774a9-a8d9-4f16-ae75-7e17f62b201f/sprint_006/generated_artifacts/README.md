# README.md

# Project Title

## Introduction
This is a project aimed at educational institutions to manage courses and teachers effectively.

## API Endpoints

### 1. Assign a Teacher to a Course
- **Endpoint**: `PATCH /courses/{id}`
- **Description**: Assign a teacher to a specific course by updating the course details to include the teacher's ID.
- **Request Body**:
    ```json
    {
      "teacher_id": "integer (required)"
    }
    ```
- **Responses**:
    - **200 OK**: The updated course object, including the `teacher_id`.
    - **400 Bad Request**: If the `teacher_id` is invalid.

**Example Request**:
```bash
curl -X PATCH "http://localhost:8000/courses/1" -H "Content-Type: application/json" -d '{"teacher_id": 3}'
```

**Example Response**:
```json
{
  "id": 1,
  "name": "Mathematics",
  "teacher_id": 3,
  "teacher_name": "John Doe"
}
```

### 2. Retrieve Course Information
- **Endpoint**: `GET /courses/{id}`
- **Description**: Retrieve details of a specific course, including the associated teacher's information.
- **Responses**:
    - **200 OK**: The requested course object, including `teacher_id` and `teacher_name`.
    - **404 Not Found**: If the course does not exist.

**Example Request**:
```bash
curl -X GET "http://localhost:8000/courses/1"
```

**Example Response**:
```json
{
  "id": 1,
  "name": "Mathematics",
  "teacher_id": 3,
  "teacher_name": "John Doe"
}
```

### 3. List All Courses with Teachers
- **Endpoint**: `GET /courses`
- **Description**: Obtain a complete list of all courses, including the names of assigned teachers.
- **Responses**:
    - **200 OK**: An array of course objects, each including `id`, `name`, and `teacher_name`.

**Example Request**:
```bash
curl -X GET "http://localhost:8000/courses"
```

**Example Response**:
```json
[
  {
    "id": 1,
    "name": "Mathematics",
    "teacher_name": "John Doe"
  },
  {
    "id": 2,
    "name": "Science",
    "teacher_name": "Jane Smith"
  }
]
```

### Error Handling
- If a user attempts to assign a teacher using an invalid teacher ID, the application will provide appropriate feedback with a `400 Bad Request` response.

**Example Error Response for Invalid Teacher ID**:
```json
{
  "error": {
    "code": "E001",
    "message": "Invalid teacher ID provided.",
    "details": {}
  }
}
```

---

## Testing
- Verify that a teacher can be successfully assigned to a course through an update operation.
- Confirm that retrieving a course by its ID returns the course details along with the associated teacher information.
- Validate that listing all courses displays both course and teacher details accurately.
- Ensure appropriate error messages are generated for invalid teacher ID assignments.