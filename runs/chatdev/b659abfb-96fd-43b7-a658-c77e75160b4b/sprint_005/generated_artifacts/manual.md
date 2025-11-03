Here's the `manual.md` file that provides a detailed user manual for the software, including an introduction to its main functions, installation instructions, and usage guidelines.

```markdown
# Teacher Management System

A web application for managing students, courses, and teachers with an integrated dashboard.

## Overview

The Teacher Management System allows users to manage students, courses, and teachers efficiently. Users can add new students and teachers, associate students with courses, and view the details of each entity through a simple GUI and RESTful API.

## Main Functions

- **Student Management**: Create, read, and manage student records, including their names, emails, and associated courses.
- **Course Management**: Create and manage courses, including their names and levels.
- **Teacher Management**: Create and manage teacher records, including their names and emails.
- **Integrated Dashboard**: A user-friendly GUI built with Tkinter for easy interaction with the API.

## Quick Install

To set up the environment and install the necessary dependencies, follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-repo/teacher-management-system.git
   cd teacher-management-system
   ```

2. **Create a Virtual Environment** (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies**:
   ```bash
   pip install fastapi[all] sqlalchemy pydantic requests
   ```

4. **Run the Application**:
   ```bash
   uvicorn main:app --reload
   ```

5. **Access the API**:
   Open your browser and go to `http://127.0.0.1:8000/docs` to view the interactive API documentation.

## How to Use the Application

### Adding a Student

1. Open the GUI application.
2. Enter the student's name and email.
3. If applicable, enter the course IDs (comma-separated) that the student will be enrolled in.
4. Click the "Add Student" button to submit the form.

### Adding a Teacher

1. Use the API endpoint `/teachers` to add a new teacher.
2. Send a POST request with the following JSON body:
   ```json
   {
       "name": "Teacher Name",
       "email": "teacher@example.com"
   }
   ```

### Adding a Course

1. Use the API endpoint `/courses` to add a new course.
2. Send a POST request with the following JSON body:
   ```json
   {
       "name": "Course Name",
       "level": "Course Level"
   }
   ```

### Viewing Data

- You can view the list of students, teachers, and courses by accessing the respective API endpoints:
  - `/students`
  - `/teachers`
  - `/courses`

## Additional Information

- **Database**: The application uses SQLite for data storage. The database file is located in the project directory as `students.db`.
- **Migrations**: The application includes migration scripts to ensure that the database schema is updated without losing existing data.

## Support

For any issues or questions, please reach out to the development team via the support channel or open an issue in the repository.

```

This manual provides a comprehensive guide for users to understand the application, install it, and utilize its features effectively.