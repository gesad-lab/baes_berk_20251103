Here is the `manual.md` file that provides a detailed user manual for the software, including the introduction to its main functions, installation instructions, and usage guidelines.

```markdown
# Teacher Management Application

A simple application for managing teachers, students, and courses.

## Overview

The Teacher Management Application allows users to create and manage entities for teachers, students, and courses. The application provides a RESTful API for performing CRUD operations on these entities. This manual will guide you through the installation, setup, and usage of the application.

## Main Functions

- **Create Teacher**: Add a new teacher with a name and email.
- **Read Teacher**: Retrieve information about a specific teacher by their ID.
- **Create Student**: Add a new student with a name, email, and associated courses.
- **Read Student**: Retrieve information about a specific student by their ID.
- **Create Course**: Add a new course with a name and level.
- **Read Course**: Retrieve information about a specific course by its ID.

## Installation

To run the Teacher Management Application, you need to set up your environment and install the required dependencies. Follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/teacher-management-app.git
   cd teacher-management-app
   ```

2. **Create a Virtual Environment** (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies**:
   Make sure you have `pip` installed. Then run:
   ```bash
   pip install fastapi[all] sqlalchemy pydantic
   ```

4. **Database Setup**:
   The application uses SQLite as the database. The database will be created automatically when you run the application for the first time.

## Running the Application

To start the application, run the following command:

```bash
uvicorn main:app --reload
```

This will start the server at `http://127.0.0.1:8000`. You can access the interactive API documentation at `http://127.0.0.1:8000/docs`.

## Usage

### Creating a Teacher

To create a new teacher, send a POST request to `/teachers/` with the following JSON body:

```json
{
  "name": "John Doe",
  "email": "john.doe@example.com"
}
```

### Reading a Teacher

To retrieve a teacher's information, send a GET request to `/teachers/{teacher_id}`, replacing `{teacher_id}` with the actual ID of the teacher.

### Creating a Student

To create a new student, send a POST request to `/students/` with the following JSON body:

```json
{
  "name": "Jane Smith",
  "email": "jane.smith@example.com",
  "course_ids": [1, 2]  // Optional: List of course IDs
}
```

### Reading a Student

To retrieve a student's information, send a GET request to `/students/{student_id}`, replacing `{student_id}` with the actual ID of the student.

### Creating a Course

To create a new course, send a POST request to `/courses/` with the following JSON body:

```json
{
  "name": "Mathematics",
  "level": "Beginner"
}
```

### Reading a Course

To retrieve a course's information, send a GET request to `/courses/{course_id}`, replacing `{course_id}` with the actual ID of the course.

## Conclusion

This application provides a straightforward way to manage teachers, students, and courses. For further assistance or to report issues, please contact the development team.

Happy coding!
```

This manual provides a comprehensive guide for users to understand and utilize the Teacher Management Application effectively.