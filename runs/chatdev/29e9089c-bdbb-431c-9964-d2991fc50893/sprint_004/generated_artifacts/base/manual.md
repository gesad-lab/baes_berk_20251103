Here is the `manual.md` file that provides a detailed user manual for the software, including an introduction to its main functions, installation instructions, and usage guidelines.

```markdown
# Course Management System

A simple API for managing students and courses, built with FastAPI and SQLAlchemy.

## Overview

This software allows users to create and manage students and courses. The main functionalities include:

- **Student Management**: Create and retrieve student records.
- **Course Management**: Create and retrieve course records.
- **Database Migration**: Automatically updates the database schema while preserving existing data.

## Quick Install

To set up the environment and install the necessary dependencies, follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-repo/course-management-system.git
   cd course-management-system
   ```

2. **Create a Virtual Environment** (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies**:
   ```bash
   pip install fastapi[all] sqlalchemy alembic pydantic
   ```

4. **Run Database Migrations**:
   Ensure that the database schema is up to date by running the migration script:
   ```bash
   alembic upgrade head
   ```

5. **Start the Application**:
   ```bash
   uvicorn main:app --reload
   ```

## Main Functions

### Student Management

- **Create a Student**:
  - Endpoint: `POST /students/`
  - Request Body:
    ```json
    {
      "name": "John Doe",
      "email": "john.doe@example.com"
    }
    ```

- **Get Students**:
  - Endpoint: `GET /students/`
  - Query Parameters:
    - `skip`: Number of records to skip (default: 0)
    - `limit`: Number of records to return (default: 10)

### Course Management

- **Create a Course**:
  - Endpoint: `POST /courses/`
  - Request Body:
    ```json
    {
      "name": "Introduction to Programming",
      "level": "Beginner"
    }
    ```

- **Get Courses**:
  - Endpoint: `GET /courses/`
  - Query Parameters:
    - `skip`: Number of records to skip (default: 0)
    - `limit`: Number of records to return (default: 10)

## Database Schema

The application uses SQLite as the database, with the following tables:

- **students**: Stores student information (id, name, email).
- **courses**: Stores course information (id, name, level).

## Database Migration

The application uses Alembic for database migrations. The migration script ensures that any changes to the database schema do not affect existing student data.

## Usage Example

1. **Create a Student**:
   ```bash
   curl -X POST "http://127.0.0.1:8000/students/" -H "Content-Type: application/json" -d '{"name": "Jane Doe", "email": "jane.doe@example.com"}'
   ```

2. **Get All Students**:
   ```bash
   curl -X GET "http://127.0.0.1:8000/students/"
   ```

3. **Create a Course**:
   ```bash
   curl -X POST "http://127.0.0.1:8000/courses/" -H "Content-Type: application/json" -d '{"name": "Data Science", "level": "Intermediate"}'
   ```

4. **Get All Courses**:
   ```bash
   curl -X GET "http://127.0.0.1:8000/courses/"
   ```

## Conclusion

This Course Management System provides a straightforward API for managing students and courses. For further information, please refer to the code documentation or contact support.
```

This manual provides a comprehensive overview of the software, installation instructions, and usage examples to help users effectively utilize the Course Management System.