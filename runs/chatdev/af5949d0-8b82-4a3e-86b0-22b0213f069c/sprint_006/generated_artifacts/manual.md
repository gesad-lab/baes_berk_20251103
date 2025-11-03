```markdown
# Student Management System

A comprehensive application for managing students, courses, and teachers, built using FastAPI and Tkinter for a user-friendly interface.

## Main Functions

- **Student Management**: Add, view, and manage student information.
- **Course Management**: Create and manage courses, including associating them with teachers.
- **Teacher Management**: Add and manage teacher information.
- **Enrollment**: Enroll students in courses.

## Quick Install

To set up the environment and install the necessary dependencies, follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone <repository-url>
   cd student_app
   ```

2. **Create a Virtual Environment** (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies**:
   Create a `requirements.txt` file with the following content:
   ```
   fastapi
   uvicorn
   sqlalchemy
   pydantic
   alembic
   requests
   ```
   Then run:
   ```bash
   pip install -r requirements.txt
   ```

## Database Migration

Before running the application, ensure that the database schema is up to date. Run the migration script using Alembic:

1. **Initialize Alembic** (if not already done):
   ```bash
   alembic init alembic
   ```

2. **Run Migrations**:
   ```bash
   alembic upgrade head
   ```

## How to Use the Application

1. **Run the FastAPI Server**:
   Start the FastAPI server using Uvicorn:
   ```bash
   uvicorn main:app --reload
   ```

2. **Launch the GUI**:
   Run the GUI application:
   ```bash
   python gui.py
   ```

3. **Using the GUI**:
   - **Add Student**: Enter the student's name and email, then click "Add Student".
   - **Add Course**: Enter the course name, level, and optionally the teacher ID, then click "Add Course".
   - **Add Teacher**: Enter the teacher's name and email, then click "Add Teacher".
   - **Enroll Student in Course**: Enter the student ID and course ID, then click "Enroll Student in Course".

## API Endpoints

The application exposes the following API endpoints:

- **Students**:
  - `POST /students/`: Create a new student.
  - `GET /students/`: Retrieve a list of students.

- **Courses**:
  - `POST /courses/`: Create a new course.
  - `GET /courses/`: Retrieve a list of courses.

- **Teachers**:
  - `POST /teachers/`: Create a new teacher.
  - `GET /teachers/`: Retrieve a list of teachers.

- **Enrollment**:
  - `POST /students/{student_id}/courses/{course_id}/enroll`: Enroll a student in a course.

## Additional Information

For more detailed documentation on FastAPI, SQLAlchemy, and other libraries used, please refer to their respective official documentation:

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [SQLAlchemy Documentation](https://docs.sqlalchemy.org/)
- [Pydantic Documentation](https://pydantic-docs.helpmanual.io/)
- [Alembic Documentation](https://alembic.sqlalchemy.org/en/latest/)

Feel free to reach out for support or contribute to the project!
```