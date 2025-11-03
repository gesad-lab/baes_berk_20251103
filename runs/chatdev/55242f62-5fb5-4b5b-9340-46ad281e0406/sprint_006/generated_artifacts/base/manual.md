```markdown
# Teacher Management System

A simple application for managing teachers, students, and courses using FastAPI and SQLAlchemy.

## Introduction

This application allows users to create and manage entities for teachers, students, and courses. It provides a RESTful API for creating, retrieving, and managing these entities. The main functionalities include:

- Creating new teachers with their names and emails.
- Creating new students with their names and emails.
- Creating new courses with their names and levels.
- Enrolling students in courses.

## Quick Install

To set up the environment and install the necessary dependencies, follow these steps:

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Create a virtual environment (optional but recommended):**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install the required dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## Environment Dependencies

The following dependencies are required for the application:

- **fastapi**: The web framework used to build the API.
- **uvicorn**: An ASGI server for running FastAPI applications.
- **sqlalchemy**: The ORM used for database interactions.
- **alembic**: A database migration tool for SQLAlchemy.
- **pydantic**: Used for data validation and settings management.

## How to Use the Application

1. **Run the application:**
   ```bash
   uvicorn main:app --reload
   ```

2. **Access the API documentation:**
   Open your web browser and navigate to `http://127.0.0.1:8000/docs` to view the interactive API documentation provided by FastAPI.

3. **Creating a Teacher:**
   To create a new teacher, send a POST request to `/teachers/` with the following JSON body:
   ```json
   {
       "name": "John Doe",
       "email": "john.doe@example.com"
   }
   ```

4. **Creating a Student:**
   To create a new student, send a POST request to `/students/` with the following JSON body:
   ```json
   {
       "name": "Jane Smith",
       "email": "jane.smith@example.com"
   }
   ```

5. **Creating a Course:**
   To create a new course, send a POST request to `/courses/` with the following JSON body:
   ```json
   {
       "name": "Mathematics",
       "level": "Beginner"
   }
   ```

6. **Enrolling a Student in a Course:**
   To enroll a student in a course, send a POST request to `/students/{student_id}/enroll/` with the following JSON body:
   ```json
   {
       "course_id": 1  # Replace with the actual course ID
   }
   ```

## Database Migration

To add the Teacher entity to the database schema without losing existing Student and Course data, the migration scripts are provided using Alembic. To run the migrations, execute the following command:

```bash
alembic upgrade head
```

This will create the necessary tables and columns in the database.

## Conclusion

This application provides a straightforward way to manage teachers, students, and courses. With the FastAPI framework, it offers a fast and efficient API for handling these entities. For further customization or enhancements, feel free to modify the code as needed.

For any issues or support, please reach out to the development team.
```