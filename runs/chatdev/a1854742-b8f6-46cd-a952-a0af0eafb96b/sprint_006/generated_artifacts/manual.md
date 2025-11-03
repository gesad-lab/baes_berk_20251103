```markdown
# ChatDev Course Management System

A comprehensive API for managing students, courses, and teachers in an educational environment.

## Overview

The ChatDev Course Management System allows users to create and manage students, courses, and teachers. This API is built using FastAPI and SQLAlchemy, providing a robust and efficient way to handle educational data.

### Main Functions

- **Student Management**: Create, read, and enroll students in courses.
- **Course Management**: Create and manage courses, including assigning teachers.
- **Teacher Management**: Create and manage teachers, linking them to courses.

## Installation

To set up the environment and install the necessary dependencies, follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-repo/chatdev-course-management.git
   cd chatdev-course-management
   ```

2. **Create a Virtual Environment** (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies**:
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

Before running the application, you need to set up the database schema. Use Alembic for database migrations:

1. **Run Migrations**:
   ```bash
   alembic upgrade head
   ```

This command will create the necessary tables in the SQLite database while preserving existing data.

## Running the Application

To start the FastAPI application, run the following command:

```bash
uvicorn main:app --reload
```

The application will be accessible at `http://127.0.0.1:8000`.

## API Endpoints

### Students

- **Create a Student**: `POST /students/`
- **Enroll Student in Course**: `POST /students/{student_id}/courses/{course_id}/`

### Courses

- **Create a Course**: `POST /courses/`

### Teachers

- **Create a Teacher**: `POST /teachers/`

## Using the API

You can interact with the API using tools like Postman or cURL. Below are examples of how to use the API:

### Example: Create a Teacher

```bash
curl -X POST "http://127.0.0.1:8000/teachers/" -H "Content-Type: application/json" -d '{"name": "John Doe", "email": "john.doe@example.com"}'
```

### Example: Create a Course

```bash
curl -X POST "http://127.0.0.1:8000/courses/" -H "Content-Type: application/json" -d '{"name": "Mathematics", "level": "Beginner", "teacher_id": 1}'
```

### Example: Create a Student

```bash
curl -X POST "http://127.0.0.1:8000/students/" -H "Content-Type: application/json" -d '{"name": "Jane Smith", "email": "jane.smith@example.com", "course_ids": [1]}'
```

## Documentation

For more detailed documentation, including API reference and usage examples, please refer to the [FastAPI documentation](https://fastapi.tiangolo.com/).

## Conclusion

The ChatDev Course Management System provides a powerful and flexible API for managing educational data. With its easy-to-use endpoints and robust backend, it is designed to meet the needs of educational institutions and developers alike.
```