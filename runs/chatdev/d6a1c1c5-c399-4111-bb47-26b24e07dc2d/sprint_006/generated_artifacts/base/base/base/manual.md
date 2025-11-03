Here's a detailed user manual for the software, formatted in Markdown as requested:

```markdown
# Course Management System

A simple API for managing students and courses.

## Overview

This application allows users to create and manage students and courses. It provides endpoints to create and retrieve student and course information. The application is built using FastAPI and SQLAlchemy, ensuring a robust and efficient backend.

## Main Functions

- **Create Student**: Add a new student with a name and email.
- **Get Students**: Retrieve a list of all students.
- **Create Course**: Add a new course with a name and level.
- **Get Courses**: Retrieve a list of all courses.

## Quick Install

To set up the environment and install the necessary dependencies, follow these steps:

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd student_app
   ```

2. **Create a virtual environment** (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies**:
   ```bash
   pip install fastapi[all] sqlalchemy alembic
   ```

4. **Initialize the database**:
   ```bash
   python -c "from database import init_db; init_db()"
   ```

## Usage

### Running the Application

To start the FastAPI application, run the following command:

```bash
uvicorn main:app --reload
```

This will start the server at `http://127.0.0.1:8000`.

### API Endpoints

#### Students

- **Create Student**
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

- **Get Students**
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

#### Courses

- **Create Course**
  - **Endpoint**: `POST /courses/`
  - **Request Body**:
    ```json
    {
      "name": "Mathematics",
      "level": "Beginner"
    }
    ```
  - **Response**:
    ```json
    {
      "id": 1,
      "name": "Mathematics",
      "level": "Beginner"
    }
    ```

- **Get Courses**
  - **Endpoint**: `GET /courses/`
  - **Response**:
    ```json
    [
      {
        "id": 1,
        "name": "Mathematics",
        "level": "Beginner"
      }
    ]
    ```

## Database Migration

The application uses Alembic for database migrations. To ensure that existing student data is preserved when creating the new Course table, the migration scripts should be carefully managed. You can run migrations using:

```bash
alembic upgrade head
```

## Conclusion

This Course Management System provides a simple yet effective way to manage students and courses. For further customization or feature requests, please reach out to the development team.

```

This manual provides a comprehensive overview of the application, including installation instructions, usage guidelines, and API endpoint details. Let me know if you need any modifications or additional information!