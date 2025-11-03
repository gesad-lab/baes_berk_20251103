Here's a detailed user manual for the software, formatted in Markdown as requested:

```markdown
# Course Management System

A simple API for managing students and courses, built using FastAPI and SQLAlchemy.

## Overview

This software allows users to create and manage `Student` and `Course` entities. The main functionalities include creating new students and courses, as well as retrieving lists of existing students and courses. The application is designed to be easy to use and extendable for future features.

## Main Functions

- **Create Student**: Add a new student with a name and email.
- **Retrieve Students**: Get a list of all registered students.
- **Create Course**: Add a new course with a name and level.
- **Retrieve Courses**: Get a list of all available courses.

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

## Running the Application

1. **Initialize the Database**:
   Before running the application, ensure the database is set up. You can do this by running the following command to create the initial database schema:
   ```bash
   python -m alembic upgrade head
   ```

2. **Start the FastAPI Application**:
   You can run the application using Uvicorn:
   ```bash
   uvicorn main:app --reload
   ```

3. **Access the API**:
   Once the server is running, you can access the API at `http://127.0.0.1:8000`. The interactive API documentation is available at `http://127.0.0.1:8000/docs`.

## API Endpoints

### Students

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

- **Retrieve Students**:
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

- **Retrieve Courses**:
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

## Conclusion

This Course Management System provides a simple yet effective way to manage students and courses. With the provided API, you can easily extend the functionality to suit your needs. For any issues or feature requests, please reach out to the development team.

Happy coding!
```

This manual provides a comprehensive overview of the software, its installation process, and how to use the API effectively.