# README.md

# Course Management API

This project is a Course Management API built using FastAPI and SQLAlchemy. It provides endpoints to manage courses and enroll students in them.

## API Endpoints

### Courses

#### Create a Course

- **Endpoint**: `POST /api/v1/courses`
- **Request Body**:
  ```json
  {
    "name": "Course Name",
    "level": "Beginner/Intermediate/Advanced"
  }
  ```
- **Response**: 
  - `201 Created`: Course created successfully.
  - `400 Bad Request`: Validation errors.

---

### Student Enrollment

#### Enroll a Student in a Course

- **Endpoint**: `POST /api/v1/enroll`
- **Request Body**:
  ```json
  {
    "student_id": 1,
    "course_id": 2
  }
  ```
- **Response**: 
  - `200 OK`: Student enrolled successfully.
  - `400 Bad Request`: Validation errors (e.g., invalid course_id or student_id).

#### Retrieve Student's Courses

- **Endpoint**: `GET /api/v1/students/{student_id}/courses`
- **Response**: 
  ```json
  {
    "courses": [
      {
        "id": 1,
        "name": "Course Name",
        "level": "Beginner"
      }
    ]
  }
  ```
- **Response Codes**:
  - `200 OK`: Returned list of courses for the student.
  - `404 Not Found`: Student not found.

## Database Schema

The project uses an SQLite database to store courses and student enrollments. The schema includes tables for `students`, `courses`, and a join table `student_courses` which maintains many-to-many relationships between students and courses.

## Requirements

This project requires the following dependencies:

- `fastapi`
- `uvicorn`
- `sqlalchemy`
- `httpx`

Make sure to install the required packages using:

```bash
pip install -r requirements.txt
```

## Running the Application

To run the application, use the command:

```bash
uvicorn main:app --reload
```

This will start the FastAPI server, and you can access the API at `http://localhost:8000`.

## Testing

To run the tests, make sure you have pytest installed, then execute:

```bash
pytest
```

You can run specific tests using:

```bash
pytest tests/test_courses.py
```

## Contributing

Feel free to submit a pull request or raise an issue for any enhancements or bug fixes. We welcome contributions!

--- 

Keep this document updated with any additional changes made to the API or its functionalities.