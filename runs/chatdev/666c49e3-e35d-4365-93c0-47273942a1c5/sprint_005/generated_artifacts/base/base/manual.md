Here’s a detailed user manual for the software, including an introduction to its main functions, installation instructions, and usage guidelines.

```markdown
# Course Management System

A simple API for managing students and courses using FastAPI and SQLAlchemy.

## Overview

The Course Management System allows users to create and manage students and courses. It provides a RESTful API to perform operations such as creating and retrieving students and courses. The system is built using FastAPI, SQLAlchemy for ORM, and Alembic for database migrations.

### Main Functions

- **Create Student**: Add a new student with a name and email.
- **Get Students**: Retrieve a list of students with pagination support.
- **Create Course**: Add a new course with a name and level.
- **Get Courses**: Retrieve a list of courses with pagination support.

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

## Database Initialization

Before running the application, ensure the database is initialized:

1. **Run the Application**:
   ```bash
   python main.py
   ```

2. **Database Migration**:
   If you need to create the initial database schema, run the Alembic migration:
   ```bash
   alembic upgrade head
   ```

## Usage

### API Endpoints

The API provides the following endpoints:

- **Students**:
  - `POST /students/`: Create a new student.
    - Request Body:
      ```json
      {
        "name": "John Doe",
        "email": "john.doe@example.com"
      }
      ```
    - Response:
      ```json
      {
        "id": 1,
        "name": "John Doe",
        "email": "john.doe@example.com"
      }
      ```

  - `GET /students/`: Retrieve a list of students.
    - Query Parameters: `skip`, `limit`
    - Response:
      ```json
      [
        {
          "id": 1,
          "name": "John Doe",
          "email": "john.doe@example.com"
        }
      ]
      ```

- **Courses**:
  - `POST /courses/`: Create a new course.
    - Request Body:
      ```json
      {
        "name": "Mathematics",
        "level": "Beginner"
      }
      ```
    - Response:
      ```json
      {
        "id": 1,
        "name": "Mathematics",
        "level": "Beginner"
      }
      ```

  - `GET /courses/`: Retrieve a list of courses.
    - Query Parameters: `skip`, `limit`
    - Response:
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

This Course Management System provides a simple yet effective way to manage students and courses through a RESTful API. For further customization and enhancements, feel free to modify the codebase as per your requirements.

For any issues or support, please reach out to the development team.
```

This manual provides a comprehensive guide for users to understand the software's functionality, installation, and usage.