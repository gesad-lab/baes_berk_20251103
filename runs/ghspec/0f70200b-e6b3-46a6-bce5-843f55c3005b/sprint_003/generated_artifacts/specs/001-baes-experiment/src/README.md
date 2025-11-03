```markdown
# README.md

# Course Management API

This document outlines the Course Management API, including the endpoints for creating and retrieving courses.

## API Endpoints

### 1. Create a Course
- **Endpoint**: `POST /courses`
- **Description**: Create a new course by providing both a name and a level.
- **Request Body**:
  ```json
  {
    "name": "string", // Required: Name of the course
    "level": "string" // Required: Level of the course
  }
  ```
- **Responses**:
  - `201 Created`: Course successfully created.
  - `400 Bad Request`: 
    - If `name` is missing: `{"error": {"code": "E001", "message": "Course name is required."}}`
    - If `level` is missing: `{"error": {"code": "E002", "message": "Course level is required."}}`

### 2. Retrieve a Course
- **Endpoint**: `GET /courses/{id}`
- **Description**: Retrieve the details of a course using its ID.
- **Responses**:
  - `200 OK`: Returns course data.
    ```json
    {
      "id": "course_id", // ID of the course
      "name": "string",  // Name of the course
      "level": "string"  // Level of the course
    }
    ```
  - `404 Not Found`: If the course with the specified ID does not exist: `{"error": {"code": "E003", "message": "Course not found."}}`

### 3. Retrieve All Courses
- **Endpoint**: `GET /courses`
- **Description**: Retrieve a list of all existing courses.
- **Responses**:
  - `200 OK`: Returns all courses in an array format.
    ```json
    [
      {
        "id": "course_id",
        "name": "string",
        "level": "string"
      },
      ...
    ]
    ```

## Course Data Model
- The `Course` entity includes the following attributes:
  - `id` (auto-generated, unique identifier)
  - `name` (string, required)
  - `level` (string, required)

## Examples
### Successful Retrieval of a Course
#### Request
```
GET /courses/123
```
#### Response
```json
{
  "id": "123",
  "name": "Introduction to Programming",
  "level": "Beginner"
}
```

### Error Response for Non-Existent Course
#### Request
```
GET /courses/999
```
#### Response
```json
{
  "error": {
    "code": "E003",
    "message": "Course not found."
  }
}
```

## Testing
Test cases for retrieving a specific course by ID are implemented to ensure functionality is working as expected.
```python
def test_retrieve_course_by_id(client):
    """Verify that a GET request to /courses/{id} returns the correct course data."""
    response = client.get("/courses/1")  # Replace with actual test ID
    assert response.status_code == 200
    assert response.json() == {
        "id": "1",
        "name": "Example Course",
        "level": "Intermediate"
    }
```  
```