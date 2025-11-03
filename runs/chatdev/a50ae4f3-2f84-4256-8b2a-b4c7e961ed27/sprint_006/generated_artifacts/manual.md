```markdown
# ChatDev Course Management System

Welcome to the ChatDev Course Management System, a comprehensive application designed to manage students, courses, and teachers efficiently. This software allows users to create and manage relationships between courses and teachers, ensuring a streamlined educational experience.

## Main Functions

- **Student Management**: Create and manage student profiles.
- **Course Management**: Create courses and associate them with teachers.
- **Teacher Management**: Create and manage teacher profiles.
- **Course Enrollment**: Enroll students in courses and view their enrolled courses.

## Quick Install

To set up the environment and install the necessary dependencies, follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-repo/chatdev-course-management.git
   cd chatdev-course-management
   ```

2. **Create a Virtual Environment** (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies**:
   Create a `requirements.txt` file with the following content:
   ```
   fastapi
   uvicorn
   sqlalchemy
   pydantic
   requests
   alembic
   ```
   Then run:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run Database Migrations**:
   Ensure that the database schema is up to date by running the Alembic migration:
   ```bash
   alembic upgrade head
   ```

5. **Start the Application**:
   Run the FastAPI application using Uvicorn:
   ```bash
   uvicorn main:app --reload
   ```

## How to Use the Application

### GUI Interaction

1. **Launch the Application**:
   Run the `gui.py` script to open the graphical user interface:
   ```bash
   python gui.py
   ```

2. **Managing Students**:
   - **Create Student**: Enter the student's name and email, then click "Create Student".
   - **Get Students**: Click "Get Students" to view the list of all students.

3. **Managing Courses**:
   - **Create Course**: Enter the course name, level, and the teacher's ID, then click "Create Course".
   - **Get Courses**: Click "Get Courses" to view the list of all courses.

4. **Managing Teachers**:
   - **Create Teacher**: Enter the teacher's name and email, then click "Create Teacher".
   - **Get Teachers**: Click "Get Teachers" to view the list of all teachers.

5. **Enroll Students in Courses**:
   - Use the provided functionality to add courses to students by specifying their IDs.

### API Interaction

The application also exposes a RESTful API for programmatic access. Here are some key endpoints:

- **Students**:
  - `POST /students/`: Create a new student.
  - `GET /students/`: Retrieve all students.

- **Courses**:
  - `POST /courses/`: Create a new course.
  - `GET /courses/`: Retrieve all courses.

- **Teachers**:
  - `POST /teachers/`: Create a new teacher.
  - `GET /teachers/`: Retrieve all teachers.

### Database Schema

The application uses SQLite as the database backend. The schema includes tables for students, courses, and teachers, with relationships established between courses and teachers.

## Conclusion

The ChatDev Course Management System is a powerful tool for managing educational resources. With its intuitive GUI and robust API, it simplifies the process of managing students, courses, and teachers. For further assistance, please refer to the documentation or contact support.
```