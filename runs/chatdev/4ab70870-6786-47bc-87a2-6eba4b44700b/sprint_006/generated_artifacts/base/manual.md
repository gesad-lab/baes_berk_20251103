Here's a detailed user manual for the software that includes the main functions, installation instructions, and usage guidelines.

```markdown
# Teacher Management System

A simple application for managing teachers, students, and courses using FastAPI and SQLAlchemy.

## Main Functions

This application allows users to perform the following operations:

- **Manage Teachers**: Create, read, and manage teacher records.
- **Manage Students**: Create, read, and manage student records.
- **Manage Courses**: Create, read, and manage course records.
- **Relationships**: Establish many-to-many relationships between students and courses.

## Quick Install

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
   pip install fastapi[all] sqlalchemy alembic pydantic
   ```

4. **Set Up the Database**:
   The application uses SQLite for the database. The database will be created automatically when the application starts.

## How to Use the Application

### Starting the Application

To start the FastAPI application, run the following command:

```bash
uvicorn main:app --reload
```

This will start the server at `http://127.0.0.1:8000`.

### API Endpoints

The application exposes the following API endpoints:

#### Teacher Endpoints

- **Create a Teacher**:
  - **Endpoint**: `POST /teachers/`
  - **Request Body**:
    ```json
    {
      "name": "John Doe",
      "email": "john.doe@example.com"
    }
    ```
  - **Response**: Returns the created teacher object.

- **Get All Teachers**:
  - **Endpoint**: `GET /teachers/`
  - **Response**: Returns a list of all teachers.

#### Student Endpoints

- **Create a Student**:
  - **Endpoint**: `POST /students/`
  - **Request Body**:
    ```json
    {
      "name": "Jane Doe",
      "email": "jane.doe@example.com"
    }
    ```
  - **Response**: Returns the created student object.

- **Get All Students**:
  - **Endpoint**: `GET /students/`
  - **Response**: Returns a list of all students.

#### Course Endpoints

- **Create a Course**:
  - **Endpoint**: `POST /courses/`
  - **Request Body**:
    ```json
    {
      "name": "Mathematics",
      "level": "Beginner"
    }
    ```
  - **Response**: Returns the created course object.

- **Get All Courses**:
  - **Endpoint**: `GET /courses/`
  - **Response**: Returns a list of all courses.

### Database Migration

The application uses Alembic for database migrations. To apply migrations, run:

```bash
alembic upgrade head
```

This will create the necessary tables in the database, including the `teachers`, `students`, and `courses` tables.

## Conclusion

This Teacher Management System provides a simple interface for managing teachers, students, and courses. With the FastAPI framework, it offers a fast and efficient way to handle requests and manage data. For further customization and enhancements, feel free to modify the code as needed.

For more detailed documentation, please refer to the FastAPI documentation [here](https://fastapi.tiangolo.com/).
```

This manual provides a comprehensive overview of the application, its functionalities, and how to set it up and use it effectively.