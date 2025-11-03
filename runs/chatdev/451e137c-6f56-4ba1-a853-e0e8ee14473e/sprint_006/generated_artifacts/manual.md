```markdown
# Student, Course, and Teacher Management Application

Welcome to the Student, Course, and Teacher Management Application! This software allows users to manage students, courses, and teachers efficiently. Below is a comprehensive guide on how to install the necessary dependencies, use the application, and understand its main functionalities.

## Main Functions

The application provides the following functionalities:

- **Student Management**: Add, retrieve, and manage student information.
- **Course Management**: Create courses, assign teachers to courses, and retrieve course information.
- **Teacher Management**: Add and manage teacher information.
- **User Interface**: A simple GUI built with Tkinter for easy interaction with the application.

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

3. **Install Required Packages**:
   ```bash
   pip install fastapi[all] sqlalchemy pydantic requests
   ```

4. **Install Tkinter** (if not already installed):
   - For Ubuntu:
     ```bash
     sudo apt-get install python3-tk
     ```
   - For Windows, Tkinter is included with Python installations.

## How to Use the Application

1. **Run the Application**:
   Start the FastAPI server by running the following command in your terminal:
   ```bash
   uvicorn main:app --reload
   ```

2. **Open the GUI**:
   After starting the server, run the GUI application:
   ```bash
   python gui.py
   ```

3. **Adding Students**:
   - Enter the student's name and email in the respective fields.
   - Click the "Add Student" button to save the student information.

4. **Adding Teachers**:
   - Enter the teacher's name and email in the respective fields.
   - Click the "Add Teacher" button to save the teacher information.

5. **Adding Courses**:
   - Enter the course name and level in the respective fields.
   - Enter the teacher's ID (make sure the teacher exists).
   - Click the "Add Course" button to save the course information.

6. **Displaying Students**:
   - Click the "Display Students" button to retrieve and display all students in the output area.

## Database Migration

The application includes migration scripts to ensure that the database schema is updated without losing existing data. The migration scripts handle the addition of the Teacher entity and the relationship between Courses and Teachers.

## Conclusion

This application serves as a comprehensive tool for managing students, courses, and teachers. With a user-friendly interface and robust backend, it simplifies educational administration tasks. For further assistance, please refer to the documentation or contact support.

Happy managing!
```