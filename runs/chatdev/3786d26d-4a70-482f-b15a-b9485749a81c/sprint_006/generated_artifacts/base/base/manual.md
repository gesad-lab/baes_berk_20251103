```markdown
# Student and Course Management System

A simple application for managing students and courses, allowing users to add students, add courses, and enroll students in courses.

## Main Functions

- **Add Student**: Allows you to add a new student by providing their name and email.
- **Get Students**: Fetches and displays a list of all students in the system.
- **Add Course**: Allows you to add a new course by providing its name and level.
- **Get Courses**: Fetches and displays a list of all courses in the system.
- **Enroll Student in Course**: Allows you to enroll a student in a specific course by providing their ID and the course ID.

## Installation

To run the application, you need to set up your environment and install the required dependencies. Follow these steps:

1. **Clone the repository**:
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
   pip install -r requirements.txt
   ```

   Make sure you have the following packages in your `requirements.txt`:
   ```
   fastapi
   sqlalchemy
   alembic
   pydantic
   requests
   tkinter
   ```

4. **Run the database migration**:
   ```bash
   python main.py
   ```

   This will create the necessary tables in the SQLite database and ensure that existing data is preserved.

## How to Use the Application

1. **Start the application**:
   Run the following command to start the GUI:
   ```bash
   python gui.py
   ```

2. **Adding a Student**:
   - Enter the student's name and email in the respective fields.
   - Click on the "Add Student" button to add the student to the system.

3. **Viewing Students**:
   - Click on the "Get Students" button to fetch and display the list of all students.

4. **Adding a Course**:
   - Enter the course name and level in the respective fields.
   - Click on the "Add Course" button to add the course to the system.

5. **Viewing Courses**:
   - Click on the "Get Courses" button to fetch and display the list of all courses.

6. **Enrolling a Student in a Course**:
   - Enter the student ID and course ID in the respective fields.
   - Click on the "Enroll Student in Course" button to enroll the student in the selected course.

## Conclusion

This application provides a simple interface for managing students and courses, making it easy to add, view, and enroll students in courses. For any issues or feature requests, please contact the development team.

Happy managing!
```