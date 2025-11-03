```markdown
# ChatDev Course Management System

Welcome to the ChatDev Course Management System! This software allows you to manage students, courses, and teachers effectively. You can create, retrieve, and manage relationships between these entities seamlessly.

## Main Functions

- **Student Management**: Create and manage student records.
- **Course Management**: Create and manage courses, including associating them with teachers.
- **Teacher Management**: Create and manage teacher records.
- **Enrollment**: Enroll students in courses.
- **Data Persistence**: All data is stored in a SQLite database, ensuring data integrity and persistence.

## Quick Install

To set up the environment and install the required dependencies, follow these steps:

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
   alembic
   pydantic
   ```
   Then run:
   ```bash
   pip install -r requirements.txt
   ```

## How to Use the Application

1. **Start the Application**:
   Run the FastAPI application using Uvicorn:
   ```bash
   uvicorn main:app --reload
   ```
   This will start the server at `http://127.0.0.1:8000`.

2. **Access the API Documentation**:
   Open your web browser and navigate to `http://127.0.0.1:8000/docs`. This will take you to the interactive API documentation where you can test the endpoints.

3. **API Endpoints**:
   - **Students**:
     - `POST /students/`: Create a new student.
     - `GET /students/`: Retrieve a list of students.
   - **Courses**:
     - `POST /courses/`: Create a new course (include `teacher_id` to associate with a teacher).
     - `GET /courses/`: Retrieve a list of courses.
   - **Teachers**:
     - `POST /teachers/`: Create a new teacher.
     - `GET /teachers/`: Retrieve a list of teachers.
   - **Enrollment**:
     - `POST /students/{student_id}/courses/{course_id}/enroll`: Enroll a student in a course.

4. **Database Migration**:
   The application uses Alembic for database migrations. To apply migrations, ensure that the `migration_script.py` is set up correctly and run:
   ```bash
   alembic upgrade head
   ```

## Conclusion

This Course Management System is designed to simplify the management of educational entities. With the ability to create and manage students, courses, and teachers, along with the enrollment functionality, you can efficiently handle the educational workflow.

For further assistance or to report issues, please contact our support team.
```
