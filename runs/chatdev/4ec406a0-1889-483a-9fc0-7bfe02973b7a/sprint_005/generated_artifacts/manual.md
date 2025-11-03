Here's a detailed user manual for the software, including installation instructions, main functions, and usage guidelines.

```markdown
# Teacher Management System

A comprehensive application for managing teachers, students, and courses.

## Overview

The Teacher Management System allows users to create, read, and manage data related to teachers, students, and courses. This application is built using FastAPI and SQLAlchemy, providing a robust and efficient way to handle educational data.

## Main Functions

- **Manage Teachers**: Create and retrieve teacher records with essential details such as name and email.
- **Manage Students**: Create and retrieve student records, including their associated courses.
- **Manage Courses**: Create and retrieve course records, detailing course names and levels.

## Quick Install

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

   Ensure that you have the following dependencies in your `requirements.txt`:
   ```
   fastapi
   sqlalchemy
   alembic
   pydantic
   uvicorn
   ```

4. **Set Up the Database**:
   Run the database migrations to create the necessary tables:
   ```bash
   alembic upgrade head
   ```

## Usage

### Running the Application

To start the FastAPI application, run the following command:
```bash
uvicorn main:app --reload
```

This will start the server at `http://127.0.0.1:8000`. You can access the interactive API documentation at `http://127.0.0.1:8000/docs`.

### API Endpoints

#### Teacher Management

- **Create a Teacher**:
  - **Endpoint**: `POST /teachers/`
  - **Request Body**:
    ```json
    {
      "name": "John Doe",
      "email": "john.doe@example.com"
    }
    ```
  - **Response**: Returns the created teacher object.

- **Retrieve Teachers**:
  - **Endpoint**: `GET /teachers/`
  - **Response**: Returns a list of all teachers.

#### Student Management

- **Create a Student**:
  - **Endpoint**: `POST /students/`
  - **Request Body**:
    ```json
    {
      "name": "Jane Smith",
      "email": "jane.smith@example.com"
    }
    ```
  - **Response**: Returns the created student object.

- **Retrieve Students**:
  - **Endpoint**: `GET /students/`
  - **Response**: Returns a list of all students.

#### Course Management

- **Create a Course**:
  - **Endpoint**: `POST /courses/`
  - **Request Body**:
    ```json
    {
      "name": "Mathematics",
      "level": "Beginner"
    }
    ```
  - **Response**: Returns the created course object.

- **Retrieve Courses**:
  - **Endpoint**: `GET /courses/`
  - **Response**: Returns a list of all courses.

## Database Migrations

Database migrations are handled using Alembic. To create a new migration after making changes to the models, run:
```bash
alembic revision --autogenerate -m "Your migration message"
```
Then apply the migration with:
```bash
alembic upgrade head
```

## Conclusion

This Teacher Management System provides a streamlined approach to managing educational data. With the ability to manage teachers, students, and courses, it serves as a foundational tool for educational institutions.

For further assistance, please refer to the documentation or contact support.
```

This manual provides a comprehensive guide for users to understand the functionalities of the Teacher Management System, install the necessary dependencies, and utilize the application effectively.