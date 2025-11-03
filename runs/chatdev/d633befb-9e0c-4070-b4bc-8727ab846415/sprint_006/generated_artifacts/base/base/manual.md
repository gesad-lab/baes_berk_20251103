```markdown
# Student and Course Management System

A simple application for managing students and courses, allowing students to enroll in courses and view their course information.

## Main Functions

- **Add Student**: Create a new student with a name and email.
- **View Student**: Retrieve information about a specific student, including the courses they are enrolled in.
- **Add Course**: Create a new course with a name and level.
- **View Course**: Retrieve information about a specific course, including the students enrolled in it.
- **Enroll Student in Course**: Enroll a student in a specific course.

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

3. **Install Dependencies**:
   Make sure you have `pip` installed, then run:
   ```bash
   pip install fastapi[all] sqlalchemy alembic requests
   ```

4. **Set Up the Database**:
   The application uses SQLite by default. You can change the database URL in `database.py` if needed.

5. **Run Database Migrations**:
   To create the necessary tables in the database, run:
   ```bash
   alembic upgrade head
   ```

6. **Start the Application**:
   Run the FastAPI application using:
   ```bash
   uvicorn main:app --reload
   ```

   The application will be accessible at `http://127.0.0.1:8000`.

## How to Use the Application

### User Interface

The application provides a simple GUI built with Tkinter. Follow these steps to interact with the application:

1. **Add a Student**:
   - Enter the student's name and email in the respective fields.
   - Click the "Add Student" button to create a new student.

2. **Add a Course**:
   - Enter the course name and level in the respective fields.
   - Click the "Add Course" button to create a new course.

3. **Enroll a Student in a Course**:
   - Enter the Student ID and Course ID in the respective fields.
   - Click the "Enroll Student in Course" button to enroll the student in the specified course.

4. **View Student and Course Information**:
   - You can retrieve student and course information by using the respective API endpoints directly or by implementing additional functionality in the GUI.

### API Endpoints

The application exposes the following API endpoints:

- **Students**:
  - `POST /students`: Create a new student.
  - `GET /students/{student_id}`: Retrieve a specific student's information.
  - `POST /students/{student_id}/courses/{course_id}`: Enroll a student in a course.

- **Courses**:
  - `POST /courses`: Create a new course.
  - `GET /courses/{course_id}`: Retrieve a specific course's information.

## Conclusion

This Student and Course Management System provides a straightforward way to manage students and their course enrollments. You can extend its functionality by adding more features as needed.

For further assistance, please refer to the code comments and documentation within the repository.
```