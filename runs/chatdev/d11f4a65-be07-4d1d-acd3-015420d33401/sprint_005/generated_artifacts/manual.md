```markdown
# Teacher Management System

A simple application for managing teachers, students, and courses using a graphical user interface (GUI) built with Tkinter and a backend API.

## Main Functions

The Teacher Management System allows users to:

- **Add Students**: Input student names and emails to create new student records.
- **Add Courses**: Input course names and levels to create new course records.
- **Add Teachers**: Input teacher names and emails to create new teacher records.
- **View Outputs**: Display success or failure messages for each operation in the GUI.

## Installation

To set up the environment and run the application, follow these steps:

### Prerequisites

Ensure you have Python 3.x installed on your machine. You can download it from [python.org](https://www.python.org/downloads/).

### Step 1: Install Dependencies

Create a virtual environment (optional but recommended):

```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

Install the required packages using pip:

```bash
pip install sqlalchemy alembic pydantic requests tkinter
```

### Step 2: Set Up the Database

The application uses SQLite for the database. The database file will be created automatically when you run the application for the first time.

### Step 3: Run Database Migrations

Before running the application, you need to apply the database migrations to create the necessary tables. Run the following command:

```bash
alembic upgrade head
```

This command will apply all migrations, including creating the `students`, `courses`, and `teachers` tables while preserving existing data.

## How to Use the Application

1. **Run the Application**: Execute the main application script.

   ```bash
   python main.py
   ```

2. **Adding Students**:
   - Enter the student's name in the "Student Name" field.
   - Enter the student's email in the "Student Email" field.
   - Click the "Add Student" button to submit the information.

3. **Adding Courses**:
   - Enter the course name in the "Course Name" field.
   - Enter the course level in the "Course Level" field.
   - Click the "Add Course" button to submit the information.

4. **Adding Teachers**:
   - Enter the teacher's name in the "Teacher Name" field.
   - Enter the teacher's email in the "Teacher Email" field.
   - Click the "Add Teacher" button to submit the information.

5. **View Outputs**: The output area will display messages indicating whether the addition of a student, course, or teacher was successful or if it failed.

## Conclusion

This Teacher Management System provides a simple interface for managing educational entities. It is designed to be user-friendly and efficient, allowing for easy addition and management of students, courses, and teachers.

For any issues or feature requests, please contact the development team.
```