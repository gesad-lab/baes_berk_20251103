```markdown
# Student and Course Management System

A simple GUI application for managing students and courses, allowing users to create students and courses, list them, and enroll students in courses.

## Main Functions

- **Create Student**: Add a new student by providing their name and email.
- **List Students**: Retrieve and display a list of all registered students.
- **Create Course**: Add a new course by providing its name and level.
- **List Courses**: Retrieve and display a list of all available courses.
- **Enroll Student in Course**: Enroll a student in a specific course using their IDs.
- **Get Student Courses**: Retrieve and display all courses a specific student is enrolled in.

## Installation

To run this application, you need to install the required dependencies. Follow the steps below:

1. **Set up a Python environment**: It's recommended to use a virtual environment to manage dependencies. You can create one using `venv`:

   ```bash
   python -m venv env
   source env/bin/activate  # On Windows use `env\Scripts\activate`
   ```

2. **Install the required packages**: Use `pip` to install the necessary libraries:

   ```bash
   pip install fastapi[all] sqlalchemy alembic requests tkinter
   ```

3. **Set up the database**: The application uses SQLite for the database. The database will be created automatically when you run the application for the first time.

## How to Use the Application

1. **Run the FastAPI server**: Start the FastAPI application by running the following command in your terminal:

   ```bash
   python main.py
   ```

   This will start the server at `http://127.0.0.1:8000`.

2. **Launch the GUI**: Open another terminal and run the GUI application:

   ```bash
   python gui.py
   ```

3. **Using the GUI**:
   - **Creating a Student**:
     - Enter the student's name and email in the respective fields.
     - Click on "Create Student" to add the student.
   - **Listing Students**:
     - Click on "List Students" to display all registered students in the list box.
   - **Creating a Course**:
     - Enter the course name and level in the respective fields.
     - Click on "Create Course" to add the course.
   - **Listing Courses**:
     - Click on "List Courses" to display all available courses in the list box.
   - **Enrolling a Student in a Course**:
     - Enter the student ID and course ID in the respective fields.
     - Click on "Enroll Student in Course" to enroll the student.
   - **Getting Student Courses**:
     - You can extend the functionality to retrieve courses for a specific student by implementing a new button and corresponding function.

## Additional Information

- **Database Migration**: The application includes a migration script (`migration_script.py`) that creates the necessary tables and relationships in the database. You can run this script using Alembic to ensure your database schema is up to date.
- **Error Handling**: The application includes basic error handling to inform users of any issues during student or course creation and enrollment.

For further assistance, please refer to the code comments or reach out to the development team.
```