```markdown
# Teacher Management System

A simple API for managing teachers, students, and courses using FastAPI and SQLAlchemy.

## Main Functions

This software provides the following main functionalities:

- **Create and manage Teachers**: Add new teachers with their names and email addresses.
- **Create and manage Students**: Add new students with their names and email addresses.
- **Create and manage Courses**: Add new courses with their names and levels.
- **Enroll Students in Courses**: Associate students with courses they are enrolled in.
- **Retrieve information**: Get lists of teachers, students, and courses.

## Installation

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
   Create a `requirements.txt` file with the following content:
   ```
   fastapi
   uvicorn
   sqlalchemy
   pydantic
   alembic
   ```
   Then, run:
   ```bash
   pip install -r requirements.txt
   ```

## Database Migration

Before running the application, you need to set up the database schema. Use Alembic to manage database migrations:

1. **Create a new migration script**:
   ```bash
   alembic revision -m "Create Teacher table and add email field to students"
   ```

2. **Run the migration**:
   ```bash
   alembic upgrade head
   ```

## Running the Application

To start the FastAPI application, run the following command:
```bash
uvicorn main:app --reload
```

The application will be available at `http://127.0.0.1:8000`.

## Using the API

You can interact with the API using tools like Postman or curl. Here are some example endpoints:

### Create a Teacher
- **Endpoint**: `POST /teachers/`
- **Request Body**:
  ```json
  {
    "name": "John Doe",
    "email": "john.doe@example.com"
  }
  ```

### Get All Teachers
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

### Create a Student
- **Endpoint**: `POST /students/`
- **Request Body**:
  ```json
  {
    "name": "Jane Smith",
    "email": "jane.smith@example.com"
  }
  ```

### Get All Students
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

### Create a Course
- **Endpoint**: `POST /courses/`
- **Request Body**:
  ```json
  {
    "name": "Mathematics",
    "level": "Beginner"
  }
  ```

### Get All Courses
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

### Enroll a Student in a Course
- **Endpoint**: `POST /students/{student_id}/courses/{course_id}`
- **Response**:
  ```json
  {
    "student_id": 1,
    "course_id": 1
  }
  ```

## Conclusion

This Teacher Management System provides a simple yet effective way to manage teachers, students, and courses. You can extend its functionalities as needed to fit your requirements. For more detailed information on FastAPI, SQLAlchemy, and Pydantic, please refer to their official documentation.
```