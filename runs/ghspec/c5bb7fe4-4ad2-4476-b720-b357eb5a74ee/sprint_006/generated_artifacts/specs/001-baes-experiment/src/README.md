# Updated README.md

# Student Management Web Application

## API Documentation

### Assign Teacher to Course
- **Endpoint**: `POST /courses/{courseId}/assign-teacher`
- **Request Body**: 
  - Required:
    - `teacher_id` (integer)
- **Response**: 
  - **Status**: 200 OK
  - **Body**: JSON representation of the updated Course with assigned Teacher.

### Retrieve Course with Teacher
- **Endpoint**: `GET /courses/{id}`
- **Response**:
  - **Status**: 200 OK
  - **Body**: JSON representation of the Course, including associated Teacher details (name, email).

### Update Teacher Assignment
- **Endpoint**: `PUT /courses/{courseId}/update-teacher`
- **Request Body**: 
  - Required:
    - `teacher_id` (integer)
- **Response**: 
  - **Status**: 200 OK
  - **Body**: JSON representation of the updated Course showing the new Teacher assignment.

### Database Schema Update
- Update the Course table to include a new field:
  - `teacher_id` (integer, foreign key referencing Teacher.id).
- The migration process must ensure that the existing Student, Course, and Teacher data remains intact and unchanged.