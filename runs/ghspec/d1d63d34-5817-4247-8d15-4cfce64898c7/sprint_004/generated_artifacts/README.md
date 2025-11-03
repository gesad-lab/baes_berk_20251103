# README.md

# Project Title

## API Documentation

### Overview
The API allows for managing courses and students, with functionalities including the creation, assignment, and retrieval of courses. This documentation provides detailed information on how to interact with the provided endpoints.

### Endpoints

#### Students

##### 1. Assign Courses to Student
- **Endpoint**: `POST /students/{student_id}/assign_courses`
- **Description**: Assign one or more course IDs to a student.
- **Parameters**:
  - **student_id** (path): The ID of the student to whom courses will be assigned (integer).
- **Request Body**:
  ```json
  {
    "course_ids": [1, 2, 3]
  }
  ```
- **Response**:
  - **201 Created**: Returns the list of course IDs assigned to the student.
  - **400 Bad Request**: If the request body is invalid.
  - **404 Not Found**: If the student ID does not exist.
  
##### 2. Get Student Courses
- **Endpoint**: `GET /students/{student_id}/courses`
- **Description**: Retrieve all courses assigned to a specific student.
- **Parameters**:
  - **student_id** (path): The ID of the student whose courses are being retrieved (integer).
- **Response**:
  - **200 OK**: Returns a list of courses assigned to the student.
  - **404 Not Found**: If the student ID does not exist.

##### 3. Remove Course from Student
- **Endpoint**: `DELETE /students/{student_id}/remove_course/{course_id}`
- **Description**: Remove a specific course from a student's enrollment.
- **Parameters**:
  - **student_id** (path): The ID of the student (integer).
  - **course_id** (path): The ID of the course to remove (integer).
- **Response**:
  - **204 No Content**: If the course was successfully removed.
  - **404 Not Found**: If either the student ID or course ID does not exist.

### Data Models

#### Student Model
- **Attributes**:
  - `id`: Integer (auto-generated, primary key)
  - `name`: String (required)
  - `courses`: List of Course IDs (relation to Course entity)

```python
class Student(BaseModel):
    id: int
    name: str
    courses: List[int]
```

### Conclusion
This document outlines the key aspects of the API related to course assignment and gives an overview of the provided endpoints and their functionalities. For any questions or feedback, please refer to the project repository or contact the API support team.