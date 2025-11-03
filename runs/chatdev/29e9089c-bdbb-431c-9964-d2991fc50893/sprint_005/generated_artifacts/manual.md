```markdown
# ChatDev Teacher Management System

Welcome to the ChatDev Teacher Management System, a powerful API built using FastAPI and SQLAlchemy for managing teachers, students, and courses. This manual will guide you through the main functions of the software, how to install the necessary environment dependencies, and how to use the API effectively.

## Main Functions

The ChatDev Teacher Management System provides the following functionalities:

- **Teacher Management**: Create and retrieve teacher records with essential information such as name and email.
- **Student Management**: Create and retrieve student records, including their associated courses.
- **Course Management**: Create and retrieve course records, along with managing student enrollments in courses.

### API Endpoints

- **Teachers**
  - `POST /teachers/`: Create a new teacher.
  - `GET /teachers/`: Retrieve a list of teachers.

- **Students**
  - `POST /students/`: Create a new student.
  - `GET /students/`: Retrieve a list of students.
  - `POST /students/{student_id}/courses/{course_id}`: Enroll a student in a course.
  - `GET /students/{student_id}/courses/`: Retrieve courses for a specific student.

- **Courses**
  - `POST /courses/`: Create a new course.
  - `GET /courses/`: Retrieve a list of courses.

## Quick Install

To set up the environment for the ChatDev Teacher Management System, follow these steps:

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Create a virtual environment** (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install the required dependencies**:
   Create a `requirements.txt` file with the following content:
   ```
   fastapi
   uvicorn
   sqlalchemy
   alembic
   pydantic
   ```
   Then run:
   ```bash
   pip install -r requirements.txt
   ```

## How to Use the API

1. **Run the Application**:
   Start the FastAPI application using Uvicorn:
   ```bash
   uvicorn main:app --reload
   ```
   The application will be available at `http://127.0.0.1:8000`.

2. **Access the API Documentation**:
   Open your web browser and navigate to `http://127.0.0.1:8000/docs` to access the interactive API documentation provided by Swagger UI.

3. **Creating a Teacher**:
   To create a new teacher, send a `POST` request to `/teachers/` with the following JSON body:
   ```json
   {
       "name": "John Doe",
       "email": "john.doe@example.com"
   }
   ```

4. **Retrieving Teachers**:
   To retrieve a list of teachers, send a `GET` request to `/teachers/`.

5. **Creating a Student**:
   To create a new student, send a `POST` request to `/students/` with the following JSON body:
   ```json
   {
       "name": "Jane Smith",
       "email": "jane.smith@example.com"
   }
   ```

6. **Creating a Course**:
   To create a new course, send a `POST` request to `/courses/` with the following JSON body:
   ```json
   {
       "name": "Mathematics",
       "level": "Beginner"
   }
   ```

7. **Enrolling a Student in a Course**:
   To enroll a student in a course, send a `POST` request to `/students/{student_id}/courses/{course_id}`.

8. **Retrieving Courses for a Student**:
   To get the courses for a specific student, send a `GET` request to `/students/{student_id}/courses/`.

## Conclusion

The ChatDev Teacher Management System provides a robust API for managing educational entities such as teachers, students, and courses. By following the instructions in this manual, you can easily set up the environment and start using the API to manage your educational data effectively.

For further assistance, please refer to the API documentation or contact our support team.
```