```markdown
# Course Management API

A simple API for managing students and courses using FastAPI and SQLAlchemy.

## Overview

This API allows users to create and manage students and courses. It provides endpoints for creating new students and courses, as well as retrieving lists of existing students and courses. The API is built using FastAPI, a modern web framework for building APIs with Python, and SQLAlchemy for database interactions.

## Main Functions

- **Create a Student**: Add a new student with a name and email.
- **Retrieve Students**: Get a list of all students in the database.
- **Create a Course**: Add a new course with a name and level.
- **Retrieve Courses**: Get a list of all courses in the database.

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
   pydantic
   alembic
   ```
   Then run:
   ```bash
   pip install -r requirements.txt
   ```

## Running the API

To run the API, use the following command:
```bash
uvicorn main:app --reload
```
This will start the FastAPI server, and you can access the API at `http://127.0.0.1:8000`.

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

- **Retrieve Students**
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
      "level": "Beginner"
    }
    ```
  - **Response**:
    ```json
    {
      "id": 1,
      "name": "Mathematics",
      "level": "Beginner"
    }
    ```

- **Retrieve Courses**
  - **Endpoint**: `GET /courses/`
  - **Response**:
    ```json
    [
      {
        "id": 1,
        "name": "Mathematics",
        "level": "Beginner"
      }
    ]
    ```

## Database Migration

To ensure that the database schema is up-to-date, you can use Alembic for migrations. The existing Student data will be preserved during the migration process.

1. **Create Migration Script**:
   Run the following command to create a new migration script:
   ```bash
   alembic revision --autogenerate -m "Add Course table"
   ```

2. **Apply Migrations**:
   To apply the migrations, run:
   ```bash
   alembic upgrade head
   ```

## Conclusion

This API provides a straightforward way to manage students and courses. For further customization or additional features, feel free to modify the code as needed. If you have any questions or need support, please reach out to the development team.

```
