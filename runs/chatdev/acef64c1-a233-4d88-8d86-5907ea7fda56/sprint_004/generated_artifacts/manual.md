Here's a detailed user manual for the software, formatted in Markdown as requested:

```markdown
# Student Course Management System

A FastAPI application for managing students and their enrolled courses.

## Main Functions

This application allows users to:

- Create and manage student records.
- Create and manage course records.
- Enroll students in courses.
- Retrieve student information along with their enrolled courses.

## Quick Install

To set up the environment and install the necessary dependencies, follow these steps:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-repo/student-course-management.git
   cd student-course-management
   ```

2. **Create a virtual environment (optional but recommended):**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install the required dependencies:**
   ```bash
   pip install fastapi[all] sqlalchemy alembic
   ```

4. **Run the database migration:**
   Make sure to have Alembic installed and run the migration script to set up the database schema.
   ```bash
   alembic upgrade head
   ```

5. **Start the application:**
   ```bash
   uvicorn main:app --reload
   ```

## 🤔 What is this?

The Student Course Management System is designed to facilitate the management of students and their courses. It provides a RESTful API for creating, retrieving, and managing student and course data. The application uses FastAPI for building the API and SQLAlchemy for database interactions.

## 📖 API Documentation

### Endpoints

1. **Create a Student**
   - **Endpoint:** `POST /students/`
   - **Request Body:**
     ```json
     {
       "name": "John Doe",
       "email": "john.doe@example.com"
     }
     ```
   - **Response:**
     ```json
     {
       "id": 1,
       "name": "John Doe",
       "email": "john.doe@example.com",
       "courses": []
     }
     ```

2. **Get All Students**
   - **Endpoint:** `GET /students/`
   - **Response:**
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

3. **Create a Course**
   - **Endpoint:** `POST /courses/`
   - **Request Body:**
     ```json
     {
       "name": "Mathematics",
       "level": "Beginner"
     }
     ```
   - **Response:**
     ```json
     {
       "id": 1,
       "name": "Mathematics",
       "level": "Beginner"
     }
     ```

4. **Enroll Student in Course**
   - **Endpoint:** `POST /students/{student_id}/courses/{course_id}`
   - **Response:**
     ```json
     {
       "message": "Student enrolled in course successfully"
     }
     ```

## Usage

- To create a student, send a POST request to `/students/` with the student's name and email.
- To retrieve all students, send a GET request to `/students/`.
- To create a course, send a POST request to `/courses/` with the course name and level.
- To enroll a student in a course, send a POST request to `/students/{student_id}/courses/{course_id}`.

## Additional Information

- The application uses SQLite as the database. You can change the `DATABASE_URL` in `database.py` to use a different database if needed.
- Ensure that the database migration script is run to create the necessary tables before starting the application.

For more detailed information on the API, please refer to the code comments and the FastAPI documentation.
```

This manual provides a comprehensive overview of the software, installation instructions, and usage guidelines to help users effectively utilize the Student Course Management System.