```markdown
# ChatDev Course Management System

Welcome to the ChatDev Course Management System! This software allows users to manage students, courses, and teachers efficiently. Below is a detailed user manual that covers the main functions of the software, installation instructions, and usage guidelines.

## Main Functions

1. **Student Management**: 
   - Add new students with their names, emails, and enrolled courses.
   - Retrieve a list of all students.

2. **Course Management**: 
   - Create new courses with associated names, levels, and teachers.
   - Retrieve a list of all courses.

3. **Teacher Management**: 
   - Add new teachers with their names and emails.
   - Retrieve a list of all teachers.

4. **Relationships**: 
   - Each course can have an associated teacher.
   - Students can enroll in multiple courses.

## Installation Instructions

To set up the environment and run the ChatDev Course Management System, follow these steps:

### Prerequisites

- Ensure you have Python 3.7 or higher installed on your machine.
- Install pip (Python package installer) if it is not already installed.

### Step 1: Clone the Repository

Clone the repository containing the source code:

```bash
git clone https://github.com/your-repo/chatdev-course-management.git
cd chatdev-course-management
```

### Step 2: Install Dependencies

Install the required dependencies using pip:

```bash
pip install -r requirements.txt
```

Make sure to include the following dependencies in your `requirements.txt`:

```
fastapi
uvicorn
sqlalchemy
pydantic
alembic
requests
tkinter
```

### Step 3: Database Migration

Run the database migration to set up the necessary tables:

```bash
alembic upgrade head
```

This command will create the `students`, `courses`, and `teachers` tables in your SQLite database while preserving existing data.

### Step 4: Run the Application

Start the FastAPI application using Uvicorn:

```bash
uvicorn main:app --reload
```

The application will be accessible at `http://127.0.0.1:8000`.

### Step 5: Launch the GUI

Run the GUI application by executing:

```bash
python main.py
```

## How to Use the Application

### Adding a Student

1. Enter the student's name in the "Enter Student Name" field.
2. Enter the student's email in the "Enter Student Email" field.
3. Enter the course IDs (comma-separated) in the "Enter Course IDs" field.
4. Click the "Submit Student" button to add the student.

### Adding a Teacher

1. Enter the teacher's name in the "Enter Teacher Name" field.
2. Enter the teacher's email in the "Enter Teacher Email" field.
3. Click the "Submit Teacher" button to add the teacher.

### Adding a Course

1. Enter the course name in the "Enter Course Name" field.
2. Enter the course level in the "Enter Course Level" field.
3. Enter the teacher ID for the course in the "Enter Teacher ID for Course" field.
4. Click the "Submit Course" button to add the course.

### Viewing Data

- You can view all students, teachers, and courses by using the respective retrieval functions in the backend or by implementing additional GUI features.

## Conclusion

The ChatDev Course Management System provides a comprehensive solution for managing educational entities. With its user-friendly interface and robust backend, you can efficiently handle students, courses, and teachers. For any issues or feature requests, please reach out to our support team.

Happy managing!
```