```markdown
# Student-Course Management System

A FastAPI application for managing students and their course enrollments.

## Overview

This application allows users to create and manage students and courses, as well as enroll students in courses. It utilizes FastAPI for the web framework, SQLAlchemy for database interactions, and Alembic for database migrations.

## Main Functions

- **Create Students**: Add new students to the system with their names and email addresses.
- **Retrieve Students**: Fetch a list of students with pagination support.
- **Create Courses**: Add new courses with their names and levels.
- **Retrieve Courses**: Fetch a list of courses with pagination support.
- **Enroll Students in Courses**: Associate students with courses they are enrolled in.

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
   ```plaintext
   fastapi
   uvicorn
   sqlalchemy
   alembic
   pydantic
   ```
   Then run:
   ```bash
   pip install -r requirements.txt
   ```

## Database Initialization

Before running the application, initialize the database:

1. **Run Migrations**:
   To create the necessary database tables, run the following command:
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

### Students

- **Create a Student**:
  - **Endpoint**: `POST /students/`
  - **Request Body**:
    ```json
    {
      "name": "John Doe",
      "email": "john.doe@example.com"
    }
    ```

- **Get Students**:
  - **Endpoint**: `GET /students/`
  - **Query Parameters**: `skip` (int), `limit` (int)

### Courses

- **Create a Course**:
  - **Endpoint**: `POST /courses/`
  - **Request Body**:
    ```json
    {
      "name": "Mathematics",
      "level": "Beginner"
    }
    ```

- **Get Courses**:
  - **Endpoint**: `GET /courses/`
  - **Query Parameters**: `skip` (int), `limit` (int)

### Enrollment

- **Enroll a Student in a Course**:
  - **Endpoint**: `POST /students/{student_id}/courses/{course_id}`
  - **Path Parameters**: `student_id` (int), `course_id` (int)

## Conclusion

This application provides a simple yet effective way to manage students and their course enrollments. For further customization and enhancements, feel free to modify the codebase as per your requirements.

For any issues or feature requests, please reach out to the development team.
```