Here's a detailed user manual for the software, including an introduction to its main functions, installation instructions, and usage guidelines.

```markdown
# Course Management System

A simple API for managing students and courses in an educational environment.

## Overview

The Course Management System allows users to create and manage students and courses. The main functionalities include:

- **Creating Students**: Add new students to the database with their name and email.
- **Retrieving Students**: Fetch a list of existing students.
- **Creating Courses**: Add new courses with a name and level.
- **Database Management**: The system uses SQLite for data storage and supports migrations to update the database schema.

## Quick Install

To get started with the Course Management System, you need to install the required dependencies. You can do this using pip:

```bash
pip install fastapi sqlalchemy alembic pydantic
```

## Getting Started

### 1. Clone the Repository

Clone the repository to your local machine:

```bash
git clone <repository-url>
cd student_app
```

### 2. Set Up the Database

The application uses SQLite as its database. The database will be created automatically when you run the application for the first time.

### 3. Run the Application

You can run the application using the following command:

```bash
uvicorn main:app --reload
```

This will start the FastAPI application on `http://127.0.0.1:8000`.

## API Endpoints

### Students

- **Create a Student**

  **Endpoint**: `POST /students/`

  **Request Body**:
  ```json
  {
    "name": "John Doe",
    "email": "john.doe@example.com"
  }
  ```

  **Response**:
  ```json
  {
    "id": 1,
    "name": "John Doe",
    "email": "john.doe@example.com"
  }
  ```

- **Get Students**

  **Endpoint**: `GET /students/`

  **Query Parameters**:
  - `skip`: Number of records to skip (default is 0).
  - `limit`: Maximum number of records to return (default is 10).

  **Response**:
  ```json
  [
    {
      "id": 1,
      "name": "John Doe",
      "email": "john.doe@example.com"
    },
    ...
  ]
  ```

### Courses

- **Create a Course**

  **Endpoint**: `POST /courses/`

  **Request Body**:
  ```json
  {
    "name": "Mathematics",
    "level": "Intermediate"
  }
  ```

  **Response**:
  ```json
  {
    "id": 1,
    "name": "Mathematics",
    "level": "Intermediate"
  }
  ```

## Database Migration

The application uses Alembic for database migrations. To create the Course table, run the following command:

```bash
alembic upgrade head
```

This command will apply the latest migrations and create the `courses` table while preserving existing student data.

## Conclusion

This Course Management System provides a straightforward way to manage students and courses. For further customization or feature requests, feel free to reach out to the development team.

For more detailed documentation on FastAPI, SQLAlchemy, and Alembic, please refer to their respective official documentation.

```

This manual provides a comprehensive overview of the Course Management System, including installation steps, API usage, and migration instructions. Let me know if you need any further modifications or additional information!