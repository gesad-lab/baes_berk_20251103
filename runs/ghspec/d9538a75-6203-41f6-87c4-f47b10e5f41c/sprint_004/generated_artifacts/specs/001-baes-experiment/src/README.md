# README.md

# Student Course Management API

## Overview
This application allows students to be associated with multiple courses, improving user engagement and creating a better mechanism for educational tracking and management.

## Functional Requirements
1. **Student and Course Relationship**: 
   - A student can have multiple associated courses.
   - Each course can have multiple associated students.

2. **Database Schema**: 
   - A new table, `StudentCourses`, has been introduced with the following fields:
     - `id`: Auto-incrementing integer.
     - `student_id`: Foreign key linked to the `Student` entity.
     - `course_id`: Foreign key linked to the `Course` entity.

## API Endpoints
1. `POST /students/{student_id}/courses`
   - Associates a course with a student.
   - **Request Body**: `{ "course_id": <course_id> }`
   - **Response**: 
     - `201 Created` on success.
     - `400 Bad Request` if the course ID is invalid.

2. `GET /students/{student_id}/courses`
   - Retrieves all courses associated with a specific student.
   - **Response**:
     - `200 OK` with a list of courses.

## Migration
Ensure to run the migration to add the `StudentCourses` table without altering existing `Student` and `Course` data. The migration file is located in the `migrations` directory:

```bash
python migrations/add_student_courses_table.py
```

## Testing
- All new API functionality includes automated tests to ensure at least 70% coverage for the business logic. 
- The tests are located in the `tests` directory, under `test_routes.py`.

## Example Usage
### Associating Courses to a Student
```bash
curl -X POST http://localhost:5000/students/1/courses -H "Content-Type: application/json" -d '{"course_id": 2}'
```

### Retrieving Courses for a Student
```bash
curl -X GET http://localhost:5000/students/1/courses
```

## Setup
1. Ensure the virtual environment is set up.
2. Install required packages:
   ```bash
   pip install -r requirements.txt
   ```

## Documentation
Documentation for the API is available at the `docs` directory, outlining all endpoints, request/response formats, and examples.

## Disclaimer
This application is under active development. Stay updated for enhancements and new features.

---
