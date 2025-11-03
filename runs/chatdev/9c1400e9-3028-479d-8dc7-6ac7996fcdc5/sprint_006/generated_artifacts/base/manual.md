```markdown
# Teacher Management System

A simple application for managing students, courses, and teachers using FastAPI and SQLite.

## Main Functions

This application provides the following functionalities:

- **Student Management**: Create and manage student records with name and email.
- **Course Management**: Create and manage courses with name and level.
- **Teacher Management**: Create and manage teacher records with name and email.
- **Database Management**: Migrations to ensure data integrity and schema updates.

## Quick Install

To set up the environment and install the necessary dependencies, follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-repo/teacher-management-system.git
   cd teacher-management-system
   ```

2. **Create a Virtual Environment** (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies**:
   ```bash
   pip install fastapi[all] sqlalchemy alembic requests
   ```

4. **Run Database Migrations**:
   Ensure you have Alembic configured properly. Run the following command to apply migrations:
   ```bash
   alembic upgrade head
   ```

5. **Start the Application**:
   Run the FastAPI application using Uvicorn:
   ```bash
   uvicorn main:app --reload
   ```

6. **Access the API Documentation**:
   Open your browser and navigate to `http://127.0.0.1:8000/docs` to access the interactive API documentation.

## How to Use the Application

### 1. Registering a Student

- **Endpoint**: `POST /students`
- **Request Body**:
  ```json
  {
    "name": "John Doe",
    "email": "john.doe@example.com"
  }
  ```

### 2. Registering a Course

- **Endpoint**: `POST /courses`
- **Request Body**:
  ```json
  {
    "name": "Mathematics",
    "level": "Intermediate"
  }
  ```

### 3. Registering a Teacher

- **Endpoint**: `POST /teachers`
- **Request Body**:
  ```json
  {
    "name": "Jane Smith",
    "email": "jane.smith@example.com"
  }
  ```

### 4. Using the GUI

The application also includes a simple GUI built with Tkinter for easier interaction:

1. Run the `gui.py` script:
   ```bash
   python gui.py
   ```

2. Fill in the respective fields for students, courses, and teachers, and click the "Submit" button to register them.

## Database Schema

The application uses SQLite as the database backend. The following tables are created:

- **students**: Stores student records with name and email.
- **courses**: Stores course records with name and level.
- **teachers**: Stores teacher records with name and email.
- **student_courses**: An association table for many-to-many relationships between students and courses.

## Additional Information

For more detailed documentation on FastAPI, SQLAlchemy, and Alembic, please refer to their respective official documentation:

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [SQLAlchemy Documentation](https://docs.sqlalchemy.org/)
- [Alembic Documentation](https://alembic.sqlalchemy.org/)

Feel free to reach out for any questions or support regarding the application.
```