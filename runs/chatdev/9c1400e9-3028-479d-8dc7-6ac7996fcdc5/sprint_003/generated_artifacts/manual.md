Here's the `manual.md` file that provides a detailed user manual for the software, including an introduction to the main functions, installation instructions, and usage guidelines.

```markdown
# Course and Student Registration System

A simple application for managing student and course registrations using FastAPI and a SQLite database.

## Main Functions

This application allows users to perform the following operations:

- **Student Registration**: Users can register students by providing their name and email.
- **Course Registration**: Users can create courses by specifying the course name and level.
- **Database Management**: The application uses SQLAlchemy to manage database interactions and Alembic for migrations.

## Quick Install

To set up the environment and install the necessary dependencies, follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-repo/course-student-registration.git
   cd course-student-registration
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
   Ensure that the database schema is up to date by running the migration script:
   ```bash
   alembic upgrade head
   ```

5. **Start the Application**:
   Run the FastAPI application:
   ```bash
   uvicorn main:app --reload
   ```

## How to Use the Application

### Accessing the API

Once the application is running, you can access the API at `http://127.0.0.1:8000`.

### Student Registration

To register a student, send a POST request to `/students` with the following JSON body:

```json
{
  "name": "John Doe",
  "email": "john.doe@example.com"
}
```

You can use tools like Postman or cURL to test the API.

### Course Registration

To create a course, send a POST request to `/courses` with the following JSON body:

```json
{
  "name": "Introduction to Programming",
  "level": "Beginner"
}
```

### Using the GUI

The application also includes a simple GUI built with Tkinter for easy interaction:

1. **Run the GUI**:
   Ensure the FastAPI server is running, then run the `gui.py` script:
   ```bash
   python gui.py
   ```

2. **Register a Student**:
   - Enter the student's name and email.
   - Click the "Submit Student" button.

3. **Register a Course**:
   - Enter the course name and level.
   - Click the "Submit Course" button.

## Documentation

For more detailed documentation on the API endpoints and usage, please refer to the FastAPI documentation at [FastAPI Documentation](https://fastapi.tiangolo.com).

## Additional Notes

- Ensure that the SQLite database file (`students.db`) is created in the project directory.
- The application is designed to preserve existing student data during database migrations.
- Feel free to contribute to the project by submitting issues or pull requests.

```

This manual provides a comprehensive overview of the software, guiding users through installation, usage, and additional resources.