Here's a detailed user manual for the software, formatted in Markdown as requested:

```markdown
# Teacher Management System

A simple application for managing students, courses, and teachers.

## Main Functions

This software provides the following functionalities:

- **Manage Students**: Add, view, and manage student records.
- **Manage Courses**: Add, view, and manage course records.
- **Manage Teachers**: Add, view, and manage teacher records.
- **Enroll Students**: Enroll students in courses.

## Quick Install

To set up the environment and install the necessary dependencies, follow these steps:

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

3. **Install Required Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

   Ensure you have the following dependencies in your `requirements.txt`:
   ```
   sqlalchemy
   alembic
   requests
   pydantic
   tkinter
   ```

4. **Run Database Migration**:
   To create the necessary database tables, run:
   ```bash
   python main.py
   ```

## How to Use the Application

1. **Start the Application**:
   Run the GUI application using:
   ```bash
   python gui.py
   ```

2. **Managing Students**:
   - **Add Student**: Enter the student's name and email, then click "Add Student".
   - **View Students**: Click "Get Students" to see the list of all students.

3. **Managing Courses**:
   - **Add Course**: Enter the course name and level, then click "Add Course".
   - **View Courses**: Click "Get Courses" to see the list of all courses.

4. **Managing Teachers**:
   - **Add Teacher**: Enter the teacher's name and email, then click "Add Teacher".
   - **View Teachers**: Click "Get Teachers" to see the list of all teachers.

5. **Enroll Students in Courses**:
   - Enter the student ID and course ID, then click "Enroll Student in Course" to enroll the student.

## Additional Information

- **Database**: The application uses SQLite for data storage. The database file is named `students.db`.
- **Data Preservation**: The database migration process ensures that existing student and course data is preserved when adding the Teacher entity.

## Support

For any issues or questions, please reach out to our support team at [support@chatdev.com](mailto:support@chatdev.com).

```

This manual provides a comprehensive overview of the application, including installation instructions, usage guidelines, and support information. Let me know if you need any further modifications or additional sections!