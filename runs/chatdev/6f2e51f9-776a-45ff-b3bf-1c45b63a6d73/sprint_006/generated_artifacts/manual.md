```markdown
# Student Course Management System

A simple application for managing students, courses, and teachers using FastAPI and SQLAlchemy.

## Overview

This application allows users to create and manage students, courses, and teachers. It includes functionalities to establish relationships between courses and teachers, enabling a more organized educational structure.

## Main Functions

- **Student Management**: Create and retrieve student records.
- **Course Management**: Create and retrieve course records, including assigning a teacher to each course.
- **Teacher Management**: Create and retrieve teacher records.

## Installation

To set up the environment and install the necessary dependencies, follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/student_app.git
   cd student_app
   ```

2. **Create a Virtual Environment** (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies**:
   ```bash
   pip install fastapi[all] sqlalchemy alembic
   ```

4. **Initialize the Database**:
   The application uses SQLite for the database. The database will be created automatically when you run the application for the first time.

## Usage

1. **Run the Application**:
   Start the FastAPI application using the following command:
   ```bash
   uvicorn main:app --reload
   ```

2. **Access the API**:
   Open your browser and navigate to `http://127.0.0.1:8000/docs` to access the interactive API documentation provided by FastAPI. Here you can test the various endpoints.

### API Endpoints

- **Students**:
  - `POST /students/`: Create a new student.
  - `GET /students/`: Retrieve a list of students.

- **Courses**:
  - `POST /courses/`: Create a new course (requires `teacher_id`).
  - `GET /courses/`: Retrieve a list of courses.

- **Teachers**:
  - `POST /teachers/`: Create a new teacher.
  - `GET /teachers/`: Retrieve a list of teachers.

### Example Requests

- **Create a Student**:
  ```json
  POST /students/
  {
      "name": "John Doe",
      "email": "john.doe@example.com"
  }
  ```

- **Create a Teacher**:
  ```json
  POST /teachers/
  {
      "name": "Jane Smith",
      "email": "jane.smith@example.com"
  }
  ```

- **Create a Course**:
  ```json
  POST /courses/
  {
      "name": "Mathematics",
      "level": "Beginner",
      "teacher_id": 1  // Replace with the actual teacher ID
  }
  ```

## Database Migration

To manage database migrations, Alembic is used. When you need to add new fields or modify existing ones, create a migration script and run it using Alembic commands.

### Example Migration Command
```bash
alembic revision --autogenerate -m "Add teacher relationship to Course"
alembic upgrade head
```

## Conclusion

This application provides a foundational structure for managing students, courses, and teachers. It can be extended with additional features such as authentication, advanced querying, and user roles as needed.

For further assistance or to report issues, please contact the development team.
```