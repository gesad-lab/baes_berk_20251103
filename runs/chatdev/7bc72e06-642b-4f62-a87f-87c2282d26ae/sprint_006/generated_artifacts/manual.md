```markdown
# ChatDev Course Management System

Welcome to the ChatDev Course Management System! This software allows you to manage students, courses, and teachers efficiently. You can create, read, and assign courses to students, as well as manage teacher relationships with courses.

## Main Functions

- **Student Management**: Create and manage student profiles, including their courses.
- **Course Management**: Create and manage courses, including assigning teachers to courses.
- **Teacher Management**: Create and manage teacher profiles.
- **Course Assignments**: Assign courses to students and retrieve their enrolled courses.

## Quick Install

To set up the environment and install the necessary dependencies, follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-repo/chatdev-course-management.git
   cd chatdev-course-management
   ```

2. **Create a Virtual Environment** (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies**:
   ```bash
   pip install fastapi sqlalchemy pydantic alembic
   ```

4. **Run Database Migrations**:
   Ensure you have Alembic installed and run the following commands to set up your database schema:
   ```bash
   alembic upgrade head
   ```

5. **Start the Application**:
   You can run the FastAPI application using Uvicorn:
   ```bash
   uvicorn main:app --reload
   ```

## How to Use the Application

### 1. Accessing the API

Once the application is running, you can access the API documentation at:
```
http://127.0.0.1:8000/docs
```

### 2. Managing Students

- **Create a Student**:
  Send a POST request to `/students/` with the following JSON body:
  ```json
  {
    "name": "John Doe",
    "email": "john.doe@example.com"
  }
  ```

- **Get All Students**:
  Send a GET request to `/students/`.

### 3. Managing Courses

- **Create a Course**:
  Send a POST request to `/courses/` with the following JSON body:
  ```json
  {
    "name": "Mathematics",
    "level": "Beginner",
    "teacher_id": 1  // Optional, if you want to assign a teacher
  }
  ```

- **Get All Courses**:
  Send a GET request to `/courses/`.

### 4. Managing Teachers

- **Create a Teacher**:
  Send a POST request to `/teachers/` with the following JSON body:
  ```json
  {
    "name": "Jane Smith",
    "email": "jane.smith@example.com"
  }
  ```

- **Get All Teachers**:
  Send a GET request to `/teachers/`.

### 5. Assigning Courses to Students

- **Assign a Course to a Student**:
  Send a POST request to `/students/{student_id}/courses/{course_id}/` to assign a course to a student.

- **Get Courses for a Student**:
  Send a GET request to `/students/{student_id}/courses/` to retrieve all courses assigned to a specific student.

## Conclusion

This application provides a comprehensive solution for managing courses, students, and teachers. Feel free to explore the API and integrate it into your educational platform. For any issues or feature requests, please reach out to the ChatDev support team.
```