```markdown
# ChatDev Course Management System

Welcome to the ChatDev Course Management System! This software allows you to manage students, courses, and teachers efficiently. You can create, read, and associate students with courses, as well as assign teachers to courses.

## Main Functions

- **Student Management**: Create and manage student profiles, including their associated courses.
- **Course Management**: Create and manage courses, including assigning teachers to courses.
- **Teacher Management**: Create and manage teacher profiles.
- **Relationships**: Establish relationships between students, courses, and teachers.

## Quick Install

To set up the environment and install the necessary dependencies, follow these steps:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-repo/chatdev-course-management.git
   cd chatdev-course-management
   ```

2. **Create a virtual environment** (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies**:
   ```bash
   pip install fastapi sqlalchemy pydantic
   ```

4. **Run the application**:
   ```bash
   uvicorn api:router --reload
   ```

## How to Use the Application

### API Endpoints

The application exposes several API endpoints for managing students, courses, and teachers. Below are the main endpoints:

- **Students**:
  - `POST /students/`: Create a new student.
  - `GET /students/{student_id}`: Retrieve a student by ID.

- **Courses**:
  - `POST /courses/`: Create a new course (assign a teacher if needed).
  - `GET /courses/{course_id}`: Retrieve a course by ID.

- **Teachers**:
  - `POST /teachers/`: Create a new teacher.
  - `GET /teachers/{teacher_id}`: Retrieve a teacher by ID.

### Example Usage

1. **Create a Teacher**:
   ```bash
   curl -X POST "http://localhost:8000/teachers/" -H "Content-Type: application/json" -d '{"name": "John Doe", "email": "john.doe@example.com"}'
   ```

2. **Create a Course**:
   ```bash
   curl -X POST "http://localhost:8000/courses/" -H "Content-Type: application/json" -d '{"name": "Mathematics", "level": "Beginner", "teacher_id": 1}'
   ```

3. **Create a Student**:
   ```bash
   curl -X POST "http://localhost:8000/students/" -H "Content-Type: application/json" -d '{"name": "Jane Smith", "email": "jane.smith@example.com", "course_ids": [1]}'
   ```

4. **Retrieve a Course**:
   ```bash
   curl -X GET "http://localhost:8000/courses/1"
   ```

## Database Migration

The application uses SQLite for data storage. When you run the application for the first time, it will automatically create the necessary database tables and preserve any existing data for students, courses, and teachers.

To perform a database migration, simply run the `main.py` script:
```bash
python main.py
```

This will ensure that the database schema is up-to-date with the latest changes.

## Conclusion

The ChatDev Course Management System is designed to streamline the management of educational entities. With its simple API and robust functionality, you can efficiently manage students, courses, and teachers. For further assistance, please refer to the documentation or contact our support team.

Happy coding!
```