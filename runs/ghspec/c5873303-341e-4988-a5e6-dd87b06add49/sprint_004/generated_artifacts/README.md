# README.md

# Student Management System

## Overview & Purpose
The purpose of this feature is to establish a relationship between the Student and Course entities within the existing system. By enabling Students to enroll in multiple Courses, we aim to improve the tracking of student academic progress and curriculum management. This functionality allows better alignment of student data with their respective course enrollments, ultimately enhancing the usability of the system for academic coordination and reporting.

## API Documentation

### Enroll Student in Courses Endpoint
- **Endpoint**: `POST /students/{student_id}/enroll`
- **Request Body**: Must contain a `course_ids` field (array of integers, required) representing the IDs of the courses to enroll the student in.
  - Example Request:
    ```json
    {
        "course_ids": [1, 2, 3]
    }
    ```
- **Expected Response**: 
  - Status 200 OK
  - JSON object containing a success message and updated enrollment status.
  - Example Response:
    ```json
    {
        "message": "Enrollment successful",
        "enrollment_status": {
            "student_id": 123,
            "enrolled_courses": [1, 2, 3]
        }
    }
    ```

### Retrieve Student Courses Endpoint
- **Endpoint**: `GET /students/{student_id}/courses`
- **Expected Response**:
  - Status 200 OK
  - JSON array of course objects, each containing the `name` and `level` fields corresponding to the courses the student is enrolled in.
  - Example Response:
    ```json
    [
        {
            "name": "Mathematics",
            "level": "Intermediate"
        },
        {
            "name": "Science",
            "level": "Advanced"
        }
    ]
    ```

## Database Schema Update
- **Database Update**:
  - Implement migration scripts to create the `student_courses` join table:
    ```sql
    CREATE TABLE student_courses (
        student_id INTEGER,
        course_id INTEGER,
        PRIMARY KEY (student_id, course_id),
        FOREIGN KEY (student_id) REFERENCES students(id) ON DELETE CASCADE,
        FOREIGN KEY (course_id) REFERENCES courses(id) ON DELETE CASCADE
    );
    ```
  - Ensure that this implementation does not interfere with the existing Student or Course data during the migration process.

## Success Criteria
- The application allows successful enrollment of students in multiple courses and correctly retrieves the list of courses they are enrolled in.
- The application returns JSON responses for all requests concerning student enrollments and course retrieval as expected.
- All tests pass successfully.

## Testing
- Implement test cases for:
  - Enrolling a student in valid courses.
  - Attempting enrollment in non-existent courses and verifying the error response.
  - Retrieving courses for a given student. 

---

Ensure to update other parts of the documentation as necessary to reflect any changes to the functionality.