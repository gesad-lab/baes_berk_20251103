```markdown
# Teacher Management System

A simple application for managing students, courses, and teachers. This system allows users to add and manage students, courses, and teachers, as well as enroll students in courses.

## Main Functions

- **Add Students**: Create new student entries with a name and email.
- **View Students**: Retrieve a list of all students.
- **Add Courses**: Create new course entries with a name and level.
- **View Courses**: Retrieve a list of all courses.
- **Add Teachers**: Create new teacher entries with a name and email.
- **View Teachers**: Retrieve a list of all teachers.
- **Enroll Students in Courses**: Enroll a student in a specific course.

## Installation

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
   pip install fastapi sqlalchemy pydantic requests alembic
   ```

4. **Run Database Migration**:
   Ensure that the database schema is up to date by running the migration script:
   ```bash
   alembic upgrade head
   ```

## How to Use the Application

1. **Start the FastAPI Server**:
   Run the following command to start the FastAPI server:
   ```bash
   uvicorn main:app --reload
   ```

2. **Access the GUI**:
   Open your web browser and navigate to `http://127.0.0.1:8000` to access the GUI.

3. **Adding Students**:
   - Enter the student's name and email in the respective fields.
   - Click on "Add Student" to create a new student entry.

4. **Viewing Students**:
   - The application will automatically display the list of students added.

5. **Adding Courses**:
   - Enter the course name and level in the respective fields.
   - Click on "Add Course" to create a new course entry.

6. **Viewing Courses**:
   - The application will automatically display the list of courses added.

7. **Adding Teachers**:
   - Enter the teacher's name and email in the respective fields.
   - Click on "Add Teacher" to create a new teacher entry.

8. **Viewing Teachers**:
   - The application will automatically display the list of teachers added.

9. **Enrolling Students in Courses**:
   - Enter the Student ID and Course ID in the respective fields.
   - Click on "Enroll Student in Course" to enroll the student in the specified course.

## Additional Information

- The application uses SQLite as the database, and the database file is created in the project directory.
- The application is built using FastAPI for the backend and Tkinter for the GUI.
- Ensure that the server is running before interacting with the GUI.

For further documentation and details, please refer to the code comments and structure within the project files.
```