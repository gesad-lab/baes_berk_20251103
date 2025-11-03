```markdown
# Course Management System

A simple web application for managing courses and students, built using FastAPI and SQLAlchemy.

## Overview

This application allows users to create and manage courses and students. The main functionalities include:

- Creating new courses with a name and level.
- Retrieving a list of all courses.
- Creating new students with a name and email.
- Retrieving a list of all students.

## Quick Install

To set up the environment and install the necessary dependencies, follow these steps:

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Create a virtual environment (optional but recommended):**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install the required dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## Requirements

The following dependencies are required for the application:

- **fastapi**: The web framework used to build the API.
- **uvicorn**: The ASGI server for running the FastAPI application.
- **sqlalchemy**: The ORM used for database interactions.
- **alembic**: The migration tool for handling database schema changes.
- **pydantic**: The data validation and settings management library used for defining schemas.

Make sure to adjust the version numbers according to your project's requirements or the latest stable versions available at the time of installation.

## Database Setup

The application uses SQLite as the database. The database schema is managed using Alembic for migrations. 

### Running Migrations

To create the necessary database tables, run the following command:

```bash
alembic upgrade head
```

This command will apply all the migrations, including creating the `students` and `courses` tables.

## Usage

### Running the Application

To start the FastAPI application, use the following command:

```bash
uvicorn main:app --reload
```

This will start the server at `http://127.0.0.1:8000`.

### API Endpoints

#### Students

- **Create a Student**
  - **Endpoint:** `POST /students/`
  - **Request Body:**
    ```json
    {
      "name": "John Doe",
      "email": "john.doe@example.com"
    }
    ```
  - **Response:**
    ```json
    {
      "id": 1,
      "name": "John Doe",
      "email": "john.doe@example.com"
    }
    ```

- **Get All Students**
  - **Endpoint:** `GET /students/`
  - **Response:**
    ```json
    [
      {
        "id": 1,
        "name": "John Doe",
        "email": "john.doe@example.com"
      }
    ]
    ```

#### Courses

- **Create a Course**
  - **Endpoint:** `POST /courses/`
  - **Request Body:**
    ```json
    {
      "name": "Mathematics",
      "level": "Beginner"
    }
    ```
  - **Response:**
    ```json
    {
      "id": 1,
      "name": "Mathematics",
      "level": "Beginner"
    }
    ```

- **Get All Courses**
  - **Endpoint:** `GET /courses/`
  - **Response:**
    ```json
    [
      {
        "id": 1,
        "name": "Mathematics",
        "level": "Beginner"
      }
    ]
    ```

## Conclusion

This Course Management System provides a simple interface for managing students and courses. You can extend its functionality by adding more features as needed. For any issues or feature requests, please contact the development team.
```