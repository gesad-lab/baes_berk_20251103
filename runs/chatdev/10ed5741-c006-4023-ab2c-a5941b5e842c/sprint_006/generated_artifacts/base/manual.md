Here's a detailed user manual for the software, formatted in Markdown as requested:

```markdown
# Teacher Management System

A simple application for managing teachers, students, and courses.

## Introduction

The Teacher Management System allows users to manage teachers, students, and courses efficiently. The application provides a user-friendly interface for adding and retrieving information about teachers and their associated students and courses.

### Main Functions

- **Add Teacher**: Create a new teacher with a name and email.
- **View Teachers**: Retrieve a list of all teachers in the system.
- **Add Student**: Create a new student with a name, email, and associated courses.
- **View Students**: Retrieve a list of all students in the system.
- **Add Course**: Create a new course with a name and level.
- **View Courses**: Retrieve a list of all courses in the system.

## Installation

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

1. **Database Migration**:
   Before running the application, ensure that the database schema is up to date. Run the migration script:
   ```bash
   alembic upgrade head
   ```

2. **Start the API Server**:
   Run the FastAPI application using Uvicorn:
   ```bash
   uvicorn api:router --reload
   ```

3. **Launch the GUI**:
   Run the GUI application:
   ```bash
   python main.py
   ```

## Using the Application

### Adding a Teacher

1. Open the GUI application.
2. Enter the teacher's name in the "Enter Teacher Name" field.
3. Enter the teacher's email in the "Enter Teacher Email" field.
4. Click the "Add Teacher" button.
5. A confirmation message will appear if the teacher is added successfully.

### Viewing Teachers

- The application currently does not have a dedicated view for teachers. You can retrieve the list of teachers through the API endpoint `/teachers/` using a tool like Postman or a web browser.

### Adding a Student

1. Enter the student's name in the "Enter Student Name" field.
2. Enter the student's email in the "Enter Student Email" field.
3. Enter the course IDs (comma-separated) in the "Enter Course IDs" field.
4. Click the "Add Student" button.
5. A confirmation message will appear if the student is added successfully.

### Adding a Course

1. Enter the course name in the "Enter Course Name" field.
2. Enter the course level in the "Enter Course Level" field.
3. Click the "Add Course" button.
4. A confirmation message will appear if the course is added successfully.

### Viewing Students and Courses

- Similar to viewing teachers, you can retrieve the lists of students and courses through their respective API endpoints (`/students/` and `/courses/`).

## Conclusion

The Teacher Management System is a straightforward application designed to help manage educational entities effectively. For further enhancements or support, please reach out to the development team.

```

This manual provides a comprehensive overview of the application, including installation instructions, usage guidelines, and descriptions of the main functions.