# Updated File: docs/api.md

# API Documentation

## Course Management API

### Assign a Teacher to a Course

**Endpoint:** `PUT /courses/{course_id}/assign-teacher`

**Description:**
Assign a teacher to a specified course. This endpoint updates the course record to include the specified teacher.

**Request Parameters:**
- `course_id` (path parameter): The ID of the course to which the teacher will be assigned.
- Request Body (JSON):
  ```json
  {
    "teacher_id": 1
  }
  ```

**Response:**
- Status Code: `200 OK`
- Response Body (JSON):
  ```json
  {
    "course_id": 1,
    "teacher_id": 1,
    "course_name": "Mathematics",
    "assigned_teacher": {
      "id": 1,
      "name": "John Doe"
    }
  }
  ```

**Error Responses:**
- Status Code: `404 Not Found`
  - Description: The specified course or teacher does not exist.
  - Response Body (JSON):
  ```json
  {
    "error": {
      "code": "E404",
      "message": "Teacher or course not found."
    }
  }
  ```

### Unassign a Teacher from a Course

**Endpoint:** `DELETE /courses/{course_id}/unassign-teacher`

**Description:**
Remove the assigned teacher from the specified course. This endpoint updates the course record to remove the teacher association.

**Request Parameters:**
- `course_id` (path parameter): The ID of the course from which the teacher will be unassigned.

**Response:**
- Status Code: `200 OK`
- Response Body (JSON):
  ```json
  {
    "course_id": 1,
    "teacher_id": null,
    "course_name": "Mathematics",
    "message": "Teacher successfully unassigned."
  }
  ```

**Error Responses:**
- Status Code: `404 Not Found`
  - Description: The specified course or teacher does not exist.
  - Response Body (JSON):
  ```json
  {
    "error": {
      "code": "E404",
      "message": "Course not found."
    }
  }
  ```

### Summary of Behavior

1. **Assigning a Teacher:**
   - When a valid request is made to assign a teacher to a course, the system responds with the updated course details including the assigned teacher.

2. **Invalid Teacher Assignments:**
   - If an attempt is made to assign a non-existent teacher to a course, the system sends back a `404 Not Found` error with a relevant message.

3. **Unassigning a Teacher:**
   - When a request is made to unassign a teacher, if successful, the system confirms the operation and returns the course details with `teacher_id` set to null.

This documentation provides a clear reference for developers integrating or using these new endpoints, ensuring that interactions with the Course-Teacher relationship are well understood and easily accessible.