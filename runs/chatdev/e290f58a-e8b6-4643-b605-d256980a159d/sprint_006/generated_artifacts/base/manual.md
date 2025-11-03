```markdown
# Teacher Management System

A simple application for managing teachers, students, and courses using FastAPI and SQLAlchemy.

## Overview

This application allows you to create and manage entities for teachers, students, and courses. The main functionalities include creating a Teacher entity with required fields (name and email), as well as managing existing Student and Course data without data loss during database migrations.

## Main Functions

- **Create Teacher**: Allows you to create a new teacher with a name and email.
- **Manage Students**: Create and retrieve student information.
- **Manage Courses**: Create and retrieve course information.
- **Database Migration**: Safely update the database schema to include the Teacher table while preserving existing Student and Course data.

## Installation

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
   Create a `requirements.txt` file with the following content:
   ```
   fastapi
   uvicorn
   sqlalchemy
   pydantic
   ```
   Then run:
   ```bash
   pip install -r requirements.txt
   ```

## Running the Application

To run the FastAPI application, execute the following command in your terminal:
```bash
uvicorn main:app --reload
```

This will start the server, and you can access the API at `http://127.0.0.1:8000`.

## API Endpoints

### Create a Teacher

- **Endpoint**: `POST /teachers`
- **Request Body**:
  ```json
  {
    "name": "John Doe",
    "email": "john.doe@example.com"
  }
  ```
- **Response**:
  - **201 Created**: Returns the created teacher object with an ID.
  
### Example Request

Using `curl`:
```bash
curl -X POST "http://127.0.0.1:8000/teachers" -H "Content-Type: application/json" -d '{"name": "John Doe", "email": "john.doe@example.com"}'
```

### Database Migration

To create the Teacher table and ensure existing Student and Course data is preserved, run the migration script:
```bash
python main.py
```

This will execute the `upgrade()` function, creating the necessary tables in the database.

## Conclusion

This application provides a foundational structure for managing teachers, students, and courses. You can extend its functionality by adding more features as needed. For further documentation and examples, please refer to the FastAPI and SQLAlchemy documentation.

Happy coding!
```