```markdown
# Student-Course Management System

A FastAPI application for managing students and their course enrollments.

## Overview

This application allows users to create and manage students and courses, as well as enroll students in courses. It provides a RESTful API for easy integration and interaction.

## Main Functions

- **Create a Student**: Add a new student to the database.
- **Read Students**: Retrieve a list of all students.
- **Create a Course**: Add a new course to the database.
- **Read Courses**: Retrieve a list of all courses.
- **Enroll Student in Course**: Enroll a specific student in a specific course.
- **Get Student Courses**: Retrieve all courses that a specific student is enrolled in.

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
   pip install fastapi[all] sqlalchemy alembic pydantic
   ```

4. **Run Database Migrations**:
   Ensure that the database schema is up to date with the following command:
   ```bash
   alembic upgrade head
   ```

5. **Run the Application**:
   Start the FastAPI server:
   ```bash
   uvicorn main:app --reload
   ```

## API Usage

### Create a Student

**Endpoint**: `POST /students/`

**Request Body**:
```json
{
    "name": "John Doe",
    "email": "john.doe@example.com"
}
```

**Response**:
```json
{
    "id": 1,
    "name": "John Doe",
    "email": "john.doe@example.com",
    "courses": []
}
```

### Read Students

**Endpoint**: `GET /students/`

**Response**:
```json
[
    {
        "id": 1,
        "name": "John Doe",
        "email": "john.doe@example.com",
        "courses": []
    }
]
```

### Create a Course

**Endpoint**: `POST /courses/`

**Request Body**:
```json
{
    "name": "Mathematics",
    "level": "Beginner"
}
```

**Response**:
```json
{
    "id": 1,
    "name": "Mathematics",
    "level": "Beginner",
    "students": []
}
```

### Read Courses

**Endpoint**: `GET /courses/`

**Response**:
```json
[
    {
        "id": 1,
        "name": "Mathematics",
        "level": "Beginner",
        "students": []
    }
]
```

### Enroll Student in Course

**Endpoint**: `POST /students/{student_id}/courses/{course_id}`

**Example**: Enroll student with ID 1 in course with ID 1.

**Response**:
```json
{
    "message": "Student enrolled in course successfully."
}
```

### Get Student Courses

**Endpoint**: `GET /students/{student_id}/courses`

**Response**:
```json
[
    {
        "id": 1,
        "name": "Mathematics",
        "level": "Beginner",
        "students": []
    }
]
```

## Conclusion

This Student-Course Management System provides a simple yet powerful way to manage students and their course enrollments. For further customization or feature requests, please reach out to our support team.

```
