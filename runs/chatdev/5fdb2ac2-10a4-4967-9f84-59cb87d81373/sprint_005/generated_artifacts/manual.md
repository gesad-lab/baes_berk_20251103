```markdown
# Teacher Management System

A simple application for managing students, courses, and teachers using FastAPI and SQLAlchemy.

## Overview

This application allows users to create, retrieve, and manage records for students, courses, and teachers. It provides a user-friendly GUI for interacting with the FastAPI backend, making it easy to manage educational data.

## Main Functions

- **Student Management**: Create and retrieve student records, including their names, emails, and associated courses.
- **Course Management**: Create and retrieve course records, including course names and levels.
- **Teacher Management**: Create and retrieve teacher records, including names and emails.

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

3. **Install Required Packages**:
   ```bash
   pip install fastapi[all] sqlalchemy alembic pydantic requests
   ```

4. **Set Up the Database**:
   The application uses SQLite for the database. The database will be created automatically when the application starts.

## Running the Application

To run the application, execute the following command:

```bash
uvicorn main:app --reload
```

This will start the FastAPI server on `http://127.0.0.1:8000`.

## Using the Application

### GUI Interaction

1. **Open the GUI**:
   The GUI will launch automatically when you run the `gui.py` file. You can run it with:
   ```bash
   python gui.py
   ```

2. **Managing Students**:
   - **Create Student**: Enter the student's name, email, and course IDs (comma-separated) and click "Create Student".
   - **Get Students**: Click "Get Students" to retrieve and display a list of all students.

3. **Managing Courses**:
   - **Create Course**: Enter the course name and level, then click "Create Course".
   - **Get Courses**: Click "Get Courses" to retrieve and display a list of all courses.

4. **Managing Teachers**:
   - **Create Teacher**: Enter the teacher's name and email, then click "Create Teacher".
   - **Get Teachers**: Click "Get Teachers" to retrieve and display a list of all teachers.

### API Endpoints

You can also interact with the application via the following API endpoints:

- **Students**:
  - `POST /students/`: Create a new student.
  - `GET /students/`: Retrieve a list of students.

- **Courses**:
  - `POST /courses/`: Create a new course.
  - `GET /courses/`: Retrieve a list of courses.

- **Teachers**:
  - `POST /teachers/`: Create a new teacher.
  - `GET /teachers/`: Retrieve a list of teachers.

## Database Migration

The application uses Alembic for database migrations. To apply migrations, ensure you have the latest migration scripts and run:

```bash
alembic upgrade head
```

This will create the necessary tables in the database, including the `students`, `courses`, and `teachers` tables.

## Conclusion

This Teacher Management System provides a simple yet effective way to manage educational data. With its easy-to-use GUI and RESTful API, users can efficiently handle student, course, and teacher records.

For further assistance or feature requests, please contact the development team.
```