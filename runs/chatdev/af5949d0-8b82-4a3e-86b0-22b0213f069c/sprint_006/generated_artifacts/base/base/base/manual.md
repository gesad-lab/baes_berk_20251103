```markdown
# Student Management System

A simple application for managing students and courses using a web-based interface.

## Main Functions

The Student Management System allows users to:

- **Add Students**: Create new student records with a name and email.
- **View Students**: Retrieve a list of all registered students.
- **Add Courses**: Create new course records with a name and level.
- **View Courses**: Retrieve a list of all available courses.

## Installation Guide

To set up the Student Management System, follow these steps:

### Prerequisites

Ensure you have Python 3.7 or higher installed on your machine. You can download it from [python.org](https://www.python.org/downloads/).

### Step 1: Clone the Repository

Clone the repository containing the application code:

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
pip install fastapi[all] sqlalchemy alembic requests
```

### Step 4: Initialize the Database

Run the following command to create the database and tables:

```bash
python -c "from database import init_db; init_db()"
```

### Step 5: Run the Application

Start the FastAPI server:

```bash
uvicorn main:app --reload
```

The application will be accessible at `http://127.0.0.1:8000`.

## How to Use the Application

### Adding Students

1. Open the application in your web browser at `http://127.0.0.1:8000`.
2. Enter the student's name and email in the respective fields.
3. Click the "Add Student" button to submit the form.
4. You will see a confirmation message if the student was added successfully.

### Viewing Students

- The application will automatically display the list of students after adding a new student.

### Adding Courses

1. Enter the course name and level in the respective fields.
2. Click the "Add Course" button to submit the form.
3. You will see a confirmation message if the course was added successfully.

### Viewing Courses

- The application will automatically display the list of courses after adding a new course.

## Additional Information

For more details on the API endpoints, you can visit the automatically generated documentation at `http://127.0.0.1:8000/docs`.

## Troubleshooting

If you encounter any issues, ensure that all dependencies are installed correctly and that the FastAPI server is running. Check the console for any error messages.

For further assistance, please reach out to the support team or consult the documentation for FastAPI and SQLAlchemy.

```
