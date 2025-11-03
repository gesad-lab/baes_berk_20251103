```markdown
# Student and Course Management System

A simple GUI application for managing students and courses using FastAPI and Tkinter.

## Main Functions

This software allows users to:
- Create and manage students with associated courses.
- Create and manage courses.
- View lists of students and courses.
- Enroll students in multiple courses.

## Quick Install

To set up the environment and run the application, follow these steps:

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

3. **Install the required dependencies:**
   ```bash
   pip install fastapi[all] sqlalchemy pydantic requests
   ```

4. **Install Alembic for database migrations:**
   ```bash
   pip install alembic
   ```

5. **Run the FastAPI application:**
   ```bash
   uvicorn main:app --reload
   ```

6. **Run the GUI application:**
   ```bash
   python gui.py
   ```

## 🤔 What is this?

This application provides a user-friendly interface for managing students and their courses. It leverages FastAPI for the backend and Tkinter for the GUI, allowing users to perform CRUD operations on students and courses.

### Features:
- **Add Student:** Enter the student's name, email, and associated course IDs to create a new student.
- **Add Course:** Enter the course name and level to create a new course.
- **View Students:** Retrieve and display a list of all students along with their enrolled courses.
- **View Courses:** Retrieve and display a list of all courses.

## 📖 How to Use

1. **Adding a Student:**
   - Enter the student's name and email in the respective fields.
   - Provide course IDs (comma-separated) in the "Course IDs" field.
   - Click the "Add Student" button to create the student.

2. **Adding a Course:**
   - Enter the course name and level in the respective fields.
   - Click the "Add Course" button to create the course.

3. **Viewing Students:**
   - Click the "Get Students" button to retrieve and display all students in the list.

4. **Viewing Courses:**
   - Click the "Get Courses" button to retrieve and display all courses in the list.

## Database Migration

The application uses Alembic for database migrations. The `alembic_migration.py` file contains the migration script for creating the association table between students and courses. To apply migrations, run the following command:

```bash
alembic upgrade head
```

## Conclusion

This application provides a simple yet effective way to manage students and courses. Feel free to explore the code and customize it according to your needs. For any issues or feature requests, please reach out to the development team.
```