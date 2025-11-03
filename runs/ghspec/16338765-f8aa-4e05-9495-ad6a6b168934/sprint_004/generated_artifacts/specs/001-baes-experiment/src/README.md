# README.md

# Project Overview

This application is designed to manage Students and Courses with an associated enrollment process, allowing Students to be enrolled in multiple Courses.

## Functional Requirements

### 1. Update The Student Entity
- Enhanced the `Student` entity to establish a relationship with `Course`.
- Each Student can have multiple associated Course records.

### 2. Database Schema Changes
- Introduced a new table, **StudentCourse**, to manage the many-to-many relationship between Students and Courses.
  
  **Table Name**: `StudentCourse`
  
  **Columns**:
  - `student_id`: Integer (Foreign Key referencing `Student.id`, required)
  - `course_id`: Integer (Foreign Key referencing `Course.id`, required)

### 3. API Endpoints for Course Enrollments

#### 3.1 Enroll a Student in a Course
- **Endpoint**: `POST /students/{student_id}/courses`
- **Input**: 
  ```json
  {
    "course_id": 1 // Integer, required
  }
  ```
- **Output**: 
  ```json
  {
    "student_id": 1,
    "course_id": 1,
    "message": "Enrollment successful"
  }
  ```

#### 3.2 Retrieve Student's Courses
- **Endpoint**: `GET /students/{student_id}/courses`
- **Output**:
  ```json
  [
    {
      "course_id": 1,
      "course_name": "Mathematics 101"
    },
    {
      "course_id": 2,
      "course_name": "Physics 101"
    }
  ]
  ```

#### 3.3 Update Course Enrollment
- **Endpoint**: `PUT /students/{student_id}/courses`
- **Input**:
  ```json
  {
    "course_ids": [1, 2] // Array of Integers, required for updates to reflect current courses
  }
  ```
- **Output**:
  ```json
  {
    "student_id": 1,
    "updated_courses": [1, 2],
    "message": "Course enrollment updated successfully"
  }
  ```

### 4. Database Migration
- The migration for adding the **StudentCourse** table has been implemented to ensure that existing `Student` and `Course` data remains intact during deployment.

## Usage Instructions
1. Ensure you have all dependencies installed.
2. Run the migration script to update the database schema.
3. Use the documented API endpoints to manage course enrollments.