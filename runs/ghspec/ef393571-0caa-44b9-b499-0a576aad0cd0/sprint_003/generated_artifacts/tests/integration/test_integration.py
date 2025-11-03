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
- **Response:** Returns a list of all students in JSON format.

## Course API

### Add a Course

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
- **Response:** Returns a list of all courses, including their names and levels, in JSON format.

## Database Migration

The application supports adding a new Course entity while preserving existing Student data. The database schema has been updated to include a new Course table with the following specifications:

- **Course Table:**
  - `id`: Integer (Auto-incremented primary key)
  - `name`: String (Required)
  - `level`: String (Required)

## Usage

1. Start the application.
2. Use the `/students` and `/courses` endpoints to manage students and courses via the API.
3. Ensure that the required fields are provided in the request bodies for successful responses.

---

Feel free to reach out with any questions or issues regarding the API!