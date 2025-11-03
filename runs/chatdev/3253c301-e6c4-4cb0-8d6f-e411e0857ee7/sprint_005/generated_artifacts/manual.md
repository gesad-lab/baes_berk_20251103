```markdown
# Teacher Management System

A simple application for managing teachers, students, and courses using FastAPI and SQLAlchemy.

## Main Functions

The Teacher Management System allows users to perform the following operations:

- **Create and Retrieve Students**: Add new students with their names and emails, and retrieve a list of all students.
- **Create and Retrieve Courses**: Add new courses with their names and levels, and retrieve a list of all courses.
- **Create and Retrieve Teachers**: Add new teachers with their names and emails, and retrieve a list of all teachers.
- **Database Management**: The application manages a SQLite database to store all entities while preserving existing data during migrations.

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

3. **Install Required Packages**:
   ```bash
   pip install fastapi[all] sqlalchemy alembic pydantic
   ```

4. **Run Database Migrations**:
   Ensure that the database schema is up to date by running the migration script:
   ```bash
   alembic upgrade head
   ```

## Usage

To start the application, run the following command:

```bash
uvicorn main:app --reload
```

The application will be accessible at `http://127.0.0.1:8000`.

### API Endpoints

The following endpoints are available:

- **Students**:
  - `POST /students/`: Create a new student.
    - Request Body: 
      ```json
      {
        "name": "John Doe",
        "email": "john.doe@example.com"
      }
      ```
  - `GET /students/`: Retrieve a list of all students.

- **Courses**:
  - `POST /courses/`: Create a new course.
    - Request Body: 
      ```json
      {
        "name": "Mathematics",
        "level": "Beginner"
      }
      ```
  - `GET /courses/`: Retrieve a list of all courses.

- **Teachers**:
  - `POST /teachers/`: Create a new teacher.
    - Request Body: 
      ```json
      {
        "name": "Jane Smith",
        "email": "jane.smith@example.com"
      }
      ```
  - `GET /teachers/`: Retrieve a list of all teachers.

### Example Requests

You can use tools like Postman or curl to interact with the API. Here are some example requests:

- **Create a Teacher**:
  ```bash
  curl -X POST "http://127.0.0.1:8000/teachers/" -H "Content-Type: application/json" -d '{"name": "Jane Smith", "email": "jane.smith@example.com"}'
  ```

- **Get All Teachers**:
  ```bash
  curl -X GET "http://127.0.0.1:8000/teachers/"
  ```

## Documentation

For more detailed information about the API and its usage, please refer to the [FastAPI documentation](https://fastapi.tiangolo.com/).

## Conclusion

The Teacher Management System provides a straightforward way to manage educational entities. By following the installation and usage instructions, you can quickly set up and start using the application.
```