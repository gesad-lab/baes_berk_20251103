Here's a detailed user manual for the software, including an introduction to its main functions, installation instructions, and usage guidelines.

```markdown
# Student Management Application

A simple web application for managing students and courses.

## Overview

The Student Management Application allows users to create and manage student and course records. It provides a RESTful API built with FastAPI, enabling easy integration with front-end applications or other services. The application supports operations for creating and retrieving students and courses, ensuring that all data is stored in a SQLite database.

## Main Functions

- **Student Management**:
  - Create new students with their names and email addresses.
  - Retrieve a list of existing students.

- **Course Management**:
  - Create new courses with their names and levels.
  - Retrieve a list of existing courses.

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
   ```bash
   pip install fastapi[all] sqlalchemy pydantic
   ```

4. **Run the Application**:
   ```bash
   uvicorn main:app --reload
   ```

   The application will be accessible at `http://127.0.0.1:8000`.

## API Endpoints

### Student Endpoints

- **Create a Student**:
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

- **Get Students**:
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

### Course Endpoints

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

- **Get Courses**:
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

The application uses SQLAlchemy to manage the database schema. When you run the application for the first time, it will automatically create the necessary tables for students and courses in the SQLite database (`students.db`). Existing student data will be preserved during any future migrations.

## Conclusion

This Student Management Application provides a straightforward way to manage student and course data through a RESTful API. For further customization or enhancements, feel free to modify the codebase as needed.

For any issues or support, please reach out to the development team.
```

This manual provides a comprehensive guide for users to understand the application, install it, and utilize its features effectively.