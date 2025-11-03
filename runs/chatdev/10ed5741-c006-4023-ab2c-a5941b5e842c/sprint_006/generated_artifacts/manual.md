```markdown
# Student Management Application

A comprehensive application for managing students, courses, and teachers, built using FastAPI and Tkinter.

## Main Functions

The Student Management Application provides the following functionalities:

- **Manage Students**: Create, view, and associate students with courses.
- **Manage Courses**: Create and manage courses, including associating them with teachers.
- **Manage Teachers**: Create and manage teacher profiles.

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
   ```bash
   pip install fastapi[all] sqlalchemy alembic requests
   ```

4. **Run Database Migrations**:
   Ensure that the database schema is up to date by running the migration scripts:
   ```bash
   alembic upgrade head
   ```

5. **Start the Application**:
   Run the FastAPI application:
   ```bash
   uvicorn api:router --reload
   ```

6. **Run the GUI**:
   In a separate terminal, run the GUI application:
   ```bash
   python main.py
   ```

## How to Use the Application

### 1. Adding a Student
- Enter the student's name and email.
- Optionally, enter course IDs (comma-separated) to associate the student with courses.
- Click the "Add Student" button to save the student.

### 2. Adding a Course
- Enter the course name and level.
- Optionally, enter a teacher ID to associate the course with a teacher.
- Click the "Add Course" button to save the course.

### 3. Adding a Teacher
- Enter the teacher's name and email.
- Click the "Add Teacher" button to save the teacher.

### 4. Viewing Data
- The application will display success messages upon adding students, courses, or teachers.
- You can check the database directly to view the stored data.

## Database Schema

The application uses SQLite as the database backend. The main entities are:

- **Students**: Contains student information and their associated courses.
- **Courses**: Contains course information and the associated teacher.
- **Teachers**: Contains teacher information and the courses they teach.

## Migration Scripts

The application includes migration scripts to manage database schema changes. Ensure to run the migrations whenever you update the models.

## Conclusion

This Student Management Application provides a robust solution for managing educational entities. By following the installation and usage instructions, you can effectively manage students, courses, and teachers in your educational institution.

For further assistance, please refer to the documentation or contact support.
```