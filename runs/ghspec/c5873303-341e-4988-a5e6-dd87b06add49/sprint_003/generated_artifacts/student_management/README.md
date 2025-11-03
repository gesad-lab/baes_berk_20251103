# student_management/README.md

# Student Management System

## Overview & Purpose
The purpose of this system is to manage student records and their associated educational courses. This functionality helps in organizing, tracking, and enhancing the educational journey of students.

## API Documentation

### Course Creation Endpoint
- **Endpoint**: `POST /courses`
- **Request Body**:
  - `name`: (string, required) The name of the course.
  - `level`: (string, required) The level of the course (e.g., beginner, intermediate, advanced).
- **Expected Response**:
  - A JSON object containing:
    - `message`: A success message indicating that the course has been created.
    - `id`: The unique identifier of the newly created course.

#### Example Request
```json
{
  "name": "Introduction to Python",
  "level": "beginner"
}
```

#### Example Response
```json
{
  "message": "Course created successfully.",
  "id": 1
}
```

### Retrieve All Courses Endpoint
- **Endpoint**: `GET /courses`
- **Expected Response**: 
  - A JSON array of course objects, each containing:
    - `id`: The unique identifier of the course.
    - `name`: The name of the course.
    - `level`: The level of the course.

#### Example Response
```json
[
  {
    "id": 1,
    "name": "Introduction to Python",
    "level": "beginner"
  },
  {
    "id": 2,
    "name": "Data Science Essentials",
    "level": "intermediate"
  }
]
```

## Database Schema Update
- **Courses Table**: A new table called `courses` will be added to the database schema.
  - Fields:
    - `id`: INTEGER PRIMARY KEY AUTOINCREMENT
    - `name`: TEXT NOT NULL
    - `level`: TEXT NOT NULL

### Database Migration
- Implement a migration script to create the new `courses` table without interfering with existing student data.

## User Scenarios & Testing
1. **Scenario 1: Create a New Course**
   - As an admin user, I want to submit a request to create a new course record with a name and level so that I can include it in the course offerings.

2. **Scenario 2: Retrieve All Courses**
   - As an admin user, I want to request a list of all courses so that I can review the available courses in the system.

## Testing
- Ensure that the following is tested:
  - Creating a course with valid data returns a success message and course ID.
  - Retrieving all courses returns a correct JSON structure.
  - Appropriate validation errors are raised for missing required fields. 

> Please refer to the respective endpoint documentation and scenarios for further integration in your client applications.