```markdown
# Student Management Application

A simple application for managing students and courses using FastAPI and SQLite.

## Main Functions

The Student Management Application allows users to:

- **Add Students**: Create new student records with a name and email.
- **View Students**: Retrieve and display a list of all registered students.
- **Add Courses**: Create new course records with a name and level.
- **View Courses**: Retrieve and display a list of all available courses.

## Quick Install

To set up the environment and run the application, follow these steps:

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

3. **Install Required Dependencies**:
   ```bash
   pip install fastapi[all] sqlalchemy alembic requests
   ```

4. **Run Database Migration**:
   Before running the application, ensure that the database schema is up to date. Run the migration script:
   ```bash
   alembic upgrade head
   ```

5. **Run the Application**:
   Start the FastAPI server:
   ```bash
   uvicorn main:app --reload
   ```

6. **Access the Application**:
   Open your web browser and navigate to `http://127.0.0.1:8000/docs` to access the interactive API documentation.

## How to Use the Application

### Adding a Student

1. In the GUI, enter the student's name and email in the provided fields.
2. Click the "Add Student" button.
3. If successful, the student will be added to the database, and a confirmation message will be displayed.

### Viewing Students

1. Click the "View Students" button in the GUI.
2. The application will retrieve and display a list of all students, including their IDs, names, and emails.

### Adding a Course

To add a course, you will need to implement a similar GUI component as the student addition. The backend API function `create_course` can be used to handle course creation.

### Viewing Courses

Similar to viewing students, you can implement a GUI component to retrieve and display courses using the `get_courses` API function.

## Database Structure

The application uses SQLite as the database, with two main tables:

- **students**: Contains fields for student ID, name, and email.
- **courses**: Contains fields for course ID, name, and level.

## Additional Information

For further details on the API endpoints and their usage, refer to the interactive documentation available at `http://127.0.0.1:8000/docs`.

For any issues or feature requests, please contact the development team.

Happy coding!
```