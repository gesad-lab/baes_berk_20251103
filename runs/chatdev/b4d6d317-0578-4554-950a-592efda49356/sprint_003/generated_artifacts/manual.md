```markdown
# Student Management System

A simple application for managing students and courses, allowing users to add and view student and course information.

## Main Functions

- **Add Student**: Allows users to create a new student by entering their name and email.
- **Show Students**: Displays a list of all students in the database.
- **Add Course**: Allows users to create a new course by entering its name and level.
- **Show Courses**: Displays a list of all courses in the database.

## Installation

To set up the environment and install the necessary dependencies, follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/student_management_system.git
   cd student_management_system
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

4. **Create the Database**:
   Ensure that the database is created by running the application for the first time. The application will automatically create the necessary tables.

## Usage

1. **Run the Application**:
   Start the FastAPI server by running the following command:
   ```bash
   uvicorn main:app --reload
   ```

2. **Access the GUI**:
   Open your web browser and navigate to `http://127.0.0.1:8000` to access the Student Management System GUI.

3. **Add a Student**:
   - Enter the student's name and email in the respective fields.
   - Click on the "Add Student" button to save the student to the database.

4. **Show Students**:
   - Click on the "Show Students" button to display a list of all students.

5. **Add a Course**:
   - Enter the course name and level in the respective fields.
   - Click on the "Add Course" button to save the course to the database.

6. **Show Courses**:
   - Click on the "Show Courses" button to display a list of all courses.

## Additional Information

- The application uses SQLite as the database, which is lightweight and easy to set up.
- The backend is built using FastAPI, providing a RESTful API for managing students and courses.
- The frontend is implemented using Tkinter, a standard GUI toolkit for Python.

For further assistance or to report issues, please contact support at support@yourcompany.com.
```