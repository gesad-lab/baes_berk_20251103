```markdown
# Student-Course Management System

A web application for managing students and their course enrollments.

## Overview

This application allows users to create and manage students and courses, as well as enroll students in courses. The system is built using FastAPI and SQLAlchemy, providing a robust and efficient way to handle data.

## Main Functions

- **Create Students**: Add new students to the system with their name and email.
- **Retrieve Students**: Fetch a list of students with pagination support.
- **Create Courses**: Add new courses with their name and level.
- **Retrieve Courses**: Fetch a list of courses with pagination support.
- **Enroll Students in Courses**: Associate students with courses through a many-to-many relationship.

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
   pip install fastapi[all] sqlalchemy alembic
   ```

4. **Run Database Migrations**:
   Ensure that the database schema is up to date by running the migration script:
   ```bash
   alembic upgrade head
   ```

5. **Start the Application**:
   Run the application using Uvicorn:
   ```bash
   uvicorn main:app --reload
   ```

## How to Use the Application

### API Endpoints

The application exposes several API endpoints to interact with the student and course data.

#### 1. Create a Student

- **Endpoint**: `POST /students/`
- **Request Body**:
  ```json
  {
    "name": "John Doe",
    "email": "john.doe@example.com"
  }
  ```

#### 2. Retrieve Students

- **Endpoint**: `GET /students/`
- **Query Parameters**: `skip` (int), `limit` (int)
- **Response**: List of students.

#### 3. Create a Course

- **Endpoint**: `POST /courses/`
- **Request Body**:
  ```json
  {
    "name": "Mathematics",
    "level": "Intermediate"
  }
  ```

#### 4. Retrieve Courses

- **Endpoint**: `GET /courses/`
- **Query Parameters**: `skip` (int), `limit` (int)
- **Response**: List of courses.

#### 5. Enroll a Student in a Course

- **Endpoint**: `POST /students/{student_id}/courses/{course_id}`
- **Path Parameters**: `student_id` (int), `course_id` (int)
- **Response**: Confirmation message.

## Database Schema

The application uses SQLite as the database. The following tables are created:

- **students**: Stores student information (id, name, email).
- **courses**: Stores course information (id, name, level).
- **student_courses**: Junction table to manage the many-to-many relationship between students and courses.

## Conclusion

This Student-Course Management System provides a simple yet effective way to manage student enrollments in courses. With the provided API endpoints, users can easily interact with the system to create and manage data.

For further assistance or support, please reach out to the development team.
```