```markdown
# Student Management System

A comprehensive application for managing students, courses, and teachers. This software allows users to create and manage student records, course offerings, and teacher assignments efficiently.

## Main Functions

- **Student Management**: Add, view, and manage student records.
- **Course Management**: Create and manage courses, including assigning teachers to courses.
- **Teacher Management**: Add, view, and manage teacher records.
- **Enrollment**: Enroll students in courses and manage their course selections.

## Installation Instructions

To run the Student Management System, you need to set up the environment and install the required dependencies. Follow these steps:

### Prerequisites

- Python 3.7 or higher
- pip (Python package installer)

### Step 1: Clone the Repository

Clone the repository to your local machine using the following command:

```bash
git clone https://github.com/yourusername/student_management_system.git
cd student_management_system
```

### Step 2: Create a Virtual Environment (Optional but Recommended)

It's a good practice to create a virtual environment to manage dependencies:

```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

### Step 3: Install Dependencies

Install the required Python packages using pip:

```bash
pip install fastapi sqlalchemy alembic requests
```

### Step 4: Run Database Migration

Before running the application, ensure the database schema is up to date. Run the migration script to create the necessary tables:

```bash
alembic upgrade head
```

## How to Use the Application

### Step 1: Start the Application

Run the application using the following command:

```bash
uvicorn main:app --reload
```

This will start the FastAPI server on `http://127.0.0.1:8000`.

### Step 2: Access the GUI

Open your web browser and navigate to `http://127.0.0.1:8000/docs` to access the interactive API documentation. You can also use the GUI provided in the application.

### Step 3: Managing Students

- **Add Student**: Enter the student's name and email, then click "Add Student".
- **View Students**: Click "View Students" to see the list of all students.

### Step 4: Managing Teachers

- **Add Teacher**: Enter the teacher's name and email, then click "Add Teacher".
- **View Teachers**: Click "View Teachers" to see the list of all teachers.

### Step 5: Managing Courses

- **Add Course**: Enter the course name, level, and select a teacher from the list, then click "Add Course".
- **View Courses**: Click "View Courses" to see the list of all courses.

### Step 6: Enroll Students in Courses

- Select a student from the list and a course from the courses list, then click "Enroll Student in Course" to enroll the selected student in the selected course.

## Conclusion

The Student Management System provides a user-friendly interface for managing students, teachers, and courses. With its robust backend powered by FastAPI and SQLAlchemy, it ensures efficient data handling and retrieval. For any issues or feature requests, please contact the development team.
```