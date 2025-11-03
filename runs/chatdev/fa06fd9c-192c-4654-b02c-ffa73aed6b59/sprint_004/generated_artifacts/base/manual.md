```markdown
# Student Management System

A simple application for managing students and courses using FastAPI and Tkinter.

## Overview

The Student Management System allows users to add and view students and courses. It provides a graphical user interface (GUI) for easy interaction and uses a RESTful API for backend operations. The application is built using Python, FastAPI, and SQLAlchemy.

## Main Functions

- **Add Student**: Users can add new students by providing their name and email.
- **View Students**: Users can view a list of all registered students.
- **Add Course**: Users can add new courses by providing the course name and level.
- **View Courses**: Users can view a list of all available courses.

## Installation Instructions

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
   ```plaintext
   fastapi
   uvicorn
   sqlalchemy
   pydantic
   requests
   ```
   Then run:
   ```bash
   pip install -r requirements.txt
   ```

4. **Initialize the Database**:
   Before running the application, ensure that the database is initialized. You can do this by running the following command in a Python shell:
   ```python
   from database import init_db
   init_db()
   ```

## Running the Application

1. **Start the FastAPI Server**:
   In the terminal, run the following command to start the FastAPI server:
   ```bash
   uvicorn main:app --reload
   ```

2. **Launch the GUI**:
   In a new terminal window, run the following command to start the Tkinter GUI:
   ```bash
   python gui.py
   ```

3. **Access the Application**:
   - The GUI will open, allowing you to add and view students and courses.
   - You can also access the API directly at `http://127.0.0.1:8000/docs` to see the available endpoints.

## How to Use the Application

### Adding a Student
1. Enter the student's name in the "Student Name" field.
2. Enter the student's email in the "Student Email" field.
3. Click the "Add Student" button to add the student to the database.
4. Click "Show Students" to view the list of added students.

### Adding a Course
1. Enter the course name in the "Course Name" field.
2. Enter the course level in the "Course Level" field.
3. Click the "Add Course" button to add the course to the database.
4. Click "Show Courses" to view the list of added courses.

## Conclusion

The Student Management System provides a simple and effective way to manage students and courses. With its user-friendly interface and robust backend, it is suitable for educational institutions and training programs. For further enhancements or features, feel free to contribute to the project or reach out for support.
```