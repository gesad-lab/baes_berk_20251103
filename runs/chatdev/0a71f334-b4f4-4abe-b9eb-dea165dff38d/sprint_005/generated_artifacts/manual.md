```markdown
# Teacher Management API

A FastAPI application for managing teachers, students, and courses in an educational environment.

## Overview

This API allows users to create, read, and manage entities such as Teachers, Students, and Courses. The main functionalities include:

- **Create and manage Teachers**: Add new teachers with their names and emails.
- **Create and manage Students**: Add new students and associate them with courses.
- **Create and manage Courses**: Add new courses and manage student enrollments.

## Quick Install

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

3. **Install the required dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## Dependencies

The following dependencies are required for the application:

- **fastapi**: The web framework used to build the API.
- **uvicorn**: The ASGI server for running the FastAPI application.
- **sqlalchemy**: The ORM used for database interactions.
- **alembic**: The database migration tool used to manage schema changes.
- **pydantic**: The data validation library used for request and response schemas.

## Database Setup

The application uses SQLite as the database. The database schema will be created automatically when the application starts. However, if you need to run migrations manually, you can do so with Alembic:

1. **Create a migration**:
   ```bash
   alembic revision --autogenerate -m "Add Teacher table"
   ```

2. **Apply the migration**:
   ```bash
   alembic upgrade head
   ```

## API Usage

### Endpoints

#### Teachers

- **Create a Teacher**
  - **Endpoint**: `POST /teachers/`
  - **Request Body**:
    ```json
    {
      "name": "John Doe",
      "email": "john.doe@example.com"
    }
    ```
  - **Response**: Returns the created teacher object.

- **Get all Teachers**
  - **Endpoint**: `GET /teachers/`
  - **Query Parameters**: `skip` (optional), `limit` (optional)
  - **Response**: Returns a list of teachers.

#### Students

- **Create a Student**
  - **Endpoint**: `POST /students/`
  - **Request Body**:
    ```json
    {
      "name": "Jane Smith",
      "email": "jane.smith@example.com"
    }
    ```
  - **Response**: Returns the created student object.

- **Get all Students**
  - **Endpoint**: `GET /students/`
  - **Query Parameters**: `skip` (optional), `limit` (optional)
  - **Response**: Returns a list of students.

#### Courses

- **Create a Course**
  - **Endpoint**: `POST /courses/`
  - **Request Body**:
    ```json
    {
      "name": "Mathematics",
      "level": "Beginner"
    }
    ```
  - **Response**: Returns the created course object.

- **Get all Courses**
  - **Endpoint**: `GET /courses/`
  - **Query Parameters**: `skip` (optional), `limit` (optional)
  - **Response**: Returns a list of courses.

## Running the Application

To run the FastAPI application, use the following command:

```bash
uvicorn main:app --reload
```

This will start the server at `http://127.0.0.1:8000`. You can access the interactive API documentation at `http://127.0.0.1:8000/docs`.

## Conclusion

This API provides a robust framework for managing teachers, students, and courses in an educational setting. You can extend its functionality as needed to fit your specific requirements.
```
