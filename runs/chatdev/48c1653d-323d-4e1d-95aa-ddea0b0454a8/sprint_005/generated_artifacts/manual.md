Here's a detailed user manual for the software, formatted in Markdown as requested:

```markdown
# Teacher Management System

A simple web application for managing teachers, students, and courses.

## Overview

The Teacher Management System allows users to create and manage entities for teachers, students, and courses. This application is built using FastAPI and SQLAlchemy, providing a RESTful API for easy interaction with the database.

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
   pip install -r requirements.txt
   ```

   Ensure you have the following dependencies in your `requirements.txt`:
   ```
   fastapi
   sqlalchemy
   alembic
   pydantic
   uvicorn
   ```

4. **Run Database Migrations**:
   To create the necessary database tables, run the following command:
   ```bash
   alembic upgrade head
   ```

5. **Start the Application**:
   Run the FastAPI application using Uvicorn:
   ```bash
   uvicorn main:app --reload
   ```

   The application will be accessible at `http://127.0.0.1:8000`.

## API Usage

### Creating a Teacher

To create a new teacher, send a POST request to `/teachers/` with the following JSON body:

```json
{
  "name": "John Doe",
  "email": "john.doe@example.com"
}
```

### Retrieving Teachers

To retrieve a list of all teachers, send a GET request to `/teachers/`.

### Creating a Student

To create a new student, send a POST request to `/students/` with the following JSON body:

```json
{
  "name": "Jane Smith",
  "email": "jane.smith@example.com"
}
```

### Retrieving Students

To retrieve a list of all students, send a GET request to `/students/`.

### Creating a Course

To create a new course, send a POST request to `/courses/` with the following JSON body:

```json
{
  "name": "Mathematics",
  "level": "Beginner"
}
```

### Retrieving Courses

To retrieve a list of all courses, send a GET request to `/courses/`.

## Conclusion

The Teacher Management System provides a straightforward way to manage teachers, students, and courses through a RESTful API. For further details on the API endpoints and usage, please refer to the FastAPI documentation or the source code comments.

For any issues or support, please reach out to our support team.
```

This manual provides a comprehensive overview of the software, including installation instructions, main functionalities, and usage examples for the API.