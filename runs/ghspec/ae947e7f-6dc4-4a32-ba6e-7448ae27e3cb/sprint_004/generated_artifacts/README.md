# Updated README.md

# Project Title

## Introduction
This project includes an API for managing students and their associated courses. 

## API Endpoints

### Student-Course Association Endpoints

1. **POST /students/{id}/courses**
   - **Description**: Associate one or more courses with a student.
   - **Request Body** (JSON):
     ```json
     {
       "course_ids": [1, 2, 3]  // Replace with actual course IDs
     }
     ```
   - **Response**:
     - **201 Created**: If the association is successful.
       ```json
       {
         "message": "Courses associated with student successfully.",
         "student_id": 1,
         "associated_courses": [1, 2, 3]
       }
       ```
     - **400 Bad Request**: If the provided course IDs are invalid or not found.
       ```json
       {
         "error": {
           "code": "E001",
           "message": "Invalid course IDs provided.",
           "details": {}
         }
       }
       ```

2. **GET /students/{id}/courses**
   - **Description**: Retrieve all courses associated with a given student.
   - **Response**:
     - **200 OK**: If the request is successful.
       ```json
       {
         "student_id": 1,
         "courses": [
           {"id": 1, "name": "Mathematics", "level": "Beginner"},
           {"id": 2, "name": "Science", "level": "Intermediate"}
         ]
       }
       ```
     - **404 Not Found**: If the student with the specified ID does not exist.
       ```json
       {
         "error": {
           "code": "E002",
           "message": "Student not found.",
           "details": {}
         }
       }
       ```

## StudentCourse Model
The `StudentCourse` model represents the relationship between students and courses. It is implemented using a junction table containing the following fields:
- **student_id**: Integer (Foreign Key referencing Student)
- **course_id**: Integer (Foreign Key referencing Course)

## Usage Examples

To associate courses with a student, send a POST request to `/students/{id}/courses` with the appropriate `course_ids` in the request body.

To retrieve courses associated with a student, send a GET request to `/students/{id}/courses`.

## Conclusion
This README includes essential details for interacting with the API, specifically regarding the student-course relationships. For further information, please refer to the API documentation or source code comments.