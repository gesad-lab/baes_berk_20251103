```markdown
# Student Management System

A comprehensive application for managing students and their course enrollments.

## Main Functions

The Student Management System allows users to:

- **Add Students**: Create new student records with names and emails.
- **View Students**: Retrieve and display a list of all students in the database.
- **Add Courses**: Create new course records with names and levels.
- **View Courses**: Retrieve and display a list of all courses in the database.
- **Enroll Students in Courses**: Enroll a student in a selected course, establishing a many-to-many relationship between students and courses.

## Installation Instructions

To set up the Student Management System, follow these steps:

### Prerequisites

Ensure you have Python 3.7 or higher installed on your machine. You can download it from [python.org](https://www.python.org/downloads/).

### Step 1: Clone the Repository

Clone the repository containing the code:

```bash
git clone <repository-url>
cd student_app
```

### Step 2: Create a Virtual Environment

It's recommended to create a virtual environment to manage dependencies:

```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

### Step 3: Install Required Dependencies

Install the necessary Python packages using pip:

```bash
pip install fastapi sqlalchemy alembic requests
```

### Step 4: Run Database Migration

Before running the application, you need to apply the database migrations to create the necessary tables:

```bash
alembic upgrade head
```

## How to Use the Application

### Step 1: Start the FastAPI Server

Run the FastAPI server to host the API:

```bash
uvicorn main:app --reload
```

### Step 2: Access the GUI

The GUI is built using Tkinter. Run the GUI application:

```bash
python gui.py
```

### Step 3: Interact with the Application

1. **Add a Student**:
   - Enter the student's name and email in the respective fields.
   - Click on "Add Student" to save the student to the database.

2. **View Students**:
   - Click on "View Students" to display the list of all students.

3. **Add a Course**:
   - Enter the course name and level in the respective fields.
   - Click on "Add Course" to save the course to the database.

4. **View Courses**:
   - Click on "View Courses" to display the list of all courses.

5. **Enroll a Student in a Course**:
   - Select a student from the list and a course from the courses list.
   - Click on "Enroll Student in Course" to enroll the selected student in the selected course.

## Conclusion

The Student Management System provides a user-friendly interface for managing students and their course enrollments. With the ability to add, view, and enroll students and courses, it serves as a powerful tool for educational institutions.

For any issues or feature requests, please contact the support team.
```