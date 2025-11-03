# README.md

# Student Management System

## Overview

This project is a student management system designed to manage courses, students, and teachers efficiently. The system allows the assignment of courses to teachers, handling registration, and updating course details seamlessly.

## API Endpoints

### 1. Course Management

#### Create Course
- **Endpoint**: `POST /courses`
- **Description**: Creates a new course. Optionally, a teacher can be assigned to the course.
- **Request Body**:
  ```json
  {
    "course_name": "Introduction to Programming",
    "teacher_id": 1  // Optional: ID of the teacher to be assigned
  }
  ```
- **Response**:
  - **201 Created**: Returns the created course details.
  - **400 Bad Request**: If the `teacher_id` does not exist in the Teacher table.
  
#### Update Course
- **Endpoint**: `PUT /courses/<course_id>`
- **Description**: Updates an existing course.
- **Request Body**:
  ```json
  {
    "course_name": "Advanced Programming",
    "teacher_id": 1  // Optional: Updated ID of the teacher to be assigned
  }
  ```
- **Response**:
  - **200 OK**: Returns the updated course details.
  - **400 Bad Request**: If the `teacher_id` does not exist in the Teacher table.

### 2. Teacher Management

#### Create Teacher
- **Endpoint**: `POST /teachers`
- **Description**: Creates a new teacher.
- **Request Body**:
  ```json
  {
    "name": "John Doe"
  }
  ```
- **Response**:
  - **201 Created**: Returns the created teacher details.

### Error Handling
- If a `teacher_id` provided during course creation or update does not exist, the API will return a 400 Bad Request with a message indicating that the teacher does not exist.
- If a course is created without assigning a teacher, the operation will succeed with the teacher_id being set to null.

## Database Schema Update
The Course table schema has been updated to include a foreign key column:
- `teacher_id`: Optional foreign key linking to the Teacher entity.

## Data Migration
A database migration has been implemented to ensure that existing data in the Student, Course, and Teacher tables is preserved while accommodating for the new schema changes.

## Error Handling Improvements
New error handling scenarios have been added for cases where:
- A non-existing `teacher_id` is specified during course operations.
- Courses can be created without a teacher assignment without generating errors.

## Development Setup
To set up your development environment, clone the repository and run the following commands:

```bash
pip install -r requirements.txt
```

## Running Tests
To ensure everything is working correctly, run the tests using:

```bash
pytest
```

## Acknowledgements
This project uses Flask for the web framework, SQLAlchemy for ORM, pytest for testing, and SQLite as the database backend.