```markdown
# Student Course Management System

A FastAPI application for managing students and their enrolled courses.

## Main Functions

This software provides the following main functionalities:

- **Create Students**: Add new students to the system.
- **Retrieve Students**: List all students in the system.
- **Create Courses**: Add new courses to the system.
- **Retrieve Courses**: List all courses in the system.
- **Enroll Students in Courses**: Associate students with courses they are enrolled in.

## Installation

To set up the environment and install the necessary dependencies, follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone <repository-url>
   cd student_app
   ```

2. **Create a Virtual Environment** (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies**:
   Make sure you have `pip` installed, then run:
   ```bash
   pip install fastapi[all] sqlalchemy alembic
   ```

4. **Initialize the Database**:
   The application uses SQLite by default. You can initialize the database by running:
   ```bash
   python main.py
   ```

5. **Run Migrations**:
   To create the necessary database tables, run the following commands:
   ```bash
   alembic revision --autogenerate -m "Add Course table"
   alembic upgrade head
   ```

## How to Use the Application

Once the application is running, you can interact with it through the API endpoints. Here’s how to use the main functionalities:

### Creating a Student

To create a new student, send a POST request to `/students/` with a JSON body containing the student's name and email.

**Example**:
```bash
curl -X POST "http://localhost:8000/students/" -H "Content-Type: application/json" -d '{"name": "John Doe", "email": "john@example.com"}'
```

### Retrieving Students

To retrieve a list of all students, send a GET request to `/students/`.

**Example**:
```bash
curl -X GET "http://localhost:8000/students/"
```

### Creating a Course

To create a new course, send a POST request to `/courses/` with a JSON body containing the course's name and level.

**Example**:
```bash
curl -X POST "http://localhost:8000/courses/" -H "Content-Type: application/json" -d '{"name": "Mathematics", "level": "Beginner"}'
```

### Retrieving Courses

To retrieve a list of all courses, send a GET request to `/courses/`.

**Example**:
```bash
curl -X GET "http://localhost:8000/courses/"
```

### Enrolling a Student in a Course

To enroll a student in a course, send a POST request to `/students/{student_id}/courses/{course_id}`.

**Example**:
```bash
curl -X POST "http://localhost:8000/students/1/courses/1"
```

## Conclusion

This Student Course Management System provides a simple yet effective way to manage students and their courses. With FastAPI's performance and ease of use, you can easily extend this application to fit your needs.

For further documentation and examples, please refer to the FastAPI documentation [here](https://fastapi.tiangolo.com/).
```