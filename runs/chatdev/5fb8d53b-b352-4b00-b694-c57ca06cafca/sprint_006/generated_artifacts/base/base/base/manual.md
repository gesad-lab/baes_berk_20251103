Here's a detailed user manual for the software, formatted in Markdown as requested:

```markdown
# Course Management API

A simple API for managing students and courses using FastAPI and SQLAlchemy.

## Overview

This API allows you to perform CRUD operations on two entities: **Students** and **Courses**. You can create, read, and manage student and course data through RESTful endpoints.

### Main Functions

- **Student Management**: Create and retrieve student records.
- **Course Management**: Create and retrieve course records.
- **Database Management**: Automatically handles SQLite database connections and schema creation.

## Quick Install

To set up the environment and install the necessary dependencies, follow these steps:

1. **Clone the repository** (if applicable):
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

## Requirements

The following dependencies are required for the API to function:

- **fastapi**: The web framework used to create the API endpoints.
- **uvicorn**: The ASGI server used to run the FastAPI application.
- **sqlalchemy**: The ORM (Object Relational Mapper) used for database interactions.

## How to Use the API

### Starting the Application

To run the FastAPI application, execute the following command:

```bash
python run.py
```

The application will start, and you can access the API at `http://127.0.0.1:8000`.

### API Endpoints

#### Student Endpoints

- **Create a Student**
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

- **Get a Student by ID**
  - **Endpoint**: `GET /students/{student_id}`
  - **Response**:
    ```json
    {
      "id": 1,
      "name": "John Doe",
      "email": "john.doe@example.com"
    }
    ```

#### Course Endpoints

- **Create a Course**
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

- **Get a Course by ID**
  - **Endpoint**: `GET /courses/{course_id}`
  - **Response**:
    ```json
    {
      "id": 1,
      "name": "Mathematics",
      "level": "Beginner"
    }
    ```

## Database Migration

The database schema is automatically created when the application starts. The migration process preserves existing student data while adding the new Course table.

### Database Initialization

The database is initialized using the `init_db()` function in `database.py`, which creates the necessary tables for both Students and Courses.

## Additional Resources

For more detailed documentation on FastAPI and SQLAlchemy, please refer to the following links:

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [SQLAlchemy Documentation](https://docs.sqlalchemy.org/)

## Conclusion

This API provides a straightforward way to manage student and course data. By following the instructions above, you can set up and run the application with ease. For any issues or further assistance, please reach out to the development team.
```

This manual provides a comprehensive overview of the API, installation instructions, usage details, and additional resources for users to get started effectively.