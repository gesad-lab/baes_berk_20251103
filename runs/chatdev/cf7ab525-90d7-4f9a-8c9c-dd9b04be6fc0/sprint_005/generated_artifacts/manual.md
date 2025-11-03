```markdown
# Teacher Management System

A simple application for managing teachers, students, and courses using FastAPI and SQLAlchemy.

## Main Functions

This application allows you to:

- Create and manage **Teachers** with their names and email addresses.
- Create and manage **Students** with their names, email addresses, and enrolled courses.
- Create and manage **Courses** with their names and levels.
- Retrieve lists of teachers, students, and courses.

## Quick Install

To set up the environment and install the necessary dependencies, follow these steps:

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Create a virtual environment (optional but recommended):**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install the required packages:**
   ```bash
   pip install fastapi[all] sqlalchemy alembic
   ```

4. **Set up the database:**
   The application uses SQLite for the database. You can initialize the database by running the main application:
   ```bash
   python main.py
   ```

## How to Use the Application

### Starting the Application

To start the FastAPI application, run:
```bash
uvicorn main:app --reload
```
This will start the server at `http://127.0.0.1:8000`.

### API Endpoints

You can interact with the application using the following API endpoints:

#### Teachers

- **Create a Teacher**
  - **Endpoint:** `POST /teachers/`
  - **Request Body:**
    ```json
    {
      "name": "John Doe",
      "email": "john.doe@example.com"
    }
    ```

- **Get List of Teachers**
  - **Endpoint:** `GET /teachers/`
  - **Query Parameters:** `skip`, `limit` (for pagination)

#### Students

- **Create a Student**
  - **Endpoint:** `POST /students/`
  - **Request Body:**
    ```json
    {
      "name": "Jane Smith",
      "email": "jane.smith@example.com",
      "course_ids": [1, 2]  // Optional: List of course IDs for enrollment
    }
    ```

- **Get List of Students**
  - **Endpoint:** `GET /students/`
  - **Query Parameters:** `skip`, `limit` (for pagination)

#### Courses

- **Create a Course**
  - **Endpoint:** `POST /courses/`
  - **Request Body:**
    ```json
    {
      "name": "Mathematics",
      "level": "Beginner"
    }
    ```

- **Get List of Courses**
  - **Endpoint:** `GET /courses/`
  - **Query Parameters:** `skip`, `limit` (for pagination)

## Database Migrations

The application uses Alembic for database migrations. To create the necessary tables and columns, run the migration scripts as follows:

1. **Create the Teachers table:**
   ```bash
   alembic upgrade head
   ```

2. **To downgrade the migration (if needed):**
   ```bash
   alembic downgrade -1
   ```

## Conclusion

This application provides a simple interface for managing teachers, students, and courses. You can extend its functionality by adding more features as needed. For further assistance, please refer to the FastAPI and SQLAlchemy documentation.
```
