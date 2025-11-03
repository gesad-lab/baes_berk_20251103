```markdown
# Teacher Management System

A simple application for managing students, courses, and teachers using FastAPI and SQLite.

## Overview

This application allows users to create, retrieve, and manage records for students, courses, and teachers. It provides a user-friendly GUI built with Tkinter, enabling easy interaction with the underlying API.

### Main Functions

- **Student Management**: Create and retrieve student records.
- **Course Management**: Create and retrieve course records.
- **Teacher Management**: Create and retrieve teacher records.
- **Enrollment**: Enroll students in courses.

## Installation Guide

To set up the environment and install the necessary dependencies, follow these steps:

### Prerequisites

Make sure you have Python 3.7 or higher installed on your machine.

### Step 1: Clone the Repository

Clone the repository to your local machine:

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
pip install -r requirements.txt
```

### Step 4: Run Database Migrations

Run the database migrations to create the necessary tables:

```bash
alembic upgrade head
```

### Step 5: Start the Application

Run the FastAPI application using Uvicorn:

```bash
uvicorn main:app --reload
```

## How to Use the Application

### Accessing the GUI

Once the application is running, you can access the GUI by opening a new terminal and running:

```bash
python gui.py
```

### Managing Students

1. **Add a Student**:
   - Enter the student's name and email in the respective fields.
   - Click the "Submit" button to create a new student record.

2. **View Students**:
   - The application will display a list of students after successful creation.

### Managing Courses

1. **Add a Course**:
   - Enter the course name and level in the respective fields.
   - Click the "Submit" button to create a new course record.

2. **View Courses**:
   - The application will display a list of courses after successful creation.

### Managing Teachers

1. **Add a Teacher**:
   - Enter the teacher's name and email in the respective fields.
   - Click the "Submit" button to create a new teacher record.

2. **View Teachers**:
   - The application will display a list of teachers after successful creation.

### Enrolling Students in Courses

1. **Enroll a Student**:
   - Use the API endpoint to enroll a student in a course by providing the student ID and course ID.

## API Endpoints

The application exposes the following API endpoints:

- **Students**:
  - `POST /students/`: Create a new student.
  - `GET /students/`: Retrieve a list of students.

- **Courses**:
  - `POST /courses/`: Create a new course.
  - `GET /courses/`: Retrieve a list of courses.

- **Teachers**:
  - `POST /teachers/`: Create a new teacher.
  - `GET /teachers/`: Retrieve a list of teachers.

## Conclusion

This Teacher Management System provides a simple yet effective way to manage students, courses, and teachers. With a clean GUI and a robust backend, it serves as a foundational tool for educational institutions.

For further assistance, please refer to the documentation or reach out for support.
```