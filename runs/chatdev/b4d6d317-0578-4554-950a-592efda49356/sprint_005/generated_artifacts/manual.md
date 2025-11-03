# Teacher Management System

A simple application to manage teachers, students, and courses using FastAPI and SQLAlchemy.

## Overview

This application allows users to create and manage entities for teachers, students, and courses. The main functionalities include creating new teachers, students, and courses, as well as enrolling students in courses. The application is built using Python with FastAPI for the web framework and SQLAlchemy for database interactions.

## Main Functions

- **Create Teacher**: Add a new teacher with a name and email.
- **Create Student**: Add a new student with a name and email.
- **Create Course**: Add a new course with a name and level.
- **Enroll Student in Course**: Enroll a student in a specific course.
- **Retrieve Students**: Get a list of all students.
- **Retrieve Courses**: Get a list of all courses.

## Installation

To set up the environment and install the necessary dependencies, follow these steps:

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd student_app
   ```

2. **Create a virtual environment** (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies**:
   ```bash
   pip install fastapi[all] sqlalchemy alembic
   ```

4. **Set up the database**:
   The application uses SQLite for the database. The database will be created automatically when you run the application for the first time.

## Usage

1. **Run the application**:
   ```bash
   uvicorn main:app --reload
   ```

2. **Access the API**:
   The API will be available at `http://127.0.0.1:8000`. You can use tools like Postman or curl to interact with the API.

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

- **Create a Student**:
   - **Endpoint**: `POST /students/`
   - **Request Body**:
     ```json
     {
       "name": "Jane Smith",
       "email": "jane.smith@example.com"
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

- **Enroll a Student in a Course**:
   - **Endpoint**: `POST /students/{student_id}/courses/{course_id}`
   - **Path Parameters**: `student_id`, `course_id`

- **Retrieve Students**:
   - **Endpoint**: `GET /students/`

- **Retrieve Courses**:
   - **Endpoint**: `GET /courses/`

## Database Migration

The application uses Alembic for database migrations. When you run the application, it will automatically create the necessary tables for teachers, students, and courses without losing existing data.

## Conclusion

This application provides a simple interface for managing teachers, students, and courses. It can be extended with additional features as needed. For further customization or support, please reach out to the development team.