```markdown
# Course and Student Management System

A simple application for managing students and courses using FastAPI and Tkinter.

## Main Functions

This application allows users to perform the following operations:

- **Manage Students**: Create new students and view existing students.
- **Manage Courses**: Create new courses and view existing courses.

## Installation

To run this application, you need to install the required dependencies. Follow these steps:

1. **Clone the repository** (if applicable):
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Set up a virtual environment** (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install the required dependencies**:
   ```bash
   pip install fastapi[all] sqlalchemy pydantic requests
   ```

4. **Run the FastAPI application**:
   ```bash
   uvicorn main:app --reload
   ```

5. **Run the GUI**:
   Open another terminal and run:
   ```bash
   python gui.py
   ```

## How to Use the Application

### Student Management

1. **Add a Student**:
   - Enter the student's name in the "Student Name" field.
   - Enter the student's email in the "Student Email" field.
   - Click the "Add Student" button to create the student.

2. **View Students**:
   - Click the "Get Students" button to retrieve and display the list of existing students.

### Course Management

1. **Add a Course**:
   - Enter the course name in the "Course Name" field.
   - Enter the course level in the "Course Level" field.
   - Click the "Add Course" button to create the course.

2. **View Courses**:
   - Click the "Get Courses" button to retrieve and display the list of existing courses.

## Database Schema

The application uses SQLite as the database, with the following tables:

- **students**: Contains student records with fields for `id`, `name`, and `email`.
- **courses**: Contains course records with fields for `id`, `name`, and `level`.

### Database Migration

The database migration process ensures that existing student data is preserved when the new Course table is added.

## Additional Information

For more detailed documentation on FastAPI, SQLAlchemy, and Tkinter, please refer to the respective official documentation:

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [SQLAlchemy Documentation](https://docs.sqlalchemy.org/en/14/)
- [Tkinter Documentation](https://docs.python.org/3/library/tkinter.html)

For any issues or feature requests, please contact the development team.
```