```markdown
# Student Management System

A comprehensive application for managing students and their course enrollments.

## Main Functions

The Student Management System allows users to:

- **Add Students**: Create new student profiles with names and email addresses.
- **Add Courses**: Create new courses with names and levels.
- **Enroll Students in Courses**: Enroll students in various courses to manage their academic progress.
- **View Students**: Retrieve and display a list of all registered students.

## Installation Guide

To set up the Student Management System, follow these steps:

### Prerequisites

Ensure you have Python 3.7 or higher installed on your machine. You can download it from [python.org](https://www.python.org/downloads/).

### Step 1: Clone the Repository

Clone the repository containing the Student Management System code:

```bash
git clone https://github.com/yourusername/student_management_system.git
cd student_management_system
```

### Step 2: Create a Virtual Environment

It's recommended to create a virtual environment to manage dependencies:

```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

### Step 3: Install Dependencies

Install the required dependencies using pip:

```bash
pip install fastapi sqlalchemy alembic requests tkinter
```

### Step 4: Run Database Migrations

Before starting the application, run the database migrations to set up the database schema:

```bash
python -m alembic upgrade head
```

## How to Use the Application

### Step 1: Start the Application

Run the application by executing the following command:

```bash
python main.py
```

### Step 2: Interact with the GUI

Once the application is running, a GUI window will appear. You can use the following features:

1. **Add Student**:
   - Enter the student's name and email in the respective fields.
   - Click the "Add Student" button to create a new student profile.

2. **Add Course**:
   - Enter the course name and level in the respective fields.
   - Click the "Add Course" button to create a new course.

3. **Show Students**:
   - Click the "Show Students" button to retrieve and display a list of all registered students.

### Step 3: Enroll Students in Courses

To enroll a student in a course, you can use the API endpoint `/students/{student_id}/courses/{course_id}/enroll` via a tool like Postman or cURL. Replace `{student_id}` and `{course_id}` with the respective IDs of the student and course.

## Additional Information

For more detailed documentation on FastAPI, SQLAlchemy, and Alembic, please refer to their official documentation:

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [SQLAlchemy Documentation](https://docs.sqlalchemy.org/)
- [Alembic Documentation](https://alembic.sqlalchemy.org/en/latest/)

For any issues or feature requests, please open an issue on the repository or contact the development team.

Happy managing!
```