# File: README.md

# Project Title

## Overview & Purpose
The purpose of this feature is to establish a relationship between the Course and Teacher entities. This enhancement will allow each course to be associated with a specific teacher, thereby facilitating better management of academic assignments and instructional oversight. By integrating this relationship, we aim to improve the organization of course offerings and enhance the overall educational experience.

## API Endpoints

### Assign Teacher to Course

- **Endpoint**: `POST /courses/{course_id}/assign-teacher`
- **Description**: Assign a teacher to a specific course.
- **Input**: 
    - JSON body: 
      ```json
      {
        "teacher_id": "string"  // required
      }
      ```
- **Output**: 
    - Successful assignment confirmation including the updated course object:
      ```json
      {
        "message": "Teacher assigned successfully.",
        "course": {
          "id": "string",
          "name": "string",
          "teacher_id": "string",
          "teacher_name": "string",
          "teacher_email": "string"
        }
      }
      ```
- **Validation**:
  - Ensure the provided `teacher_id` exists in the system.
  - If assigning a teacher to a course that already has a teacher, confirm that the assignment can be updated.

### Retrieve Course with Teacher

- **Endpoint**: `GET /courses/{course_id}`
- **Description**: Retrieve the details of a specific course along with the assigned teacher's details.
- **Input**:
    - **Path Parameter**: 
      - `course_id`: "string" (required)
- **Output**:
    - JSON object containing course details and assigned teacher's information:
      ```json
      {
        "course": {
          "id": "string",
          "name": "string",
          "teacher": {
            "name": "string",
            "email": "string"
          }
        }
      }
      ```

## Database Migration
- Update the existing database schema to support the relationship between Course and Teacher. The migration must ensure that existing Student, Course, and Teacher data remains intact and consistent throughout this process.

## Error Handling
- Return appropriate error messages for any invalid assignments. For example:
  - `400 Bad Request` if `teacher_id` does not exist.
  - `409 Conflict` if trying to assign a teacher to a course with an existing teacher. 

## Example

### Assign Teacher to Course Example
```bash
curl -X POST http://localhost:8000/courses/1/assign-teacher \
-H "Content-Type: application/json" \
-d '{"teacher_id": "123"}'
```

### Retrieve Course with Teacher Example
```bash
curl -X GET http://localhost:8000/courses/1
``` 

This new functionality enhances the API, allowing for better management of course assignments and improving the clarity of course-related data.