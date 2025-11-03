```markdown
# Teacher Management Application

A simple application for managing students, courses, and teachers. This application allows users to add, view, and manage information related to students, courses, and teachers.

## Main Functions

- **Add Student**: Enter the name and email of a student to add them to the database.
- **View Students**: Retrieve and display a list of all students in the database.
- **Add Course**: Enter the name and level of a course to add it to the database.
- **View Courses**: Retrieve and display a list of all courses in the database.
- **Add Teacher**: Enter the name and email of a teacher to add them to the database.
- **View Teachers**: Retrieve and display a list of all teachers in the database.

## Installation Guide

To run the Teacher Management Application, you need to set up the environment and install the necessary dependencies. Follow the steps below:

### Step 1: Clone the Repository

Clone the repository to your local machine using the following command:

```bash
git clone <repository-url>
cd student_app
```

### Step 2: Set Up a Virtual Environment

It is recommended to use a virtual environment to manage dependencies. You can create one using `venv`:

```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

### Step 3: Install Dependencies

Install the required dependencies using `pip`. Make sure you have `FastAPI`, `SQLAlchemy`, `Pydantic`, and `requests` installed:

```bash
pip install fastapi sqlalchemy pydantic requests
```

### Step 4: Set Up the Database

The application uses SQLite as the database. You can create the database and tables by running the following command:

```bash
python -c "from database import create_database; create_database()"
```

### Step 5: Run the Application

To start the FastAPI server, run the following command:

```bash
uvicorn main:app --reload
```

This will start the server at `http://127.0.0.1:8000`.

### Step 6: Launch the GUI

Run the GUI application using:

```bash
python gui.py
```

## How to Use the Application

1. **Adding Students**:
   - Enter the student's name and email in the respective fields.
   - Click the "Add Student" button to save the information.

2. **Viewing Students**:
   - Click the "View Students" button to display all students in the database.

3. **Adding Courses**:
   - Enter the course name and level in the respective fields.
   - Click the "Add Course" button to save the information.

4. **Viewing Courses**:
   - Click the "View Courses" button to display all courses in the database.

5. **Adding Teachers**:
   - Enter the teacher's name and email in the respective fields.
   - Click the "Add Teacher" button to save the information.

6. **Viewing Teachers**:
   - Click the "View Teachers" button to display all teachers in the database.

## Conclusion

This application provides a simple interface for managing students, courses, and teachers. It is designed to be user-friendly and efficient, allowing users to easily add and view information. For any issues or feature requests, please contact the development team.
```