Here's a detailed user manual for the software, formatted in Markdown as requested:

```markdown
# Course Management System

A simple web application for managing students and courses, built with FastAPI and SQLAlchemy.

## Overview

This application allows users to create and manage students and courses. It provides a RESTful API for interacting with the data, including functionalities for adding students, adding courses, and retrieving lists of both.

## Main Functions

- **Create Student**: Add a new student with a name and email.
- **Read Students**: Retrieve a list of all students.
- **Create Course**: Add a new course with a name and level.
- **Read Courses**: Retrieve a list of all courses.

## Quick Install

To set up the environment and install the necessary dependencies, follow these steps:

1. **Clone the repository** (if applicable):
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Create a virtual environment** (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## Environment Dependencies

The following dependencies are required for the application:

- **fastapi**: The web framework used to create the API.
- **uvicorn**: An ASGI server for running FastAPI applications.
- **sqlalchemy**: The ORM used for database interactions.
- **pydantic**: Used for data validation and settings management.
- **alembic**: A database migration tool for SQLAlchemy.

Make sure to adjust the version numbers in `requirements.txt` as needed based on your project's requirements or compatibility.

## How to Use the Application

1. **Run the Application**:
   Start the FastAPI application using Uvicorn:
   ```bash
   uvicorn main:app --reload
   ```
   The application will be running at `http://127.0.0.1:8000`.

2. **Interact with the API**:
   You can use tools like Postman or cURL to interact with the API endpoints.

   - **Create a Student**:
     ```http
     POST /students/
     Content-Type: application/json

     {
       "name": "John Doe",
       "email": "john.doe@example.com"
     }
     ```

   - **Read Students**:
     ```http
     GET /students/
     ```

   - **Create a Course**:
     ```http
     POST /courses/
     Content-Type: application/json

     {
       "name": "Mathematics",
       "level": "Beginner"
     }
     ```

   - **Read Courses**:
     ```http
     GET /courses/
     ```

3. **Database Migration**:
   To apply database migrations, run the migration script using Alembic:
   ```bash
   alembic upgrade head
   ```

## Documentation

For more detailed documentation, including examples and API references, please refer to the FastAPI documentation [here](https://fastapi.tiangolo.com/).

## Support

If you encounter any issues or need further assistance, please reach out to our support team.

```

This manual provides a comprehensive overview of the application, installation instructions, usage guidelines, and links to further documentation. Let me know if you need any modifications or additional information!