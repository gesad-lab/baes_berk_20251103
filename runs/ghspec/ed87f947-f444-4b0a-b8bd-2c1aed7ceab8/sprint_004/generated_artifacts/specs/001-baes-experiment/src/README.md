# README.md

# Project Overview

This project provides a RESTful API for managing students and courses in an educational application. Users can create, read, update, and delete data related to students and courses, including enrollment in multiple courses.

## API Endpoints

### Student Endpoints

#### Enroll a Student in a Course
- **Endpoint**: `POST /students/{studentId}/courses`
- **Description**: Enroll a student in a specified course.
- **Parameters**:
  - `studentId`: ID of the student to enroll.
  - **Body**:
    - `courseId`: ID of the course to which the student will be enrolled.
- **Response**:
  - **201 Created**: Returns the enrollment confirmation.
  - **400 Bad Request**: Invalid course ID or student ID.
  - **404 Not Found**: Student or course does not exist.
```json
{
  "courseId": 1
}
```

#### Retrieve All Courses for a Student
- **Endpoint**: `GET /students/{studentId}/courses`
- **Description**: Retrieve a list of courses a student is enrolled in.
- **Parameters**:
  - `studentId`: ID of the student.
- **Response**:
  - **200 OK**: Returns a list of courses.
  - **404 Not Found**: Student does not exist.
```json
{
  "courses": [
    {
      "courseId": 1,
      "name": "Data Science 101"
    },
    {
      "courseId": 2,
      "name": "Mathematics"
    }
  ]
}
```

#### Remove a Student from a Course
- **Endpoint**: `DELETE /students/{studentId}/courses/{courseId}`
- **Description**: Remove a student from a specified course.
- **Parameters**:
  - `studentId`: ID of the student to remove.
  - `courseId`: ID of the course from which the student will be removed.
- **Response**:
  - **204 No Content**: Successfully removed from the course.
  - **400 Bad Request**: Invalid course ID or student ID.
  - **404 Not Found**: Student or course does not exist.

## Database Migration

To support the many-to-many relationship between students and courses, a `student_courses` linking table must be created:

```sql
CREATE TABLE student_courses (
    student_id INTEGER NOT NULL,
    course_id INTEGER NOT NULL,
    PRIMARY KEY (student_id, course_id),
    FOREIGN KEY (student_id) REFERENCES students(id),
    FOREIGN KEY (course_id) REFERENCES courses(id)
);
```

This migration ensures that existing Student and Course data remain intact, preserving data integrity.

## Usage Examples

- To enroll a student in a course:
  ```bash
  curl -X POST "http://api.example.com/students/1/courses" -H "Content-Type: application/json" -d '{"courseId": 2}'
  ```

- To retrieve courses for a student:
  ```bash
  curl -X GET "http://api.example.com/students/1/courses"
  ```

- To remove a student from a course:
  ```bash
  curl -X DELETE "http://api.example.com/students/1/courses/2"
  ```

## Conclusion
This API enhancement enables a more robust management of student course enrollments and improves educational tracking and reporting for educators and students alike. Ensure timely updates to the documentation as new features and changes are implemented.