```markdown
# Teacher Management System

A simple application for managing teachers, students, and courses using FastAPI and SQLAlchemy.

## Overview

This application allows users to create and manage teachers, students, and courses. The main functionalities include:

- Creating and retrieving teacher records.
- Creating and retrieving student records.
- Creating and retrieving course records.
- Enrolling students in courses.

## Features

- **Teacher Management**: Create and manage teacher records with name and email.
- **Student Management**: Create and manage student records with name and email.
- **Course Management**: Create and manage courses with name and level.
- **Enrollment**: Enroll students in courses and retrieve their enrolled courses.

## Installation

To set up the environment and run the application, follow these steps:

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
   ```bash
   pip install fastapi[all] sqlalchemy alembic pydantic
   ```

4. **Set up the database**:
   The application uses SQLite for the database. The database will be created automatically when you run the application for the first time.

5. **Run the application**:
   ```bash
   uvicorn main:app --reload
   ```

## Usage

Once the application is running, you can interact with it using HTTP requests. Below are some examples of how to use the API.

### Creating a Teacher

To create a new teacher, send a POST request to `/teachers/` with the following JSON body:

```json
{
  "name": "John Doe",
  "email": "john.doe@example.com"
}
```

### Retrieving Teachers

To retrieve a list of teachers, send a GET request to `/teachers/`.

### Creating a Student

To create a new student, send a POST request to `/students/` with the following JSON body:

```json
{
  "name": "Jane Smith",
  "email": "jane.smith@example.com"
}
```

### Retrieving Students

To retrieve a list of students, send a GET request to `/students/`.

### Creating a Course

To create a new course, send a POST request to `/courses/` with the following JSON body:

```json
{
  "name": "Mathematics",
  "level": "Beginner"
}
```

### Retrieving Courses

To retrieve a list of courses, send a GET request to `/courses/`.

### Enrolling a Student in a Course

To enroll a student in a course, send a POST request to `/students/{student_id}/courses/{course_id}`.

### Retrieving a Student's Courses

To retrieve the courses a specific student is enrolled in, send a GET request to `/students/{student_id}/courses`.

## Database Migrations

The application uses Alembic for database migrations. When you add new features or modify the database schema, you can create migration scripts to apply those changes without losing existing data.

To create a migration for the Teacher table, you can use the following command:

```bash
alembic revision --autogenerate -m "Create Teacher table"
```

Then, apply the migration with:

```bash
alembic upgrade head
```

## Conclusion

This application provides a simple yet effective way to manage teachers, students, and courses. You can extend its functionality by adding more features or integrating it with other systems as needed.

For further documentation and examples, please refer to the FastAPI documentation [here](https://fastapi.tiangolo.com/).
```