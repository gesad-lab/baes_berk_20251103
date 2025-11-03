```markdown
# Student Management Application

A comprehensive application for managing students and their associated courses. This software allows users to create, view, and manage student and course records seamlessly.

## Main Functions

- **Add Student**: Create a new student record with their name, email, and associated course IDs.
- **View Students**: Retrieve and display a list of all students along with their associated courses.
- **Add Course**: Create a new course record with its name and level.
- **View Courses**: Retrieve and display a list of all courses available in the system.

## Installation Guide

To set up the environment and run the Student Management Application, follow these steps:

### Prerequisites

Make sure you have Python 3.7 or higher installed on your machine. You can download it from [python.org](https://www.python.org/downloads/).

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

### Step 3: Install Required Dependencies

Install the necessary dependencies using pip:

```bash
pip install fastapi[all] sqlalchemy alembic requests
```

### Step 4: Run Database Migration

Before running the application, you need to set up the database schema. Run the migration script:

```bash
alembic upgrade head
```

### Step 5: Start the Application

Run the FastAPI application:

```bash
uvicorn api:app --reload
```

The application will be available at `http://127.0.0.1:8000`.

### Step 6: Launch the GUI

To use the graphical user interface (GUI), run the following command:

```bash
python main.py
```

## How to Use the Application

### Adding a Student

1. Open the GUI.
2. Enter the student's name and email in the respective fields.
3. Enter the course IDs (comma-separated) that the student is enrolled in.
4. Click the "Add Student" button to save the student record.

### Viewing Students

- The application will automatically display all students along with their associated courses in the GUI.

### Adding a Course

1. Enter the course name and level in the respective fields.
2. Click the "Add Course" button to save the course record.

### Viewing Courses

- The application will automatically display all courses available in the system.

## Conclusion

The Student Management Application provides a user-friendly interface for managing students and courses. With the ability to add and view records, it simplifies the process of educational administration. For any issues or feature requests, please reach out to the development team.

```
