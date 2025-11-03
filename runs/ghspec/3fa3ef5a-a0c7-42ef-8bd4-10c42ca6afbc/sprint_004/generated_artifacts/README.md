# README.md

# API Documentation

## User Scenarios & Testing

### Assigning Courses to a Student
- **Endpoint**: `POST /students/{student_id}/courses`
- **Request Body**:
  ```json
  {
    "course_ids": [1, 2, 3]
  }
  ```
- **Response**: `200 OK`
  - Returns updated student object:
  ```json
  {
    "id": 1,
    "name": "John Doe",
    "courses": [
      {
        "id": 1,
        "name": "Mathematics",
        "level": "Beginner"
      },
      {
        "id": 2,
        "name": "Science",
        "level": "Intermediate"
      }
    ]
  }
  ```

### Retrieving Courses for a Student
- **Endpoint**: `GET /students/{id}`
- **Response**: `200 OK`
  - Returns student information and associated courses:
  ```json
  {
    "id": 1,
    "name": "John Doe",
    "courses": [
      {
        "id": 1,
        "name": "Mathematics",
        "level": "Beginner"
      },
      {
        "id": 3,
        "name": "History",
        "level": "Intermediate"
      }
    ]
  }
  ```

### Handling Requests to Assign Non-Existent Courses
- **Endpoint**: `POST /students/{student_id}/courses`
- **Request Body**:
  ```json
  {
    "course_ids": [999, 1000]  // Non-existent course IDs
  }
  ```
- **Response**: `400 Bad Request`
  - Returns error message:
  ```json
  {
    "error": {
      "code": "E001",
      "message": "The following course IDs do not exist: [999, 1000]"
    }
  }
  ```

### Removing Courses from a Student
- **Endpoint**: `DELETE /students/{student_id}/courses/{course_id}`
- **Response**: `200 OK`
  - Returns updated student object after disassociation:
  ```json
  {
    "id": 1,
    "name": "John Doe",
    "courses": [
      {
        "id": 2,
        "name": "Science",
        "level": "Intermediate"
      }
    ]
  }
  ```

### Retrieving Students with No Assigned Courses
- **Endpoint**: `GET /students/{id}`
- **Response**: `200 OK`
  - Returns student details:
  ```json
  {
    "id": 2,
    "name": "Jane Smith",
    "courses": []
  }
  ```

## Success Criteria
1. The application successfully associates courses with students and accurately reflects those associations in API responses.
2. The application can retrieve a student's details, including associated courses, and handle cases of missing courses appropriately.
3. The application updates the database schema to accommodate the relationship without losing existing `Student` or `Course` data.
4. All functionalities adhere to best practices for maintainability and code quality within the existing system's structure.