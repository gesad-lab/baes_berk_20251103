```markdown
# ChatDev Course Management System

Welcome to the ChatDev Course Management System! This software allows you to manage students, courses, and teachers effectively. You can add students, create courses, and assign teachers to those courses.

## Main Functions

- **Student Management**: Add, view, and manage student information including their names and emails.
- **Course Management**: Create courses with specific levels and assign teachers to those courses.
- **Teacher Management**: Add and manage teacher information including their names and emails.
- **Relationships**: Establish relationships between students, courses, and teachers.

## Quick Install

To set up the environment and install the necessary dependencies, follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-repo/chatdev-course-management.git
   cd chatdev-course-management
   ```

2. **Create a Virtual Environment** (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run Database Migrations**:
   Ensure that the database schema is up to date by running the migration scripts:
   ```bash
   alembic upgrade head
   ```

## How to Use the Application

1. **Start the Application**:
   Run the main application script:
   ```bash
   python main.py
   ```

2. **User Interface**:
   The application will launch a graphical user interface (GUI) using Tkinter. You will see three sections for managing students, courses, and teachers.

   - **Student Management**:
     - Enter the student's name and email.
     - Click "Add Student" to save the information.

   - **Course Management**:
     - Enter the course name and level.
     - Enter the Teacher ID to associate the course with a teacher.
     - Click "Add Course" to save the information.

   - **Teacher Management**:
     - Enter the teacher's name and email.
     - Click "Add Teacher" to save the information.

3. **Viewing Information**:
   After adding students, courses, or teachers, you will see confirmation messages in the output area of the GUI.

## Database Schema

The application uses SQLite as the database backend. The following tables are created:

- **students**: Stores student information including ID, name, and email.
- **courses**: Stores course information including ID, name, level, and associated teacher ID.
- **teachers**: Stores teacher information including ID, name, and email.
- **student_courses**: An association table that links students to courses.

## Important Notes

- Ensure that the database is properly migrated before running the application to avoid any schema-related issues.
- The application is designed to preserve existing data during migrations, so you can safely update the schema without losing information.

## Support

For any issues or questions, please reach out to our support team or check the documentation for further assistance.

Thank you for using the ChatDev Course Management System!
```