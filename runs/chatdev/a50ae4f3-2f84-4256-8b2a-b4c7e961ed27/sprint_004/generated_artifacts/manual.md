```markdown
# Student and Course Management System

This application allows users to manage students and their associated courses through a simple graphical user interface (GUI). Users can create students and courses, add courses to students, and view the courses associated with each student.

## Main Functions

- **Create Student**: Allows users to add a new student by providing their name and email.
- **Get Students**: Fetches and displays a list of all students in the system.
- **Create Course**: Enables users to create a new course by specifying its name and level.
- **Get Courses**: Retrieves and displays a list of all courses available in the system.
- **Add Course to Student**: Associates a specified course with a student.
- **Get Student Courses**: Displays all courses associated with a specific student.

## Installation

To run the application, you need to set up your environment and install the required dependencies. Follow these steps:

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
   Make sure you have `pip` installed, then run:
   ```bash
   pip install fastapi[all] sqlalchemy pydantic requests
   ```

4. **Set Up the Database**:
   Ensure you have SQLite installed (it comes with Python). The application will create a database file named `students.db` automatically.

5. **Run the Application**:
   Start the FastAPI server by running:
   ```bash
   uvicorn main:app --reload
   ```

6. **Launch the GUI**:
   In another terminal, run:
   ```bash
   python gui.py
   ```

## How to Use the Application

1. **Creating a Student**:
   - Enter the student's name and email in the respective fields.
   - Click the "Create Student" button to add the student to the database.

2. **Viewing Students**:
   - Click the "Get Students" button to fetch and display a list of all students.

3. **Creating a Course**:
   - Fill in the course name and level.
   - Click the "Create Course" button to add the course to the database.

4. **Viewing Courses**:
   - Click the "Get Courses" button to fetch and display a list of all courses.

5. **Adding a Course to a Student**:
   - Enter the Student ID and Course ID in the respective fields.
   - Click the "Add Course to Student" button to associate the course with the student.

6. **Viewing Student's Courses**:
   - Enter the Student ID and click the "Get Student Courses" button to display all courses associated with that student.

## Additional Information

- The application uses FastAPI for the backend and Tkinter for the GUI.
- The database schema is managed using SQLAlchemy, and migrations are handled with Alembic.
- The application is designed to preserve existing data during schema updates.

For any issues or feature requests, please contact the development team.
```