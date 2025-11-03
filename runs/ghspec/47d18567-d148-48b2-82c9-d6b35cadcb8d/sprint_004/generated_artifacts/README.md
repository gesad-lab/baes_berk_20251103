# Updated README.md 

# Student Management App API Documentation

## Overview
This application allows management of students and their associated courses. Below are the details for the newly implemented course association and retrieval functionalities.

## API Endpoints

### 1. Associate Courses with a Student
- **Endpoint**: `PATCH /students/{student_id}`
- **Description**: Associates one or more course IDs with a student's profile.
- **Request Body**:
  ```json
  {
    "course_ids": [1, 2, 3]
  }
  ```
- **Response**:
  - **200 OK**: Successfully associated courses.
  - **400 Bad Request**: Invalid course ID(s).
  - **Response Body** (for 400 errors):
  ```json
  {
    "error": {
      "code": "E001",
      "message": "Invalid course ID(s): [3]",
      "details": {}
    }
  }
  ```

### 2. Retrieve a Student's Courses
- **Endpoint**: `GET /students/{student_id}/courses`
- **Description**: Retrieves all courses associated with a student's profile.
- **Response**:
  - **200 OK**: A list of courses associated with the student.
  - **Response Body**:
  ```json
  [
    {
      "course_id": 1,
      "name": "Introduction to Programming",
      "level": "Beginner"
    },
    {
      "course_id": 2,
      "name": "Advanced Mathematics",
      "level": "Intermediate"
    }
  ]
  ```

### 3. Error Handling for Course Association
- **Error Codes**:
  - **E001**: Invalid course ID format or non-existent course.
- All errors when associating courses will return clear and actionable messages that help users understand what went wrong.

## Example Use Cases

### Associating Courses with a Student
To associate courses with a student, send a PATCH request to the endpoint with the student's ID and an array of course IDs that you wish to associate.

**Example Request**:
```bash
curl -X PATCH "http://localhost:8000/students/1" -H "Content-Type: application/json" -d '{"course_ids": [1, 2]}'
```

### Retrieving a Student's Courses
To get a list of courses for a specific student, send a GET request to the respective endpoint.

**Example Request**:
```bash
curl -X GET "http://localhost:8000/students/1/courses"
```

## Testing
Testing for course association and retrieval functionalities was implemented in `tests/test_course.py` to ensure proper coverage as per the user scenarios defined:

- Valid course associations are successfully saved and retrieved.
- Non-existent course IDs lead to appropriate error messages.

Make sure to execute tests regularly to catch any issues early on.

--- 

**Note**: Replace the `localhost:8000` with the appropriate base URL for your deployment environment. Ensure that you have the necessary permissions to make requests to these endpoints.