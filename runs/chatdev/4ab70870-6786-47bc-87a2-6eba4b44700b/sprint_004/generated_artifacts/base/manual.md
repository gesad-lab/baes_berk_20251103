```markdown
# Course Management API

A simple API for managing students and courses using FastAPI and SQLAlchemy.

## Overview

This API allows users to create and manage student and course records. It supports the following functionalities:

- Create and retrieve student records.
- Create and retrieve course records.
- The database schema is designed to preserve existing student data while adding new course functionality.

## Main Functions

### Student Management

- **Create Student**: Add a new student with a name and email.
- **Retrieve Students**: Get a list of students with pagination support.

### Course Management

- **Create Course**: Add a new course with a name and level.
- **Retrieve Courses**: Get a list of courses with pagination support.

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
   pydantic
   alembic
   ```
   Then, run:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. **Run the Application**:
   Start the FastAPI application using Uvicorn:
   ```bash
   uvicorn main:app --reload
   ```

2. **Access the API**:
   Open your browser and navigate to `http://127.0.0.1:8000/docs` to access the interactive API documentation provided by FastAPI.

### API Endpoints

#### Student Endpoints

- **Create a Student**:
  - **POST** `/students/`
  - **Request Body**:
    ```json
    {
      "name": "John Doe",
      "email": "john.doe@example.com"
    }
    ```

- **Retrieve Students**:
  - **GET** `/students/`
  - **Query Parameters**: `skip` (int), `limit` (int)

#### Course Endpoints

- **Create a Course**:
  - **POST** `/courses/`
  - **Request Body**:
    ```json
    {
      "name": "Mathematics",
      "level": "Beginner"
    }
    ```

- **Retrieve Courses**:
  - **GET** `/courses/`
  - **Query Parameters**: `skip` (int), `limit` (int)

## Database Migration

The application uses Alembic for database migrations. To apply the migrations, run the following command:
```bash
alembic upgrade head
```

This will create the necessary tables in the database, including the `students` and `courses` tables.

## Conclusion

This Course Management API provides a straightforward way to manage students and courses. With FastAPI's intuitive design and SQLAlchemy's powerful ORM capabilities, you can easily extend and modify the application to fit your needs.
```
