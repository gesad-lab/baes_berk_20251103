# Updated README.md

# Course Management API

## Overview
The Course Management API allows users to efficiently manage courses and their associated teachers, along with functionalities for assigning and removing teachers to/from courses.

## API Endpoints

### 1. Assign Teacher to Course

- **Endpoint**: `/courses/{course_id}/assign_teacher`
- **Method**: `POST`
- **Description**: Assign a teacher to an existing course by providing the teacher's ID in the request body.

#### Request Body
```json
{
  "teacher_id": "string"  // The ID of the teacher to be assigned
}
```

#### Response
- **Status Code**: `200 OK`
- **Content**:
```json
{
  "message": "Teacher successfully assigned to course."
}
```

#### Error Responses
- **400 Bad Request**: If the teacher does not exist.
    ```json
    {
      "error": {
        "code": "E001",
        "message": "The specified teacher does not exist."
      }
    }
    ```

### 2. Retrieve Course with Teacher Information

- **Endpoint**: `/courses/{course_id}`
- **Method**: `GET`
- **Description**: Retrieve details of a specific course, including the assigned teacher's information.

#### Response
- **Status Code**: `200 OK`
- **Content**:
```json
{
  "course_id": "string",
  "course_name": "string",
  "teacher": {
    "teacher_id": "string",
    "teacher_name": "string"
  }
}
```

### 3. Remove Teacher from Course

- **Endpoint**: `/courses/{course_id}/remove_teacher`
- **Method**: `DELETE`
- **Description**: Remove the teacher assignment from a course.

#### Response
- **Status Code**: `200 OK`
- **Content**:
```json
{
  "message": "Teacher successfully removed from course."
}
```

### Error Handling
If any errors occur during the assignment or retrieval of teacher information, the API returns a structured error object with a relevant error code and message.

---

## Example User Scenarios
1. **Assigning a Teacher to a Course**:
   - A user can assign a teacher to a course by making a POST request to the assign teacher endpoint with the appropriate teacher ID.

2. **Retrieving Course with Teacher Information**:
   - When a user retrieves course information, the system returns the course details along with the teacher's name if an assignment exists.

3. **Removing a Teacher from a Course**:
   - Users can remove a teacher from a course by sending a DELETE request to the corresponding endpoint, which updates the course accordingly.

4. **Handling Errors in Assigning Teachers**:
   - If a user tries to assign a non-existent teacher, the API provides a clear error message indicating that the teacher does not exist.

## Conclusion
This functionality enhances course management capabilities by providing clear relationships between courses and teachers, ensuring efficient tracking and administration within the educational system.