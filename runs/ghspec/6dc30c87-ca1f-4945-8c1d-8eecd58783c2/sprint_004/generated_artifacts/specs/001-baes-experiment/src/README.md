# Updated README.md

# Course Management API

This project provides a RESTful API for managing student enrollment in courses using FastAPI and SQLAlchemy.

## 1. Getting Started

### 1.1 Prerequisites

Ensure you have the following installed:
- Python 3.9+
- Pip (Python package manager)

### 1.2 Set Up Development Environment

1. **Clone the repository**
   ```bash
   git clone <repository_url>
   cd <repository_directory>
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

### 1.3 Database Setup

- Ensure the SQLite database is initialized and running.
- Use SQLAlchemy to manage the database schema, including the creation of tables.

## 2. API Endpoints

### 2.1 Student Enrollment

- **POST** `/students/{student_id}/enroll`
  - Enroll a student in a course.
  - **Request Body**: JSON object containing `course_id`.
  - **Response**: Confirmation of enrollment.

- **GET** `/students/{student_id}/courses`
  - Retrieve a list of courses a student is enrolled in.
  - **Response**: JSON array of enrolled courses.

### 2.2 Input Validation

- Both `student_id` and `course_id` must exist and be valid for all API calls.

## 3. Database Models

### 3.1 StudentCourses Model

A junction table (`StudentCourses`) is created to link students and courses. Ensure it is referenced correctly in your models.

## 4. Testing

- Utilize `pytest` for unit and integration tests.
- Ensure all tests pass before deployment.

## 5. Documentation

- FastAPI provides automatic documentation for the API. Access it at:
  - **Swagger UI**: `http://localhost:8000/docs`
  - **Redoc**: `http://localhost:8000/redoc`

## 6. Additional Information

- If you need to make changes to the API, ensure that you document the endpoints and test any new features thoroughly.
- Check for the latest environment and database requirements in your `requirements.txt` and ensure compatibility.

This documentation is designed to help developers understand and effectively use the Course Management API. For further assistance or issues, please refer to inline comments within the code or reach out to the development team.