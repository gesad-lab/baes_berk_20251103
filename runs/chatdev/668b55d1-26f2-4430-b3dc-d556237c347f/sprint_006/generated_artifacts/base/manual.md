Here's the `manual.md` file for the software, detailing the main functions, installation instructions, and usage guidelines:

```markdown
# Teacher Management System

A simple application for managing teachers, students, and courses.

## Overview

The Teacher Management System allows you to create and manage entities for teachers, students, and courses. The application provides a RESTful API to facilitate the creation and retrieval of these entities.

### Main Functions

- **Create Teacher**: Add a new teacher with a name and email.
- **Create Student**: Add a new student with a name, email, and associated courses.
- **Create Course**: Add a new course with a name and level.
- **Data Persistence**: All data is stored in a SQLite database, ensuring persistence across sessions.

## Quick Install

To set up the environment and install the necessary dependencies, follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/teacher-management-system.git
   cd teacher-management-system
   ```

2. **Create a Virtual Environment** (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

   Ensure you have the following dependencies:
   - FastAPI
   - SQLAlchemy
   - Pydantic
   - Alembic

## Database Migration

Before running the application, you need to apply the database migrations to create the necessary tables:

1. **Run Migrations**:
   ```bash
   alembic upgrade head
   ```

This command will create the `teachers`, `students`, and `courses` tables in your SQLite database while preserving existing data.

## Usage

### Starting the Application

To start the application, run the following command:

```bash
uvicorn main:app --reload
```

This will start the FastAPI server, and you can access the API documentation at `http://127.0.0.1:8000/docs`.

### API Endpoints

- **Create a Teacher**:
  - **Endpoint**: `POST /teachers/`
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

- **Create a Student**:
  - **Endpoint**: `POST /students/`
  - **Request Body**:
    ```json
    {
      "name": "Jane Smith",
      "email": "jane.smith@example.com",
      "course_ids": [1, 2]
    }
    ```
  - **Response**:
    ```json
    {
      "id": 1,
      "name": "Jane Smith",
      "email": "jane.smith@example.com",
      "course_ids": [1, 2]
    }
    ```

- **Create a Course**:
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

## Conclusion

This Teacher Management System provides a straightforward way to manage teachers, students, and courses through a RESTful API. For further customization or enhancements, feel free to modify the codebase as per your requirements.

For any issues or feature requests, please reach out to the development team.
```

This manual provides a comprehensive guide for users to understand the software's functionality, installation process, and how to interact with the API.