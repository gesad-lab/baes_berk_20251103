```markdown
# Course Management System

A simple application for managing students and courses, allowing students to enroll in various courses and view their details.

## Main Functions

- **Student Management**: Create and retrieve student information, including their enrolled courses.
- **Course Management**: Create and retrieve course information.
- **Enrollment**: Enroll students in courses and view their course details.

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
   ```bash
   pip install fastapi[all] sqlalchemy alembic pydantic
   ```

4. **Run Database Migrations**:
   Ensure that the database schema is up to date by running the migration script:
   ```bash
   alembic upgrade head
   ```

5. **Start the Application**:
   Run the FastAPI application:
   ```bash
   uvicorn main:app --reload
   ```

## How to Use the Application

### Accessing the API

The application provides a RESTful API for managing students and courses. You can access the API at `http://127.0.0.1:8000`.

### API Endpoints

- **Students**:
  - `POST /students/`: Create a new student.
    - Request Body: `{ "name": "Student Name", "email": "student@example.com" }`
  - `GET /students/`: Retrieve a list of students with their enrolled courses.
  
- **Courses**:
  - `POST /courses/`: Create a new course.
    - Request Body: `{ "name": "Course Name", "level": "Beginner" }`
  - `GET /courses/`: Retrieve a list of courses.

- **Enrollment**:
  - `POST /students/{student_id}/courses/{course_id}`: Enroll a student in a course.
    - Replace `{student_id}` and `{course_id}` with the respective IDs.

### Graphical User Interface (GUI)

The application also includes a simple GUI for managing courses. To run the GUI:

1. Ensure the FastAPI application is running.
2. Execute the GUI script:
   ```bash
   python gui.py
   ```
3. Use the GUI to add new courses and view existing ones.

### Example Usage

1. **Create a Student**:
   - Use the `POST /students/` endpoint to create a new student.
   
2. **Create a Course**:
   - Use the `POST /courses/` endpoint to create a new course.

3. **Enroll a Student in a Course**:
   - Use the `POST /students/{student_id}/courses/{course_id}` endpoint to enroll the student.

4. **View Students and Courses**:
   - Use the `GET /students/` and `GET /courses/` endpoints to retrieve lists of students and courses.

## Conclusion

This Course Management System provides a straightforward way to manage students and their courses. With the RESTful API and GUI, users can easily create, retrieve, and manage their data. For further customization or features, feel free to modify the code as needed.
```