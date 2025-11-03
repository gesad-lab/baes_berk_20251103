Here's a detailed user manual for the software, formatted in Markdown as requested:

```markdown
# Teacher Management System

A simple application for managing students, courses, and teachers through a graphical user interface (GUI) and a FastAPI backend.

## Main Functions

The Teacher Management System allows users to:

- **Create and manage students**: Add new students with their names and emails, and view the list of existing students.
- **Create and manage courses**: Add new courses with their names and levels, and view the list of existing courses.
- **Create and manage teachers**: Add new teachers with their names and emails, and view the list of existing teachers.
- **Enroll students in courses**: Enroll students in specific courses.

## Installation

To set up the environment and run the application, follow these steps:

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Create a virtual environment** (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install the required dependencies**:
   ```bash
   pip install fastapi[all] sqlalchemy alembic pydantic requests
   ```

4. **Run the database migration**:
   Ensure that the migration script is executed to create the necessary database tables:
   ```bash
   alembic upgrade head
   ```

5. **Start the FastAPI server**:
   Run the main application:
   ```bash
   uvicorn main:app --reload
   ```

6. **Run the GUI**:
   In a separate terminal, run the GUI application:
   ```bash
   python gui.py
   ```

## How to Use the Application

### GUI Overview

- **Student Management**:
  - Enter the student's name and email in the respective fields and click "Create Student" to add a new student.
  - Click "List Students" to view all existing students.

- **Course Management**:
  - Enter the course name and level in the respective fields and click "Create Course" to add a new course.
  - Click "List Courses" to view all existing courses.

- **Teacher Management**:
  - Enter the teacher's name and email in the respective fields and click "Create Teacher" to add a new teacher.
  - Click "List Teachers" to view all existing teachers.

- **Enrollment**:
  - Enter the student ID and course ID in the respective fields and click "Enroll Student in Course" to enroll a student in a course.

### API Endpoints

The application also exposes several API endpoints for programmatic access:

- **Students**:
  - `POST /students/`: Create a new student.
  - `GET /students/`: Retrieve a list of students.

- **Courses**:
  - `POST /courses/`: Create a new course.
  - `GET /courses/`: Retrieve a list of courses.

- **Teachers**:
  - `POST /teachers/`: Create a new teacher.
  - `GET /teachers/`: Retrieve a list of teachers.

- **Enrollment**:
  - `POST /students/{student_id}/courses/{course_id}`: Enroll a student in a course.

## Conclusion

This Teacher Management System provides a simple yet effective way to manage students, courses, and teachers. By following the installation and usage instructions, you can easily set up and run the application. For further assistance, please refer to the code documentation or reach out to the development team.
```

This manual provides a comprehensive overview of the application, including its main functions, installation instructions, and usage guidelines. Let me know if you need any modifications or additional information!