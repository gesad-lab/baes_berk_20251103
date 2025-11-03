```markdown
# Teacher Management System

A simple API for managing Teachers, Students, and Courses using FastAPI and SQLAlchemy.

## Main Functions

This software provides the following main functionalities:

- **Create and Manage Teachers**: Add new teachers with their names and email addresses.
- **Create and Manage Students**: Add new students with their names and email addresses.
- **Create and Manage Courses**: Add new courses with their names and levels.
- **Link Students to Courses**: Associate students with multiple courses.
- **Retrieve Data**: Get lists of teachers, students, and courses.

## Quick Install

To set up the environment and install the necessary dependencies, follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone <repository-url>
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
   Run the following command to create the initial database schema:
   ```bash
   python -m database
   ```

5. **Run the Application**:
   Start the FastAPI application using:
   ```bash
   uvicorn main:app --reload
   ```

## How to Use the API

### Base URL

The API can be accessed at `http://127.0.0.1:8000`.

### API Endpoints

#### Teachers

- **Create a Teacher**:
  - **Endpoint**: `POST /teachers/`
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
      "name": "John Doe",
      "email": "john.doe@example.com"
    }
    ```

- **Get All Teachers**:
  - **Endpoint**: `GET /teachers/`
  - **Response**:
    ```json
    [
      {
        "name": "John Doe",
        "email": "john.doe@example.com"
      }
    ]
    ```

#### Students

- **Create a Student**:
  - **Endpoint**: `POST /students/`
  - **Request Body**:
    ```json
    {
      "name": "Jane Smith",
      "email": "jane.smith@example.com"
    }
    ```
  - **Response**:
    ```json
    {
      "name": "Jane Smith",
      "email": "jane.smith@example.com"
    }
    ```

- **Get All Students**:
  - **Endpoint**: `GET /students/`
  - **Response**:
    ```json
    [
      {
        "name": "Jane Smith",
        "email": "jane.smith@example.com"
      }
    ]
    ```

#### Courses

- **Create a Course**:
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
      "name": "Mathematics",
      "level": "Beginner"
    }
    ```

- **Get All Courses**:
  - **Endpoint**: `GET /courses/`
  - **Response**:
    ```json
    [
      {
        "name": "Mathematics",
        "level": "Beginner"
      }
    ]
    ```

### Database Migration

To add the Teacher entity to the database without losing existing Student and Course data, run the following Alembic command after modifying the `env.py` migration script:

```bash
alembic upgrade head
```

This will create the `teachers` table in the database while preserving existing data.

## Conclusion

This Teacher Management System provides a straightforward way to manage teachers, students, and courses through a RESTful API. For further details, please refer to the code documentation or the FastAPI documentation.
```