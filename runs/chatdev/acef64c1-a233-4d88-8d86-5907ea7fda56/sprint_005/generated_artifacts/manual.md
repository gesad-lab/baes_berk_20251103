```markdown
# Teacher Management API

A FastAPI application for managing teachers, students, and courses in an educational environment.

## Main Functions

This application provides the following functionalities:

- **Create and Retrieve Teachers**: You can create new teachers and retrieve a list of all teachers.
- **Create and Retrieve Students**: You can create new students and retrieve a list of all students along with their enrolled courses.
- **Create Courses and Enroll Students**: You can create new courses and enroll students in those courses.

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
   Create a `requirements.txt` file with the following content:
   ```
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

## Database Setup

The application uses SQLite for the database. To create the database and tables, run the following command:

```bash
python -c "from database import create_database; create_database()"
```

## Running the Application

To start the FastAPI application, use the following command:

```bash
uvicorn main:app --reload
```

This will start the server at `http://127.0.0.1:8000`. You can access the interactive API documentation at `http://127.0.0.1:8000/docs`.

## API Endpoints

### Teachers

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
      "id": 1,
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
        "id": 1,
        "name": "John Doe",
        "email": "john.doe@example.com"
      }
    ]
    ```

### Students

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
      "id": 1,
      "name": "Jane Smith",
      "email": "jane.smith@example.com",
      "courses": []
    }
    ```

- **Get All Students**:
  - **Endpoint**: `GET /students/`
  - **Response**:
    ```json
    [
      {
        "id": 1,
        "name": "Jane Smith",
        "email": "jane.smith@example.com",
        "courses": []
      }
    ]
    ```

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
  - **Response**:
    ```json
    {
      "id": 1,
      "name": "Mathematics",
      "level": "Beginner"
    }
    ```

- **Enroll a Student in a Course**:
  - **Endpoint**: `POST /students/{student_id}/courses/{course_id}`
  - **Response**:
    ```json
    {
      "message": "Student enrolled in course successfully"
    }
    ```

## Database Migration

To add the Teacher entity to the database schema, run the migration script using Alembic. Ensure you have Alembic set up and configured correctly.

```bash
alembic upgrade head
```

This will create the `teachers` table while preserving existing `students` and `courses` data.

## Conclusion

This application provides a simple yet effective way to manage teachers, students, and courses in an educational setting. For further customization and enhancements, feel free to modify the code as needed.
```