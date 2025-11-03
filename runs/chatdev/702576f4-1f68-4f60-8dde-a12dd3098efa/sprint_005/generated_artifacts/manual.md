```markdown
# Teacher Management System

A simple application for managing students, courses, and teachers using FastAPI and SQLite.

## Main Functions

The Teacher Management System provides the following functionalities:

- **Manage Students**: Add, retrieve, and enroll students in courses.
- **Manage Courses**: Add and retrieve courses.
- **Manage Teachers**: Add and retrieve teachers.
- **Enroll Students in Courses**: Enroll students in specific courses.

## Installation

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

3. **Install Required Dependencies**:
   ```bash
   pip install fastapi[all] sqlalchemy alembic requests
   ```

4. **Run Database Migrations**:
   Ensure that the database schema is up to date by running the migration command:
   ```bash
   alembic upgrade head
   ```

## How to Use the Application

### Running the Application

To start the application, run the following command:
```bash
python main.py
```
The application will be accessible at `http://127.0.0.1:8000`.

### Using the API

You can interact with the API using tools like Postman or directly through the provided GUI.

#### API Endpoints

- **Students**:
  - `POST /students/`: Add a new student.
  - `GET /students/`: Retrieve a list of students.

- **Courses**:
  - `POST /courses/`: Add a new course.
  - `GET /courses/`: Retrieve a list of courses.

- **Teachers**:
  - `POST /teachers/`: Add a new teacher.
  - `GET /teachers/`: Retrieve a list of teachers.

- **Enrollments**:
  - `POST /students/{student_id}/courses/{course_id}`: Enroll a student in a course.
  - `GET /students/{student_id}/courses/`: Retrieve courses for a specific student.

### Using the GUI

1. **Launch the GUI**:
   The GUI is integrated into the application. You can interact with it after starting the application.

2. **Add Students**:
   - Enter the student's name and email, then click "Add Student".

3. **Show Students**:
   - Click "Show Students" to view the list of added students.

4. **Add Courses**:
   - Enter the course name and level, then click "Add Course".

5. **Show Courses**:
   - Click "Show Courses" to view the list of added courses.

6. **Add Teachers**:
   - Enter the teacher's name and email, then click "Add Teacher".

7. **Show Teachers**:
   - Click "Show Teachers" to view the list of added teachers.

8. **Enroll Students**:
   - Enter the Student ID and Course ID, then click "Enroll" to enroll the student in the specified course.

## Conclusion

This Teacher Management System provides a simple and effective way to manage students, courses, and teachers. With the FastAPI framework, it offers a robust backend and a user-friendly GUI for easy interaction. For further customization and enhancements, feel free to explore the codebase and contribute!
```