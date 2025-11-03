```markdown
# Teacher Management System

A simple application for managing students, courses, and teachers using FastAPI and a Tkinter GUI.

## Overview

This application allows users to create and manage students, courses, and teachers. It provides a user-friendly interface for adding new entries and retrieving existing data. The backend is built using FastAPI, and the database is managed with SQLAlchemy.

## Main Functions

- **Create Students**: Add new students with their names, emails, and associated course IDs.
- **Create Courses**: Add new courses with their names and levels.
- **Create Teachers**: Add new teachers with their names and emails.
- **Retrieve Data**: View the list of students, courses, and teachers.

## Installation

To set up the environment and run the application, follow these steps:

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

4. **Run Database Migration**:
   Ensure that the Alembic migration script is executed to create the necessary database tables.
   ```bash
   alembic upgrade head
   ```

5. **Run the Application**:
   Start the FastAPI server:
   ```bash
   uvicorn main:app --reload
   ```

6. **Run the GUI**:
   In a separate terminal, run the GUI application:
   ```bash
   python gui.py
   ```

## How to Use the Application

### Adding Students

1. Enter the student's name in the "Student Name" field.
2. Enter the student's email in the "Student Email" field.
3. Enter the course IDs (comma-separated) in the "Course IDs" field.
4. Click the "Add Student" button to create the student.
5. Click the "Get Students" button to view the list of students.

### Adding Courses

1. Enter the course name in the "Course Name" field.
2. Enter the course level in the "Course Level" field.
3. Click the "Add Course" button to create the course.
4. Click the "Get Courses" button to view the list of courses.

### Adding Teachers

1. Enter the teacher's name in the "Teacher Name" field.
2. Enter the teacher's email in the "Teacher Email" field.
3. Click the "Add Teacher" button to create the teacher.
4. Click the "Get Teachers" button to view the list of teachers.

### Viewing Data

- Use the "Get Students", "Get Courses", and "Get Teachers" buttons to retrieve and display the respective lists in the GUI.

## Conclusion

This Teacher Management System provides a simple yet effective way to manage educational entities. With the FastAPI backend and Tkinter GUI, users can easily interact with the database and perform CRUD operations on students, courses, and teachers.

For further documentation and details, please refer to the code comments and the FastAPI documentation.
```