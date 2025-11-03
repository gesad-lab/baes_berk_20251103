```markdown
# Student Management System

A comprehensive application for managing students and courses, allowing users to add, view, and manage student and course data.

## Main Functions

- **Add Student**: Allows users to input student details (name and email) and save them to the database.
- **View Students**: Displays a list of all students currently stored in the database.
- **Add Course**: Enables users to create new courses by specifying the course name and level.
- **View Courses**: Shows a list of all courses available in the database.

## Installation Guide

To run the Student Management System, you need to set up your environment with the necessary dependencies. Follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-repo/student-management-system.git
   cd student-management-system
   ```

2. **Create a Virtual Environment** (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Required Dependencies**:
   You can install the required dependencies using pip. Make sure you have `pip` installed.
   ```bash
   pip install fastapi sqlalchemy alembic requests
   ```

4. **Install Tkinter**:
   Tkinter is required for the GUI. It usually comes pre-installed with Python, but if not, you can install it using your package manager. For example, on Ubuntu:
   ```bash
   sudo apt-get install python3-tk
   ```

5. **Run Database Migration**:
   Before starting the application, you need to run the migration script to create the necessary database tables.
   ```bash
   alembic upgrade head
   ```

## How to Use the Application

1. **Start the Application**:
   Run the main application file to start the GUI.
   ```bash
   python main.py
   ```

2. **Adding Students**:
   - Enter the student's name in the "Enter Student Name" field.
   - Enter the student's email in the "Enter Student Email" field.
   - Click the "Add Student" button to save the student to the database.

3. **Viewing Students**:
   - Click the "View Students" button to retrieve and display the list of students.

4. **Adding Courses**:
   - Enter the course name in the "Enter Course Name" field.
   - Enter the course level in the "Enter Course Level" field.
   - Click the "Add Course" button to save the course to the database.

5. **Viewing Courses**:
   - Click the "View Courses" button to retrieve and display the list of courses.

## Additional Information

- The application uses SQLite as the database, which is lightweight and easy to set up.
- The backend is built using FastAPI, providing a RESTful API for managing students and courses.
- The application is designed to preserve existing student data during database migrations.

For any issues or feature requests, please reach out to the development team.

```
