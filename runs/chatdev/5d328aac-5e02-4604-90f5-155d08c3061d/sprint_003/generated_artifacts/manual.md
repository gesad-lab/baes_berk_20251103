```markdown
# Course Management System

A simple API for managing students and courses, built using FastAPI and SQLAlchemy.

## Overview

This software allows users to create and manage students and courses through a RESTful API. The main functionalities include adding new students, retrieving a list of students, adding new courses, and retrieving a list of courses. The database is designed to preserve existing student data while adding new course entities.

## Main Functions

- **Add Student**: Create a new student with a name and email.
- **Retrieve Students**: Get a list of all students in the database.
- **Add Course**: Create a new course with a name and level.
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
   ```bash
   pip install fastapi sqlalchemy alembic
   ```

4. **Set Up the Database**:
   The application uses SQLite for the database. The database will be created automatically on startup.

## Usage

1. **Run the Application**:
   Start the FastAPI application using the following command:
   ```bash
   uvicorn main:app --reload
   ```

2. **Access the API**:
   The API will be available at `http://127.0.0.1:8000`. You can use tools like Postman or curl to interact with the API.

3. **API Endpoints**:
   - **Add Student**:
     - **Endpoint**: `POST /students/`
     - **Request Body**:
       ```json
       {
         "name": "John Doe",
         "email": "john.doe@example.com"
       }
       ```
   - **Retrieve Students**:
     - **Endpoint**: `GET /students/`
   - **Add Course**:
     - **Endpoint**: `POST /courses/`
     - **Request Body**:
       ```json
       {
         "name": "Mathematics",
         "level": "Intermediate"
       }
       ```
   - **Retrieve Courses**:
     - **Endpoint**: `GET /courses/`

## Database Migration

The application uses Alembic for database migrations. To create the necessary tables, run the following command:
```bash
alembic upgrade head
```

This will create the `courses` table while preserving existing student data.

## Documentation

For more detailed information on FastAPI and SQLAlchemy, please refer to the following resources:

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [SQLAlchemy Documentation](https://docs.sqlalchemy.org/en/14/)

## Support

If you encounter any issues or have questions, please reach out through our support channels.

```
