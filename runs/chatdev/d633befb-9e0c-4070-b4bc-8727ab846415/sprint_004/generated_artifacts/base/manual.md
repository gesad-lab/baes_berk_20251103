Here is the `manual.md` file that provides a detailed user manual for the software, including an introduction to the main functions, installation instructions, and usage guidelines.

```markdown
# Course and Student Management System

A simple application for managing students and courses using FastAPI and SQLite.

## Main Functions

This application allows users to perform the following functions:

- **Add Students**: Create new student records with a name and email.
- **View Students**: Retrieve details of a specific student by their ID.
- **Add Courses**: Create new course records with a name and level.
- **View Courses**: Retrieve details of a specific course by its ID.

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
   pip install fastapi[all] sqlalchemy alembic requests
   ```

4. **Run Database Migrations**:
   To create the necessary database tables, run:
   ```bash
   alembic revision --autogenerate -m "Add Course table"
   alembic upgrade head
   ```

5. **Start the Application**:
   Run the FastAPI application using:
   ```bash
   uvicorn main:app --reload
   ```

## Usage

Once the application is running, you can interact with it through the GUI or directly via the API.

### Using the GUI

1. **Open the GUI**:
   The GUI will launch automatically when you run `gui.py`.

2. **Add a Student**:
   - Enter the student's name and email in the respective fields.
   - Click the "Add Student" button to create a new student record.

3. **Add a Course**:
   - Enter the course name and level in the respective fields.
   - Click the "Add Course" button to create a new course record.

4. **View Results**:
   - After adding a student or course, a message will display whether the operation was successful or if there was an error.

### Using the API

You can also interact with the application using HTTP requests:

- **Add a Student**:
  ```http
  POST /students
  Content-Type: application/json

  {
      "name": "John Doe",
      "email": "john.doe@example.com"
  }
  ```

- **Get a Student**:
  ```http
  GET /students/{student_id}
  ```

- **Add a Course**:
  ```http
  POST /courses
  Content-Type: application/json

  {
      "name": "Mathematics",
      "level": "Intermediate"
  }
  ```

- **Get a Course**:
  ```http
  GET /courses/{course_id}
  ```

## Additional Information

For more detailed documentation on FastAPI, SQLAlchemy, and Alembic, please refer to their respective official documentation:

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [SQLAlchemy Documentation](https://docs.sqlalchemy.org/)
- [Alembic Documentation](https://alembic.sqlalchemy.org/)

Feel free to reach out for support or contributions to improve the application!
```

This manual provides a comprehensive overview of the application, installation steps, and usage instructions, ensuring that users can easily understand and utilize the software.