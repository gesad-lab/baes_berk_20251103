```markdown
# Student Course Management System

A simple application for managing students and their associated courses.

## Overview

This application allows users to create and manage students and courses. Each student can be associated with multiple courses, and the application provides an easy-to-use API for creating and retrieving this data.

## Main Functions

- **Create a Student**: Add a new student with a name, email, and optional course associations.
- **Create a Course**: Add a new course with a name and level.
- **Retrieve Students**: Get information about students, including their associated courses.
- **Retrieve Courses**: Get information about courses and the students enrolled in them.

## Installation

To set up the environment and install the necessary dependencies, follow these steps:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-repo/student-course-management.git
   cd student-course-management
   ```

2. **Create a virtual environment** (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies**:
   ```bash
   pip install fastapi[all] sqlalchemy pydantic
   ```

4. **Run the application**:
   ```bash
   uvicorn main:app --reload
   ```

## Usage

### API Endpoints

The application exposes the following API endpoints:

1. **Create a Student**
   - **Endpoint**: `POST /students/`
   - **Request Body**:
     ```json
     {
       "name": "John Doe",
       "email": "john.doe@example.com",
       "course_ids": [1, 2]  // Optional: List of course IDs to associate with the student
     }
     ```
   - **Response**:
     ```json
     {
       "id": 1,
       "name": "John Doe",
       "email": "john.doe@example.com",
       "courses": []  // List of associated courses
     }
     ```

2. **Create a Course**
   - **Endpoint**: `POST /courses/`
   - **Request Body**:
     ```json
     {
       "name": "Mathematics",
       "level": "Intermediate"
     }
     ```
   - **Response**:
     ```json
     {
       "id": 1,
       "name": "Mathematics",
       "level": "Intermediate"
     }
     ```

3. **Retrieve Students**
   - **Endpoint**: `GET /students/`
   - **Response**:
     ```json
     [
       {
         "id": 1,
         "name": "John Doe",
         "email": "john.doe@example.com",
         "courses": []  // List of associated courses
       }
     ]
     ```

4. **Retrieve Courses**
   - **Endpoint**: `GET /courses/`
   - **Response**:
     ```json
     [
       {
         "id": 1,
         "name": "Mathematics",
         "level": "Intermediate",
         "students": []  // List of associated students
       }
     ]
     ```

## Database Migration

The application includes a migration script that ensures the database schema is updated to support the new relationships between students and courses without losing existing data. This is handled automatically on application startup.

## Conclusion

This Student Course Management System provides a straightforward way to manage students and their courses. With the provided API, users can easily create and retrieve data as needed. For further enhancements or features, feel free to contribute or reach out for support.
```