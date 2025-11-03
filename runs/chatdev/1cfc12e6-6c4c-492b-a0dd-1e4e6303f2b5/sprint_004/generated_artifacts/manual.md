```markdown
# Student Management Application

A comprehensive application for managing students and courses, allowing users to create student profiles, enroll students in courses, and view student information.

## Main Functions

- **Create Student**: Add new students to the database by providing their name and email.
- **Create Course**: Add new courses to the database by providing the course name and level.
- **Enroll Student in Course**: Enroll a student in a specific course using their ID and the course ID.
- **View Students**: Retrieve and display a list of all students in the database.

## Installation

To run the Student Management Application, you need to install the required dependencies. Follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/student_management_app.git
   cd student_management_app
   ```

2. **Create a Virtual Environment** (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies**:
   ```bash
   pip install fastapi[all] sqlalchemy alembic requests
   ```

4. **Run Database Migration**:
   Ensure that the database schema is up to date by running the migration script:
   ```bash
   alembic upgrade head
   ```

## How to Use the Application

1. **Start the API Server**:
   Run the FastAPI server to expose the API endpoints:
   ```bash
   uvicorn api:app --reload
   ```

2. **Launch the GUI**:
   Open another terminal window and run the GUI application:
   ```bash
   python main.py
   ```

3. **Adding a Student**:
   - Enter the student's name and email in the provided fields.
   - Click the "Add Student" button to create a new student record.

4. **Enrolling a Student in a Course**:
   - Enter the student ID (you can find this in the "View Students" section) and the course ID.
   - Click the "Enroll in Course" button to enroll the student.

5. **Viewing Students**:
   - Click the "View Students" button to retrieve and display all students in the database.

## Additional Information

- The application uses SQLite for the database, which is lightweight and easy to set up.
- The many-to-many relationship between students and courses is managed through an association table called `student_courses`.
- Ensure that the FastAPI server is running before using the GUI to avoid connection errors.

For any issues or feature requests, please contact the development team.

```
