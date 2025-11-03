# ChatDev Student-Course Management System

Welcome to the ChatDev Student-Course Management System! This software allows you to manage students and their associated courses efficiently. Below is a detailed user manual to help you get started.

## Main Functions

- **Student Management**: Create, read, and manage student records, including their names, emails, and associated courses.
- **Course Management**: Create, read, and manage course records, including course names and levels.
- **Course Assignment**: Assign courses to students and retrieve a list of courses associated with a specific student.

## Quick Install

To set up the environment and install the necessary dependencies, follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-repo/chatdev-student-course-management.git
   cd chatdev-student-course-management
   ```

2. **Create a Virtual Environment** (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies**:
   ```bash
   pip install fastapi sqlalchemy alembic pydantic
   ```

4. **Run Database Migrations**:
   ```bash
   alembic upgrade head
   ```

5. **Start the Application**:
   ```bash
   uvicorn main:app --reload
   ```

## How to Use the Software

### API Endpoints

The application exposes several API endpoints to interact with the student and course data.

#### Student Endpoints

- **Create a Student**:
  - **Endpoint**: `POST /students/`
  - **Request Body**:
    ```json
    {
      "name": "John Doe",
      "email": "john.doe@example.com"
    }
    ```
  - **Response**: Returns the created student object.

- **Get All Students**:
  - **Endpoint**: `GET /students/`
  - **Response**: Returns a list of all students.

- **Assign a Course to a Student**:
  - **Endpoint**: `POST /students/{student_id}/courses/{course_id}/`
  - **Response**: Returns the updated student object with the assigned course.

- **Get Courses for a Student**:
  - **Endpoint**: `GET /students/{student_id}/courses/`
  - **Response**: Returns a list of course IDs associated with the student.

#### Course Endpoints

- **Create a Course**:
  - **Endpoint**: `POST /courses/`
  - **Request Body**:
    ```json
    {
      "name": "Mathematics",
      "level": "Beginner"
    }
    ```
  - **Response**: Returns the created course object.

- **Get All Courses**:
  - **Endpoint**: `GET /courses/`
  - **Response**: Returns a list of all courses.

## Example Usage

1. **Create a Student**:
   ```bash
   curl -X POST "http://localhost:8000/students/" -H "Content-Type: application/json" -d '{"name": "John Doe", "email": "john.doe@example.com"}'
   ```

2. **Create a Course**:
   ```bash
   curl -X POST "http://localhost:8000/courses/" -H "Content-Type: application/json" -d '{"name": "Mathematics", "level": "Beginner"}'
   ```

3. **Assign Course to Student**:
   ```bash
   curl -X POST "http://localhost:8000/students/1/courses/1/"
   ```

4. **Get Student Courses**:
   ```bash
   curl -X GET "http://localhost:8000/students/1/courses/"
   ```

## Documentation

For more detailed documentation, please refer to the following sections:

- **Getting Started**: Installation, setting up the environment, and simple examples.
- **How-To Examples**: Demos, integrations, and helper functions.
- **Reference**: Full API documentation.
- **Resources**: High-level explanation of core concepts.

Feel free to reach out for support or further inquiries regarding the ChatDev Student-Course Management System!