```markdown
# Student-Course Management System

A FastAPI application for managing students and their course enrollments.

## Overview

This application allows users to manage students and their associated courses. It supports creating students and courses, enrolling students in courses, and retrieving lists of students and courses. The application uses a SQLite database for data storage and SQLAlchemy for ORM.

## Main Functions

- **Create Student**: Add a new student with a name and email.
- **Create Course**: Add a new course with a name and level.
- **Enroll Student in Course**: Associate a student with a course.
- **Retrieve Students**: Get a list of all students with their details.

## Installation

To set up the environment and install the necessary dependencies, follow these steps:

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Create a virtual environment** (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies**:
   Create a `requirements.txt` file with the following content:
   ```
   fastapi
   uvicorn
   sqlalchemy
   alembic
   pydantic
   ```
   Then run:
   ```bash
   pip install -r requirements.txt
   ```

## Database Migration

Before running the application, you need to set up the database schema. Use Alembic to apply the migrations:

1. **Run the migration script**:
   ```bash
   alembic upgrade head
   ```

## Running the Application

To start the FastAPI application, run the following command:

```bash
uvicorn main:app --reload
```

This will start the server at `http://127.0.0.1:8000`. You can access the interactive API documentation at `http://127.0.0.1:8000/docs`.

## API Endpoints

### Create Student

- **Endpoint**: `POST /students/`
- **Request Body**:
  ```json
  {
    "name": "John Doe",
    "email": "john.doe@example.com"
  }
  ```
- **Response**:
  ```json
  {
    "id": 1,
    "name": "John Doe",
    "email": "john.doe@example.com"
  }
  ```

### Create Course

- **Endpoint**: `POST /courses/`
- **Request Body**:
  ```json
  {
    "name": "Mathematics",
    "level": "Intermediate"
  }
  ```
- **Response**:
  ```json
  {
    "id": 1,
    "name": "Mathematics",
    "level": "Intermediate"
  }
  ```

### Enroll Student in Course

- **Endpoint**: `POST /students/{student_id}/courses/{course_id}/`
- **Path Parameters**:
  - `student_id`: ID of the student
  - `course_id`: ID of the course
- **Response**:
  ```json
  {
    "student_id": 1,
    "course_id": 1
  }
  ```

### Retrieve Students

- **Endpoint**: `GET /students/`
- **Response**:
  ```json
  [
    {
      "id": 1,
      "name": "John Doe",
      "email": "john.doe@example.com"
    }
  ]
  ```

## Conclusion

This application provides a simple interface for managing students and their course enrollments. You can extend its functionality by adding more features as needed. For any issues or feature requests, please contact the development team.
```