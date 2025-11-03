```markdown
# Teacher Management Application

A simple GUI application for managing students, courses, and teachers.

## Main Functions

The Teacher Management Application allows users to perform the following functions:

- **Add Students**: Input student name and email to add them to the database.
- **Fetch Students**: Retrieve and display a list of all students in the database.
- **Add Courses**: Input course name and level to add them to the database.
- **Add Teachers**: Input teacher name and email to add them to the database.

## Installation

To run the Teacher Management Application, you need to install the required environment dependencies. Follow the steps below:

1. **Install Python**: Ensure you have Python 3.6 or higher installed on your machine. You can download it from [python.org](https://www.python.org/downloads/).

2. **Create a Virtual Environment (Optional but recommended)**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Required Packages**:
   Use pip to install the necessary packages:
   ```bash
   pip install sqlalchemy alembic requests tkinter
   ```

4. **Database Setup**:
   The application uses SQLite as the database. The database file `students.db` will be created automatically when you run the application for the first time.

## How to Use the Application

1. **Run the Application**:
   Execute the following command in your terminal:
   ```bash
   python main.py
   ```

2. **Using the GUI**:
   - **Add Student**:
     - Enter the student's name in the "Student Name" field.
     - Enter the student's email in the "Student Email" field.
     - Click the "Add Student" button to save the student.
   - **Fetch Students**:
     - Click the "Fetch Students" button to display all students in the output area.
   - **Add Course**:
     - Enter the course name in the "Course Name" field.
     - Enter the course level in the "Course Level" field.
     - Click the "Add Course" button to save the course.
   - **Add Teacher**:
     - Enter the teacher's name in the "Teacher Name" field.
     - Enter the teacher's email in the "Teacher Email" field.
     - Click the "Add Teacher" button to save the teacher.

3. **Email Validation**:
   The application includes basic email validation. If an invalid email format is entered, an error message will be displayed in the output area.

## Additional Information

- The application is built using Python and utilizes the Tkinter library for the GUI.
- The database schema includes tables for students, courses, and teachers, ensuring that data is preserved during migrations.
- For any issues or feature requests, please contact the development team at ChatDev.

Enjoy managing your students, courses, and teachers with the Teacher Management Application!
```