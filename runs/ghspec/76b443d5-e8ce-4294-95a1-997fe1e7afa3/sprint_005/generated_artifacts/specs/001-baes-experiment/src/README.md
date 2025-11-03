# Updated README.md

# Project Title

## Overview

This project is an API application designed to manage educational entities such as Teachers, Students, and Courses. It utilizes FastAPI for building the API and SQLAlchemy for ORM with a relational database.

## API Endpoints

### Teacher Management

#### Create a Teacher

- **Method**: POST
- **Endpoint**: `/teachers`
- **Request Body**: 
  ```json
  {
    "name": "string (required)",
    "email": "string (required)"
  }
  ```
- **Response**: On successful creation, returns the created Teacher's details:
  ```json
  {
    "id": "integer",
    "name": "string",
    "email": "string"
  }
  ```
- **Error Responses**:
  - **400 Bad Request**: If the `name` field is missing.
  - **400 Bad Request**: If the `email` field is missing or incorrectly formatted.

### Database Schema

The application includes a `Teacher` table with the following schema to support the teacher management functionality:

- `id` (primary key, auto-increment)
- `name` (string, required)
- `email` (string, required, unique)

### Migrations

The migration process ensures that existing `Student` and `Course` data remain intact during the addition of the new `Teacher` table. The migrations can be applied automatically at startup.

```python
@app.on_event("startup")
async def startup():
    alembic_cfg = Config("alembic.ini")
    command.upgrade(alembic_cfg, "head")  # Ensure latest migrations run on startup
```

### Automatic API Documentation

Automatic API documentation is generated via FastAPI and can be accessed at `/docs`.

## Success Criteria

1. The application should successfully create a Teacher when valid `name` and `email` are provided.
2. A valid JSON response should include the created Teacher's details.
3. If the `name` field is missing, an appropriate error response must be returned.
4. An error response should also be returned for missing or inaccurately formatted `email` fields.
5. The database schema should be updated successfully without loss of any existing `Student` and `Course` data.

## Testing

To ensure reliability, comprehensive tests should be developed for unit testing and integration testing of the new functionalities.

## Install and Setup

To run this project, you will need to have Python installed. You can set up your environment using the following commands:

```bash
# Clone the repository
git clone <repository-url>

# Move into the project directory
cd <project-directory>

# Install dependencies
pip install -r requirements.txt

# Run database migrations if required
alembic upgrade head

# Start the FastAPI application
uvicorn src.main:app --reload
```

## Conclusion

This README should help you understand how to interact with the Teacher management features of the API. For further detail, access the API documentation at `/docs`.