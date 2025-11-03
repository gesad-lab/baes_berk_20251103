```markdown
# Student Management Application

A comprehensive application for managing students, courses, and teachers. This application allows users to add, view, and manage the relationships between students, courses, and teachers.

## Main Functions

- **Add Student**: Create a new student and enroll them in courses.
- **Add Course**: Create a new course and associate it with a teacher.
- **Add Teacher**: Create a new teacher.
- **View Students**: Retrieve and display a list of all students.
- **View Courses**: Retrieve and display a list of all courses.
- **View Teachers**: Retrieve and display a list of all teachers.

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

3. **Install Dependencies**:
   Create a `requirements.txt` file with the following content:
   ```
   fastapi
   uvicorn
   sqlalchemy
   alembic
   pydantic
   requests
   ```
   Then run:
   ```bash
   pip install -r requirements.txt
   ```

## Running the Application

1. **Start the FastAPI Server**:
   Open a terminal and navigate to the project directory. Run the following command to start the server:
   ```bash
   uvicorn routes:router --reload
   ```

2. **Launch the GUI**:
   In another terminal, run the following command to start the GUI:
   ```bash
   python gui.py
   ```

3. **Using the Application**:
   - **Add Student**: Enter the student's name and email, then click "Add Student".
   - **Add Course**: Enter the course name, level, and teacher ID, then click "Add Course".
   - **Add Teacher**: Enter the teacher's name and email, then click "Add Teacher".
   - **View Students**: Click "View Students" to see the list of all students.
   - **View Courses**: Click "View Courses" to see the list of all courses.
   - **View Teachers**: Click "View Teachers" to see the list of all teachers.

## Database Migration

The application uses Alembic for database migrations. To apply migrations and ensure the database schema is up-to-date, run the following command:
```bash
alembic upgrade head
```

This will create the necessary tables and relationships in the database, preserving existing data.

## Conclusion

This Student Management Application provides a user-friendly interface for managing students, courses, and teachers. By following the installation and usage instructions, users can effectively utilize the application to meet their educational management needs.
```