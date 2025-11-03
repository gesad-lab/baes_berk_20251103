```markdown
# Student and Course Management System

A simple application for managing students and their associated courses using FastAPI and SQLAlchemy.

## Main Functions

This application allows users to:

- **Create Students**: Add new students with their names, emails, and associated course IDs.
- **Get Students**: Retrieve a list of all students in the system.
- **Create Courses**: Add new courses with their names and levels.
- **Get Courses**: Retrieve a list of all courses in the system.

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
   Make sure you have `pip` installed, then run:
   ```bash
   pip install fastapi[all] sqlalchemy alembic requests
   ```

4. **Set Up the Database**:
   The application uses SQLite for the database. The database will be created automatically when you run the application for the first time.

## How to Use the Application

1. **Run the Application**:
   Start the FastAPI application by running:
   ```bash
   uvicorn main:app --reload
   ```
   The application will be accessible at `http://127.0.0.1:8000`.

2. **Access the GUI**:
   The application includes a simple GUI built with Tkinter. You can interact with the API through this interface.

3. **Creating a Student**:
   - Enter the student's name and email.
   - Enter course IDs (comma-separated) if the student is enrolled in any courses.
   - Click on "Create Student" to add the student.

4. **Viewing Students**:
   Click on "Get Students" to retrieve and display a list of all students.

5. **Creating a Course**:
   - Enter the course name and level.
   - Click on "Create Course" to add the course.

6. **Viewing Courses**:
   Click on "Get Courses" to retrieve and display a list of all courses.

## API Endpoints

The application exposes the following API endpoints:

- **POST /students/**: Create a new student.
- **GET /students/**: Retrieve a list of students.
- **POST /courses/**: Create a new course.
- **GET /courses/**: Retrieve a list of courses.

## Database Migrations

The application uses Alembic for database migrations. The following migrations are included:

- `xxxx_add_email_column.py`: Adds an email column to the Student table.
- `xxxx_add_course_table.py`: Creates the Course table.
- `xxxx_add_student_courses_table.py`: Creates the association table for the many-to-many relationship between Students and Courses.

## Conclusion

This application provides a straightforward way to manage students and their courses. Feel free to extend its functionality or modify it to suit your needs.
```
