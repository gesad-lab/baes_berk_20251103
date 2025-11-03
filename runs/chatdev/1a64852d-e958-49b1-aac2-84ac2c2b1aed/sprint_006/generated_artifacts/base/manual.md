```markdown
# Teacher Management System

A simple application for managing teachers, students, and courses using FastAPI and SQLAlchemy.

## Main Functions

- **Create Teacher**: Add a new teacher with a name and email.
- **Create Student**: Add a new student with a name and email.
- **Create Course**: Add a new course with a name and level.
- **View Students**: Retrieve a list of students along with their associated courses.
- **View Courses**: Retrieve a list of courses available in the system.

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
   pip install fastapi[all] sqlalchemy alembic pydantic
   ```

4. **Run Database Migrations**:
   Ensure that your database is set up and run the migrations to create the necessary tables.
   ```bash
   alembic upgrade head
   ```

5. **Start the Application**:
   Run the FastAPI application using Uvicorn:
   ```bash
   uvicorn main:app --reload
   ```

## How to Use the Application

### API Endpoints

The application exposes several API endpoints for managing teachers, students, and courses.

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

- **Create a Student**:
  - **Endpoint**: `POST /students/`
  - **Request Body**:
    ```json
    {
      "name": "Jane Smith",
      "email": "jane.smith@example.com"
    }
    ```
  - **Response**: Returns the created student object.

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

- **Get Students**:
  - **Endpoint**: `GET /students/`
  - **Response**: Returns a list of students with their details and associated courses.

- **Get Courses**:
  - **Endpoint**: `GET /courses/`
  - **Response**: Returns a list of courses available in the system.

### Graphical User Interface (GUI)

The application also includes a simple GUI for managing courses. To use the GUI:

1. Ensure the FastAPI server is running.
2. Run the GUI script:
   ```bash
   python gui.py
   ```
3. Use the GUI to add courses and view existing courses.

## Conclusion

This Teacher Management System provides a straightforward way to manage teachers, students, and courses. With a RESTful API and a simple GUI, it is easy to integrate into other applications or use as a standalone service.

For further assistance, please refer to the code documentation or contact support.
```