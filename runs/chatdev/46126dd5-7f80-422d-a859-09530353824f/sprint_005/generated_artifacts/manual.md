Here's a detailed user manual for the software, formatted in Markdown as requested:

```markdown
# Teacher Management System

A simple API for managing Teachers, Students, and Courses in an educational context.

## Overview

This application allows users to create, read, and manage Teacher, Student, and Course entities. The main functionalities include:

- **Creating Teachers**: Add new teachers with their names and email addresses.
- **Creating Students**: Add new students with their names, email addresses, and associated courses.
- **Creating Courses**: Add new courses with their names and levels.
- **Retrieving Information**: Fetch details about teachers, students, and courses.

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

3. **Install dependencies**:
   ```bash
   pip install fastapi sqlalchemy pydantic uvicorn
   ```

4. **Run the application**:
   ```bash
   uvicorn api:router --reload
   ```

## How to Use the Application

### API Endpoints

The application exposes several API endpoints to interact with the Teacher, Student, and Course entities.

#### 1. Create a Teacher

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

#### 2. Retrieve a Teacher

- **Endpoint**: `GET /teachers/{teacher_id}`
- **Response**:
  ```json
  {
    "id": 1,
    "name": "John Doe",
    "email": "john.doe@example.com"
  }
  ```

#### 3. Create a Student

- **Endpoint**: `POST /students/`
- **Request Body**:
  ```json
  {
    "name": "Jane Smith",
    "email": "jane.smith@example.com",
    "course_ids": [1]
  }
  ```
- **Response**:
  ```json
  {
    "id": 1,
    "name": "Jane Smith",
    "email": "jane.smith@example.com",
    "courses": [1]
  }
  ```

#### 4. Retrieve a Student

- **Endpoint**: `GET /students/{student_id}`
- **Response**:
  ```json
  {
    "id": 1,
    "name": "Jane Smith",
    "email": "jane.smith@example.com",
    "courses": [1]
  }
  ```

#### 5. Create a Course

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
    "level": "Beginner",
    "students": []
  }
  ```

#### 6. Retrieve a Course

- **Endpoint**: `GET /courses/{course_id}`
- **Response**:
  ```json
  {
    "id": 1,
    "name": "Mathematics",
    "level": "Beginner",
    "students": []
  }
  ```

## Database Migration

The application includes a migration script to create the necessary database tables and ensure that existing data for Students and Courses is preserved. To run the migration, execute:

```bash
python main.py
```

This will create the `teachers` table and ensure that existing data in the `students` and `courses` tables remains intact.

## Conclusion

This Teacher Management System provides a straightforward API for managing educational entities. For further customization or enhancements, feel free to modify the codebase as needed.

For any issues or support, please reach out to the development team.
```

This manual provides a comprehensive overview of the software, installation instructions, and usage guidelines for the API endpoints.