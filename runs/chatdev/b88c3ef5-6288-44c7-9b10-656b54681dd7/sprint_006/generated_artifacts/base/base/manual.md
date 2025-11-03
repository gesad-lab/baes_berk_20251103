```markdown
# Student-Course Management System

A simple API for managing students and their course enrollments.

## Overview

This software provides a RESTful API to manage students and courses, allowing students to enroll in multiple courses. It is built using FastAPI and SQLAlchemy, and it supports a many-to-many relationship between students and courses.

## Main Functions

- **Create a Student**: Add a new student to the system.
- **Read Student Details**: Retrieve details of a specific student, including their enrolled courses.
- **Create a Course**: Add a new course to the system.
- **Read Course Details**: Retrieve details of a specific course.
- **Enroll Student in Course**: Enroll a student in a specific course.

## Installation

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
   pip install fastapi[all] sqlalchemy
   ```

4. **Run Database Migrations**:
   The database will be automatically created when you run the application for the first time. However, you can manually run the migration script:
   ```bash
   python main.py
   ```

## Usage

### Start the API Server

To start the FastAPI server, run the following command:
```bash
uvicorn routers:app --reload
```

### API Endpoints

1. **Create a Student**
   - **Endpoint**: `POST /students/`
   - **Request Body**:
     ```json
     {
       "name": "John Doe",
       "email": "john.doe@example.com"
     }
     ```

2. **Get Student Details**
   - **Endpoint**: `GET /students/{student_id}`
   - **Response**:
     ```json
     {
       "id": 1,
       "name": "John Doe",
       "email": "john.doe@example.com",
       "courses": []
     }
     ```

3. **Create a Course**
   - **Endpoint**: `POST /courses/`
   - **Request Body**:
     ```json
     {
       "name": "Mathematics",
       "level": "Beginner"
     }
     ```

4. **Get Course Details**
   - **Endpoint**: `GET /courses/{course_id}`
   - **Response**:
     ```json
     {
       "id": 1,
       "name": "Mathematics",
       "level": "Beginner"
     }
     ```

5. **Enroll Student in Course**
   - **Endpoint**: `POST /students/{student_id}/courses/{course_id}`
   - **Response**:
     ```json
     {
       "message": "Student enrolled in course successfully"
     }
     ```

## Conclusion

This Student-Course Management System provides a robust API for managing students and their courses. You can easily extend its functionality or integrate it into larger applications as needed. For further assistance or to report issues, please contact the development team.
```