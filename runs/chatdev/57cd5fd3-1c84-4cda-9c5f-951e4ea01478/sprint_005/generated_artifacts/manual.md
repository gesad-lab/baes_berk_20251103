```markdown
# Teacher Management System

A simple application for managing teachers, students, and courses using FastAPI and SQLAlchemy.

## Main Functions

This application provides the following functionalities:

- **Create Teacher**: Add a new teacher with a name and email.
- **Create Student**: Add a new student with a name and email.
- **Create Course**: Add a new course with a name and level.
- **Enroll Student in Course**: Enroll a student in a specific course.
- **Get Students**: Retrieve a list of all students.

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

## Database Migration

Before running the application, you need to set up the database schema. Use Alembic for database migrations:

1. **Run the Migration Script**:
   ```bash
   alembic upgrade head
   ```

This will create the necessary tables in your database, including the `teachers`, `students`, and `courses` tables.

## Running the Application

To start the application, run the following command:

```bash
uvicorn main:app --reload
```

This will start the FastAPI server, and you can access the API at `http://127.0.0.1:8000`.

## API Endpoints

Here are the available API endpoints:

- **Create a Teacher**:
  - **Endpoint**: `POST /teachers/`
  - **Request Body**:
    ```json
    {
      "name": "John Doe",
      "email": "john.doe@example.com"
    }
    ```

- **Create a Student**:
  - **Endpoint**: `POST /students/`
  - **Request Body**:
    ```json
    {
      "name": "Jane Doe",
      "email": "jane.doe@example.com"
    }
    ```

- **Create a Course**:
  - **Endpoint**: `POST /courses/`
  - **Request Body**:
    ```json
    {
      "name": "Mathematics",
      "level": "Beginner"
    }
    ```

- **Enroll Student in Course**:
  - **Endpoint**: `POST /students/{student_id}/courses/{course_id}/`
  - **Path Parameters**: `student_id`, `course_id`

- **Get Students**:
  - **Endpoint**: `GET /students/`
  - **Query Parameters**: `skip`, `limit`

## Conclusion

This application provides a simple interface for managing teachers, students, and courses. You can extend its functionality by adding more features as needed. For further documentation, please refer to the FastAPI and SQLAlchemy documentation.

Happy coding!
```