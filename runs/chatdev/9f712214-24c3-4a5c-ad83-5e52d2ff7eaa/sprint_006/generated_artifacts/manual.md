```markdown
# Student Management System

A comprehensive application for managing students, courses, and teachers, built using FastAPI and Tkinter.

## Main Functions

The Student Management System provides the following functionalities:

- **Student Management**: Create, retrieve, and manage student records.
- **Course Management**: Create, retrieve, and manage courses, including associating them with teachers.
- **Teacher Management**: Create, retrieve, and manage teacher records.
- **Enrollment**: Enroll students in courses.

## Quick Install

To set up the environment and install the required dependencies, follow these steps:

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

## Database Migration

To set up the database schema, run the migration scripts using Alembic:

1. **Initialize Alembic** (if not already done):
   ```bash
   alembic init alembic
   ```

2. **Run Migrations**:
   ```bash
   alembic upgrade head
   ```

This will create the necessary tables in your SQLite database (`students.db`).

## How to Use the Application

1. **Start the FastAPI Server**:
   Run the following command to start the server:
   ```bash
   uvicorn main:app --reload
   ```

2. **Access the GUI**:
   Open a new terminal and run the GUI application:
   ```bash
   python gui.py
   ```

3. **Using the GUI**:
   - **Student Management**:
     - Enter the student's name and email, then click "Submit" to create a new student.
     - You can view the output in the text area below the input fields.

   - **Course Management**:
     - Enter the course name, level, and optional teacher ID, then click "Submit" to create a new course.
     - The output will display the created course details.

   - **Teacher Management**:
     - Enter the teacher's name and email, then click "Submit" to create a new teacher.
     - The output will show the created teacher details.

4. **Enroll Students in Courses**:
   - Use the enrollment feature by providing the student ID and course ID to enroll a student in a specific course.

## Additional Information

For more detailed documentation on FastAPI, SQLAlchemy, and Alembic, please refer to their official documentation:

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [SQLAlchemy Documentation](https://docs.sqlalchemy.org/en/14/)
- [Alembic Documentation](https://alembic.sqlalchemy.org/en/latest/)

Feel free to reach out for support or suggestions to improve the application!
```