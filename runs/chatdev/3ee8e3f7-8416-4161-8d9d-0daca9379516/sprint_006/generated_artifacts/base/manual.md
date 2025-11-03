Here's a detailed user manual for the software, formatted in Markdown as requested:

```markdown
# Teacher Management System

A simple application for managing teachers, students, and courses.

## Introduction

The Teacher Management System allows users to create and manage entities related to teachers, students, and courses. This application is built using FastAPI and SQLAlchemy, providing a RESTful API for seamless interaction with the database.

### Main Functions

- **Create and Manage Teachers**: Add new teachers with their names and email addresses.
- **Create and Manage Students**: Add new students and enroll them in courses.
- **Create and Manage Courses**: Define courses and associate them with students.
- **Retrieve Information**: Fetch lists of teachers, students, and courses.

## Quick Install

To set up the environment and install the necessary dependencies, follow these steps:

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

## Database Migration

Before running the application, ensure that the database schema is up to date. The migration script will create the necessary tables while preserving existing data for students and courses.

To run the migration, use the following command:
```bash
alembic upgrade head
```

## How to Use the Application

### Starting the Application

To start the FastAPI application, run:
```bash
uvicorn main:app --reload
```
This will start the server at `http://127.0.0.1:8000`.

### API Endpoints

The application exposes several API endpoints for interacting with teachers, students, and courses.

#### Teacher Endpoints

- **Create a Teacher**
  - **Endpoint**: `POST /teachers/`
  - **Request Body**:
    ```json
    {
      "name": "John Doe",
      "email": "john.doe@example.com"
    }
    ```
  - **Response**: Returns the created teacher object.

- **Get All Teachers**
  - **Endpoint**: `GET /teachers/`
  - **Response**: Returns a list of all teachers.

#### Student Endpoints

- **Create a Student**
  - **Endpoint**: `POST /students/`
  - **Request Body**:
    ```json
    {
      "name": "Jane Smith",
      "email": "jane.smith@example.com"
    }
    ```
  - **Response**: Returns the created student object.

- **Get All Students**
  - **Endpoint**: `GET /students/`
  - **Response**: Returns a list of all students.

#### Course Endpoints

- **Create a Course**
  - **Endpoint**: `POST /courses/`
  - **Request Body**:
    ```json
    {
      "name": "Mathematics",
      "level": "Intermediate"
    }
    ```
  - **Response**: Returns the created course object.

- **Get All Courses**
  - **Endpoint**: `GET /courses/`
  - **Response**: Returns a list of all courses.

### Example Usage

1. **Creating a Teacher**:
   ```bash
   curl -X POST "http://127.0.0.1:8000/teachers/" -H "Content-Type: application/json" -d '{"name": "John Doe", "email": "john.doe@example.com"}'
   ```

2. **Retrieving All Teachers**:
   ```bash
   curl -X GET "http://127.0.0.1:8000/teachers/"
   ```

## Conclusion

The Teacher Management System is a powerful tool for managing educational entities. With its RESTful API, users can easily create, retrieve, and manage teachers, students, and courses. For further information, please refer to the codebase and explore the API documentation provided by FastAPI.

```

This manual provides a comprehensive overview of the application, including installation instructions, usage examples, and API endpoints. It should serve as a helpful guide for users to effectively utilize the Teacher Management System.