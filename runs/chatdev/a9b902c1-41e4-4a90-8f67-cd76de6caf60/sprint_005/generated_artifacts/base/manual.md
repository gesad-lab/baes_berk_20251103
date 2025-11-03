```markdown
# Student and Course Registration System

A simple GUI application for managing student and course registrations using FastAPI and SQLite.

## Main Functions

This application allows you to:
- Create new students with associated courses.
- Create new courses.
- View existing students and courses.

## Installation

To run this application, you need to install the required dependencies. Follow the steps below to set up your environment:

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
   pip install fastapi[all] sqlalchemy pydantic requests tkinter alembic
   ```

4. **Run the database migration:**
   ```bash
   alembic upgrade head
   ```

5. **Start the FastAPI application:**
   ```bash
   uvicorn main:app --reload
   ```

6. **Run the GUI application:**
   ```bash
   python gui.py
   ```

## How to Use the Application

### Creating a Student

1. Open the GUI application.
2. Enter the student's name and email in the respective fields.
3. In the "Course IDs" field, enter the IDs of the courses the student should be enrolled in, separated by commas (e.g., `1,2`).
4. Click the "Create Student" button to register the student.

### Creating a Course

1. In the same GUI application, navigate to the course registration section.
2. Enter the course name and level in the respective fields.
3. Click the "Create Course" button to register the course.

### Viewing Students and Courses

- You can view the list of registered students and courses by accessing the FastAPI endpoints:
  - **Students:** `GET http://127.0.0.1:8000/students/`
  - **Courses:** `GET http://127.0.0.1:8000/courses/`

## Database Schema

The application uses a SQLite database with the following schema:

- **Students Table:**
  - `id`: Integer, primary key
  - `name`: String, not nullable
  - `email`: String, not nullable

- **Courses Table:**
  - `id`: Integer, primary key
  - `name`: String, not nullable
  - `level`: String, not nullable

- **Student-Courses Association Table:**
  - `student_id`: Integer, foreign key referencing Students
  - `course_id`: Integer, foreign key referencing Courses

## Additional Information

For more detailed documentation on FastAPI, SQLAlchemy, and Pydantic, please refer to their respective official documentation:

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [SQLAlchemy Documentation](https://docs.sqlalchemy.org/en/14/)
- [Pydantic Documentation](https://pydantic-docs.helpmanual.io/)

If you encounter any issues or have questions, feel free to reach out for support.
```