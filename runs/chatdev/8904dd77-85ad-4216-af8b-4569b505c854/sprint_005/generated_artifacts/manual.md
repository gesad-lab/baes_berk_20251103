```markdown
# Teacher Management System

A simple API for managing teachers, students, and courses in an educational context.

## Overview

This application allows users to create and manage entities such as Teachers, Students, and Courses. It provides endpoints to create, read, and manage these entities while ensuring that existing data is preserved during database migrations.

## Main Functions

- **Create Teacher**: Add a new teacher with a name and email.
- **Read Teachers**: Retrieve a list of all teachers.
- **Create Student**: Add a new student with a name and email.
- **Read Students**: Retrieve a list of all students.
- **Create Course**: Add a new course with a name and level.
- **Read Courses**: Retrieve a list of all courses.
- **Enroll Student in Course**: Enroll a student in a specific course.
- **Get Student Courses**: Retrieve all courses a student is enrolled in.

## Installation

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

3. **Install dependencies**:
   Create a `requirements.txt` file with the following content:
   ```
   fastapi
   uvicorn
   sqlalchemy
   pydantic
   alembic
   ```
   Then run:
   ```bash
   pip install -r requirements.txt
   ```

## Running the Application

To start the FastAPI application, use the following command:
```bash
uvicorn main:app --reload
```
This will start the server at `http://127.0.0.1:8000`.

## API Endpoints

### Teachers

- **Create Teacher**
  - **Endpoint**: `POST /teachers/`
  - **Request Body**:
    ```json
    {
      "name": "John Doe",
      "email": "john.doe@example.com"
    }
    ```
  - **Response**: Returns the created teacher object.

- **Read Teachers**
  - **Endpoint**: `GET /teachers/`
  - **Response**: Returns a list of all teachers.

### Students

- **Create Student**
  - **Endpoint**: `POST /students/`
  - **Request Body**:
    ```json
    {
      "name": "Jane Smith",
      "email": "jane.smith@example.com"
    }
    ```
  - **Response**: Returns the created student object.

- **Read Students**
  - **Endpoint**: `GET /students/`
  - **Response**: Returns a list of all students.

### Courses

- **Create Course**
  - **Endpoint**: `POST /courses/`
  - **Request Body**:
    ```json
    {
      "name": "Mathematics",
      "level": "Beginner"
    }
    ```
  - **Response**: Returns the created course object.

- **Read Courses**
  - **Endpoint**: `GET /courses/`
  - **Response**: Returns a list of all courses.

### Enrollment

- **Enroll Student in Course**
  - **Endpoint**: `POST /students/{student_id}/courses/{course_id}`
  - **Response**: Returns a success message if the enrollment is successful.

- **Get Student Courses**
  - **Endpoint**: `GET /students/{student_id}/courses`
  - **Response**: Returns a list of courses the specified student is enrolled in.

## Database Migration

To add the Teacher table to the existing database schema without losing existing Student and Course data, run the migration script using Alembic:
```bash
alembic upgrade head
```

This will create the `teachers` table while preserving the existing data.

## Conclusion

This API provides a simple yet effective way to manage educational entities. For further customization and enhancements, feel free to modify the codebase as needed.
```