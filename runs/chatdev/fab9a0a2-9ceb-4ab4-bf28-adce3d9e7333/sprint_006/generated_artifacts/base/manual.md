```markdown
# Teacher Management API

A FastAPI application for managing teachers, students, and courses in an educational environment.

## Overview

This application allows users to create and manage entities such as Teachers, Students, and Courses. It provides endpoints to create, read, and enroll students in courses, as well as to manage teacher information.

## Main Functions

- **Create Teacher**: Add a new teacher with a name and email.
- **Read Teacher**: Retrieve information about a specific teacher by their ID.
- **Create Student**: Add a new student with a name and email.
- **Read Student**: Retrieve information about a specific student by their ID.
- **Create Course**: Add a new course with a name and level.
- **Read Course**: Retrieve information about a specific course by its ID.
- **Enroll Student in Course**: Enroll a student in a specific course.

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

## Database Migration

Before running the application, you need to apply the database migrations to create the necessary tables. Run the following command:
```bash
alembic upgrade head
```

## Running the Application

To start the FastAPI application, use the following command:
```bash
uvicorn main:app --reload
```

This will start the server at `http://127.0.0.1:8000`.

## API Endpoints

### Teacher Endpoints

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

- **Read Teacher**
  - **Endpoint**: `GET /teachers/{teacher_id}`
  - **Response**: Returns the teacher object for the specified ID.

### Student Endpoints

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

- **Read Student**
  - **Endpoint**: `GET /students/{student_id}`
  - **Response**: Returns the student object for the specified ID.

### Course Endpoints

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

- **Read Course**
  - **Endpoint**: `GET /courses/{course_id}`
  - **Response**: Returns the course object for the specified ID.

### Enrollment Endpoints

- **Enroll Student in Course**
  - **Endpoint**: `POST /students/{student_id}/enroll/{course_id}`
  - **Response**: Returns a success message upon successful enrollment.

## Conclusion

This API provides a robust framework for managing teachers, students, and courses in an educational setting. For further details and advanced usage, please refer to the code documentation or reach out for support.
```