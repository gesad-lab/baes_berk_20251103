Here's a detailed user manual for the software, including an introduction to the main functions, installation instructions, and usage guidelines.

```markdown
# Student Course Management System

A comprehensive application for managing students and their course enrollments.

## Overview

The Student Course Management System allows users to manage student information and their associated courses. This application supports functionalities such as adding new students, enrolling students in courses, and retrieving student and course data.

## Main Functions

- **Student Management**: Create and manage student profiles, including their names and email addresses.
- **Course Management**: Create and manage courses, including course names and levels.
- **Enrollment**: Enroll students in multiple courses and retrieve their course information.
- **Data Persistence**: All data is stored in a SQLite database, ensuring data integrity and persistence.

## Quick Install

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
   pip install -r requirements.txt
   ```

   Ensure you have the following dependencies in your `requirements.txt`:
   ```
   sqlalchemy
   pydantic
   fastapi
   uvicorn
   ```

## Database Initialization

Before using the application, you need to initialize the database. This can be done by running the `main.py` script, which will create the necessary tables and fields in the SQLite database.

```bash
python main.py
```

## How to Use the Application

### Running the Application

To start the application, run the following command:

```bash
uvicorn gui:app --reload
```

This will start the FastAPI application, and you can access the dashboard at `http://127.0.0.1:8000`.

### API Endpoints

The application exposes several API endpoints for managing students and courses. Below are some key endpoints:

- **Create Student**:
  - **Endpoint**: `POST /students`
  - **Request Body**:
    ```json
    {
      "name": "John Doe",
      "email": "john.doe@example.com"
    }
    ```

- **Create Course**:
  - **Endpoint**: `POST /courses`
  - **Request Body**:
    ```json
    {
      "name": "Mathematics",
      "level": "Beginner"
    }
    ```

- **Enroll Student in Course**:
  - **Endpoint**: `POST /enroll`
  - **Request Body**:
    ```json
    {
      "student_id": 1,
      "course_id": 1
    }
    ```

- **Get Student Details**:
  - **Endpoint**: `GET /students/{student_id}`
  
- **Get Course Details**:
  - **Endpoint**: `GET /courses/{course_id}`

### Example Usage

1. **Create a Student**:
   Send a POST request to `/students` with the student details.

2. **Create a Course**:
   Send a POST request to `/courses` with the course details.

3. **Enroll the Student in a Course**:
   Send a POST request to `/enroll` with the student ID and course ID.

4. **Retrieve Student Information**:
   Send a GET request to `/students/{student_id}` to get the student's details along with their enrolled courses.

## Conclusion

The Student Course Management System provides a robust solution for managing student and course data. With its easy-to-use interface and powerful backend, users can efficiently handle student enrollments and course management.

For further documentation and advanced usage, please refer to the API documentation provided within the application.
```

This manual provides a comprehensive guide for users to understand the software's functionality, installation process, and usage instructions.