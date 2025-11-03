Here is the `manual.md` file that provides a detailed user manual for the software, including an introduction to its main functions, installation instructions, and usage guidelines.

```markdown
# Student Course Management System

A simple application for managing students and their course enrollments.

## Overview

This application allows users to manage student records and their associated courses. It provides functionalities to create, retrieve, and update student and course information, as well as manage the relationships between students and courses.

## Main Functions

- **Student Management**: Create, retrieve, and update student records, including their names, emails, and enrolled courses.
- **Course Management**: Create, retrieve, and update course records, including course names and levels.
- **Course Enrollment**: Associate students with multiple courses and manage their enrollments.

## Quick Install

To set up the environment and install the necessary dependencies, follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-repo/student-course-management.git
   cd student-course-management
   ```

2. **Create a Virtual Environment** (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## Database Setup

The application uses SQLite as the database. The database schema will be automatically created when you run the application for the first time. Ensure that you have the necessary permissions to create files in the directory.

## Usage

To run the application, execute the following command:

```bash
python main.py
```

### User Interface

The application provides a simple GUI for user interaction. You can perform the following actions:

- **Add Student**: Enter the student's name and email, and select the courses they are enrolling in.
- **View Students**: Display a list of all students along with their enrolled courses.
- **Add Course**: Enter the course name and level to create a new course.
- **View Courses**: Display a list of all available courses.

### Example Workflow

1. **Adding a Student**:
   - Click on the "Add Student" button.
   - Fill in the student's name and email.
   - Select the courses the student will enroll in.
   - Click "Submit" to save the student record.

2. **Viewing Students**:
   - Click on the "View Students" button to see a list of all students and their enrolled courses.

3. **Adding a Course**:
   - Click on the "Add Course" button.
   - Fill in the course name and level.
   - Click "Submit" to save the course record.

4. **Viewing Courses**:
   - Click on the "View Courses" button to see a list of all available courses.

## Database Migration

The application includes migration scripts to manage database schema changes. When you run the application, it will automatically apply any pending migrations to ensure that the database schema is up-to-date.

## Conclusion

This Student Course Management System is designed to simplify the management of student records and their course enrollments. For any issues or feature requests, please contact the development team.

```

This manual provides a comprehensive guide for users to understand and utilize the software effectively. Let me know if you need any modifications or additional information!