# Student Management System

A simple application for managing student records, including the ability to create and retrieve student information.

## Quick Install

To get started with the Student Management System, you need to install the required environment dependencies. You can do this using pip:

```bash
pip install fastapi sqlalchemy pydantic alembic
```

Alternatively, if you are using conda, you can install the dependencies as follows:

```bash
conda install fastapi sqlalchemy pydantic alembic -c conda-forge
```

## 🤔 What is this?

The Student Management System allows users to manage student records effectively. The main features of the application include:

- **Create Student**: Add a new student record with a name and email address.
- **Read Students**: Retrieve a list of all students in the system.

This application uses FastAPI for the web framework, SQLAlchemy for database interactions, and Pydantic for data validation.

## 📖 Main Functions

### 1. Create Student

To create a new student, send a POST request to the `/students/` endpoint with the following JSON payload:

```json
{
  "name": "John Doe",
  "email": "john.doe@example.com"
}
```

### 2. Read Students

To retrieve a list of students, send a GET request to the `/students/` endpoint. You can also specify optional query parameters `skip` and `limit` to paginate the results.

Example GET request:

```
GET /students/?skip=0&limit=10
```

## 🛠️ Database Migration

The application uses Alembic for database migrations. When you add the email field to the Student entity, the migration script ensures that existing student data is preserved. 

To run the migration, execute the following command:

```bash
alembic upgrade head
```

This will add the email column to the students table and populate existing records with a default value.

## 🚀 How to Run the Application

To run the FastAPI application, execute the following command:

```bash
uvicorn main:app --reload
```

This will start the server, and you can access the API at `http://127.0.0.1:8000`.

## 📚 Documentation

For more detailed documentation on FastAPI, SQLAlchemy, and Pydantic, please refer to the following links:

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [SQLAlchemy Documentation](https://docs.sqlalchemy.org/)
- [Pydantic Documentation](https://pydantic-docs.helpmanual.io/)

Feel free to explore the codebase and modify it according to your needs. Happy coding!