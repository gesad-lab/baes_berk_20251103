```markdown
# ChatDev Course Management System

Welcome to the ChatDev Course Management System! This software allows users to manage students, teachers, and courses efficiently. With a user-friendly dashboard, you can easily add and manage relationships between students, teachers, and courses.

## Main Functions

- **Student Management**: Add, view, and manage student information, including their enrolled courses.
- **Teacher Management**: Add and manage teacher information.
- **Course Management**: Create and manage courses, including assigning teachers to courses.
- **Relationships**: Establish relationships between students, teachers, and courses.

## Quick Install

To get started, you'll need to install the necessary environment dependencies. You can do this using pip:

```bash
pip install fastapi sqlalchemy pydantic requests tkinter alembic
```

Make sure you have Python installed on your machine. You can download it from [python.org](https://www.python.org/downloads/).

## How to Use the Software

1. **Run the Application**:
   - Navigate to the directory where your application files are located.
   - Start the FastAPI application by running the following command:

   ```bash
   python main.py
   ```

   This will start the server on `http://127.0.0.1:8000`.

2. **Access the Dashboard**:
   - Open a web browser and go to `http://127.0.0.1:8000/docs` to access the interactive API documentation provided by FastAPI.

3. **Using the GUI**:
   - Run the GUI application by executing:

   ```bash
   python gui.py
   ```

   This will open a Tkinter window where you can manage students, teachers, and courses.

4. **Adding Students**:
   - Fill in the student name, email, and the courses they are enrolled in (comma-separated).
   - Click the "Submit Student" button to add the student.

5. **Adding Teachers**:
   - Enter the teacher's name and email.
   - Click the "Submit Teacher" button to add the teacher.

6. **Adding Courses**:
   - Provide the course name, level, and the teacher ID (if applicable).
   - Click the "Submit Course" button to add the course.

## Database Migration

The application includes a migration script to update the database schema. To apply the migration, run the following command:

```bash
alembic upgrade head
```

This will ensure that the database schema is updated to support the new relationships between courses and teachers while preserving existing data.

## Conclusion

The ChatDev Course Management System is designed to streamline the management of educational entities. With its intuitive interface and robust backend, you can efficiently manage students, teachers, and courses. For further assistance, please refer to the API documentation or contact support.

Happy managing!
```