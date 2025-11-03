# README.md

# MyApp API Documentation

This is the API documentation for MyApp, which provides functionalities to manage students and courses.

## Student API

### Add a Student

- **Endpoint:** `POST /students`
- **Request Body:**
  ```json
  {
      "name": "string",
      "email": "string"
  }
  ```
- **Response:**
  - **201 Created**: Returns the created student object.
  - **400 Bad Request**: If name or email is missing.

### Get Students

- **Endpoint:** `GET /students`
- **Response:** Returns a list of students.

## Course API

### Create a Course

- **Endpoint:** `POST /courses`
- **Request Body:**
  ```json
  {
      "name": "string",
      "level": "string"
  }
  ```
- **Response:**
  - **201 Created**: Returns the created course object.
  - **400 Bad Request**: If name or level is missing.

### Get Courses

- **Endpoint:** `GET /courses`
- **Response:** Returns a list of courses.

## Enrollment API

### Enroll a Student in a Course

- **Endpoint:** `POST /students/{student_id}/courses`
- **Request Body:**
  ```json
  {
      "course_id": "integer"
  }
  ```
- **Response:**
  - **201 Created**: Successfully enrolls the student in the course.
  - **400 Bad Request**: If the course ID is invalid or the student ID does not exist.
  - **404 Not Found**: If the specified student or course does not exist.

### Get Courses for a Student

- **Endpoint:** `GET /students/{student_id}/courses`
- **Response:** Returns a list of courses associated with the specified student.
  - **404 Not Found**: If the student ID does not exist.

### Get Students for a Course

- **Endpoint:** `GET /courses/{course_id}/students`
- **Response:** Returns a list of students enrolled in the specified course.
  - **404 Not Found**: If the course ID does not exist.

---

This update introduces the Enrollment API for managing the relationships between students and courses. Ensure to verify that the new functionality works as expected by following the provided user scenarios and tests.