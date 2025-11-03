# README.md

# Project Documentation

## Overview

This project aims to provide a system for managing students and courses. It offers various functionalities including creating courses, enrolling students, and retrieving student-course associations.

## API Endpoints

### 1. Add Course Associations

- **Endpoint**: `POST /students/{student_id}/courses`
- **Description**: Associates a list of courses with a specific student.
- **Request Body**:
  ```json
  {
      "course_ids": [1, 2, 3]  // Array of course IDs
  }
  ```
- **Response**:
  - **201 Created**: Confirmation message if association is successful.
  - **400 Bad Request**: If any course ID is invalid.
  
### 2. Get Student Courses

- **Endpoint**: `GET /students/{student_id}/courses`
- **Description**: Retrieves all courses associated with a specific student.
- **Response**:
  ```json
  [
      {
          "id": 1,
          "name": "Mathematics",
          "level": "Beginner"
      },
      {
          "id": 2,
          "name": "Science",
          "level": "Intermediate"
      }
  ]
  ```

### 3. List Students with Courses

- **Endpoint**: `GET /students`
- **Description**: Retrieves all students along with their associated courses.
- **Response**:
  ```json
  [
      {
          "id": 1,
          "name": "John Doe",
          "courses": [
              {
                  "id": 1,
                  "name": "Mathematics",
                  "level": "Beginner"
              }
          ]
      },
      {
          "id": 2,
          "name": "Jane Smith",
          "courses": []
      }
  ]
  ```

## Database Schema Update

The `Student` entity has been updated to reflect a many-to-many relationship with the `Course` entity by adding a linking table named `StudentCourses`. 

- **StudentCourses Schema**:
  - `student_id`: Integer (Foreign Key referencing Student ID)
  - `course_id`: Integer (Foreign Key referencing Course ID)

### Migration

A migration has been created to add the `student_courses` table while preserving all existing data in both the `students` and `courses` tables.

## Error Handling

- The API returns appropriate HTTP status codes based on the request outcome, and input validation is performed to ensure that provided course IDs exist.

## Usage

For more detailed instructions on how to run the server and make requests to the API, please refer to the relevant sections below.