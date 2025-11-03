```markdown
# Student-Course Management System

A FastAPI application for managing students and their associated courses.

## Overview

This application allows users to manage students and their relationships with courses. Students can be created, and they can be associated with multiple courses. The application provides a RESTful API for performing CRUD operations on both students and courses.

## Main Functions

- **Add Student**: Create a new student with optional course associations.
- **Get Students**: Retrieve a list of all students.
- **Add Course**: Create a new course.
- **Get Courses**: Retrieve a list of all courses.

## Installation

To set up the environment and install the necessary dependencies, follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Create a Virtual Environment** (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies**:
   ```bash
   pip install fastapi[all] sqlalchemy alembic
   ```

4. **Initialize the Database**:
   Run the following command to create the necessary database tables:
   ```bash
   python -c "from database import init_db; init_db()"
   ```

5. **Run the Application**:
   Start the FastAPI application using:
   ```bash
   uvicorn main:app --reload
   ```

   The application will be accessible at `http://127.0.0.1:8000`.

## API Usage

### Add Student

**Endpoint**: `POST /students/`

**Request Body**:
```json
{
  "name": "John Doe",
  "email": "john.doe@example.com",
  "course_ids": [1, 2]
}
```

**Response**:
```json
{
  "id": 1,
  "name": "John Doe",
  "email": "john.doe@example.com",
  "courses": [1, 2]
}
```

### Get Students

**Endpoint**: `GET /students/`

**Response**:
```json
[
  {
    "id": 1,
    "name": "John Doe",
    "email": "john.doe@example.com",
    "courses": [1, 2]
  }
]
```

### Add Course

**Endpoint**: `POST /courses/`

**Request Body**:
```json
{
  "name": "Mathematics",
  "level": "Beginner"
}
```

**Response**:
```json
{
  "id": 1,
  "name": "Mathematics",
  "level": "Beginner"
}
```

### Get Courses

**Endpoint**: `GET /courses/`

**Response**:
```json
[
  {
    "id": 1,
    "name": "Mathematics",
    "level": "Beginner"
  }
]
```

## Database Migrations

The application uses Alembic for database migrations. To create the necessary tables, run the following commands:

1. **Create Migration**:
   ```bash
   alembic revision --autogenerate -m "Initial migration"
   ```

2. **Apply Migration**:
   ```bash
   alembic upgrade head
   ```

## Conclusion

This application provides a simple yet powerful way to manage students and their courses. For further information, please refer to the code comments and the FastAPI documentation.

For any issues or feature requests, please contact the development team.
```
