Here's a detailed user manual for the software, formatted in Markdown as requested:

```markdown
# Teacher Management System

A simple API for managing teachers, students, and courses in an educational environment.

## Main Functions

This application provides the following functionalities:

- **Create and manage Teachers**: Add new teachers with their names and email addresses.
- **Create and manage Students**: Add new students with their names and email addresses.
- **Create and manage Courses**: Add new courses with their names and levels.
- **Enroll Students in Courses**: Enroll students in specific courses.
- **Retrieve lists of Teachers, Students, and Courses**: Fetch all teachers, students, or courses with pagination support.

## Quick Install

To set up the environment and install the necessary dependencies, follow these steps:

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd student_app
   ```

2. **Create a virtual environment** (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies**:
   ```bash
   pip install fastapi sqlalchemy alembic
   ```

4. **Initialize the database**:
   ```bash
   python main.py
   ```

## How to Use the Application

### Starting the Server

To start the FastAPI server, run the following command in the terminal:
```bash
uvicorn main:app --reload
```
This will start the server at `http://127.0.0.1:8000`.

### API Endpoints

The application exposes several API endpoints for managing teachers, students, and courses.

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
      "id": 1,
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
        "id": 1,
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
      "id": 1,
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
        "id": 1,
        "name": "Mathematics",
        "level": "Beginner"
      }
    ]
    ```

#### Enroll Students in Courses

- **Enroll a Student**:
  - **Endpoint**: `POST /students/{student_id}/courses/{course_id}/enroll`
  - **Response**:
    ```json
    {
      "message": "Student enrolled in course successfully"
    }
    ```

## Database Migration

The application uses Alembic for database migrations. To create the Teacher table while preserving existing Student and Course data, run:
```bash
alembic upgrade head
```

## Conclusion

This Teacher Management System provides a simple and effective way to manage educational entities. For further customization or enhancements, feel free to modify the codebase as needed.
```

This manual provides a comprehensive overview of the software's functionality, installation instructions, and usage guidelines, ensuring users can effectively utilize the Teacher Management System.