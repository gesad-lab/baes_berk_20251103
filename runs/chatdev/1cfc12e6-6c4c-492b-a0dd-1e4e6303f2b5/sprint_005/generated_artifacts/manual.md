```markdown
# Teacher Management Application

A simple application for managing students, courses, and teachers. This application allows users to add and view students and teachers, as well as enroll students in courses.

## Main Functions

- **Add Student**: Allows users to input student details (name and email) and add them to the database.
- **Add Teacher**: Allows users to input teacher details (name and email) and add them to the database.
- **Enroll Student in Course**: Enables users to enroll a student in a specific course.
- **View Students**: Displays a list of all students currently in the database.

## Installation Guide

To set up the environment and run the application, follow these steps:

### Prerequisites

- Python 3.7 or higher
- pip (Python package installer)

### Step 1: Clone the Repository

```bash
git clone https://github.com/your-repo/teacher-management-app.git
cd teacher-management-app
```

### Step 2: Create a Virtual Environment

It is recommended to create a virtual environment to manage dependencies.

```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

### Step 3: Install Dependencies

Install the required dependencies using pip:

```bash
pip install fastapi sqlalchemy alembic requests tkinter
```

### Step 4: Run Database Migration

Before running the application, you need to create the database schema. Use the migration script to add the Teacher entity while preserving existing Student and Course data.

```bash
alembic upgrade head
```

### Step 5: Run the Application

Start the FastAPI server:

```bash
uvicorn api:app --reload
```

Then, run the GUI application:

```bash
python main.py
```

## How to Use the Application

1. **Adding a Student**:
   - Enter the student's name and email in the respective fields.
   - Click the "Add Student" button to save the student to the database.

2. **Adding a Teacher**:
   - Enter the teacher's name and email in the respective fields.
   - Click the "Add Teacher" button to save the teacher to the database.

3. **Enrolling a Student in a Course**:
   - Enter the student ID (you can find this in the "View Students" section) and the course ID.
   - Click the "Enroll in Course" button to enroll the student.

4. **Viewing Students**:
   - Click the "View Students" button to display all students in the database.

## Additional Information

For any issues or feature requests, please contact the development team at support@teacher-management-app.com.

Thank you for using the Teacher Management Application!
```