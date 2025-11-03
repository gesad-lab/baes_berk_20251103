```markdown
# Teacher Management System

A simple application for managing teachers, students, and courses using FastAPI and SQLAlchemy.

## Overview

This application allows users to create and manage teachers, students, and courses. The main functionalities include adding new teachers, students, and courses, as well as retrieving lists of these entities. The application is built using Python and utilizes FastAPI for the web framework and SQLAlchemy for database interactions.

## Main Functions

- **Create Teacher**: Add a new teacher with a name and email.
- **Read Teachers**: Retrieve a list of all teachers.
- **Create Student**: Add a new student with a name and email.
- **Read Students**: Retrieve a list of all students.
- **Create Course**: Add a new course with a name and level.
- **Read Courses**: Retrieve a list of all courses.

## Installation

To set up the environment and install the necessary dependencies, follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-repo/teacher-management-system.git
   cd teacher-management-system
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

4. **Set Up the Database**:
   The application uses SQLite for simplicity. The database will be created automatically when you run the application.

## Running the Application

To start the application, run the following command:

```bash
uvicorn main:app --reload
```

This will start the FastAPI server, and you can access the API at `http://127.0.0.1:8000`.

## API Endpoints

### Teacher Endpoints

- **Create a Teacher**:
  - **Endpoint**: `POST /teachers/`
  - **Request Body**:
    ```json
    {
      "name": "John Doe",
      "email": "john.doe@example.com"
    }
    ```
  - **Response**: Returns the created teacher object.

- **Get All Teachers**:
  - **Endpoint**: `GET /teachers/`
  - **Response**: Returns a list of all teachers.

### Student Endpoints

- **Create a Student**:
  - **Endpoint**: `POST /students/`
  - **Request Body**:
    ```json
    {
      "name": "Jane Smith",
      "email": "jane.smith@example.com"
    }
    ```
  - **Response**: Returns the created student object.

- **Get All Students**:
  - **Endpoint**: `GET /students/`
  - **Response**: Returns a list of all students.

### Course Endpoints

- **Create a Course**:
  - **Endpoint**: `POST /courses/`
  - **Request Body**:
    ```json
    {
      "name": "Mathematics",
      "level": "Beginner"
    }
    ```
  - **Response**: Returns the created course object.

- **Get All Courses**:
  - **Endpoint**: `GET /courses/`
  - **Response**: Returns a list of all courses.

## Database Migrations

The application uses Alembic for database migrations. To apply migrations, run:

```bash
alembic upgrade head
```

This will create the necessary tables in the database, including the `teachers`, `students`, and `courses` tables.

## Conclusion

This Teacher Management System provides a simple interface for managing teachers, students, and courses. For further customization or enhancements, feel free to modify the codebase as needed.

For any issues or feature requests, please reach out to the development team.
```