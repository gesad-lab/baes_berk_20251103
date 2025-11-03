```markdown
# Teacher Management System

A simple application for managing students, courses, and teachers using a FastAPI backend and a Tkinter GUI.

## Main Functions

The Teacher Management System allows users to:

- **Manage Students**: Add, view, and enroll students in courses.
- **Manage Courses**: Create and view courses.
- **Manage Teachers**: Add and view teachers.

## Installation

To set up the environment and run the application, follow these steps:

### Prerequisites

Ensure you have Python 3.7 or higher installed on your machine. You can download it from [python.org](https://www.python.org/downloads/).

### Step 1: Clone the Repository

Clone the repository containing the application code:

```bash
git clone <repository-url>
cd student_app
```

### Step 2: Create a Virtual Environment

It is recommended to create a virtual environment to manage dependencies:

```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

### Step 3: Install Dependencies

Install the required dependencies using pip:

```bash
pip install fastapi[all] sqlalchemy alembic requests
```

### Step 4: Run Database Migrations

Before starting the application, run the database migrations to set up the database schema:

```bash
alembic upgrade head
```

### Step 5: Start the Application

Run the FastAPI application:

```bash
uvicorn main:app --reload
```

The application will be available at `http://127.0.0.1:8000`.

### Step 6: Run the GUI

To run the GUI, execute:

```bash
python gui.py
```

## How to Use the Application

### Adding a Student

1. Enter the student's name and email in the respective fields.
2. Click the "Add Student" button.
3. The added student will be displayed in the output area.

### Adding a Course

1. Enter the course name and level in the respective fields.
2. Click the "Add Course" button.
3. The added course will be displayed in the output area.

### Adding a Teacher

1. Enter the teacher's name and email in the respective fields.
2. Click the "Add Teacher" button.
3. The added teacher will be displayed in the output area.

### Viewing Students

1. Click the "Show Students" button.
2. The list of students will be displayed in the output area.

## Conclusion

The Teacher Management System provides a straightforward interface for managing students, courses, and teachers. With a simple setup and user-friendly GUI, it is designed to facilitate educational management tasks efficiently.

For further assistance, please refer to the code comments or reach out to the development team.
```