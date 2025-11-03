```markdown
# Course Management API

A FastAPI application for managing students and courses in a database.

## Overview

This application allows users to create and manage students and courses. The main features include:

- **Create Student**: Add a new student with a name and email.
- **Retrieve Students**: Get a list of all registered students.
- **Create Course**: Add a new course with a name and level.
- **Database Migration**: Automatically updates the database schema to include the new Course entity while preserving existing Student data.

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

3. **Install the required dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## Requirements

Ensure the following dependencies are included in your `requirements.txt`:

```
fastapi
uvicorn
sqlalchemy
alembic
pydantic
```

## Running the Application

To start the FastAPI application, run the following command:

```bash
uvicorn main:app --reload
```

This will start the server at `http://127.0.0.1:8000`. You can access the interactive API documentation at `http://127.0.0.1:8000/docs`.

## API Endpoints

### Students

- **Create a Student**
  - **Endpoint**: `POST /students/`
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

- **Retrieve All Students**
  - **Endpoint**: `GET /students/`
  - **Response**:
    ```json
    [
      {
        "id": 1,
        "name": "John Doe",
        "email": "john.doe@example.com"
      }
    ]
    ```

### Courses

- **Create a Course**
  - **Endpoint**: `POST /courses/`
  - **Request Body**:
    ```json
    {
      "name": "Mathematics",
      "level": "Intermediate"
    }
    ```
  - **Response**:
    ```json
    {
      "id": 1,
      "name": "Mathematics",
      "level": "Intermediate"
    }
    ```

## Database Migration

To apply the database migration that adds the Course entity, run the following command:

```bash
alembic upgrade head
```

This command will create the `courses` table in the database while preserving existing Student data.

## Conclusion

This application provides a simple yet powerful way to manage students and courses. For further customization or enhancements, feel free to modify the code as needed. If you encounter any issues or have questions, please reach out for support.
```