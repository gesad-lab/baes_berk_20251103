```markdown
# Student Management Application

A simple application for managing students and their courses, built using Python and FastAPI. This application allows users to add students, add courses, and view the list of students and courses.

## Main Functions

- **Add Student**: Allows users to input a student's name and email to add them to the database.
- **Fetch Students**: Retrieves and displays the list of all students in the database.
- **Add Course**: Allows users to input a course name and level to add it to the database.
- **Course Relationship**: Students can be associated with multiple courses through a many-to-many relationship.

## Installation

To run the Student Management Application, you need to install the necessary environment dependencies. Follow the steps below:

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

3. **Install required packages**:
   ```bash
   pip install fastapi[all] sqlalchemy alembic requests
   ```

4. **Run database migrations**:
   Make sure you have Alembic configured properly. Run the migration script to create the necessary tables:
   ```bash
   alembic upgrade head
   ```

5. **Run the application**:
   Start the FastAPI application:
   ```bash
   uvicorn main:app --reload
   ```

## How to Use the Application

1. **Open the GUI**:
   After running the application, a GUI window will appear.

2. **Adding a Student**:
   - Enter the student's name in the "Student Name" field.
   - Enter the student's email in the "Student Email" field.
   - Click the "Add Student" button to add the student to the database.
   - If the email format is invalid, an error message will be displayed.

3. **Fetching Students**:
   - Click the "Fetch Students" button to retrieve and display the list of all students in the application.

4. **Adding a Course**:
   - Enter the course name in the "Course Name" field.
   - Enter the course level in the "Course Level" field.
   - Click the "Add Course" button to add the course to the database.
   - A success or failure message will be displayed based on the operation's outcome.

5. **Viewing Output**:
   - The output text area will display messages related to adding students, fetching students, and adding courses.

## Additional Information

- The application uses SQLite as the database backend, and the database file is named `students.db`.
- The many-to-many relationship between students and courses is managed through an association table called `student_courses`.
- Existing data in the `students` and `courses` tables will be preserved during database migrations.

For further assistance or to report issues, please contact the development team.
```