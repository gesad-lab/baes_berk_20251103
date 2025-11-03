```markdown
# ChatDev Teacher Management System

Welcome to the ChatDev Teacher Management System! This software allows you to manage teachers, students, and courses efficiently through a user-friendly API. Below, you'll find a comprehensive guide on how to install the necessary dependencies, an overview of the main functions, and instructions on how to use the application.

## Quick Install

To get started, you need to install the required Python packages. You can do this using pip:

```bash
pip install fastapi sqlalchemy alembic pydantic
```

Alternatively, if you are using conda, you can install the packages as follows:

```bash
conda install fastapi sqlalchemy alembic pydantic -c conda-forge
```

## 🛠️ Main Functions

The ChatDev Teacher Management System provides several key functionalities:

1. **Teacher Management**:
   - Create a new teacher with a name and email.
   - Retrieve a list of all teachers.

2. **Student Management**:
   - Create a new student with a name and email.
   - Retrieve a list of all students.
   - Enroll students in courses.

3. **Course Management**:
   - Create a new course with a name and level.
   - Retrieve a list of all courses.

## 📦 Database Schema

The application uses a SQLite database with the following tables:

- **teachers**: Stores teacher information (id, name, email).
- **students**: Stores student information (id, name, email).
- **courses**: Stores course information (id, name, level).
- **student_courses**: A junction table to manage the many-to-many relationship between students and courses.

## 📖 How to Use the Application

### 1. Start the Application

To run the application, execute the following command in your terminal:

```bash
uvicorn main:app --reload
```

This will start the FastAPI server, and you can access the API documentation at `http://127.0.0.1:8000/docs`.

### 2. Create a Teacher

To create a new teacher, send a POST request to the `/teachers/` endpoint with the following JSON body:

```json
{
  "name": "John Doe",
  "email": "john.doe@example.com"
}
```

### 3. Retrieve Teachers

To get a list of all teachers, send a GET request to the `/teachers/` endpoint. You can also use query parameters `skip` and `limit` for pagination.

### 4. Create a Student

To create a new student, send a POST request to the `/students/` endpoint with the following JSON body:

```json
{
  "name": "Jane Smith",
  "email": "jane.smith@example.com"
}
```

### 5. Retrieve Students

To get a list of all students, send a GET request to the `/students/` endpoint.

### 6. Create a Course

To create a new course, send a POST request to the `/courses/` endpoint with the following JSON body:

```json
{
  "name": "Mathematics",
  "level": "Intermediate"
}
```

### 7. Retrieve Courses

To get a list of all courses, send a GET request to the `/courses/` endpoint.

### 8. Enroll a Student in a Course

To enroll a student in a course, send a POST request to the `/students/{student_id}/courses/{course_id}` endpoint. Replace `{student_id}` and `{course_id}` with the respective IDs.

## 📝 Database Migration

To ensure that the database schema is up-to-date, run the migration script using Alembic. This will create the necessary tables and fields while preserving existing data.

```bash
alembic upgrade head
```

## 📚 Documentation

For more detailed documentation, please refer to the FastAPI documentation [here](https://fastapi.tiangolo.com/).

Thank you for using the ChatDev Teacher Management System! If you have any questions or need further assistance, feel free to reach out.
```