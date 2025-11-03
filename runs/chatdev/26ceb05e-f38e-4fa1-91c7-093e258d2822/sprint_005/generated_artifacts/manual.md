```markdown
# Teacher Management System

A simple application for managing students, teachers, and courses through a user-friendly dashboard interface.

## Main Functions

The Teacher Management System provides the following functionalities:

- **Add Students**: Allows users to add new students with their names and email addresses.
- **View Students**: Displays a list of all registered students along with their details.
- **Add Teachers**: Enables users to add new teachers with their names and email addresses.
- **View Teachers**: Displays a list of all registered teachers along with their details.
- **Add Courses**: Allows users to create new courses with specified names and levels.
- **View Courses**: Displays a list of all available courses.
- **Enroll Students**: Facilitates the enrollment of students in specific courses.

## Installation Guide

To set up the Teacher Management System, follow these steps:

### 1. Clone the Repository

Clone the repository to your local machine using the following command:

```bash
git clone <repository-url>
cd <repository-directory>
```

### 2. Set Up a Virtual Environment

It is recommended to create a virtual environment to manage dependencies:

```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

### 3. Install Dependencies

Install the required dependencies listed in `requirements.txt`:

```bash
pip install -r requirements.txt
```

### 4. Run the Application

To start the application, run the following command:

```bash
python main.py
```

This will launch the FastAPI application, which can be accessed at `http://127.0.0.1:8000`.

### 5. Access the Dashboard

The GUI dashboard can be accessed through the Tkinter interface that will pop up when you run `gui.py`:

```bash
python gui.py
```

## How to Use the Application

### Adding Students

1. Enter the student's name in the "Student Name" field.
2. Enter the student's email in the "Student Email" field.
3. Click the "Add Student" button to register the student.

### Viewing Students

1. Click the "Get Students" button to retrieve and display a list of all registered students.

### Adding Teachers

1. Enter the teacher's name in the "Teacher Name" field.
2. Enter the teacher's email in the "Teacher Email" field.
3. Click the "Add Teacher" button to register the teacher.

### Viewing Teachers

1. Click the "Get Teachers" button to retrieve and display a list of all registered teachers.

### Adding Courses

1. Enter the course name in the "Course Name" field.
2. Enter the course level in the "Course Level" field.
3. Click the "Add Course" button to create the course.

### Viewing Courses

1. Click the "Get Courses" button to retrieve and display a list of all available courses.

### Enrolling Students in Courses

1. Enter the Student ID of the student you wish to enroll in the "Student ID to Enroll" field.
2. Enter the Course ID of the course in which you want to enroll the student in the "Course ID to Enroll In" field.
3. Click the "Enroll Student in Course" button to complete the enrollment.

## Conclusion

The Teacher Management System is designed to simplify the management of students, teachers, and courses. By following the installation and usage instructions, users can effectively utilize the application to meet their educational management needs.
```