```markdown
# Student Course Management System

A simple application for managing students and their associated courses.

## Overview

This application allows users to create and manage students and courses. Each student can be associated with multiple courses, and the application provides a RESTful API for interacting with these entities. 

## Main Functions

- **Create Student**: Add a new student with a name, email, and associated courses.
- **Read Student**: Retrieve information about a specific student, including their associated courses.
- **Create Course**: Add a new course with a name and level.
- **Read Course**: Retrieve information about a specific course, including its associated students.

## Installation

To set up the environment and install the necessary dependencies, follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Create a Virtual Environment** (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies**:
   ```bash
   pip install fastapi sqlalchemy uvicorn
   ```

## Database Setup

The application uses SQLite as the database. The database schema will be automatically created when you run the application for the first time. 

To initialize the database and apply any migrations, run the following command:
```bash
python main.py
```

## Running the Application

To start the FastAPI application, use the following command:
```bash
uvicorn api:router --reload
```

This will start the server at `http://127.0.0.1:8000`. You can access the interactive API documentation at `http://127.0.0.1:8000/docs`.

## API Usage

### Creating a Student

To create a new student, send a POST request to `/students/` with the following JSON body:
```json
{
  "name": "John Doe",
  "email": "john.doe@example.com",
  "course_ids": [1, 2]
}
```

### Reading a Student

To retrieve a student's information, send a GET request to `/students/{student_id}` where `{student_id}` is the ID of the student.

### Creating a Course

To create a new course, send a POST request to `/courses/` with the following JSON body:
```json
{
  "name": "Mathematics",
  "level": "Beginner"
}
```

### Reading a Course

To retrieve a course's information, send a GET request to `/courses/{course_id}` where `{course_id}` is the ID of the course.

## Conclusion

This application provides a straightforward way to manage students and courses. You can extend its functionality by adding more features as needed. For any issues or feature requests, please reach out to the development team.

Happy coding!
```