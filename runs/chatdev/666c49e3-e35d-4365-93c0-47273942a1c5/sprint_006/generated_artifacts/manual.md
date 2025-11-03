```markdown
# ChatDev Course Management System

Welcome to the ChatDev Course Management System! This software allows you to manage students, courses, and teachers efficiently. You can create, read, and manage relationships between these entities seamlessly.

## Main Functions

- **Student Management**: Create and manage student records, including their names and emails.
- **Course Management**: Create and manage courses, including assigning teachers to courses.
- **Teacher Management**: Create and manage teacher records, including their names and emails.
- **Enrollment**: Enroll students in courses and manage their course registrations.

## Quick Install

To set up the environment and install the necessary dependencies, follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Create a Virtual Environment** (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies**:
   Create a `requirements.txt` file with the following content:
   ```plaintext
   fastapi
   uvicorn
   sqlalchemy
   pydantic
   alembic
   ```
   Then run:
   ```bash
   pip install -r requirements.txt
   ```

## How to Use the Application

1. **Run the Application**:
   Start the FastAPI application by running:
   ```bash
   python main.py
   ```
   The application will be accessible at `http://127.0.0.1:8000`.

2. **API Endpoints**:
   You can interact with the application using the following API endpoints:

   - **Students**:
     - `POST /students/`: Create a new student.
     - `GET /students/`: Retrieve a list of students.

   - **Courses**:
     - `POST /courses/`: Create a new course (assign a teacher if needed).
     - `GET /courses/`: Retrieve a list of courses.

   - **Teachers**:
     - `POST /teachers/`: Create a new teacher.
     - `GET /teachers/`: Retrieve a list of teachers.

   - **Enrollments**:
     - `POST /students/{student_id}/courses/{course_id}`: Enroll a student in a course.

3. **Database Migration**:
   To apply the database schema changes, run the Alembic migration script:
   ```bash
   alembic upgrade head
   ```
   This will create the necessary tables and relationships in the database while preserving existing data.

## Example Usage

### Creating a Student
```bash
curl -X POST "http://127.0.0.1:8000/students/" -H "Content-Type: application/json" -d '{"name": "John Doe", "email": "john@example.com"}'
```

### Creating a Teacher
```bash
curl -X POST "http://127.0.0.1:8000/teachers/" -H "Content-Type: application/json" -d '{"name": "Jane Smith", "email": "jane@example.com"}'
```

### Creating a Course
```bash
curl -X POST "http://127.0.0.1:8000/courses/" -H "Content-Type: application/json" -d '{"name": "Mathematics", "level": "Beginner", "teacher_id": 1}'
```

### Enrolling a Student in a Course
```bash
curl -X POST "http://127.0.0.1:8000/students/1/courses/1"
```

## Documentation

For more detailed documentation, including examples and API references, please refer to the FastAPI documentation [here](https://fastapi.tiangolo.com/).

Thank you for using the ChatDev Course Management System! We hope you find it useful for managing your educational entities.
```